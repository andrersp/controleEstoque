# -*- coding: utf-8 -*-
from Crud.conexao import Conexao
import mysql.connector


class CrudFormaPagamento(object):
    def __init__(self, idFPagamento="", descFPagamento=""):
        self.idFPagamento = idFPagamento
        self.descFPagamento = descFPagamento

    # Ultimo Id Forma de Pagamento
    def lastIdFPagamento(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT id from formaPagamento ORDER BY id DESC LIMIT 1 """)
            row = c.fetchone()

            if row:
                self.idFPagamento = row[0] + 1
            else:
                self.idFPagamento = 1

            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)
            pass

        return self.idFPagamento

    # LIstando formas de pagamento

    def listaFPagamento(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT * FROM formaPagamento """)
            row = c.fetchall()

            self.idFPagamento = []
            self.descFPagamento = []

            if row:
                for lista in row:
                    self.idFPagamento.append(lista[0])
                    self.descFPagamento.append(lista[1])

            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)
            pass

        pass

    # Cadastro forma de pagamento
    def cadFPagamento(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO formaPagamento VALUES ('{}', '{}')
            ON DUPLICATE KEY UPDATE categoria = '{}' """
                      .format(self.idFPagamento, self.descFPagamento,
                              self.descFPagamento))
            conecta.conecta.commit()
            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)


# busca = CrudFormaPagamento()
# busca.idFPagamento = 3
# busca.descFPagamento = "CARTÃO"
# busca.cadFPagamento()
