# coding=utf-8
import sys
import os
import configparser

from sqlalchemy.exc import ProgrammingError

from sql.core import Conexao, Base
import sql.Models


class CreateDb(object):
    def __init__(self, dbhandler="", DbHost="", DbName="", DbUser="",
                 DbPassword="", conecta="", erro=""):
        self.DbHost = DbHost
        self.DbName = DbName
        self.DbUser = DbUser
        self.DbPassword = DbPassword
        self.conecta = conecta
        self.erro = erro
        self.dbhandler = dbhandler

        # Caminho absoluto config.ini
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        config = configparser.ConfigParser()
        config.sections()

        # Buscando Dados config.ini
        if config.read(os.path.join(self.path, 'config.ini')):
            self.DbHost = config['DEFAULT']['DbHost']
            self.DbName = config['DEFAULT']['DbName']
            self.DbUser = config['DEFAULT']['DbUser']
            self.DbPassword = config['DEFAULT']['DbPassword']

    def createDB(self):

        # Caso banco não exista, Cria
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                user=self.DbUser, password=self.DbPassword, host=self.DbHost)
            cursor = conn.cursor()
            cursor.execute('SET sql_notes = 0 ;')
            cursor.execute("create database IF NOT EXISTS %s" %
                           self.DbName)
            # tabelas = CriarTabelas()
            # self.tabelas()

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                self.erro = 1  # Erro User e Senha
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.erro = 2  # erro banco de dados inexistente
            else:
                self.erro == err

    def tabelas(self):
        conecta = Conexao()

        try:

            Base.metadata.create_all(conecta.engine)
        except ProgrammingError as err:
            print(err)
