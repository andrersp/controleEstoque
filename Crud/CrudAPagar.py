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
                 fornecedor="", nomeStatus="", telefone="", valorPendente=""):
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
        self.valorPendente = valorPendente

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

    # Cadstar conta a Pagar
    def cadContaPagar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO contasAPagar (id, idCompra, idFornecedor,
              descricao, obs, categoria, vencimento, valor )
              VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
              ON DUPLICATE KEY UPDATE idCompra='{}', idFornecedor='{}',
              descricao='{}', obs='{}', categoria='{}', vencimento='{}',
              valor='{}' """
                      .format(self.idConta, self.idCompra, self.idFornecedor,
                              self.descricao, self.obs, self.categoria,
                              self.dataVencimento, self.valor,
                              self.idCompra, self.idFornecedor,
                              self.descricao, self.obs, self.categoria,
                              self.dataVencimento, self.valor,

                              ))
            conecta.conecta.commit()
            c.close()

        except mysql.connector.Error as err:
            print(err)

    # Pagar conta
    def PagarConta(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" UPDATE  contasAPagar SET formapagamento='{}',
            recebido='{}', 
            valorPago=valorPago + '{}', status='{}' WHERE id='{}' """
                      .format(self.formaPagamento, self.dataPagamento, self.valorPago,
                              self.updateStatusPgto(), self.idConta))
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
            self.valorPendente = []

            row = c.fetchall()

            if row:
                for lista in row:
                    self.idConta.append(lista[0])
                    self.descricao.append(lista[3])
                    self.dataVencimento.append(
                        datetime.date.strftime(lista[6], "%d-%m-%Y"))
                    self.valor.append(lista[7])
                    self.status.append(lista[11])
                    self.fornecedor.append(lista[12])
                    self.telefone.append(lista[13])
                    self.nomeStatus.append(lista[14])
                    self.valorPendente.append(lista[7] - lista[10])
        except mysql.connector.Error as err:
            print(err)

    # Selecionar conta a Pagar por id da conta
    def selectContaId(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT * FROM contasAPagar
                WHERE id = '{}' """
                .format(self.idConta))
            row = c.fetchone()

            if row:
                self.idConta = row[0]
                self.idCompra = row[1]
                self.idFornecedor = row[2]
                self.descricao = row[3]
                self.obs = row[4]
                self.categoria = row[5]
                self.dataVencimento = row[6]
                self.valor = row[7]
                self.formaPagamento = row[8]
                self.dataPagamento = row[9]
                self.valorPago = row[10]
                self.idStatus = row[11]
                self.valorPendente = row[7] - row[10]

        except mysql.connector.Error as err:
            print(err)
