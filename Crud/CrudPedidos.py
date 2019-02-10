# -*- coding: utf-8 -*-
import mysql.connector
from Crud.conexao import Conexao
import datetime


class CrudPedidos(object):

    def __init__(self, idPedido="", idCliente="", dataEmissao="",
                 prazoEntrega="", dataEntrega="",
                 desconto="", frete="", valorTotal="", valorRecebido="",
                 valorPendente="", idStatusEntrega="", IdStatusPagamento="",
                 statusEntrega="", statusPagamento="",
                 idItem="", idItemTabela="", qtde="", valorItem="",
                 totalItem="", obsItem="", nomeCliente="",
                 telefoneCliente="", itemDescricao="", dataPagamento="",
                 dataFim=""):
        self.idPedido = idPedido
        self.idCliente = idCliente
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
        self.nomeCliente = nomeCliente
        self.telefoneCliente = telefoneCliente
        self.itemDescricao = itemDescricao
        self.dataPagamento = dataPagamento
        self.dataFim = dataFim

    def lastIdPedido(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute("SELECT id FROM pedidos ORDER BY id DESC LIMIT 1")
            row = c.fetchone()
            if row:
                self.idPedido = row[0] + 1
            else:
                self.idPedido = 1
            c.close()
        except mysql.connector.Error as err:
            print(err)
        return self.idPedido

    # LIsta Vendas Tabela
    def ListaVendatabela(self, busca):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        self.idPedido = []
        self.nomeCliente = []
        self.telefoneCliente = []

        self.statusEntrega = []
        self.idStatusEntrega = []
        self.statusPagamento = []
        self.idStatusPagamento = []
        self.valorTotal = []
        self.dataEmissao = []
        self.prazoEntrega = []

        try:
            c.execute(""" SELECT pedidos.id, pedidos.dataEmissao,
                pedidos.prazoEntrega, pedidos.valorTotal, pedidos.statusEntrega,
                pedidos.statusPagamento, pedidos.categoria,  clientes.nome, clientes.celular,
                status_entrega.status_entrega, status_pagamento.status_pagamento
                FROM pedidos 
                INNER JOIN clientes ON pedidos.clienteID = clientes.id
                INNER JOIN status_entrega ON pedidos.statusEntrega = status_entrega.id
                INNER JOIN status_pagamento ON pedidos.statusPagamento = status_pagamento.id
                WHERE clientes.nome LIKE '%{}%' AND categoria = '1'
                AND dataEmissao BETWEEN '{}' AND '{}' 
                ORDER BY pedidos.id DESC""". format(busca, self.dataEmissao, self.dataFim))
            row = c.fetchall()
            if row:
                for linha in row:
                    self.idPedido.append(linha[0])
                    self.dataEmissao.append(
                        datetime.date.strftime(linha[1], "%d/%m/%Y"))
                    self.prazoEntrega.append(
                        datetime.date.strftime(linha[2], "%d/%m/%Y"))
                    self.valorTotal.append(linha[3])
                    self.idStatusEntrega.append(linha[4])
                    self.idStatusPagamento.append(linha[5])
                    self.nomeCliente.append(linha[7])
                    self.telefoneCliente.append(linha[8])
                    self.statusEntrega.append(linha[9])
                    self.statusPagamento.append(linha[10])
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # Selecionando venda por id
    def SelectVendaID(self, id):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" SELECT pedidos.*, clientes.nome, clientes.celular 
                FROM pedidos 
                INNER JOIN clientes ON pedidos.clienteId = clientes.id 
                WHERE pedidos.id = '{}' 
             """.format(id))
            row = c.fetchone()
            if row:
                self.idPedido = row[0]
                self.idCliente = row[1]
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

            self.idItemTabela = []
            self.idItem = []
            self.itemDescricao = []
            self.qtde = []
            self.valorItem = []
            self.totalItem = []
            self.obsItem = []

            c.execute(""" SELECT relacao_pedido.*, produto.descricao 
                FROM relacao_pedido 
                INNER JOIN produto ON relacao_pedido.produto = produto.id
                WHERE relacao_pedido.cod_pedido = '{}' """.format(id))
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

            # c.execute(
            #     """ SELECT sum(valor) FROM contasRecebidas WHERE idPedido = '{}' """
            #     .format(id))
            # row = c.fetchall()
            # if row:
            #     for linha in row:
            #         self.valorRecebido = linha[0]
            c.close()

        except mysql.connector.Error as err:
            print(err)

        pass

    # Cadastro venda
    def CadVenda(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" INSERT INTO pedidos (id, clienteId, dataEmissao, 
                prazoEntrega, desconto, frete, valorTotal, valorPendente, 
                statusPagamento, categoria) 
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
                ON DUPLICATE KEY UPDATE  clienteId='{}', dataEmissao='{}',
                prazoEntrega='{}', desconto='{}', frete='{}', valorTotal='{}', 
                valorPendente='{}'
                """.format(self.idPedido, self.idCliente, self.dataEmissao,
                           self.prazoEntrega, self.desconto, self.frete,
                           self.valorTotal, self.valorPendente,
                           self.statusPagamento, '1',
                           self.idCliente, self.dataEmissao,
                           self.prazoEntrega, self.desconto, self.frete,
                           self.valorTotal, self.valorPendente
                           ))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # Cadastro Itens Pedido
    def CadItensPedido(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ INSERT INTO relacao_pedido VALUES ('{}', '{}', '{}', '{}',
                '{}', '{}', '{}')  ON DUPLICATE KEY UPDATE cod_pedido='{}', 
                produto='{}', qntde='{}', valor='{}', total='{}', obs='{}' """
                .format(self.idItemTabela, self.idPedido, self.idItem,
                        self.qtde, self.valorItem, self.totalItem,
                        self.obsItem,
                        self.idPedido, self.idItem,
                        self.qtde, self.valorItem, self.totalItem,
                        self.obsItem))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)
        pass

    # Cadastro de valor recebido
    def ReceberConta(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ INSERT INTO contasRecebidas VALUES ('{}', '{}', '{}', '{}') 
                """.format('', self.idPedido, self.dataPagamento, self.valorRecebido))

            c.execute(""" SELECT valorPendente from pedidos WHERE id = '{}' """
                      .format(self.idPedido))
            row = c.fetchone()
            if row[0] == 0:
                c.execute(
                    """ UPDATE pedidos SET statusPagamento = 1 
                    WHERE id = '{}' """.format(self.idPedido))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # Entregar Pedido

    def Entregar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(
                """ UPDATE pedidos SET dataEntrega='{}', statusEntrega='{}'
                WHERE id='{}' """.format(self.dataEntrega, '1', self.idPedido))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # delete item
    def DelItem(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """DELETE FROM saida_produto WHERE idRelacao ='{}'"""
                .format(self.idItemTabela))
            c.execute("""DELETE FROM relacao_pedido WHERE id_relacao = '{}' """
                      .format(self.idItemTabela))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    def limpar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute("TRUNCATE TABLE contasRecebidas")
            c.execute("TRUNCATE TABLE pedidos")
            c.execute("TRUNCATE TABLE relacao_pedido")
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)


# busca = CrudPedidos()
# busca.dataEmissao = '2000-10-10'
# busca.dataFim = '2019-01-30'
# busca.ListaVendatabela('')
# print busca.nomeCliente

# print '{}-{}-{}'.format(busca.dataEmissao[8:10], busca.dataEmissao[5:7], busca.dataEmissao[0:4])
# busca.limpar()
# print busca.valorRecebido

# busca.CadContaReceber()
# print busca.nomeCliente
# print busca.itemDescricao
# # busca.DelItem()
