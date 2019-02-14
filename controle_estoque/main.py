# -*- coding: utf-8 -*-
import os
import sys
import random

import mysql.connector
from jinja2 import Environment, PackageLoader, FileSystemLoader

# from PySide2.QtWebEngineWidgets import QWebEnginePage
from Crud.conexao import Conexao
from Crud.CrudEmpresa import CrudEmpresa
from Funcoes.categoriaAPagar import CategoriaAPagar
from Funcoes.categoriaAReceber import CategoriaAReceber
from Funcoes.Clientes import Clientes
from Funcoes.comercial import Comercial
from Funcoes.data import DataAtual
from Funcoes.financeiro import Financeiro
from Funcoes.FormaPagamento import FormaPagamento
from Funcoes.Fornecedor import Fornecedor
from Funcoes.Funcoes import Funcao
from home import MainHome
from mainclientes import MainClientes
from maincompras import MainCompras
from mainconfig import MainConfig
from mainfinanceiro import MainFinanceiro
from mainfornecedor import MainFornecedor
from mainprodutos import MainProdutos
from mainvendas import MainVendas
from PySide2 import QtCore, QtGui, QtWidgets, QtPrintSupport
from Views.main import Ui_MainWindow


class Main(QtWidgets.QMainWindow, Ui_MainWindow, MainHome, MainProdutos,
           Funcao, MainVendas, MainClientes, MainCompras, MainFinanceiro,
           MainFornecedor, MainConfig, Financeiro, Comercial, Fornecedor,
           Clientes, FormaPagamento, CategoriaAPagar, CategoriaAReceber):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.centralizar()  # Centrelizando na tela

        # Caminho Absoluto
        self.caminho = os.path.abspath(os.path.dirname(sys.argv[0]))
        # Abrindo conteudo Home
        self.main_home(self.ct_conteudo)

        bg = QtGui.QPixmap(self.resourcepath('Images/bg.png'))

        palete = QtGui.QPalette()
        palete.setBrush(QtGui.QPalette.Background,
                        QtGui.QBrush(bg.scaled(1000, 700, QtCore.Qt.KeepAspectRatio)))
        self.setPalette(palete)

        # Icone dos botoes Topo
        self.IconeBotaoTopo(self.bt_Home, self.resourcepath(
            'Images/home.png'))  # HOme
        self.IconeBotaoTopo(self.bt_Exit, self.resourcepath(
            'Images/exit.png'))  # Sair

        # Icone botoes menu
        self.IconeBotaoMenu(self.bt_Clientes, self.resourcepath(
            'Images/tag-new.png'))  # Clientes
        self.IconeBotaoMenu(self.bt_Vendas, self.resourcepath(
            'Images/vendas.png'))  # Vendas
        self.IconeBotaoMenu(self.bt_Fornecedor, self.resourcepath(
            'Images/iconFornecedor.png'))  # Fornecedor
        self.IconeBotaoMenu(self.bt_MainProdutos, self.resourcepath(
            'Images/estoque.png'))  # Produtos
        self.IconeBotaoMenu(self.bt_Compras, self.resourcepath(
            'Images/ico-compras.png'))  # Compras
        self.IconeBotaoMenu(self.bt_Financeiro, self.resourcepath(
            'Images/financeiro.png'))  # Financeiro
        self.IconeBotaoMenu(self.bt_Conf, self.resourcepath(
            'Images/conf.png'))  # Configuracao

        """Ação dos Botões Botoes"""
        # Home
        self.bt_Home.clicked.connect(self.janelaHome)

        # Produtos
        self.bt_MainProdutos.clicked.connect(self.janelaProdutos)

        # Vendas
        self.bt_Vendas.clicked.connect(self.janelaVendas)

        # Clientes
        self.bt_Clientes.clicked.connect(self.janelaClientes)

        # Compras
        self.bt_Compras.clicked.connect(self.janelaCompras)

        # Fornecedor
        self.bt_Fornecedor.clicked.connect(self.janelaFornecedor)

        # Financeiro
        self.bt_Financeiro.clicked.connect(self.janelaFinanceiro)

        # Config
        self.bt_Conf.clicked.connect(self.janelaConfig)
        """ Fim Botoes """

        # Setando data no Header
        data = DataAtual()
        data.diaAtual()
        self.lb_Data.setText(data.diames)
        self.lb_DiaSemana.setText(data.diasemana)

        self.DbCheck()  # Checando banco de dados

    # Caminho absoluto
    def resourcepath(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(
            os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    # Centralizar Janela na Tela
    def centralizar(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    # Verificando Banco de Dados
    def DbCheck(self):
        try:
            conecta = Conexao()
            busca = CrudEmpresa()
            busca.idEmpresa = '1'
            busca.SelectEmpresaId()
            if busca.titulo:
                self.lb_NomeFantasia.setText(busca.titulo)
                self.lb_NomeFantasia2.setText(busca.subtitulo)
                self.setWindowTitle(busca.titulo + " " + busca.subtitulo)
            else:
                self.janelaConfig()
                self.tab_Config.setCurrentIndex(0)

        except:
            self.janelaConfig()
            self.tab_Config.setCurrentIndex(1)
            for botao in self.wd_menu.findChildren(QtWidgets.QPushButton):
                botao.setDisabled(True)
            self.bt_Home.setDisabled(True)

    """Abrindo conteudos externos"""
    # Home

    def janelaHome(self):
        self.LimpaFrame(self.ct_conteudo)
        self.ativaBotoes(self.wd_menu)
        self.main_home(self.ct_conteudo)

    # Main Produtos

    def janelaProdutos(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_MainProdutos)
        self.mainprodutos(self.ct_conteudo)

    # Main Vendas
    def janelaVendas(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_Vendas)
        self.mainvendas(self.ct_conteudo)

    # Main Cliente
    def janelaClientes(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_Clientes)
        self.mainclientes(self.ct_conteudo)

    # Main Fornecedor
    def janelaFornecedor(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_Fornecedor)
        self.mainfornecedor(self.ct_conteudo)

    # Main Compras
    def janelaCompras(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_Compras)
        self.maincompras(self.ct_conteudo)

    # Main Financeiro
    def janelaFinanceiro(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_Financeiro)
        self.mainfinanceiro(self.ct_conteudo)

    # Main Configuração
    def janelaConfig(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_Conf)
        self.mainconfig(self.ct_conteudo)

    """ Fim conteudos Externos """

    # Conteudo Tabela sem icone
    def conteudoTabela(self, tabela, row, col, data):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify |
                              QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        item.setFlags(QtCore.Qt.NoItemFlags)
        item.setText(data)
        tabela.setItem(row, col, item)

    def conteudoTabelaLeft(self, tabela, row, col, data):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify |
                              QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        item.setFlags(QtCore.Qt.NoItemFlags)
        item.setText(data)
        tabela.setItem(row, col, item)

    # Botão Tabela
    def botaoTabela(self, tabela, row, col, funcao, bg):
        item = QtWidgets.QPushButton()
        # item.setFixedWidth(30)
        # item.setFixedHeight(30)
        item.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        item.setFocusPolicy(QtCore.Qt.NoFocus)
        item.setFlat(QtCore.Qt.NoItemFlags)
        item.setStyleSheet("QPushButton{\n"
                           "background-color: #1E87F0;\n"
                           "border-radius: 2px;\n"
                           "padding: 2px;\n"
                           "color: #FFF;\n"
                           "font: 10px \"Tahoma\" Bold\n"
                           "}\n"
                           "QPushButton:hover{\n"
                           "background-color: #40a286\n"
                           "}")
        item.setText("EDITAR")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            self.resourcepath('Images/editar.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        tabela.setCellWidget(row, col, item)
        item.clicked.connect(funcao)

    # Botão Remove Item
    def botaoRemoveItem(self, tabela, row, col, funcao, bg):
        item = QtWidgets.QPushButton()
        # item.setFixedWidth(30)
        # item.setFixedHeight(30)
        item.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        item.setFocusPolicy(QtCore.Qt.NoFocus)
        item.setFlat(QtCore.Qt.NoItemFlags)
        item.setStyleSheet("QPushButton{\n"
                           "background-color: " + bg + ";\n"
                           "border-radius: 2px;\n"
                           "padding: 2px;\n"
                           "}\n"
                           "QPushButton:hover{\n"
                           "background-color: #40a286\n"
                           "}")
        item.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            self.resourcepath('Images/edit-delete.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        tabela.setCellWidget(row, col, item)
        item.clicked.connect(funcao)

    # Texto Tabela Valor
    def TabelaPagamento(self, tabela, row, col, valor, cor, status):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(120, 60)
        # item.setGeometry(QtCore.QRect(600, 90, 181, 60))
        item.setStyleSheet("background: #FFF")
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        item.setObjectName("textBrowser")
        html = (("""<p align="center">
    <span style="font-size:11px;"><span style="font-family:verdana,geneva,
    sans-serif;">R$: <strong><span style="font-size:14px;">{}</span></strong><br />
    <strong><span style="font-size:12px;"><span style="color:{};">{}</span></span></strong></span></span></p>
""")).format(valor, cor, status)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)

    # Texto Tabela Valor Produtos
    def ValorProduto(self, tabela, row, col, valor):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(120, 60)
        # item.setGeometry(QtCore.QRect(600, 90, 181, 60))
        item.setStyleSheet("background: #FFF")
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        item.setObjectName("textBrowser")
        html = ("""<p align="center">
    <span style="font-size:11px;"><span style="font-family:verdana,geneva,sans-serif;">R$: <strong><span style="font-size:14px;">{}</span></strong><br />
    </span></span></p>
""").format(valor)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)

    def TabelaQtdeEstoque(self, tabela, row, col, qtde):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(120, 60)
        item.setStyleSheet('background: #FFF;')
        item.setAlignment(QtCore.Qt.AlignCenter)
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        html = ("""<p align="center">
    <span style="color:#069;"><strong><span style="font-size:16px; margin: 0 auto; text-align: justify"> {}</span><br />
    </span></strong></p>""").format(qtde)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)

    # Texto Tabela Data Status

    def TabelaStatus(self, tabela, row, col, cor):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(120, 60)
        # item.setGeometry(QtCore.QRect(600, 90, 181, 60))
        item.setStyleSheet("background: {}".format(cor))
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        item.setObjectName("textBrowser")
        tabela.setCellWidget(row, col, item)

    def TabelaEntrega(self, tabela, row, col, data, cor, status):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(120, 60)
        # item.setGeometry(QtCore.QRect(600, 90, 181, 60))
        item.setStyleSheet("background: #FFF")
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        item.setObjectName("textBrowser")
        html = ("""<p align="center">
    <span style="font-size:11px;"><span style="font-family:verdana,geneva,sans-serif;"><strong><span style="font-size:14px;">{}</span></strong><br />
    <strong><span style="font-size:12px;"><span style="color:{};">{}</span></span></strong></span></span></p>
""").format(data, cor, status)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)

    def TabelaNomeTelefone(self, tabela, row, col, nome, telefone):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(250, 60)
        item.setStyleSheet('background: #FFF')
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        html = (("""<p>
    <span style="font-size:11px;"><strong><span style="font-size:15px;">{}</span></strong><br />
    <span style="font-size:12px;"><span style="color: #000;">{}</span></span></span></p>
""")).format(nome, telefone)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)

    def TabelaEmissao(self, tabela, row, col, emissao):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(120, 60)
        item.setStyleSheet('background: #FFF')
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        html = ("""<p align="center">
    <span style="font-size:9px;"><span style="font-family:verdana,geneva,sans-serif;">DATA PEDIDO:<br />
    <span style="font-size:14px;"><strong>{}</strong></span></span></span></p>""").format(emissao)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)

    def TabelaQtdeStatus(self, tabela, row, col, qtde, cor):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(120, 60)
        item.setStyleSheet('background: #FFF;')
        item.setAlignment(QtCore.Qt.AlignCenter)
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        html = ("""<p align="center">
    <span style="color:{};"><strong><span style="font-size:30px; margin: 0 auto; text-align: justify"> {}</span></strong></p>""").format(cor, qtde)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)

    def TabelaID(self, tabela, row, col, id):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(120, 60)
        item.setStyleSheet('background: #FFF;')
        item.setAlignment(QtCore.Qt.AlignCenter)
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        html = ("""<p align="left">
    <span style="color:#7AB32E;"><strong><span style="font-size:30px; margin: 0 auto; text-align: justify"> {}</span></strong></p>""").format(id)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)

    def botaoReceberParcela(self, tabela, row, col, funcao, texto, status):
        item = QtWidgets.QPushButton()
        # item.setFixedWidth(70)
        # item.setFixedHeight(30)
        item.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if status == 1:
            item.setDisabled(True)
        item.setFocusPolicy(QtCore.Qt.NoFocus)
        item.setFlat(QtCore.Qt.NoItemFlags)
        item.setStyleSheet("QPushButton{\n"
                           "background-color: #7AB32E;\n"
                           "border-radius: 2px;\n"
                           "padding: 2px;\n"
                           "border: none;\n"
                           "text-transform: uppercase;\n"
                           "font: 10px \"Arial\";\n"
                           "}\n"
                           "QPushButton:hover{\n"
                           "background-color: #40a286\n"
                           "}"
                           )
        item.setText(texto)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            self.resourcepath('Images/money.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        tabela.setCellWidget(row, col, item)
        item.clicked.connect(funcao)

    def tx_tabelaReceber(self, tabela, row, col, status, valor):
        item = QtWidgets.QLineEdit()
        # item.setGeometry(QtCore.QRect(310, 360, 80, 30))
        # item.setFixedWidth(60)
        if status == 1:
            item.setReadOnly(True)
        item.setText(valor)
        item.setFocusPolicy(QtCore.Qt.WheelFocus)
        item.setStyleSheet("QLineEdit{\n"
                           "background: #F1F1F1;\n"
                           "border: 2px solid #CFCFCF;\n"
                           "color: #000;\n"
                           "font: 12px \"Arial\" ;\n"
                           "text-transform: uppercase;\n"
                           "font-weight: bold\n"
                           "}\n"
                           "QLineEdit:Focus {\n"
                           "border: 1px solid red;\n"
                           "}")
        item.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        item.setObjectName("tx_ValorPago")
        item.setPlaceholderText("R$ 0.00")
        tabela.setCellWidget(row, col, item)

    def dt_tabela(self, tabela, row, col, data, status):
        item = QtWidgets.QDateEdit()
        # item.setGeometry(QtCore.QRect(120, 18, 140, 18))
        item.setFixedWidth(90)
        if status == 1:
            item.setReadOnly(True)
        item.setStyleSheet("QDateEdit {\n"
                           "background: #FFF;\n"
                           "border: none;\n"
                           "font-family: \"Arial\";\n"
                           "font-size: 12px;\n"
                           "font-weight: bold;\n"
                           "color: rgb(80,79,79)\n"
                           "}\n"
                           " QDateEdit::drop-down {\n"
                           "     subcontrol-origin: padding;\n"
                           "     subcontrol-position: top right;\n"
                           "     width: 20px;\n"
                           "     border-left-width: 1px;\n"
                           "     border-left-color: darkgray;\n"
                           "     border-left-style: solid; /* just a single line */\n"
                           "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                           "     border-bottom-right-radius: 3px;\n"
                           " }\n"
                           "QDateEdit::down-arrow {\n"
                           "     image: url("+self.resourcepath('Images/down.png')+");\n"
                           " }\n"
                           "QCalendarWidget QAbstractItemView:enabled \n"
                           "  {\n"
                           "border: none;\n"
                           "      font-size:13px;  \n"
                           "      color: #000;  \n"
                           "      background-color: #F1F1F1;  \n"
                           "      selection-background-color: rgb(64, 64, 64); \n"
                           "      selection-color: rgb(0, 255, 0); \n"
                           "  }\n"
                           "QCalendarWidget QToolButton {\n"
                           "    border: none;\n"
                           "      color: #000\n"
                           "  }\n"
                           "\n"
                           " QCalendarWidget QMenu {\n"
                           "      width: 150px;\n"
                           "      left: 20px;\n"
                           "      color: white;\n"
                           "      font-size: 18px;\n"
                           "      background-color: rgb(100, 100, 100);\n"
                           "  }\n"
                           "QCalendarWidget QWidget#qt_calendar_navigationbar\n"
                           "{ \n"
                           "border: none;\n"
                           "}")
        item.setCalendarPopup(True)
        item.setDate(data)
        tabela.setCellWidget(row, col, item)

    def StatusStoque(self, qtde, minimo):
        if qtde > minimo:
            cor = "#7AB32E"
        elif qtde <= minimo:
            cor = "#e69822"
        else:
            cor = "red"

        return cor

    def StatusEntrega(self, *args):
        if len(args) > 1:
            if args[0] == 1 and args[1] == 1:
                cor = "#7AB32E"
            else:
                cor = "#e69822"
        else:
            if args[0] == 1:
                cor = "#7AB32E"
            elif args[0] == 2:
                cor = "#e69822"
            else:
                cor = "red"

        return cor

    # Imprimindo
    def previaImpressao(self, arg):
        self.printer = QtPrintSupport.QPrinter()
        self.dialogo = QtPrintSupport.QPrintDialog(self.printer)

        # self.dialogo.paintRequested.connect(self.documento.print_)
        if self.dialogo.exec_() == True:
            self.documento.print(self.printer, self.okPrinter)

    def okPrinter(self, sucess):
        pass

    def renderTemplate(self, template_file, **kwargs):
        template_loader = FileSystemLoader(
            searchpath=self.resourcepath('Template/'))
        # Jinja2 template environment
        env = Environment(loader=template_loader)
        template = env.get_template(template_file)
        busca = CrudEmpresa()
        busca.idEmpresa = 1
        busca.SelectEmpresaId()
        base = {'logo': str(busca.logo, encoding='utf-8'),
                'nomeFantasia': busca.NomeFantasia,
                'razaoSocial': busca.RazaoSocial,
                'cnpj': busca.cnpj,
                'endereco': busca.endereco,
                'numero': busca.numero,
                'bairro': busca.bairro,
                'cep': busca.cep,
                'cidade': busca.cidade,
                'estado': busca.estado,
                'telefone': busca.telefone}
        html = template.render(base, **kwargs)
        with open(self.resourcepath('report.html'), 'w') as f:
            f.write(html)

        return html


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()
