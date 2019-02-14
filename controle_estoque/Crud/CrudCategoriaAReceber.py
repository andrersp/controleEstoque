# -*- coding: utf-8 -*-
from Crud.conexao import Conexao
import mysql.connector


class CrudCatAReceber(object):
    def __init__(self, idCatAReceber="", descCatAReceber=""):
        self.idCatAReceber = idCatAReceber
        self.descCatAReceber = descCatAReceber

    # Ultimo Id Forma de Pagamento
    def lastIdCatAReceber(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT id from categoriaAReceber ORDER BY id DESC LIMIT 1 """)
            row = c.fetchone()

            if row:
                self.idCatAReceber = row[0] + 1
            else:
                self.idCatAReceber = 1

            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)
            pass

        return self.idCatAReceber
        pass

    # LIstando formas de pagamento
    def listaCatAReceber(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT * FROM categoriaAReceber """)
            row = c.fetchall()

            self.idCatAReceber = []
            self.descCatAReceber = []

            if row:
                for lista in row:
                    self.idCatAReceber.append(lista[0])
                    self.descCatAReceber.append(lista[1])

            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)
            pass

        pass

    # Cadastro forma de pagamento
    def cadCatAReceber(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO categoriaAReceber VALUES ('{}', '{}')
            ON DUPLICATE KEY UPDATE categoria = '{}' """
                      .format(self.idCatAReceber, self.descCatAReceber,
                              self.descCatAReceber))
            conecta.conecta.commit()
            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)
