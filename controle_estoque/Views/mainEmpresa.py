# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainEmpresa.ui',
# licensing of 'mainEmpresa.ui' applies.
#
# Created: Fri Mar 15 09:55:46 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ct_empresa(object):
    def setMainEmpresa(self, ct_empresa):
        ct_empresa.setObjectName("ct_empresa")
        ct_empresa.resize(1000, 500)
        ct_empresa.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_empresa = QtWidgets.QFrame(ct_empresa)
        self.fr_empresa.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_empresa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_empresa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_empresa.setObjectName("fr_empresa")
        self.lb_FormFornecedor_21 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_21.setGeometry(QtCore.QRect(670, 60, 150, 20))
        self.lb_FormFornecedor_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_21.setObjectName("lb_FormFornecedor_21")
        self.tx_TelefoneEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_TelefoneEmpresa.setGeometry(QtCore.QRect(20, 205, 196, 25))
        self.tx_TelefoneEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_TelefoneEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_TelefoneEmpresa.setPlaceholderText("")
        self.tx_TelefoneEmpresa.setObjectName("tx_TelefoneEmpresa")
        self.lb_FormFornecedor_27 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_27.setGeometry(QtCore.QRect(580, 335, 50, 20))
        self.lb_FormFornecedor_27.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_27.setObjectName("lb_FormFornecedor_27")
        self.tx_RazaoSocial = QtWidgets.QLineEdit(self.fr_empresa)
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
        self.lb_FormFornecedor_28 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_28.setGeometry(QtCore.QRect(20, 335, 50, 20))
        self.lb_FormFornecedor_28.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_28.setObjectName("lb_FormFornecedor_28")
        self.lb_FormFornecedor_23 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_23.setGeometry(QtCore.QRect(670, 120, 150, 20))
        self.lb_FormFornecedor_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_23.setObjectName("lb_FormFornecedor_23")
        self.lb_FormFornecedor_20 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_20.setGeometry(QtCore.QRect(20, 390, 120, 20))
        self.lb_FormFornecedor_20.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_20.setObjectName("lb_FormFornecedor_20")
        self.lb_FormFornecedor_17 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_17.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.lb_FormFornecedor_17.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_17.setObjectName("lb_FormFornecedor_17")
        self.bt_LocalizaCepEmpresa = QtWidgets.QPushButton(self.fr_empresa)
        self.bt_LocalizaCepEmpresa.setGeometry(QtCore.QRect(120, 360, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.bt_LocalizaCepEmpresa.setFont(font)
        self.bt_LocalizaCepEmpresa.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_LocalizaCepEmpresa.setText("")
        self.bt_LocalizaCepEmpresa.setObjectName("bt_LocalizaCepEmpresa")
        self.tx_IE = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_IE.setGeometry(QtCore.QRect(236, 145, 196, 25))
        self.tx_IE.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_IE.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_IE.setPlaceholderText("")
        self.tx_IE.setObjectName("tx_IE")
        self.lb_FormFornecedor_26 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_26.setGeometry(QtCore.QRect(300, 390, 120, 20))
        self.lb_FormFornecedor_26.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_26.setObjectName("lb_FormFornecedor_26")
        self.tx_SiteEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_SiteEmpresa.setGeometry(QtCore.QRect(236, 205, 196, 25))
        self.tx_SiteEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_SiteEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_SiteEmpresa.setPlaceholderText("")
        self.tx_SiteEmpresa.setObjectName("tx_SiteEmpresa")
        self.lb_FormFornecedor_30 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_30.setGeometry(QtCore.QRect(236, 180, 190, 20))
        self.lb_FormFornecedor_30.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_30.setObjectName("lb_FormFornecedor_30")
        self.lb_FormFornecedor_16 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_16.setGeometry(QtCore.QRect(580, 390, 70, 20))
        self.lb_FormFornecedor_16.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_16.setObjectName("lb_FormFornecedor_16")
        self.lb_FormFornecedor_6 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_6.setGeometry(QtCore.QRect(236, 120, 190, 20))
        self.lb_FormFornecedor_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_6.setObjectName("lb_FormFornecedor_6")
        self.tx_BairroEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_BairroEmpresa.setGeometry(QtCore.QRect(20, 415, 260, 25))
        self.tx_BairroEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_BairroEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_BairroEmpresa.setInputMask("")
        self.tx_BairroEmpresa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_BairroEmpresa.setPlaceholderText("")
        self.tx_BairroEmpresa.setObjectName("tx_BairroEmpresa")
        self.tx_EstadoEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_EstadoEmpresa.setGeometry(QtCore.QRect(580, 415, 70, 25))
        self.tx_EstadoEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_EstadoEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_EstadoEmpresa.setInputMask("")
        self.tx_EstadoEmpresa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_EstadoEmpresa.setPlaceholderText("")
        self.tx_EstadoEmpresa.setObjectName("tx_EstadoEmpresa")
        self.tx_Cnpj = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_Cnpj.setGeometry(QtCore.QRect(20, 145, 196, 25))
        self.tx_Cnpj.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Cnpj.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Cnpj.setText("")
        self.tx_Cnpj.setPlaceholderText("")
        self.tx_Cnpj.setObjectName("tx_Cnpj")
        self.tx_NumEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_NumEmpresa.setGeometry(QtCore.QRect(580, 360, 70, 25))
        self.tx_NumEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_NumEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_NumEmpresa.setInputMask("")
        self.tx_NumEmpresa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_NumEmpresa.setPlaceholderText("")
        self.tx_NumEmpresa.setObjectName("tx_NumEmpresa")
        self.lb_FormFornecedor = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor.setGeometry(QtCore.QRect(20, 10, 950, 30))
        self.lb_FormFornecedor.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor.setObjectName("lb_FormFornecedor")
        self.lb_FormFornecedor_25 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_25.setGeometry(QtCore.QRect(452, 180, 190, 20))
        self.lb_FormFornecedor_25.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_25.setObjectName("lb_FormFornecedor_25")
        self.lb_FormFornecedor_22 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_22.setGeometry(QtCore.QRect(345, 60, 150, 20))
        self.lb_FormFornecedor_22.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_22.setObjectName("lb_FormFornecedor_22")
        self.tx_CidadeEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_CidadeEmpresa.setGeometry(QtCore.QRect(300, 415, 260, 25))
        self.tx_CidadeEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_CidadeEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_CidadeEmpresa.setInputMask("")
        self.tx_CidadeEmpresa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_CidadeEmpresa.setPlaceholderText("")
        self.tx_CidadeEmpresa.setObjectName("tx_CidadeEmpresa")
        self.tx_SubTitulo = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_SubTitulo.setGeometry(QtCore.QRect(670, 145, 300, 25))
        self.tx_SubTitulo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_SubTitulo.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_SubTitulo.setObjectName("tx_SubTitulo")
        self.frame = QtWidgets.QFrame(self.fr_empresa)
        self.frame.setGeometry(QtCore.QRect(0, 460, 1000, 40))
        self.frame.setStyleSheet("border-bottom: 2px solid #CCC;\n"
"background: #F7F7F7")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_SalvarDadosEmpresa = QtWidgets.QPushButton(self.frame)
        self.bt_SalvarDadosEmpresa.setGeometry(QtCore.QRect(880, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_SalvarDadosEmpresa.setFont(font)
        self.bt_SalvarDadosEmpresa.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_SalvarDadosEmpresa.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_SalvarDadosEmpresa.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_SalvarDadosEmpresa.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_SalvarDadosEmpresa.setIconSize(QtCore.QSize(75, 35))
        self.bt_SalvarDadosEmpresa.setObjectName("bt_SalvarDadosEmpresa")
        self.tx_CepEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_CepEmpresa.setGeometry(QtCore.QRect(20, 360, 100, 25))
        self.tx_CepEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_CepEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_CepEmpresa.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_CepEmpresa.setObjectName("tx_CepEmpresa")
        self.tx_Titulo = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_Titulo.setGeometry(QtCore.QRect(670, 85, 300, 25))
        self.tx_Titulo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Titulo.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Titulo.setObjectName("tx_Titulo")
        self.lb_FormFornecedor_29 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_29.setGeometry(QtCore.QRect(160, 335, 250, 20))
        self.lb_FormFornecedor_29.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_29.setObjectName("lb_FormFornecedor_29")
        self.lb_FormFornecedor_9 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_9.setGeometry(QtCore.QRect(20, 180, 196, 20))
        self.lb_FormFornecedor_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_9.setObjectName("lb_FormFornecedor_9")
        self.tx_Endereco = QtWidgets.QLineEdit(self.fr_empresa)
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
        self.tx_EmailEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_EmailEmpresa.setGeometry(QtCore.QRect(452, 205, 196, 25))
        self.tx_EmailEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_EmailEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_EmailEmpresa.setPlaceholderText("")
        self.tx_EmailEmpresa.setObjectName("tx_EmailEmpresa")
        self.lb_FormFornecedor_18 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_18.setGeometry(QtCore.QRect(20, 120, 190, 20))
        self.lb_FormFornecedor_18.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_18.setObjectName("lb_FormFornecedor_18")
        self.lb_LogoEmpresa = QtWidgets.QLabel(self.fr_empresa)
        self.lb_LogoEmpresa.setGeometry(QtCore.QRect(670, 205, 300, 225))
        self.lb_LogoEmpresa.setStyleSheet("border: 1px solid #A2A2A2;\n"
"background: url(\'Images/icon/Photo.svg\') center no-repeat \n"
"")
        self.lb_LogoEmpresa.setText("")
        self.lb_LogoEmpresa.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_LogoEmpresa.setObjectName("lb_LogoEmpresa")
        self.lb_FormFornecedor_31 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_31.setGeometry(QtCore.QRect(20, 290, 630, 30))
        self.lb_FormFornecedor_31.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_31.setObjectName("lb_FormFornecedor_31")
        self.lb_FormFornecedor_19 = QtWidgets.QLabel(self.fr_empresa)
        self.lb_FormFornecedor_19.setGeometry(QtCore.QRect(20, 235, 150, 20))
        self.lb_FormFornecedor_19.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_19.setObjectName("lb_FormFornecedor_19")
        self.tx_NomeFantasia = QtWidgets.QLineEdit(self.fr_empresa)
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
        self.bt_AddLogo = QtWidgets.QPushButton(self.fr_empresa)
        self.bt_AddLogo.setGeometry(QtCore.QRect(935, 400, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.bt_AddLogo.setFont(font)
        self.bt_AddLogo.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_AddLogo.setText("")
        self.bt_AddLogo.setObjectName("bt_AddLogo")
        self.tx_idEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_idEmpresa.setEnabled(False)
        self.tx_idEmpresa.setGeometry(QtCore.QRect(910, 10, 50, 30))
        self.tx_idEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border: 1px solid #A2A2A2;\n"
"color: #000;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.tx_idEmpresa.setText("")
        self.tx_idEmpresa.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_idEmpresa.setObjectName("tx_idEmpresa")
        self.tx_ObsEmpresa = QtWidgets.QLineEdit(self.fr_empresa)
        self.tx_ObsEmpresa.setGeometry(QtCore.QRect(20, 260, 630, 25))
        self.tx_ObsEmpresa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ObsEmpresa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_ObsEmpresa.setObjectName("tx_ObsEmpresa")
        self.bt_DelLogo = QtWidgets.QPushButton(self.fr_empresa)
        self.bt_DelLogo.setGeometry(QtCore.QRect(935, 400, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.bt_DelLogo.setFont(font)
        self.bt_DelLogo.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_DelLogo.setText("")
        self.bt_DelLogo.setObjectName("bt_DelLogo")

        self.tradMainEmpresa(ct_empresa)
        QtCore.QMetaObject.connectSlotsByName(ct_empresa)
        ct_empresa.setTabOrder(self.tx_idEmpresa, self.tx_NomeFantasia)
        ct_empresa.setTabOrder(self.tx_NomeFantasia, self.tx_RazaoSocial)
        ct_empresa.setTabOrder(self.tx_RazaoSocial, self.tx_Cnpj)
        ct_empresa.setTabOrder(self.tx_Cnpj, self.tx_IE)
        ct_empresa.setTabOrder(self.tx_IE, self.tx_TelefoneEmpresa)
        ct_empresa.setTabOrder(self.tx_TelefoneEmpresa, self.tx_SiteEmpresa)
        ct_empresa.setTabOrder(self.tx_SiteEmpresa, self.tx_EmailEmpresa)
        ct_empresa.setTabOrder(self.tx_EmailEmpresa, self.tx_ObsEmpresa)
        ct_empresa.setTabOrder(self.tx_ObsEmpresa, self.tx_CepEmpresa)
        ct_empresa.setTabOrder(self.tx_CepEmpresa, self.bt_LocalizaCepEmpresa)
        ct_empresa.setTabOrder(self.bt_LocalizaCepEmpresa, self.tx_Endereco)
        ct_empresa.setTabOrder(self.tx_Endereco, self.tx_NumEmpresa)
        ct_empresa.setTabOrder(self.tx_NumEmpresa, self.tx_BairroEmpresa)
        ct_empresa.setTabOrder(self.tx_BairroEmpresa, self.tx_CidadeEmpresa)
        ct_empresa.setTabOrder(self.tx_CidadeEmpresa, self.tx_EstadoEmpresa)
        ct_empresa.setTabOrder(self.tx_EstadoEmpresa, self.tx_Titulo)
        ct_empresa.setTabOrder(self.tx_Titulo, self.tx_SubTitulo)
        ct_empresa.setTabOrder(self.tx_SubTitulo, self.bt_AddLogo)
        ct_empresa.setTabOrder(self.bt_AddLogo, self.bt_DelLogo)

    def tradMainEmpresa(self, ct_empresa):
        ct_empresa.setWindowTitle(QtWidgets.QApplication.translate("ct_empresa", "Frame", None, -1))
        self.lb_FormFornecedor_21.setText(QtWidgets.QApplication.translate("ct_empresa", "TITULO", None, -1))
        self.tx_TelefoneEmpresa.setInputMask(QtWidgets.QApplication.translate("ct_empresa", "(00) 0000-0000", None, -1))
        self.tx_TelefoneEmpresa.setText(QtWidgets.QApplication.translate("ct_empresa", "() -", None, -1))
        self.lb_FormFornecedor_27.setText(QtWidgets.QApplication.translate("ct_empresa", "Nº", None, -1))
        self.tx_RazaoSocial.setPlaceholderText(QtWidgets.QApplication.translate("ct_empresa", "Razão Social", None, -1))
        self.lb_FormFornecedor_28.setText(QtWidgets.QApplication.translate("ct_empresa", "CEP", None, -1))
        self.lb_FormFornecedor_23.setText(QtWidgets.QApplication.translate("ct_empresa", "SUB-TITULO", None, -1))
        self.lb_FormFornecedor_20.setText(QtWidgets.QApplication.translate("ct_empresa", "BAIRRO", None, -1))
        self.lb_FormFornecedor_17.setText(QtWidgets.QApplication.translate("ct_empresa", "NOME FANTASIA", None, -1))
        self.lb_FormFornecedor_26.setText(QtWidgets.QApplication.translate("ct_empresa", "CIDADE", None, -1))
        self.lb_FormFornecedor_30.setText(QtWidgets.QApplication.translate("ct_empresa", "SITE", None, -1))
        self.lb_FormFornecedor_16.setText(QtWidgets.QApplication.translate("ct_empresa", "ESTADO", None, -1))
        self.lb_FormFornecedor_6.setText(QtWidgets.QApplication.translate("ct_empresa", "IE", None, -1))
        self.lb_FormFornecedor.setText(QtWidgets.QApplication.translate("ct_empresa", "DADOS DA EMPRESA", None, -1))
        self.lb_FormFornecedor_25.setText(QtWidgets.QApplication.translate("ct_empresa", "Email", None, -1))
        self.lb_FormFornecedor_22.setText(QtWidgets.QApplication.translate("ct_empresa", "RAZÃO SOCIAL", None, -1))
        self.tx_SubTitulo.setPlaceholderText(QtWidgets.QApplication.translate("ct_empresa", "SUB-TITULO", None, -1))
        self.bt_SalvarDadosEmpresa.setText(QtWidgets.QApplication.translate("ct_empresa", "SALVAR", None, -1))
        self.tx_CepEmpresa.setInputMask(QtWidgets.QApplication.translate("ct_empresa", "99999-999", None, -1))
        self.tx_CepEmpresa.setPlaceholderText(QtWidgets.QApplication.translate("ct_empresa", "123456789", None, -1))
        self.tx_Titulo.setPlaceholderText(QtWidgets.QApplication.translate("ct_empresa", "TITULO ", None, -1))
        self.lb_FormFornecedor_29.setText(QtWidgets.QApplication.translate("ct_empresa", "ENDEREÇO", None, -1))
        self.lb_FormFornecedor_9.setText(QtWidgets.QApplication.translate("ct_empresa", "TELEFONE ", None, -1))
        self.lb_FormFornecedor_18.setText(QtWidgets.QApplication.translate("ct_empresa", "CNPJ", None, -1))
        self.lb_FormFornecedor_31.setText(QtWidgets.QApplication.translate("ct_empresa", "ENDEREÇO", None, -1))
        self.lb_FormFornecedor_19.setText(QtWidgets.QApplication.translate("ct_empresa", "OBSERVAÇÃO", None, -1))
        self.tx_NomeFantasia.setPlaceholderText(QtWidgets.QApplication.translate("ct_empresa", "NOME FANTASIA", None, -1))
        self.bt_AddLogo.setToolTip(QtWidgets.QApplication.translate("ct_empresa", "<html><head/><body><p>CADASTRAR IMGEM</p></body></html>", None, -1))
        self.tx_ObsEmpresa.setPlaceholderText(QtWidgets.QApplication.translate("ct_empresa", "Observação", None, -1))
        self.bt_DelLogo.setToolTip(QtWidgets.QApplication.translate("ct_empresa", "<html><head/><body><p>Deletar Imagem</p></body></html>", None, -1))

