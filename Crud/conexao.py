# -*- coding: utf-8 -*-

import mysql.connector
import configparser
import os
import sys


class Conexao(object):
    """docstring for ClassName"""

    def __init__(self, DbHost="", DbName="", DbUser="", DbPassword="", conecta="", erro=""):
        self.DbHost = DbHost
        self.DbName = DbName
        self.DbUser = DbUser
        self.DbPassword = DbPassword
        self.conecta = conecta
        self.erro = erro
        # self.path = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        config = configparser.ConfigParser()
        config.sections()

        if config.read(os.path.join(self.path, 'config.ini')):
            self.DbHost = config['DEFAULT']['DbHost']
            self.DbName = config['DEFAULT']['DbName']
            self.DbUser = config['DEFAULT']['DbUser']
            self.DbPassword = config['DEFAULT']['DbPassword']

        try:
            self.conecta = mysql.connector.connect(
                host=self.DbHost, database=self.DbName, user=self.DbUser, password=self.DbPassword, charset="utf8", use_unicode=True)
            c = self.conecta.cursor()
            c.close()
        except mysql.connector.Error as err:
            self.erro = err


# conecta = Conexao()
# if conecta.erro:
#     print conecta.erro

# config = configparser.ConfigParser()
# config['DEFAULT'] = {'DbHost': '127.0.0.1',
#                      'DbName': 'sistema',
#                      'DbUser': 'andre',
#                      'DbPassword': 'rsp'}

# with open('config.ini', 'w') as configfile:
#     config.write(configfile)
