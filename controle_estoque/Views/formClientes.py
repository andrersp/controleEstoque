# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formClientes.ui',
# licensing of 'formClientes.ui' applies.
#
# Created: Sat Feb  9 00:37:37 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_FormClientes(object):
    def setFormClientes(self, ct_FormClientes):
        ct_FormClientes.setObjectName("ct_FormClientes")
        ct_FormClientes.resize(1000, 500)
        ct_FormClientes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormClientes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormClientes = QtWidgets.QFrame(ct_FormClientes)
        self.fr_FormClientes.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormClientes.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormClientes.setObjectName("fr_FormClientes")
        self.lb_FormProdutos = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(100, 10, 880, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.tx_Id = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Id.setEnabled(False)
        self.tx_Id.setGeometry(QtCore.QRect(20, 10, 50, 30))
        self.tx_Id.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border: 1px solid #A2A2A2;\n"
"color: #000;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.tx_Id.setText("")
        self.tx_Id.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Id.setObjectName("tx_Id")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_NomeFantasia = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_NomeFantasia.setGeometry(QtCore.QRect(20, 85, 305, 25))
        self.tx_NomeFantasia.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_NomeFantasia.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_NomeFantasia.setObjectName("tx_NomeFantasia")
        self.lb_FormProdutos_3 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_3.setGeometry(QtCore.QRect(20, 120, 190, 20))
        self.lb_FormProdutos_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_3.setObjectName("lb_FormProdutos_3")
        self.lb_FormProdutos_4 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_4.setGeometry(QtCore.QRect(236, 120, 190, 20))
        self.lb_FormProdutos_4.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_4.setObjectName("lb_FormProdutos_4")
        self.lb_FormProdutos_5 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_5.setGeometry(QtCore.QRect(20, 180, 196, 20))
        self.lb_FormProdutos_5.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_5.setObjectName("lb_FormProdutos_5")
        self.tx_Celular = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Celular.setGeometry(QtCore.QRect(20, 205, 196, 25))
        self.tx_Celular.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Celular.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Celular.setPlaceholderText("")
        self.tx_Celular.setObjectName("tx_Celular")
        self.tx_InscEstadual = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_InscEstadual.setGeometry(QtCore.QRect(236, 145, 196, 25))
        self.tx_InscEstadual.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_InscEstadual.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_InscEstadual.setPlaceholderText("")
        self.tx_InscEstadual.setObjectName("tx_InscEstadual")
        self.tx_Obs = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Obs.setGeometry(QtCore.QRect(20, 260, 630, 25))
        self.tx_Obs.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Obs.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Obs.setObjectName("tx_Obs")
        self.lb_FormProdutos_7 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_7.setGeometry(QtCore.QRect(20, 235, 150, 20))
        self.lb_FormProdutos_7.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_7.setObjectName("lb_FormProdutos_7")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(20, 290, 630, 30))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tb_Historico = QtWidgets.QTableWidget(self.fr_FormClientes)
        self.tb_Historico.setGeometry(QtCore.QRect(680, 90, 310, 320))
        self.tb_Historico.setStyleSheet("QTableView{\n"
"color: #797979;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"background: #FFF;\n"
"}\n"
"QHeaderView:section{\n"
"background: #FFF;\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #797979;\n"
"border: none;\n"
"border-bottom: 1px solid #CCC;\n"
"height: 25px;\n"
"}\n"
"QTableView::item {\n"
"border-bottom: 2px solid #CCC;\n"
"padding: 2px;\n"
"}\n"
"")
        self.tb_Historico.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tb_Historico.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Historico.setShowGrid(False)
        self.tb_Historico.setObjectName("tb_Historico")
        self.tb_Historico.setColumnCount(4)
        self.tb_Historico.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Historico.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Historico.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Historico.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Historico.setHorizontalHeaderItem(3, item)
        self.tb_Historico.verticalHeader().setVisible(False)
        self.tb_Historico.verticalHeader().setHighlightSections(False)
        self.lb_FormProdutos_9 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_9.setGeometry(QtCore.QRect(670, 60, 310, 20))
        self.lb_FormProdutos_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_9.setObjectName("lb_FormProdutos_9")
        self.tx_Cep = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Cep.setGeometry(QtCore.QRect(20, 360, 100, 25))
        self.tx_Cep.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Cep.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Cep.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Cep.setObjectName("tx_Cep")
        self.lb_FormProdutos_10 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(20, 335, 50, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_FormClientes)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")
        self.bt_Voltar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_Voltar.setGeometry(QtCore.QRect(880, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_Voltar.setFont(font)
        self.bt_Voltar.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Voltar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Voltar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Voltar.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_Voltar.setIconSize(QtCore.QSize(75, 35))
        self.bt_Voltar.setObjectName("bt_Voltar")
        self.bt_Salvar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_Salvar.setGeometry(QtCore.QRect(750, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_Salvar.setFont(font)
        self.bt_Salvar.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Salvar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Salvar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Salvar.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_Salvar.setIconSize(QtCore.QSize(75, 35))
        self.bt_Salvar.setObjectName("bt_Salvar")
        self.lb_FormProdutos_21 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_21.setGeometry(QtCore.QRect(345, 60, 150, 20))
        self.lb_FormProdutos_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_21.setObjectName("lb_FormProdutos_21")
        self.tx_RazaoSocial = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_RazaoSocial.setGeometry(QtCore.QRect(345, 85, 305, 25))
        self.tx_RazaoSocial.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_RazaoSocial.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_RazaoSocial.setObjectName("tx_RazaoSocial")
        self.tx_cnpj = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_cnpj.setGeometry(QtCore.QRect(20, 145, 196, 25))
        self.tx_cnpj.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cnpj.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cnpj.setPlaceholderText("")
        self.tx_cnpj.setObjectName("tx_cnpj")
        self.lb_FormProdutos_23 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_23.setGeometry(QtCore.QRect(452, 180, 190, 20))
        self.lb_FormProdutos_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_23.setObjectName("lb_FormProdutos_23")
        self.lb_FormProdutos_24 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_24.setGeometry(QtCore.QRect(236, 180, 190, 20))
        self.lb_FormProdutos_24.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_24.setObjectName("lb_FormProdutos_24")
        self.tx_Email = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Email.setGeometry(QtCore.QRect(452, 205, 196, 25))
        self.tx_Email.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Email.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Email.setPlaceholderText("")
        self.tx_Email.setObjectName("tx_Email")
        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Telefone.setGeometry(QtCore.QRect(236, 205, 196, 25))
        self.tx_Telefone.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Telefone.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Telefone.setPlaceholderText("")
        self.tx_Telefone.setObjectName("tx_Telefone")
        self.lb_FormProdutos_11 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_11.setGeometry(QtCore.QRect(160, 335, 250, 20))
        self.lb_FormProdutos_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_11.setObjectName("lb_FormProdutos_11")
        self.tx_Endereco = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Endereco.setGeometry(QtCore.QRect(160, 360, 400, 25))
        self.tx_Endereco.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Endereco.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Endereco.setInputMask("")
        self.tx_Endereco.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Endereco.setPlaceholderText("")
        self.tx_Endereco.setObjectName("tx_Endereco")
        self.lb_FormProdutos_12 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(580, 335, 50, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.tx_Numero = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Numero.setGeometry(QtCore.QRect(580, 360, 70, 25))
        self.tx_Numero.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Numero.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Numero.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tx_Numero.setInputMask("")
        self.tx_Numero.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Numero.setPlaceholderText("")
        self.tx_Numero.setObjectName("tx_Numero")
        self.tx_Bairro = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Bairro.setGeometry(QtCore.QRect(20, 415, 260, 25))
        self.tx_Bairro.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Bairro.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Bairro.setInputMask("")
        self.tx_Bairro.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Bairro.setPlaceholderText("")
        self.tx_Bairro.setObjectName("tx_Bairro")
        self.lb_FormProdutos_13 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_13.setGeometry(QtCore.QRect(20, 390, 120, 20))
        self.lb_FormProdutos_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_13.setObjectName("lb_FormProdutos_13")
        self.tx_Cidade = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Cidade.setGeometry(QtCore.QRect(300, 415, 260, 25))
        self.tx_Cidade.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Cidade.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Cidade.setInputMask("")
        self.tx_Cidade.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Cidade.setPlaceholderText("")
        self.tx_Cidade.setObjectName("tx_Cidade")
        self.lb_FormProdutos_14 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(300, 390, 120, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")
        self.lb_FormProdutos_15 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_15.setGeometry(QtCore.QRect(580, 390, 70, 20))
        self.lb_FormProdutos_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_15.setObjectName("lb_FormProdutos_15")
        self.tx_Estado = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Estado.setGeometry(QtCore.QRect(580, 415, 70, 25))
        self.tx_Estado.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Estado.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Estado.setInputMask("")
        self.tx_Estado.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Estado.setPlaceholderText("")
        self.tx_Estado.setObjectName("tx_Estado")
        self.bt_BuscaCep = QtWidgets.QPushButton(self.fr_FormClientes)
        self.bt_BuscaCep.setGeometry(QtCore.QRect(120, 360, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.bt_BuscaCep.setFont(font)
        self.bt_BuscaCep.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_BuscaCep.setText("")
        self.bt_BuscaCep.setObjectName("bt_BuscaCep")
        self.lb_TotalHistorico = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_TotalHistorico.setGeometry(QtCore.QRect(910, 415, 81, 25))
        self.lb_TotalHistorico.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_TotalHistorico.setStyleSheet("QLabel{\n"
"font-size: 20px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_TotalHistorico.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_TotalHistorico.setObjectName("lb_TotalHistorico")
        self.lb_FormVenda_11 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormVenda_11.setGeometry(QtCore.QRect(680, 415, 211, 25))
        self.lb_FormVenda_11.setStyleSheet("QLabel{\n"
"font-size: 15px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_11.setObjectName("lb_FormVenda_11")

        self.tradFormClientes(ct_FormClientes)
        QtCore.QMetaObject.connectSlotsByName(ct_FormClientes)
        ct_FormClientes.setTabOrder(self.tx_Id, self.tx_NomeFantasia)
        ct_FormClientes.setTabOrder(self.tx_NomeFantasia, self.tx_RazaoSocial)
        ct_FormClientes.setTabOrder(self.tx_RazaoSocial, self.tx_cnpj)
        ct_FormClientes.setTabOrder(self.tx_cnpj, self.tx_InscEstadual)
        ct_FormClientes.setTabOrder(self.tx_InscEstadual, self.tx_Celular)
        ct_FormClientes.setTabOrder(self.tx_Celular, self.tx_Telefone)
        ct_FormClientes.setTabOrder(self.tx_Telefone, self.tx_Email)
        ct_FormClientes.setTabOrder(self.tx_Email, self.tx_Obs)
        ct_FormClientes.setTabOrder(self.tx_Obs, self.tx_Cep)
        ct_FormClientes.setTabOrder(self.tx_Cep, self.bt_BuscaCep)
        ct_FormClientes.setTabOrder(self.bt_BuscaCep, self.tx_Endereco)
        ct_FormClientes.setTabOrder(self.tx_Endereco, self.tx_Numero)
        ct_FormClientes.setTabOrder(self.tx_Numero, self.tx_Bairro)
        ct_FormClientes.setTabOrder(self.tx_Bairro, self.tx_Cidade)
        ct_FormClientes.setTabOrder(self.tx_Cidade, self.tx_Estado)
        ct_FormClientes.setTabOrder(self.tx_Estado, self.tb_Historico)

    def tradFormClientes(self, ct_FormClientes):
        ct_FormClientes.setWindowTitle(QtWidgets.QApplication.translate("ct_FormClientes", "Frame", None, -1))
        self.lb_FormProdutos.setText(QtWidgets.QApplication.translate("ct_FormClientes", "FICHA CADASTRAL CLIENTE", None, -1))
        self.lb_FormProdutos_2.setText(QtWidgets.QApplication.translate("ct_FormClientes", "NOME", None, -1))
        self.tx_NomeFantasia.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "NOME COMPLETO", None, -1))
        self.lb_FormProdutos_3.setText(QtWidgets.QApplication.translate("ct_FormClientes", "CPF", None, -1))
        self.lb_FormProdutos_4.setText(QtWidgets.QApplication.translate("ct_FormClientes", "RG", None, -1))
        self.lb_FormProdutos_5.setText(QtWidgets.QApplication.translate("ct_FormClientes", "CELULAR", None, -1))
        self.tx_Celular.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "(00) 00000-0000", None, -1))
        self.tx_Celular.setText(QtWidgets.QApplication.translate("ct_FormClientes", "() -", None, -1))
        self.tx_InscEstadual.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "00.000.000-0", None, -1))
        self.tx_Obs.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "Observação", None, -1))
        self.lb_FormProdutos_7.setText(QtWidgets.QApplication.translate("ct_FormClientes", "OBSERVAÇÃO", None, -1))
        self.lb_FormProdutos_8.setText(QtWidgets.QApplication.translate("ct_FormClientes", "ENDEREÇO", None, -1))
        self.tb_Historico.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ct_FormClientes", "EMISÂO", None, -1))
        self.tb_Historico.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ct_FormClientes", "ENTREGA", None, -1))
        self.tb_Historico.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ct_FormClientes", "VALOR", None, -1))
        self.tb_Historico.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("ct_FormClientes", "VER", None, -1))
        self.lb_FormProdutos_9.setText(QtWidgets.QApplication.translate("ct_FormClientes", "HISTÓRICO DE PEDIDOS", None, -1))
        self.tx_Cep.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "99999-999", None, -1))
        self.tx_Cep.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "123456789", None, -1))
        self.lb_FormProdutos_10.setText(QtWidgets.QApplication.translate("ct_FormClientes", "CEP", None, -1))
        self.bt_Voltar.setText(QtWidgets.QApplication.translate("ct_FormClientes", "VOLTAR", None, -1))
        self.bt_Salvar.setText(QtWidgets.QApplication.translate("ct_FormClientes", "SALVAR", None, -1))
        self.lb_FormProdutos_21.setText(QtWidgets.QApplication.translate("ct_FormClientes", "SOBRENOME", None, -1))
        self.tx_RazaoSocial.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "APELIDO (se HOUVER)", None, -1))
        self.tx_cnpj.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "000.000.000-00", None, -1))
        self.tx_cnpj.setText(QtWidgets.QApplication.translate("ct_FormClientes", "..-", None, -1))
        self.lb_FormProdutos_23.setText(QtWidgets.QApplication.translate("ct_FormClientes", "Email", None, -1))
        self.lb_FormProdutos_24.setText(QtWidgets.QApplication.translate("ct_FormClientes", "TELEFONE", None, -1))
        self.tx_Telefone.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "(00) 0000-0000", None, -1))
        self.lb_FormProdutos_11.setText(QtWidgets.QApplication.translate("ct_FormClientes", "ENDEREÇO", None, -1))
        self.lb_FormProdutos_12.setText(QtWidgets.QApplication.translate("ct_FormClientes", "Nº", None, -1))
        self.lb_FormProdutos_13.setText(QtWidgets.QApplication.translate("ct_FormClientes", "BAIRRO", None, -1))
        self.lb_FormProdutos_14.setText(QtWidgets.QApplication.translate("ct_FormClientes", "CIDADE", None, -1))
        self.lb_FormProdutos_15.setText(QtWidgets.QApplication.translate("ct_FormClientes", "ESTADO", None, -1))
        self.lb_TotalHistorico.setText(QtWidgets.QApplication.translate("ct_FormClientes", "0.00", None, -1))
        self.lb_FormVenda_11.setText(QtWidgets.QApplication.translate("ct_FormClientes", "Total", None, -1))

