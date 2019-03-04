# -*- coding: utf-8 -*-

import os
import configparser
import os
import sys


from PySide2.QtGui import QPixmap
import mysql.connector


from Views.mainDbConfig import Ui_ct_dbConf
from Crud.Conexao import CreateDb, CriarTabelas
# from Crud.Conexao import Conexao


class MainDbConf(Ui_ct_dbConf):

    def maindbconf(self, frame):
        super(MainDbConf, self).setDbConf(frame)
        self.fr_dbConf.show()

        # icone padrão
        self.IconeBotaoForm(self.bt_SalvarConfigDB,
                            self.resourcepath('Images/salvar.png'))

        # Botao Teste banco de Dados
        self.bt_TestarConexao.clicked.connect(self.ConfiDbTeste)
        # Botao Salvando Conexao Banco de Dados
        self.bt_SalvarConfigDB.clicked.connect(self.ConfigDbSave)

        # Inserindo Dados Conexao Banco de Dados Caso exista
        config = configparser.ConfigParser()
        config.sections()

        if config.read(os.path.join(self.caminho, 'config.ini')):
            self.tx_IpServer.setText(config['DEFAULT']['DbHost'])
            self.tx_DbName.setText(config['DEFAULT']['DbName'])
            self.tx_DbUser.setText(config['DEFAULT']['DbUser'])
            self.tx_DbPass.setText(config['DEFAULT']['DbPassword'])

    #  Testar Configuração

    def ConfiDbTeste(self):
        conecta = ConexaoTeste()

        conecta.DbHost = str(self.tx_IpServer.text())
        conecta.DbName = str(self.tx_DbName.text())
        conecta.DbUser = str(self.tx_DbUser.text())
        conecta.DbPassword = str(self.tx_DbPass.text())

        self.lb_status_db.clear()
        self.lb_status_senha.clear()
        self.lb_status_user.clear()

        try:
            conecta.conectar()

            if not conecta.erro:
                self.lb_StatusTesteDb.setPixmap(
                    QPixmap(self.resourcepath('Images/Sucesso.png')))
                self.lb_status_db.setPixmap(
                    QPixmap(self.resourcepath('Images/Sucesso.png')))
                self.lb_status_user.setPixmap(
                    QPixmap(self.resourcepath('Images/Sucesso.png')))
                self.lb_status_senha.setPixmap(
                    QPixmap(self.resourcepath('Images/Sucesso.png')))
                self.lb_StatusTesteDb.setScaledContents(True)
                self.bt_SalvarConfigDB.setEnabled(True)

            elif conecta.erro == 1:
                self.lb_status_user.setText("Erro de Usuaŕio ou Senha")
                self.lb_status_senha.setText("Erro de Usuaŕio ou Senha")
                self.lb_StatusTesteDb.setPixmap(
                    QPixmap(self.resourcepath('Images/Fail.png')))
                self.lb_StatusTesteDb.setScaledContents(True)
            elif conecta.erro == 2:
                self.lb_status_db.setText("O banco de dados será criado")
                self.lb_StatusTesteDb.setPixmap(
                    QPixmap(self.resourcepath('Images/Sucesso.png')))

                self.lb_status_user.setPixmap(
                    QPixmap(self.resourcepath('Images/Sucesso.png')))
                self.lb_status_senha.setPixmap(
                    QPixmap(self.resourcepath('Images/Sucesso.png')))
                self.lb_StatusTesteDb.setScaledContents(True)
                self.bt_SalvarConfigDB.setEnabled(True)

        except:

            self.lb_StatusTesteDb.setPixmap(
                QPixmap(self.resourcepath('Images/Fail.png')))
            self.lb_StatusTesteDb.setScaledContents(True)

    # Salvar Configuracao
    def ConfigDbSave(self):

        DbHost = str(self.tx_IpServer.text())
        DbName = str(self.tx_DbName.text())
        DbUser = str(self.tx_DbUser.text())
        DbPassword = str(self.tx_DbPass.text())
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'DbHost': DbHost,
                             'DbName': DbName,
                             'DbUser': DbUser,
                             'DbPassword': DbPassword}
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        with open(os.path.join(path, 'config.ini'), 'w') as configfile:
            config.write(configfile)
        CreateDb().createDB()
        CriarTabelas().tabelas()
        self.janelaConfig()


class ConexaoTeste(object):

    def __init__(self, DbHost="", DbName="", DbUser="", DbPassword="", conecta="", erro=""):
        self.DbHost = DbHost
        self.DbName = DbName
        self.DbUser = DbUser
        self.DbPassword = DbPassword
        self.conecta = conecta
        self.erro = erro

    def conectar(self):
        try:
            # print config.sections()
            self.conecta = mysql.connector.connect(
                host=self.DbHost, database=self.DbName, user=self.DbUser, password=self.DbPassword, charset="utf8", use_unicode=True)
            c = self.conecta.cursor()
            c.close()

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                self.erro = 1  # Erro User e Senha
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.erro = 2  # erro banco de dados inexistente
            else:
                print(err)
