# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formFornecedor.ui',
# licensing of 'formFornecedor.ui' applies.
#
# Created: Fri Mar 15 09:54:22 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_FormFornecedor(object):
    def setFormFornecedor(self, ct_FormFornecedor):
        ct_FormFornecedor.setObjectName("ct_FormFornecedor")
        ct_FormFornecedor.resize(1000, 500)
        ct_FormFornecedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormFornecedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormFornecedor = QtWidgets.QFrame(ct_FormFornecedor)
        self.fr_FormFornecedor.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormFornecedor.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormFornecedor.setObjectName("fr_FormFornecedor")
        self.lb_FormFornecedor = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor.setGeometry(QtCore.QRect(100, 10, 880, 30))
        self.lb_FormFornecedor.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor.setObjectName("lb_FormFornecedor")
        self.tx_Id = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.lb_FormFornecedor_2 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_2.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.lb_FormFornecedor_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_2.setObjectName("lb_FormFornecedor_2")
        self.tx_NomeFantasia = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.lb_FormFornecedor_3 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_3.setGeometry(QtCore.QRect(20, 120, 190, 20))
        self.lb_FormFornecedor_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_3.setObjectName("lb_FormFornecedor_3")
        self.lb_FormFornecedor_4 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_4.setGeometry(QtCore.QRect(236, 120, 190, 20))
        self.lb_FormFornecedor_4.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_4.setObjectName("lb_FormFornecedor_4")
        self.lb_FormFornecedor_5 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_5.setGeometry(QtCore.QRect(20, 180, 196, 20))
        self.lb_FormFornecedor_5.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_5.setObjectName("lb_FormFornecedor_5")
        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Telefone.setGeometry(QtCore.QRect(20, 205, 196, 25))
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
        self.tx_InscEstadual = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.tx_Obs = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.lb_FormFornecedor_7 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_7.setGeometry(QtCore.QRect(20, 235, 150, 20))
        self.lb_FormFornecedor_7.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_7.setObjectName("lb_FormFornecedor_7")
        self.lb_FormFornecedor_8 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_8.setGeometry(QtCore.QRect(20, 290, 630, 30))
        self.lb_FormFornecedor_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_8.setObjectName("lb_FormFornecedor_8")
        self.tb_Historico = QtWidgets.QTableWidget(self.fr_FormFornecedor)
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
"")
        self.tb_Historico.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Historico.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Historico.setShowGrid(False)
        self.tb_Historico.setObjectName("tb_Historico")
        self.tb_Historico.setColumnCount(3)
        self.tb_Historico.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Historico.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Historico.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Historico.setHorizontalHeaderItem(2, item)
        self.tb_Historico.verticalHeader().setVisible(False)
        self.tb_Historico.verticalHeader().setHighlightSections(False)
        self.lb_FormFornecedor_9 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_9.setGeometry(QtCore.QRect(670, 60, 310, 20))
        self.lb_FormFornecedor_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_9.setObjectName("lb_FormFornecedor_9")
        self.tx_Cep = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.lb_FormFornecedor_10 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_10.setGeometry(QtCore.QRect(20, 335, 50, 20))
        self.lb_FormFornecedor_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_10.setObjectName("lb_FormFornecedor_10")
        self.fr_BotoesFormFornecedor = QtWidgets.QFrame(self.fr_FormFornecedor)
        self.fr_BotoesFormFornecedor.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormFornecedor.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormFornecedor.setObjectName("fr_BotoesFormFornecedor")
        self.bt_Voltar = QtWidgets.QPushButton(self.fr_BotoesFormFornecedor)
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
        self.bt_Salvar = QtWidgets.QPushButton(self.fr_BotoesFormFornecedor)
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
        self.lb_FormFornecedor_21 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_21.setGeometry(QtCore.QRect(345, 60, 150, 20))
        self.lb_FormFornecedor_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_21.setObjectName("lb_FormFornecedor_21")
        self.tx_RazaoSocial = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.tx_cnpj = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.tx_cnpj.setText("")
        self.tx_cnpj.setPlaceholderText("")
        self.tx_cnpj.setObjectName("tx_cnpj")
        self.lb_FormFornecedor_23 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_23.setGeometry(QtCore.QRect(452, 180, 190, 20))
        self.lb_FormFornecedor_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_23.setObjectName("lb_FormFornecedor_23")
        self.lb_FormFornecedor_24 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_24.setGeometry(QtCore.QRect(236, 180, 190, 20))
        self.lb_FormFornecedor_24.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_24.setObjectName("lb_FormFornecedor_24")
        self.tx_Email = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Email.setGeometry(QtCore.QRect(452, 205, 196, 25))
        self.tx_Email.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Email.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Email.setPlaceholderText("")
        self.tx_Email.setObjectName("tx_Email")
        self.tx_Site = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Site.setGeometry(QtCore.QRect(236, 205, 196, 25))
        self.tx_Site.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Site.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Site.setPlaceholderText("")
        self.tx_Site.setObjectName("tx_Site")
        self.lb_FormFornecedor_11 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_11.setGeometry(QtCore.QRect(160, 335, 250, 20))
        self.lb_FormFornecedor_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_11.setObjectName("lb_FormFornecedor_11")
        self.tx_Endereco = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.lb_FormFornecedor_12 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_12.setGeometry(QtCore.QRect(580, 335, 50, 20))
        self.lb_FormFornecedor_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_12.setObjectName("lb_FormFornecedor_12")
        self.tx_Numero = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.tx_Numero.setInputMask("")
        self.tx_Numero.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Numero.setPlaceholderText("")
        self.tx_Numero.setObjectName("tx_Numero")
        self.tx_Bairro = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.lb_FormFornecedor_13 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_13.setGeometry(QtCore.QRect(20, 390, 120, 20))
        self.lb_FormFornecedor_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_13.setObjectName("lb_FormFornecedor_13")
        self.tx_Cidade = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.lb_FormFornecedor_14 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_14.setGeometry(QtCore.QRect(300, 390, 120, 20))
        self.lb_FormFornecedor_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_14.setObjectName("lb_FormFornecedor_14")
        self.lb_FormFornecedor_15 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_15.setGeometry(QtCore.QRect(580, 390, 70, 20))
        self.lb_FormFornecedor_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_15.setObjectName("lb_FormFornecedor_15")
        self.tx_Estado = QtWidgets.QLineEdit(self.fr_FormFornecedor)
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
        self.bt_BuscaCep = QtWidgets.QPushButton(self.fr_FormFornecedor)
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
        self.lb_FormVenda_11 = QtWidgets.QLabel(self.fr_FormFornecedor)
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
        self.lb_TotalHistorico = QtWidgets.QLabel(self.fr_FormFornecedor)
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

        self.tradFormFornecedor(ct_FormFornecedor)
        QtCore.QMetaObject.connectSlotsByName(ct_FormFornecedor)
        ct_FormFornecedor.setTabOrder(self.tx_Id, self.tx_NomeFantasia)
        ct_FormFornecedor.setTabOrder(self.tx_NomeFantasia, self.tx_RazaoSocial)
        ct_FormFornecedor.setTabOrder(self.tx_RazaoSocial, self.tx_cnpj)
        ct_FormFornecedor.setTabOrder(self.tx_cnpj, self.tx_InscEstadual)
        ct_FormFornecedor.setTabOrder(self.tx_InscEstadual, self.tx_Telefone)
        ct_FormFornecedor.setTabOrder(self.tx_Telefone, self.tx_Site)
        ct_FormFornecedor.setTabOrder(self.tx_Site, self.tx_Email)
        ct_FormFornecedor.setTabOrder(self.tx_Email, self.tx_Obs)
        ct_FormFornecedor.setTabOrder(self.tx_Obs, self.tx_Cep)
        ct_FormFornecedor.setTabOrder(self.tx_Cep, self.bt_BuscaCep)
        ct_FormFornecedor.setTabOrder(self.bt_BuscaCep, self.tx_Endereco)
        ct_FormFornecedor.setTabOrder(self.tx_Endereco, self.tx_Numero)
        ct_FormFornecedor.setTabOrder(self.tx_Numero, self.tx_Bairro)
        ct_FormFornecedor.setTabOrder(self.tx_Bairro, self.tx_Cidade)
        ct_FormFornecedor.setTabOrder(self.tx_Cidade, self.tx_Estado)
        ct_FormFornecedor.setTabOrder(self.tx_Estado, self.tb_Historico)

    def tradFormFornecedor(self, ct_FormFornecedor):
        ct_FormFornecedor.setWindowTitle(QtWidgets.QApplication.translate("ct_FormFornecedor", "Frame", None, -1))
        self.lb_FormFornecedor.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "FICHA CADASTRAL FORNECEDOR", None, -1))
        self.lb_FormFornecedor_2.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "NOME FANTASIA", None, -1))
        self.tx_NomeFantasia.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormFornecedor", "NOME FANTASIA", None, -1))
        self.lb_FormFornecedor_3.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "CNPJ", None, -1))
        self.lb_FormFornecedor_4.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "IE", None, -1))
        self.lb_FormFornecedor_5.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "TELEFONE ", None, -1))
        self.tx_Telefone.setInputMask(QtWidgets.QApplication.translate("ct_FormFornecedor", "(00) 0000-00000", None, -1))
        self.tx_Telefone.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "() -", None, -1))
        self.tx_Obs.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormFornecedor", "Observação", None, -1))
        self.lb_FormFornecedor_7.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "OBSERVAÇÃO", None, -1))
        self.lb_FormFornecedor_8.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "ENDEREÇO", None, -1))
        self.tb_Historico.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "EMISSÂO", None, -1))
        self.tb_Historico.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "RECEBIDO", None, -1))
        self.tb_Historico.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "VALOR", None, -1))
        self.lb_FormFornecedor_9.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "HISTÓRICO DE PEDIDOS", None, -1))
        self.tx_Cep.setInputMask(QtWidgets.QApplication.translate("ct_FormFornecedor", "99999-999", None, -1))
        self.tx_Cep.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormFornecedor", "123456789", None, -1))
        self.lb_FormFornecedor_10.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "CEP", None, -1))
        self.bt_Voltar.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "VOLTAR", None, -1))
        self.bt_Salvar.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "SALVAR", None, -1))
        self.lb_FormFornecedor_21.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "RAZÃO SOCIAL", None, -1))
        self.tx_RazaoSocial.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormFornecedor", "Razão Social", None, -1))
        self.lb_FormFornecedor_23.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "Email", None, -1))
        self.lb_FormFornecedor_24.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "SITE", None, -1))
        self.lb_FormFornecedor_11.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "ENDEREÇO", None, -1))
        self.lb_FormFornecedor_12.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "Nº", None, -1))
        self.lb_FormFornecedor_13.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "BAIRRO", None, -1))
        self.lb_FormFornecedor_14.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "CIDADE", None, -1))
        self.lb_FormFornecedor_15.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "ESTADO", None, -1))
        self.lb_FormVenda_11.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "Total", None, -1))
        self.lb_TotalHistorico.setText(QtWidgets.QApplication.translate("ct_FormFornecedor", "0.00", None, -1))

