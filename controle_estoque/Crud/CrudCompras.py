# -*- coding: utf-8 -*-
import mysql.connector
from Crud.conexao import Conexao
import datetime


class CrudCompras(object):

    def __init__(self, idCompra="", idFornecedor="", dataEmissao="",
                 prazoEntrega="", dataEntrega="",
                 desconto="", frete="", valorTotal="", valorRecebido="",
                 valorPendente="", idStatusEntrega="", IdStatusPagamento="",
                 statusEntrega="", statusPagamento="",
                 idItem="", idItemTabela="", qtde="", valorItem="",
                 totalItem="", obsItem="", NomeFantasia="",
                 telefoneCliente="", itemDescricao="", dataPagamento="",
                 dataFim="", categoria=""):
        self.idCompra = idCompra
        self.idFornecedor = idFornecedor
        self.dataEmissao = dataEmissao
        self.prazoEntrega = prazoEntrega
        self.dataEntrega = dataEntrega
        self.desconto = desconto
        self.frete = frete
        self.valorTotal = valorTotal
        self.valorRecebido = valorRecebido
        self.valorPendente = valorPendente
        self.statusEntrega = statusEntrega
        self.idStatusEntrega = idStatusEntrega
        self.IdStatusPagamento = IdStatusPagamento
        self.statusPagamento = statusPagamento
        self.idItem = idItem
        self.idItemTabela = idItemTabela
        self.qtde = qtde
        self.valorItem = valorItem
        self.totalItem = totalItem
        self.obsItem = obsItem
        self.NomeFantasia = NomeFantasia
        self.telefoneCliente = telefoneCliente
        self.itemDescricao = itemDescricao
        self.dataPagamento = dataPagamento
        self.dataFim = dataFim
        self.categoria = categoria

    def lastIdCompra(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute("SELECT id FROM compras ORDER BY id DESC LIMIT 1")
            row = c.fetchone()
            if row:
                self.idCompra = row[0] + 1
            else:
                self.idCompra = 1
            c.close()
        except mysql.connector.Error as err:
            print(err)
        return self.idCompra

    # LIsta Compras Tabela
    def ListaCompratabela(self, busca):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        self.idCompra = []
        self.NomeFantasia = []
        self.telefoneCliente = []

        self.statusEntrega = []
        self.idStatusEntrega = []
        self.statusPagamento = []
        self.idStatusPagamento = []
        self.valorTotal = []
        self.dataEmissao = []
        self.prazoEntrega = []

        try:
            c.execute(""" SELECT compras.id, compras.dataEmissao,
                compras.prazoEntrega, compras.valorTotal, compras.statusEntrega,
                compras.statusPagamento,  fornecedor.nomeFantasia, fornecedor.telefone,
                status_entrega.status_entrega, status_pagamento.status_pagamento
                FROM compras 
                INNER JOIN fornecedor ON compras.fornecedorId = fornecedor.id
                INNER JOIN status_entrega ON compras.statusEntrega = status_entrega.id
                INNER JOIN status_pagamento ON compras.statusPagamento = status_pagamento.id
                WHERE fornecedor.nomeFantasia LIKE '%{}%' AND categoria = '1'
                AND dataEmissao BETWEEN '{}' AND '{}'
                ORDER BY compras.id DESC""". format(busca, self.dataEmissao, self.dataFim))
            row = c.fetchall()
            if row:
                for linha in row:
                    self.idCompra.append(linha[0])
                    self.dataEmissao.append(
                        datetime.date.strftime(linha[1], "%d/%m/%Y"))
                    self.prazoEntrega.append(
                        datetime.date.strftime(linha[2], "%d/%m/%Y"))
                    self.valorTotal.append(linha[3])
                    self.idStatusEntrega.append(linha[4])
                    self.idStatusPagamento.append(linha[5])
                    self.NomeFantasia.append(linha[6])
                    self.telefoneCliente.append(linha[7])
                    self.statusEntrega.append(linha[8])
                    self.statusPagamento.append(linha[9])
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # Selecionando Compra por id
    def SelectCompraId(self, id):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" SELECT compras.*,  status_entrega.status_entrega,
                status_pagamento.status_pagamento
                FROM compras 
                INNER JOIN status_entrega ON 
                compras.statusEntrega = status_entrega.id 
                INNER JOIN status_pagamento ON 
                compras.statusPagamento = status_pagamento.id 
                WHERE compras.id = '{}'
             """.format(id))
            row = c.fetchone()
            if row:
                self.idCompra = row[0]
                self.idFornecedor = row[1]
                self.dataEmissao = row[2]
                self.prazoEntrega = row[3]
                self.dataEntrega = row[4]
                self.desconto = row[5]
                self.frete = row[6]
                self.valorTotal = row[7]
                self.valorRecebido = row[8]
                self.valorPendente = row[9]
                self.statusEntrega = row[10]
                self.statusPagamento = row[11]
                self.idStatusEntrega = row[13]
                self.idStatusPagamento = row[14]

            self.idItemTabela = []
            self.idItem = []
            self.itemDescricao = []
            self.qtde = []
            self.valorItem = []
            self.totalItem = []
            self.obsItem = []

            c.execute(""" SELECT relacao_compra.*, produto.descricao 
                FROM relacao_compra 
                INNER JOIN produto ON relacao_compra.produto = produto.id
                WHERE relacao_compra.cod_compra = '{}' """.format(id))
            row = c.fetchall()
            if row:
                for linha in row:
                    self.idItemTabela.append(linha[0])
                    self.idItem.append(linha[2])
                    self.qtde.append(linha[3])
                    self.valorItem.append(linha[4])
                    self.totalItem.append(linha[5])
                    self.obsItem.append(linha[6])
                    self.itemDescricao.append(linha[7])

            c.close()

        except mysql.connector.Error as err:
            print(err)

        pass

    # Cadastro Compra
    def CadCompra(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" INSERT INTO compras (id, fornecedorId, dataEmissao, 
                prazoEntrega, desconto, frete, valorTotal, valorPendente, 
                statusPagamento, categoria) 
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
                ON DUPLICATE KEY UPDATE  fornecedorId='{}', dataEmissao='{}',
                prazoEntrega='{}', desconto='{}', frete='{}', valorTotal='{}', 
                valorPendente='{}', statusPagamento='{}'
                """.format(self.idCompra, self.idFornecedor, self.dataEmissao,
                           self.prazoEntrega, self.desconto, self.frete,
                           self.valorTotal, self.valorPendente,
                           self.statusPagamento, '1',
                           self.idFornecedor, self.dataEmissao,
                           self.prazoEntrega, self.desconto, self.frete,
                           self.valorTotal, self.valorPendente, self.statusPagamento))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # Cadastro Itens Pedido
    def CadItensCompra(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ INSERT INTO relacao_compra VALUES ('{}', '{}', '{}', '{}',
                '{}', '{}', '{}')  ON DUPLICATE KEY UPDATE cod_compra='{}', 
                produto='{}', qntde='{}', valor='{}', total='{}', obs='{}' """
                .format(self.idItemTabela, self.idCompra, self.idItem,
                        self.qtde, self.valorItem, self.totalItem,
                        self.obsItem,
                        self.idCompra, self.idItem,
                        self.qtde, self.valorItem, self.totalItem,
                        self.obsItem))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)
        pass

    # Cadastro de valor recebido
    def PagarConta(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ INSERT INTO contasPagas VALUES ('{}', '{}', '{}', '{}') 
                """.format('', self.idCompra, self.dataPagamento, self.valorRecebido))

            c.execute(""" SELECT valorPendente from compras WHERE id = '{}' """
                      .format(self.idCompra))
            row = c.fetchone()

            if row[0] == 0:
                c.execute(
                    """ UPDATE compras SET statusPagamento = 1 
                    WHERE id = '{}' """.format(self.idCompra))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # Receber Pedido

    def ReceberProduto(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(
                """ UPDATE compras SET dataEntrega='{}', statusEntrega='{}'
                WHERE id='{}' """.format(self.dataEntrega, '1', self.idCompra))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

        # delete item
    def DelItem(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute("""DELETE FROM relacao_compra WHERE id_relacao = '{}' """
                      .format(self.idItemTabela))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    def limpar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            # c.execute("TRUNCATE TABLE clientes")
            c.execute("TRUNCATE TABLE contasAPagar")
            c.execute("TRUNCATE TABLE contasAReceber")
            c.execute("TRUNCATE TABLE compras")
            c.execute("TRUNCATE TABLE relacao_compra")
            c.execute("TRUNCATE TABLE relacao_pedido")
            c.execute("TRUNCATE TABLE entrada_produto")
            c.execute("TRUNCATE TABLE saida_produto")
            # c.execute("TRUNCATE TABLE produto")
            c.execute("TRUNCATE TABLE pedidos")
            conecta.conecta.commit()
            c.close()
        except mysq.connector.Error as err:
            print(err)


# busca = CrudCompras()
# busca.limpar()
# print busca.valorRecebido

# busca.CadContaReceber()
# print busca.NomeFantasia
# print busca.itemDescricao
# # busca.DelItem()
