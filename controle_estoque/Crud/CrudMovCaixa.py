# -*- coding: utf-8 -*-
from Crud.conexao import Conexao
import mysql.connector


class CrudMovCaixa(object):
    def __init__(self, dataInicio="", dataFim="", totalRecebido="",
                 totaAReceber="", totalPago="", totalAPagar="", categoria=""):
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.totalRecebido = totalRecebido
        self.totaAReceber = totaAReceber
        self.totalPago = totalPago
        self.totalAPagar = totalAPagar
        self.categoria = categoria

    def movEntrada(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" 
            SELECT COALESCE(SUM(valor), 0) FROM contasAReceber
            WHERE vencimento BETWEEN '{}' AND '{}'
            """.format(self.dataInicio, self.dataFim))
            row = c.fetchone()
            self.totaAReceber = []

            if row:
                self.totaAReceber = row[0]

            c.execute(""" 
            SELECT COALESCE(SUM(valorRecebido), 0) FROM contasAReceber
            WHERE recebido BETWEEN '{}' AND '{}'
            """.format(self.dataInicio, self.dataFim))
            row = c.fetchone()
            if row:
                self.totalRecebido = row[0]
            c.close()
            pass

        except mysql.connector.Error as err:
            print(err)
            pass

    def detalheReceita(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" SELECT sum(valorRecebido),
             categoriaAReceber.categoria
             FROM contasAReceber
             INNER JOIN categoriaAReceber ON
             contasAReceber.categoria = categoriaAReceber.id
             WHERE recebido BETWEEN '{}' AND '{}'
             GROUP BY contasAReceber.categoria
             """.format(self.dataInicio, self.dataFim))

            self.totalRecebido = []
            self.categoria = []

            row = c.fetchall()

            if row:
                for lista in row:
                    self.totalRecebido.append(lista[0])
                    self.categoria.append(lista[1])

            pass
        except mysql.connector.Error as err:
            print(err)
            pass

    def movDespesa(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" 
            SELECT COALESCE(SUM(valor), 0) FROM contasAPagar
            WHERE vencimento BETWEEN '{}' AND '{}'
            """.format(self.dataInicio, self.dataFim))
            row = c.fetchone()
            self.totaAPagar = []

            if row:
                self.totaAPagar = row[0]

            c.execute(""" 
            SELECT COALESCE(SUM(valorPago), 0) FROM contasAPagar
            WHERE recebido BETWEEN '{}' AND '{}'
            """.format(self.dataInicio, self.dataFim))
            row = c.fetchone()
            if row:
                self.totalPago = row[0]
            c.close()
            pass

        except mysql.connector.Error as err:
            print(err)
            pass

    def detalheDespesa(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(""" SELECT sum(valorPago),
             categoriaAPagar.categoria
             FROM contasAPagar
             INNER JOIN categoriaAPagar ON
             contasAPagar.categoria = categoriaAPagar.id
             WHERE recebido BETWEEN '{}' AND '{}'
             GROUP BY contasAPagar.categoria
             """.format(self.dataInicio, self.dataFim))

            self.totalPago = []
            self.categoria = []

            row = c.fetchall()

            if row:
                for lista in row:
                    self.totalPago.append(lista[0])
                    self.categoria.append(lista[1])

            pass
        except mysql.connector.Error as err:
            print(err)
            pass


# busca = CrudMovCaixa()
# busca.dataInicio = '2019-02-01'
# busca.dataFim = '2019-02-28'
# busca.detalheDespesa()
# print(busca.totalPago, busca.categoria)
