# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from sqlalchemy import func

from Crud.core import Conexao
from Crud.Models import Produto, CategoriaProduto, MarcaProduto


class CrudProduto(object):

    def __init__(self, id="", produto="", imagem="",
                 categoria="", marca="", estoqueMinimo="", estoqueMaximo="",
                 qtdeProduto="", valorCompra="", valorUnitario="",
                 valorAtacado="", qtdeAtacado="", obsProduto="", query=""):

        self.id = id
        self.produto = produto
        self.imagem = imagem
        self.categoria = categoria
        self.marca = marca
        self.estoqueMinimo = estoqueMinimo
        self.estoqueMaximo = estoqueMaximo
        self.qtdeProduto = qtdeProduto
        self.valorCompra = valorCompra
        self.valorUnitario = valorUnitario
        self.valorAtacado = valorAtacado
        self.qtdeAtacado = qtdeAtacado
        self.obsProduto = obsProduto
        self.query = query

    # Recendo ultimo ID inserido

    def lastIdProduto(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            ultimo = sessao.query(Produto.id).order_by(
                desc(Produto.id)).limit(1).first()
            self.id = ultimo.id + 1

            # Fechando Conexao
            sessao.close()

        except:

            self.id = 1

        return self.id

    # Cadastro de Produto
    def inseriProduto(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = Produto(
                id=self.id,
                produto=self.produto,
                imagem=self.imagem,
                categoria=self.categoria,
                marca=self.marca,
                estoque_minimo=self.estoqueMinimo,
                estoque_maximo=self.estoqueMaximo,
                valor_compra=self.valorCompra,
                valor_unitario=self.valorUnitario,
                valor_atacado=self.valorAtacado,
                qtde_atacado=self.qtdeAtacado,
                obs=self.obsProduto

            )

            # Add query na sessao
            sessao.add(row)

            # Executando a Query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateProduto()

        pass

    # Update de Produto
    def updateProduto(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando id
            row = sessao.query(Produto).get(self.id)

            # Novos Valores

            row.produto = self.produto
            row.imagem = self.imagem
            row.categoria = self.categoria
            row.marca = self.marca
            row.estoque_minimo = self.estoqueMinimo
            row.estoque_maximo = self.estoqueMaximo
            row.valor_compra = self.valorCompra
            row.valor_unitario = self.valorUnitario
            row.valor_atacado = self.valorAtacado
            row.qtde_atacado = self.qtdeAtacado
            row.obs = self.obsProduto

            # Executando a Query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        pass

    # Busca por ID

    def selectProdutoId(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            busca = sessao.query(Produto).get(self.id)

            # Salvando resultado da Query
            self.id = busca.id
            self.produto = busca.produto
            self.imagem = busca.imagem
            self.categoria = busca.categoria
            self.marca = busca.marca
            self.estoqueMinimo = busca.estoque_minimo
            self.estoqueMaximo = busca.estoque_maximo
            self.qtdeProduto = busca.qtde
            self.valorCompra = busca.valor_compra
            self.valorUnitario = busca.valor_unitario
            self.valorAtacado = busca.valor_atacado
            self.qtdeAtacado = busca.qtde_atacado
            self.obsProduto = busca.obs

            # Fechando a Conexao
            sessao.close()

            pass

        except:
            pass

    # Busca Produto por Nome

    def listaProduto(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(Produto.id, Produto.produto,
                                       Produto.estoque_minimo, Produto.qtde,
                                       Produto.valor_unitario,
                                       Produto.valor_atacado,
                                       Produto.qtde_atacado,
                                       MarcaProduto.marca_produto
                                       )
                          .join(MarcaProduto)
                          .filter(Produto.produto.contains(self.produto))
                          )
            self.query.all()

            # Convertendo variaveis em lista
            self.id = []
            self.produto = []
            self.marca = []
            self.estoqueMinimo = []
            self.qtdeProduto = []
            self.valorUnitario = []
            self.valorAtacado = []
            self.qtdeAtacado = []

            # Salvando resultado da query e suas listas
            for row in self.query:
                self.id.append(row.id)
                self.produto.append(row.produto)
                self.marca.append(row.marca_produto)
                self.estoqueMinimo.append(row.estoque_minimo)
                self.qtdeProduto.append(row.qtde)
                self.valorUnitario.append(row.valor_unitario)
                self.valorAtacado.append(row.valor_atacado)
                self.qtdeAtacado.append(row.qtde_atacado)

           # Fechando a Conexao
            sessao.close()

            pass

        except IntegrityError as err:

            print(err)

            pass

    # Busca Nome AutoCompete
    def autoCompleteProduto(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(Produto.produto).filter(
                Produto.produto.contains(self.produto)))
            self.query.all()

            # Convertendo variavel em lista
            self.produto = []

            # salvando resultado em lista
            for row in self.query:
                self.produto.append(row.produto)

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Busca produto por Nome Autocomplete

    def buscaProdutoNome(self):

        try:

            # Abrindo a Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(Produto.id, Produto.produto).filter(
                Produto.produto == self.produto).first()

            # Salvando resultado
            self.id = self.query.id

            # Fechando a Conexao
            sessao.close()

            pass
        except:
            self.produto = 'Produto Não Encontrado'
            pass

    # Retirando produto do estoque
    def retiradaEstoque(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando ID Produto
            row = sessao.query(Produto).get(self.id)
            row.qtde = row.qtde - float(self.qtdeProduto)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Entrada Produto no estoque
    def entradaEstoque(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando ID Produto
            row = sessao.query(Produto).get(self.id)
            row.qtde = row.qtde + float(self.qtdeProduto)
            row.valorCompra = self.valorCompra
            row.obs = self.obsProduto

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # LIstar produtos com estoque abaixo do minimo
    def listaEstoqueBaixo(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = sessao.query(Produto).filter(
                Produto.qtde < Produto.estoque_minimo).count()

            # Fechando Sessao
            sessao.close()

        except IntegrityError as err:
            print(err)

        return row

    # Lista total de Produtos

    def totalProdutoCadastrado(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = sessao.query(Produto).count()

            # Fechando Sessao
            sessao.close()

        except IntegrityError as err:
            print(err)

        return row
