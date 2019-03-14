# coding=utf-8

from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, Date
from sqlalchemy.dialects.mysql import LONGBLOB


from sql.core import Base


# tabela Cliente
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    sobrenome = Column(String(40))
    cpf = Column(String(15))
    rg = Column(String(15))
    celular = Column(String(15))
    telefone = Column(String(15))
    email = Column(String(50))
    obs = Column(String(100))
    cep = Column(String(12))
    endereco = Column(String(40))
    numero = Column(String(5))
    bairro = Column(String(40))
    cidade = Column(String(40))
    estado = Column(String(2))

    def __repr__(self):
        return self.nome


# Tabela Fornecedor
class Fornecedor(Base):
    __tablename__ = 'fornecedor'
    id = Column(Integer, primary_key=True)
    nome_fantasia = Column(String(80), index=True)
    razao_social = Column(String(80))
    cnpj = Column(String(20))
    insc_estadual = Column(String(20))
    telefone = Column(String(20))
    email = Column(String(80))
    site = Column(String(80))
    obs = Column(String(100))
    cep = Column(String(12))
    endereco = Column(String(50))
    numero = Column(String(5))
    bairro = Column(String(40))
    cidade = Column(String(40))
    estado = Column(String(2))

    def __repr__(self):
        return self.nome_fantasia


# Tabela Categoria de produtos
class CategoriaProduto(Base):
    __tablename__ = 'categoria_produto'
    id = Column(Integer, primary_key=True)
    categoria_produto = Column(String(50), index=True)

    def __repr__(self):
        return self.categoria_produto


# Tabela Marca Produtos
class MarcaProduto(Base):
    __tablename__ = 'marca_produto'
    id = Column(Integer, primary_key=True)
    marca_produto = Column(String(50), index=True)

    def __repr__(self):
        return self.marca_produto


# Tabela Produtos
class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True)
    produto = Column(String(80), index=True)
    imagem = Column(LONGBLOB(length=None))
    categoria = Column(Integer, ForeignKey('categoria_produto.id'))
    marca = Column(Integer, ForeignKey('marca_produto.id'))
    estoque_minimo = Column(Integer, default=0)
    estoque_maximo = Column(Integer, default=0)
    qtde = Column(Integer, default=0)
    valor_compra = Column(Numeric(9, 2), default='0.00')
    valor_unitario = Column(Numeric(9, 2), default='0.00')
    valor_atacado = Column(Numeric(9, 2), default='0.00')
    qtde_atacado = Column(Integer, default=5)
    obs = Column(String(80))

    def __repr__(self):
        return self.produto


# Tabela Categoria a pagar
class CatAPagar(Base):
    __tablename__ = 'categoria_a_pagar'
    id = Column(Integer, primary_key=True)
    categoria_a_pagar = Column(String(80), index=True)

    def __repr__(self):
        return self.categoria_a_pagar


# Tabela Categoria a Receber
class CatAReceber(Base):
    __tablename__ = 'categoria_a_receber'
    id = Column(Integer, primary_key=True)
    categoria_a_receber = Column(String(50), index=True)

    def __repr__(self):
        return self.categoria_a_receber


# Tabela Forma de Pagamento
class FormaPagamento(Base):
    __tablename__ = 'forma_de_pagamento'
    id = Column(Integer, primary_key=True)
    forma_pagamento = Column(String(50), index=True)

    def __repr__(self):
        return self.forma_pagamento


# Tabela Status Pagamento
class StatusPagamento(Base):
    __tablename__ = 'status_pagamento'
    id = Column(Integer, primary_key=True)
    status_pagamento = Column(String(50), index=True)

    def __repr__(self):
        return self.status_pagamento


# Tabela Status Entrega
class StatusEntrega(Base):
    __tablename__ = 'status_entrega'
    id = Column(Integer, primary_key=True)
    status_entrega = Column(String(50), index=True)

    def __repr__(self):
        return self.status_entrega


# Tabela Compras
class Compra(Base):
    __tablename__ = 'compra'
    id = Column(Integer, primary_key=True)
    id_fornecedor = Column(Integer, ForeignKey('fornecedor.id'))
    data_emissao = Column(Date)
    prazo_entrega = Column(Date)
    data_entrega = Column(Date)
    categoria = Column(Integer, ForeignKey('categoria_a_pagar.id'))
    desconto = Column(Numeric(9, 2), default='0.00')
    frete = Column(Numeric(9, 2), default='0.00')
    valor_total = Column(Numeric(9, 2), default='0.00')
    valor_pago = Column(Numeric(9, 2), default='0.00')
    valor_pendente = Column(Numeric(9, 2), default='0.00')
    entrega = Column(Integer, ForeignKey('status_entrega.id'), default='2')
    pagamento = Column(Integer, ForeignKey('status_pagamento.id'), default='2')

    def __repr__(self):
        return self.id


# Tabela relação de item comprados (carrinho de compra)
class RelacaoCompra(Base):
    __tablename__ = 'relacao_compra'
    id = Column(String(25), primary_key=True)
    id_compra = Column(Integer, ForeignKey('compra.id'))
    id_produto = Column(Integer, ForeignKey('produto.id'))
    qtde = Column(Numeric(9, 2), default='0.00')
    valor_unitario = Column(Numeric(9, 2), default='0.00')
    valor_total = Column(Numeric(9, 2), default='0.00')
    obs = Column(String(50))

    def __repr__(self):
        return self.id


# Tabela Vendas
class Venda(Base):
    __tablename__ = 'venda'
    id = Column(Integer, primary_key=True)
    id_cliente = Column(
        Integer, ForeignKey('cliente.id'))
    data_emissao = Column(Date)
    prazo_entrega = Column(Date)
    data_entrega = Column(Date)
    categoria = Column(
        Integer, ForeignKey('categoria_a_receber.id'))
    desconto = Column(Numeric(9, 2), default='0.00')
    frete = Column(Numeric(9, 2), default='0.00')
    valor_total = Column(Numeric(9, 2), default='0.00')
    valor_recebido = Column(Numeric(9, 2), default='0.00')
    valor_pendente = Column(Numeric(9, 2), default='0.00')
    entrega = Column(
        Integer, ForeignKey('status_entrega.id'), default='2')
    pagamento = Column(
        Integer, ForeignKey('status_pagamento.id'), default='2')

    def __repr__(self):
        return self.id


# Tabela relação de item comprados (carrinho de compra)
class RelacaoVenda(Base):
    __tablename__ = 'relacao_venda'
    id = Column(String(25), primary_key=True)
    id_venda = Column(Integer, ForeignKey('venda.id'))
    id_produto = Column(Integer, ForeignKey('produto.id'))
    qtde = Column(Numeric(9, 2), default='0.00')
    valor_unitario = Column(Numeric(9, 2), default='0.00')
    valor_total = Column(Numeric(9, 2), default='0.00')
    obs = Column(String(80))

    def __repr__(self):
        return self.id


# Tabela Com os dados da Empresa
class Empresa(Base):
    __tablename__ = 'empresa'
    id = Column(Integer, primary_key=True)
    nome_fantasia = Column(String(80))
    razao_social = Column(String((80)))
    cnpj = Column(String(20))
    insc_estadual = Column(String(20))
    telefone = Column(String(20))
    email = Column(String(80))
    site = Column(String(80))
    obs = Column(String(80))
    cep = Column(String(12))
    endereco = Column(String(50))
    numero = Column(String(5))
    bairro = Column(String(40))
    cidade = Column(String(40))
    estado = Column(String(2))
    titulo = Column(String(20))
    subtitulo = Column(String(80))
    logo = Column(LONGBLOB(length=None))

    def __repr__(self):
        return self.nome_fantasia


# Tabela Contas a Pagar
class ContaAPagar(Base):
    __tablename__ = 'conta_a_pagar'
    id = Column(Integer, primary_key=True)
    id_compra = Column(Integer, ForeignKey('compra.id'), nullable='True')
    id_fornecedor = Column(Integer, ForeignKey('fornecedor.id'))
    descricao = Column(String(100))
    obs = Column(String(100))
    categoria = Column(Integer, ForeignKey('categoria_a_pagar.id'))
    data_vencimento = Column(Date)
    valor = Column(Numeric(9, 2), default='0.00')
    forma_pagamento = Column(Integer, ForeignKey('forma_de_pagamento.id'))
    data_pagamento = Column(Date)
    valor_pago = Column(Numeric(9, 2), default='0.00')
    pagamento = Column(Integer, ForeignKey(
        'status_pagamento.id'), default='2')

    def __repr__(self):
        return self.id


# Tabela Contas a Receber
class ContaAReceber(Base):
    __tablename__ = 'conta_a_receber'
    id = Column(Integer, primary_key=True)
    id_venda = Column(Integer, ForeignKey('venda.id'), nullable=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    descricao = Column(String(100))
    obs = Column(String(100))
    categoria = Column(Integer, ForeignKey('categoria_a_receber.id'))
    data_vencimento = Column(Date)
    valor = Column(Numeric(9, 2), default='0.00')
    forma_pagamento = Column(Integer, ForeignKey('forma_de_pagamento.id'))
    data_recebimento = Column(Date)
    valor_recebido = Column(Numeric(9, 2), default='0.00')
    pagamento = Column(Integer, ForeignKey(
        'status_pagamento.id'), default='2')

    def __repr__(self):
        return self.id
