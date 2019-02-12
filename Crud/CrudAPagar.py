# -*- coding: utf-8 *-*
import mysql.connector
from Crud.conexao import Conexao
import datetime


class CrudAPagar(object):

    def __init__(self, idConta="", idFornecedor="", idCompra="", descricao="",
                 obs="",
                 categoria="", dataVencimento="", valor="", formaPagamento="",
                 dataPagamento="", valorPago="", status="",
                 dataInicio="", dataFim="", totalDespesa="", totalAPagar="",
                 fornecedor="", nomeStatus="", telefone=""):
        self.idConta = idConta
        self.idFornecedor = idFornecedor
        self.idCompra = idCompra
        self.descricao = descricao
        self.obs = obs
        self.categoria = categoria
        self.dataVencimento = dataVencimento
        self.valor = valor
        self.formaPagamento = formaPagamento
        self.status = status
        self.dataPagamento = dataPagamento
        self.valorPago = valorPago
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.totalDespesa = totalDespesa
        self.fornecedor = fornecedor
        self.nomeStatus = nomeStatus
        self.telefone = telefone

    def lastIdAPagar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT id from contasAPagar ORDER BY id desc LIMIT 1 """)
            row = c.fetchone()
            if row:
                self.idConta = row[0] + 1
            else:
                self.idConta = 1

            c.close()
        except mysql.connector.Error as err:
            print(err)

        return self.idConta

    def listaStatus(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT * FROM status_pagamento""")
            row = c.fetchall()
            self.idStatus = []
            self.status = []
            if row:
                for lista in row:
                    self.status.append(lista[0])
                    self.nomeStatus.append(lista[1])

        except mysql.connector.Error as err:
            print(err)

    def cadContaPagar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO contasAPagar (id, idCompra, idFornecedor,
              descricao, obs, categoria, vencimento, valor, formapagamento)
              VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
              ON DUPLICATE KEY UPDATE 
              recebido='{}', valorPago= valorPago + '{}', status='{}'"""
                      .format(self.idConta, self.idCompra, self.idFornecedor,
                              self.descricao, self.obs, self.categoria,
                              self.dataVencimento, self.valor, self.formaPagamento,
                              self.dataPagamento, self.valorPago,
                              self.updateStatusPgto()
                              ))

            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    def updateStatusPgto(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT valor, valorPago FROM contasAPagar
            WHERE id = '{}' """.format(self.idConta))

            row = c.fetchone()
            if row:
                self.valor = float(row[0])
                self.valorPago = float(self.valorPago) + float(row[1])
            c.close()
        except mysql.connector.Error as err:
            print(err)

        self.status = 2
        if self.valor <= self.valorPago:
            self.status = 1

        # print(self.status)
        return self.status

    # Seleciona conta pelo código de Compra
    def selectAPagarId(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        self.idConta = []
        self.dataVencimento = []
        self.valor = []
        self.status = []
        self.valorPago = []
        try:
            c.execute(
                """ SELECT * FROM contasAPagar WHERE idCompra = '{}' """.format(self.idCompra))
            row = c.fetchall()
            for lista in row:
                self.idConta.append(lista[0])
                self.dataVencimento.append(lista[6])
                self.valor.append(lista[7])
                self.valorPago.append(lista[10])
                self.status.append(lista[11])

        except mysql.connector.Error as err:
            print(err)

    def listaAPagar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute("""
             SELECT contasAPagar.*, fornecedor.nomeFantasia, fornecedor.telefone, 
             status_pagamento.status_pagamento
             FROM contasAPagar
             INNER JOIN fornecedor ON contasAPagar.idFornecedor = fornecedor.id
             INNER JOIN status_pagamento ON
             contasAPagar.status = status_pagamento.id
             WHERE vencimento BETWEEN '{}' AND '{}' AND status = '{}'
             """.format(self.dataInicio, self.dataFim, self.status))
            self.idConta = []
            self.idCompra = []
            self.idFornecedor = []
            self.descricao = []
            self.obs = []
            self.dataVencimento = []
            self.valor = []
            self.formaPagamento = []
            self.dataPagamento = []
            self.valorPago = []
            self.status = []
            self.fornecedor = []
            self.telefone = []
            self.nomeStatus = []

            row = c.fetchall()

            if row:
                for lista in row:
                    self.idConta.append(lista[0])
                    self.descricao.append(lista[3])
                    self.dataVencimento.append(
                        datetime.date.strftime(lista[6], "%d-%m-%Y"))
                    self.valor.append(lista[7] - lista[10])
                    self.status.append(lista[11])
                    self.fornecedor.append(lista[12])
                    self.telefone.append(lista[13])
                    self.nomeStatus.append(lista[14])
        except mysql.connector.Error as err:
            print(err)


# busca = CrudAPagar()
# busca.dataInicio = '2019-02-01'
# busca.dataFim = '2019-02-28'
# busca.status = 2
# busca.listaAPagar()
# print(busca.fornecedor)
# print(busca.categoria)
# print(busca.movimentoTotalDespesa()[0])
# if busca.movimentoTotalDespesa()[0] > 0.01:
#     print(busca.movimentoTotalDespesa())

# print(busca.totalAPagar)
# data = ("10-01-2018")
# print datetime.date.strftime(datetime.datetime.strptime(data,
# "%d-%m-%Y"), "%Y-%m-%d")
