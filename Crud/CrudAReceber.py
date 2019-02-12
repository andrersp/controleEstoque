# -*- coding: utf-8 *-*
import mysql.connector
from Crud.conexao import Conexao
import datetime


class CrudAReceber(object):

    def __init__(self, idConta="", idCliente="", idVenda="", descricao="", obs="",
                 categoria="", dataVencimento="", valor="", formaPagamento="",
                 dataRecebimento="", valorRecebido="", idStatus="", dataInicio="",
                 dataFim="", totalReceita="", totalAReceber="", categoriaID="",
                 cliente="", telefoneCliente="", status=""):
        self.idConta = idConta
        self.idCliente = idCliente
        self.idVenda = idVenda
        self.descricao = descricao
        self.obs = obs
        self.categoria = categoria
        self.categoriaID = categoriaID
        self.dataVencimento = dataVencimento
        self.valor = valor
        self.formaPagamento = formaPagamento
        self.idStatus = idStatus
        self.dataRecebimento = dataRecebimento
        self.valorRecebido = valorRecebido
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.totalReceita = totalReceita
        self.cliente = cliente
        self.telefoneCliente = telefoneCliente
        self.status = status

    def lastIdAReceber(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT id from contasAReceber ORDER BY id desc LIMIT 1 """)
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
                    self.idStatus.append(lista[0])
                    self.status.append(lista[1])

        except mysql.connector.Error as err:
            print(err)

    # Cadastro Conta a Receber
    def cadContaReceber(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO contasAReceber (id, idVenda, idCliente,
              descricao, obs, categoria, vencimento, valor, formapagamento)
              VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
              ON DUPLICATE KEY UPDATE
              recebido='{}', valorRecebido= valorRecebido + '{}', status='{}'"""
                      .format(self.idConta, self.idVenda, self.idCliente,
                              self.descricao, self.obs, self.categoria,
                              self.dataVencimento, self.valor, self.formaPagamento,
                              self.dataRecebimento, self.valorRecebido,
                              self.updateStatus()
                              ))
            conecta.conecta.commit()
            c.close()

        except mysql.connector.Error as err:
            print(err)

    # Update no status caso o valor recebido seja igual ou maior que o devedor
    def updateStatus(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT valor, valorRecebido FROM contasAReceber
            WHERE id = '{}' """.format(self.idConta))

            row = c.fetchone()
            if row:
                self.valor = float(row[0])
                self.valorRecebido = float(self.valorRecebido) + float(row[1])
            c.close()
        except mysql.connector.Error as err:
            print(err)

        self.idStatus = 2
        if self.valor <= self.valorRecebido:
            self.idStatus = 1

        return self.idStatus

    # Busca parcelas por ID da Venda
    def selectAReceberId(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT * FROM contasAReceber WHERE idVenda = '{}' """
                .format(self.idVenda))
            row = c.fetchall()

            self.idConta = []
            self.idVenda = []
            self.idCliente = []
            self.descricao = []
            self.obs = []
            self.categoria = []
            self.dataVencimento = []
            self.valor = []
            self.formaPagamento = []
            self.dataRecebimento = []
            self.valorRecebido = []
            self.idStatus = []

            for lista in row:
                self.idConta.append(lista[0])
                self.idVenda.append(lista[1])
                self.idCliente.append(lista[2])
                self.descricao.append(lista[3])
                self.obs.append(lista[4])
                self.categoria.append(lista[5])
                self.dataVencimento.append(lista[6])
                self.valor.append(lista[7])
                self.formaPagamento.append(lista[8])
                self.dataRecebimento.append(lista[9])
                self.valorRecebido.append(lista[10])
                self.idStatus.append(lista[11])

        except mysql.connector.Error as err:
            print(err)
    # Tabela contas a Receber

    def listaAReceber(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute("""
             SELECT contasAReceber.*, clientes.nome, clientes.celular, 
             categoriaAReceber.categoria, status_pagamento.status_pagamento
             FROM contasAReceber
             INNER JOIN clientes ON contasAReceber.idCliente = clientes.id
             INNER JOIN categoriaAReceber ON
             contasAReceber.categoria = categoriaAReceber.id
             INNER JOIN status_pagamento ON
             contasAReceber.status = status_pagamento.id
             WHERE vencimento BETWEEN '{}' AND '{}' AND status = '{}'
             """.format(self.dataInicio, self.dataFim, self.idStatus))
            self.idConta = []
            self.idVenda = []
            self.idCliente = []
            self.descricao = []
            self.obs = []
            self.categoria = []
            self.dataVencimento = []
            self.valor = []
            self.formaPagamento = []
            self.dataRecebimento = []
            self.valorRecebido = []
            self.idStatus = []
            self.cliente = []
            self.telefoneCliente = []
            self.status = []
            row = c.fetchall()

            if row:
                for lista in row:
                    self.idConta.append(lista[0])
                    self.descricao.append(lista[3])
                    self.dataVencimento.append(
                        datetime.date.strftime(lista[6], "%d-%m-%Y"))
                    self.valor.append(lista[7] - lista[10])
                    self.idStatus.append(lista[11])
                    self.cliente.append(lista[12])
                    self.telefoneCliente.append(lista[13])
                    self.status.append(lista[15])
        except mysql.connector.Error as err:
            print(err)


# busca = CrudAReceber()
# busca.listaStatus()
# print(busca.status)
# busca.dataInicio = '2019-02-01'
# busca.dataFim = '2019-03-28'
# busca.idStatus = 2
# busca.listaAReceber()
# print(busca.idConta)
# print(busca.cliente)
# print(busca.descricao)
# print(busca.idStatus)

# print(busca.dataVencimento)
# i = 0
# while i < len(busca.totalReceita):
#     print(busca.totalReceita[i])
#     print(busca.categoria[i])
#     i += 1


# print(busca.totalReceita)
# print(busca.categoria)
# busca.idConta = 4
# print(busca.updateidStatus())
# # busca.selectAReceberId()
# # print busca.dataVencimento
# # print busca.lastIdAReceber()
# # data = ("10-01-2018")
# # print datetime.date.strftime(datetime.datetime.strptime(data,
# # "%d-%m-%Y"), "%Y-%m-%d")

# conecta = Conexao()
# c = conecta.conecta.cursor()

# try:
#     c.execute(""" SELECT clientes.nome
#     FROM clientes WHERE nome LIKE '%{}%'
#     UNION ALL
#     SELECT fornecedor.nomeFantasia
#     FROM fornecedor WHERE nomeFantasia LIKE '%{}%'
#     """.format('Sandra', 'Sandra'))
#     row = c.fetchall()
#     nome = []
#     for lista in row:
#         nome.append(lista[0])
# except mysql.connector.Error as err:
#     print(err)

# print(nome)
