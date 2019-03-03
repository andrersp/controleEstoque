# -*- coding: utf-8 -*-
from conexao import Conexao
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
            SELECT COALESCE(SUM(valor), 0) FROM conta_a_receber
            WHERE data_vencimento BETWEEN '{}' AND '{}'
            """.format(self.dataInicio, self.dataFim))
            row = c.fetchone()
            self.totaAReceber = []

            if row:
                self.totaAReceber = row[0]

            c.execute(""" 
            SELECT COALESCE(SUM(valor_recebido), 0) FROM conta_a_receber
            WHERE data_recebimento BETWEEN '{}' AND '{}'
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
             FROM conta_a_receber
             INNER JOIN categoriaAReceber ON
             conta_a_receber.categoria = categoriaAReceber.id
             WHERE recebido BETWEEN '{}' AND '{}'
             GROUP BY conta_a_receber.categoria
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
            SELECT COALESCE(SUM(valor), 0) FROM conta_a_pagar
            WHERE vencimento BETWEEN '{}' AND '{}'
            """.format(self.dataInicio, self.dataFim))
            row = c.fetchone()
            self.totaAPagar = []

            if row:
                self.totaAPagar = row[0]

            c.execute(""" 
            SELECT COALESCE(SUM(valorPago), 0) FROM conta_a_pagar
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
             FROM conta_a_pagar
             INNER JOIN categoriaAPagar ON
             conta_a_pagar.categoria = categoriaAPagar.id
             WHERE recebido BETWEEN '{}' AND '{}'
             GROUP BY conta_a_pagar.categoria
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


busca = CrudMovCaixa()
busca.dataInicio = '2019-03-01'
busca.dataFim = '2019-03-28'
busca.movEntrada()
print(busca.totaAReceber, busca.totalRecebido)
