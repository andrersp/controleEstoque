# -*- coding: utf-8 -*-
from Crud.conexao import Conexao
import mysql.connector


class CrudCatAPagar(object):
    def __init__(self, idCatAPagar="", descCatAPagar=""):
        self.idCatAPagar = idCatAPagar
        self.descCatAPagar = descCatAPagar

    # Ultimo Id Forma de Pagamento
    def lastIdCatAPagar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT id from categoriaAPagar ORDER BY id DESC LIMIT 1 """)
            row = c.fetchone()

            if row:
                self.idCatAPagar = row[0] + 1
            else:
                self.idCatAPagar = 1

            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)
            pass

        return self.idCatAPagar
        pass

    # LIstando formas de pagamento
    def listaCatAPagar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT * FROM categoriaAPagar """)
            row = c.fetchall()

            self.idCatAPagar = []
            self.descCatAPagar = []

            if row:
                for lista in row:
                    self.idCatAPagar.append(lista[0])
                    self.descCatAPagar.append(lista[1])

            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)
            pass

        pass

    # Cadastro forma de pagamento
    def cadCatAPagar(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO categoriaAPagar VALUES ('{}', '{}')
            ON DUPLICATE KEY UPDATE categoria = '{}' """
                      .format(self.idCatAPagar, self.descCatAPagar,
                              self.descCatAPagar))
            conecta.conecta.commit()
            c.close()
            pass
        except mysql.connector.Error as err:
            print(err)
