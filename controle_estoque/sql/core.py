# coding=utf-8
import sys
import os
import configparser


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InterfaceError


class Conexao(object):
    def __init__(self, DbHost='', DbName='', DbUser='', DbPassword='',
                 engine='', Base='', Session=''):
        self.DbHost = DbHost
        self.DbName = DbName
        self.DbUser = DbUser
        self.DbPassword = DbPassword
        self.engine = engine
        self.Base = Base
        self.Session = Session

        # # Caminho absoluto config.ini
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        config = configparser.ConfigParser()
        config.sections()

        # Buscando Dados config.ini
        if config.read(os.path.join(path, 'config.ini')):
            self.DbHost = config['DEFAULT']['DbHost']
            self.DbName = config['DEFAULT']['DbName']
            self.DbUser = config['DEFAULT']['DbUser']
            self.DbPassword = config['DEFAULT']['DbPassword']
        else:
            DbHost = ''
            DbName = ''
            DbUser = ''
            DbPassword = ''

        # Engine
        self.engine = create_engine(
            'mysql+mysqlconnector://{}:{}@{}/{}?charset=utf8'
            .format(self.DbUser, self.DbPassword,
                    self.DbHost, self.DbName),
            echo=True)

        # Criando Sessao
        self.Session = sessionmaker(bind=self.engine)

        # Declarando Base
        self.Base = declarative_base()


Base = declarative_base()
