# -*- coding: utf-8 -*-
import configparser
import os
import sys
import re
import base64

from PySide2.QtCore import QByteArray, QBuffer, Qt
from PySide2.QtWidgets import QFileDialog
from PySide2.QtGui import QPixmap
from Views.mainConfig import Ui_ct_MainConfig
import mysql.connector

from orm.Conexao import CreateDb, CriarTabelas


from orm.CrudEmpresa import CrudEmpresa


class MainConfig(Ui_ct_MainConfig):

    def mainconfig(self, frame):
        super(MainConfig, self).setMainConfig(frame)
        self.frameMainConfig.show()

        # Icone Botoes
        self.IconeBotaoMenu(self.bt_AddLogo,
                            self.resourcepath('Images/edit-add.png'))
        self.IconeBotaoMenu(self.bt_DelLogo,
                            self.resourcepath('Images/edit-delete.png'))
        self.IconeBotaoMenu(self.bt_LocalizaCepEmpresa,
                            self.resourcepath('Images/search.png'))

        self.IconeBotaoForm(self.bt_SalvarDadosEmpresa,
                            self.resourcepath('Images/salvar.png'))
        self.IconeBotaoForm(self.bt_SalvarConfigDB,
                            self.resourcepath('Images/salvar.png'))

        # Hidden id input
        self.tx_idEmpresa.setHidden(True)
        # Hidden bt Del Logo
        self.bt_DelLogo.setHidden(True)
        # Desabilitar Salvar Antes de Testar Conf DB
        self.bt_SalvarConfigDB.setDisabled(True)

        # Botao Add Logo
        self.bt_AddLogo.clicked.connect(self.UploadLogo)
        # Botao Del Logo
        self.bt_DelLogo.clicked.connect(self.DelLogo)

        # # Caminho Absoluto
        # self.caminho = os.path.abspath(os.path.dirname(sys.argv[0]))
        # if not os.path.isdir(os.path.join(self.caminho, 'Uploads')):
        #     os.mkdir(os.path.join(self.caminho, 'Uploads'))

    # Inserindo Dados Conexao Banco de Dados Caso exista
        config = configparser.ConfigParser()
        config.sections()

        if config.read(os.path.join(self.caminho, 'config.ini')):
            self.tx_IpServer.setText(config['DEFAULT']['DbHost'])
            self.tx_DbName.setText(config['DEFAULT']['DbName'])
            self.tx_DbUser.setText(config['DEFAULT']['DbUser'])
            self.tx_DbPass.setText(config['DEFAULT']['DbPassword'])

        # Botao Teste banco de Dados
        self.bt_TestarConexao.clicked.connect(self.ConfiDbTeste)
        # Botao Salvando Conexao Banco de Dados
        self.bt_SalvarConfigDB.clicked.connect(self.ConfigDbSave)

        # Botao salvar Empresa
        self.bt_SalvarDadosEmpresa.clicked.connect(self.CadEmpresa)

        # # Set ID Empresa
        self.LastIdEmpresa()

    # upload Logo
    def UploadLogo(self):
        Dialog = QFileDialog()
        Dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        fname = Dialog.getOpenFileName(
            self, "Selecionar Logo", "", "Image files (*.jpg *.png)")[0]

        self.lb_LogoEmpresa.setPixmap(QPixmap(fname).scaledToWidth(
            300, Qt.TransformationMode(Qt.FastTransformation)))
        # self.lb_LogoEmpresa.setScaledContents(True)
        self.bt_AddLogo.setHidden(True)
        self.bt_DelLogo.setVisible(True)

    def DelLogo(self):
        self.lb_LogoEmpresa.clear()
        self.bt_DelLogo.setHidden(True)
        self.bt_AddLogo.setVisible(True)

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
        CreateDb().CreateDB()
        CriarTabelas().tabelas()
        self.janelaConfig()

    def LastIdEmpresa(self):
        try:
            busca = CrudEmpresa()
            self.tx_idEmpresa.setText(str(busca.lastIdEmpresa()))
            self.SelectEmpresa()
        except:
            self.tx_idEmpresa.setText(str(1))

    def SelectEmpresa(self):
        busca = CrudEmpresa()
        busca.idEmpresa = self.tx_idEmpresa.text()
        busca.SelectEmpresaId()
        self.tx_idEmpresa.setText(str(busca.id))
        self.tx_NomeFantasia.setText(busca.nomeFantasia)
        self.tx_RazaoSocial.setText(busca.razaoSocial)
        self.tx_Cnpj.setText(str(busca.cnpj))
        self.tx_IE.setText(str(busca.inscEstadual))
        self.tx_TelefoneEmpresa.setText(str(busca.telefone))
        self.tx_SiteEmpresa.setText(busca.site)
        self.tx_EmailEmpresa.setText(busca.email)
        self.tx_ObsEmpresa.setText(busca.obs)
        self.tx_CepEmpresa.setText(busca.cep)
        self.tx_Endereco.setText(busca.endereco)
        self.tx_NumEmpresa.setText(str(busca.numero))
        self.tx_BairroEmpresa.setText(busca.bairro)
        self.tx_CidadeEmpresa.setText(busca.cidade)
        self.tx_EstadoEmpresa.setText(busca.estado)
        self.tx_Titulo.setText(busca.titulo)
        self.tx_SubTitulo.setText(busca.subtitulo)
        if busca.logo:
            self.bt_AddLogo.setHidden(True)
            self.bt_DelLogo.setVisible(True)
            # print busca.logo
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(
                busca.logo))
            self.lb_LogoEmpresa.setPixmap(pixmap.scaledToWidth(
                300, Qt.TransformationMode(Qt.FastTransformation)))

        pass

    # Cadastrando Empresa

    def CadEmpresa(self):
        INSERI = CrudEmpresa()
        INSERI.id = self.tx_idEmpresa.text()
        INSERI.nomeFantasia = self.tx_NomeFantasia.text().upper()
        INSERI.razaoSocial = self.tx_RazaoSocial.text().upper()
        INSERI.cnpj = self.tx_Cnpj.text()
        INSERI.inscEstadual = self.tx_IE.text()
        INSERI.telefone = re.sub(
            '[^[0-9]', '', (self.tx_TelefoneEmpresa.text()))
        INSERI.email = self.tx_EmailEmpresa.text()
        INSERI.site = self.tx_SiteEmpresa.text()
        INSERI.obs = self.tx_ObsEmpresa.text().upper()
        INSERI.cep = re.sub('[^[0-9]', '', (self.tx_CepEmpresa.text()))
        INSERI.endereco = self.tx_Endereco.text().upper()
        INSERI.numero = self.tx_NumEmpresa.text()
        INSERI.bairro = self.tx_BairroEmpresa.text().upper()
        INSERI.cidade = self.tx_CidadeEmpresa.text().upper()
        INSERI.estado = self.tx_EstadoEmpresa.text().upper()
        INSERI.titulo = self.tx_Titulo.text()
        INSERI.subtitulo = self.tx_SubTitulo.text()

        if self.lb_LogoEmpresa.pixmap():
            image = QPixmap(self.lb_LogoEmpresa.pixmap())
            data = QByteArray()
            buf = QBuffer(data)
            image.save(buf, 'PNG')
            logo = str(data.toBase64())[2:-1]
            INSERI.logo = logo

        INSERI.inseriEmpresa()
        self.lb_NomeFantasia.setText(self.tx_Titulo.text())
        self.lb_NomeFantasia2.setText(INSERI.subtitulo)
        self.setWindowTitle(INSERI.titulo + " " + INSERI.subtitulo)


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
