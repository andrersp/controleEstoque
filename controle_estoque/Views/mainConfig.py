# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainConfig.ui'
#
# Created by: PySide2 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ct_MainConfig(object):
    def setMainConfig(self, ct_MainConfig):
        ct_MainConfig.setObjectName("ct_MainConfig")
        ct_MainConfig.resize(1000, 600)
        ct_MainConfig.setStyleSheet("border:none")
        self.frameMainConfig = QtWidgets.QFrame(ct_MainConfig)
        self.frameMainConfig.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainConfig.setObjectName("frameMainConfig")
        self.fr_TituloConfig = QtWidgets.QFrame(self.frameMainConfig)
        self.fr_TituloConfig.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloConfig.setStyleSheet("border: none")
        self.fr_TituloConfig.setObjectName("fr_TituloConfig")
        self.lb_tituloConfig = QtWidgets.QLabel(self.fr_TituloConfig)
        self.lb_tituloConfig.setGeometry(QtCore.QRect(10, 15, 271, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloConfig.setFont(font)
        self.lb_tituloConfig.setStyleSheet("color: #FFF")
        self.lb_tituloConfig.setObjectName("lb_tituloConfig")
        self.tab_Config = QtWidgets.QTabWidget(self.frameMainConfig)
        self.tab_Config.setGeometry(QtCore.QRect(0, 65, 1000, 535))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.tab_Config.setFont(font)
        self.tab_Config.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_Config.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px solid #069;\n"
"background-color: #FFF;\n"
"        }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     left: 2px; /* move to the right by 5px */\n"
"     background: red;\n"
"\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"background: #40A286 ;\n"
"border: none;\n"
"color: #FFF;\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8px;\n"
"     padding: 5px 10px;\n"
"margin: 0 2px 0 0;\n"
"width: 200px;\n"
"height: 26px;\n"
" }\n"
"\n"
"\n"
" QTabBar::tab:selected {\n"
"     background: #7AB32E;\n"
"     border-color: #9B9B9B;\n"
"    height: 30px\n"
"     /* border-bottom-color: red; same as pane color */\n"
" }\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 4px; /* make non-selected tabs look smaller */\n"
" }")
        self.tab_Config.setIconSize(QtCore.QSize(25, 25))
        self.tab_Config.setUsesScrollButtons(False)
        self.tab_Config.setObjectName("tab_Config")
        self.tab_empresa = QtWidgets.QWidget()
        self.tab_empresa.setObjectName("tab_empresa")
        self.fr_BotoesEmpresa = QtWidgets.QFrame(self.tab_empresa)
        self.fr_BotoesEmpresa.setGeometry(QtCore.QRect(0, 463, 1000, 30))
        self.fr_BotoesEmpresa.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesEmpresa.setObjectName("fr_BotoesEmpresa")
        self.bt_SalvarDadosEmpresa = QtWidgets.QPushButton(self.fr_BotoesEmpresa)
        self.bt_SalvarDadosEmpresa.setGeometry(QtCore.QRect(880, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_SalvarDadosEmpresa.setFont(font)
        self.bt_SalvarDadosEmpresa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.tx_IE = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_6 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_6.setGeometry(QtCore.QRect(236, 120, 190, 20))
        self.lb_FormFornecedor_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_6.setObjectName("lb_FormFornecedor_6")
        self.tx_CidadeEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_16 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_16.setGeometry(QtCore.QRect(580, 390, 70, 20))
        self.lb_FormFornecedor_16.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_16.setObjectName("lb_FormFornecedor_16")
        self.lb_FormFornecedor_25 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_25.setGeometry(QtCore.QRect(452, 180, 190, 20))
        self.lb_FormFornecedor_25.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_25.setObjectName("lb_FormFornecedor_25")
        self.lb_FormFornecedor_9 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_9.setGeometry(QtCore.QRect(20, 180, 196, 20))
        self.lb_FormFornecedor_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_9.setObjectName("lb_FormFornecedor_9")
        self.tx_Cnpj = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.tx_EmailEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_17 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_17.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.lb_FormFornecedor_17.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_17.setObjectName("lb_FormFornecedor_17")
        self.tx_ObsEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_18 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_18.setGeometry(QtCore.QRect(20, 120, 190, 20))
        self.lb_FormFornecedor_18.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_18.setObjectName("lb_FormFornecedor_18")
        self.lb_FormFornecedor_19 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_19.setGeometry(QtCore.QRect(20, 235, 150, 20))
        self.lb_FormFornecedor_19.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_19.setObjectName("lb_FormFornecedor_19")
        self.tx_SiteEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_22 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_22.setGeometry(QtCore.QRect(345, 60, 150, 20))
        self.lb_FormFornecedor_22.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_22.setObjectName("lb_FormFornecedor_22")
        self.tx_NumEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_20 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_20.setGeometry(QtCore.QRect(20, 390, 120, 20))
        self.lb_FormFornecedor_20.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_20.setObjectName("lb_FormFornecedor_20")
        self.bt_LocalizaCepEmpresa = QtWidgets.QPushButton(self.tab_empresa)
        self.bt_LocalizaCepEmpresa.setGeometry(QtCore.QRect(120, 360, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
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
        self.tx_RazaoSocial = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.tx_TelefoneEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.tx_CepEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.tx_Endereco = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_26 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_26.setGeometry(QtCore.QRect(300, 390, 120, 20))
        self.lb_FormFornecedor_26.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_26.setObjectName("lb_FormFornecedor_26")
        self.lb_FormFornecedor_27 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_27.setGeometry(QtCore.QRect(580, 335, 50, 20))
        self.lb_FormFornecedor_27.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_27.setObjectName("lb_FormFornecedor_27")
        self.tx_BairroEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_28 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_28.setGeometry(QtCore.QRect(20, 335, 50, 20))
        self.lb_FormFornecedor_28.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_28.setObjectName("lb_FormFornecedor_28")
        self.lb_FormFornecedor_29 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_29.setGeometry(QtCore.QRect(160, 335, 250, 20))
        self.lb_FormFornecedor_29.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_29.setObjectName("lb_FormFornecedor_29")
        self.tx_NomeFantasia = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.tx_EstadoEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_30 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_30.setGeometry(QtCore.QRect(236, 180, 190, 20))
        self.lb_FormFornecedor_30.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_30.setObjectName("lb_FormFornecedor_30")
        self.lb_FormFornecedor_31 = QtWidgets.QLabel(self.tab_empresa)
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
        self.tx_idEmpresa = QtWidgets.QLineEdit(self.tab_empresa)
        self.tx_idEmpresa.setEnabled(False)
        self.tx_idEmpresa.setGeometry(QtCore.QRect(920, 10, 50, 30))
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
        self.lb_FormFornecedor = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor.setGeometry(QtCore.QRect(20, 10, 950, 30))
        self.lb_FormFornecedor.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor.setObjectName("lb_FormFornecedor")
        self.bt_AddLogo = QtWidgets.QPushButton(self.tab_empresa)
        self.bt_AddLogo.setGeometry(QtCore.QRect(935, 400, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
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
        self.lb_LogoEmpresa = QtWidgets.QLabel(self.tab_empresa)
        self.lb_LogoEmpresa.setGeometry(QtCore.QRect(670, 205, 300, 225))
        self.lb_LogoEmpresa.setStyleSheet("border: 1px solid #A2A2A2;\n"
"background: url(\'Images/icon/Photo.svg\') center no-repeat \n"
"")
        self.lb_LogoEmpresa.setText("")
        self.lb_LogoEmpresa.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_LogoEmpresa.setObjectName("lb_LogoEmpresa")
        self.tx_Titulo = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.lb_FormFornecedor_21 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_21.setGeometry(QtCore.QRect(670, 60, 150, 20))
        self.lb_FormFornecedor_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_21.setObjectName("lb_FormFornecedor_21")
        self.lb_FormFornecedor_23 = QtWidgets.QLabel(self.tab_empresa)
        self.lb_FormFornecedor_23.setGeometry(QtCore.QRect(670, 120, 150, 20))
        self.lb_FormFornecedor_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_23.setObjectName("lb_FormFornecedor_23")
        self.tx_SubTitulo = QtWidgets.QLineEdit(self.tab_empresa)
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
        self.bt_DelLogo = QtWidgets.QPushButton(self.tab_empresa)
        self.bt_DelLogo.setGeometry(QtCore.QRect(935, 400, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
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
        self.fr_BotoesEmpresa.raise_()
        self.tx_IE.raise_()
        self.lb_FormFornecedor_6.raise_()
        self.tx_CidadeEmpresa.raise_()
        self.lb_FormFornecedor_16.raise_()
        self.lb_FormFornecedor_25.raise_()
        self.lb_FormFornecedor_9.raise_()
        self.tx_Cnpj.raise_()
        self.tx_EmailEmpresa.raise_()
        self.lb_FormFornecedor_17.raise_()
        self.tx_ObsEmpresa.raise_()
        self.lb_FormFornecedor_18.raise_()
        self.lb_FormFornecedor_19.raise_()
        self.tx_SiteEmpresa.raise_()
        self.lb_FormFornecedor_22.raise_()
        self.tx_NumEmpresa.raise_()
        self.lb_FormFornecedor_20.raise_()
        self.bt_LocalizaCepEmpresa.raise_()
        self.tx_RazaoSocial.raise_()
        self.tx_TelefoneEmpresa.raise_()
        self.tx_CepEmpresa.raise_()
        self.tx_Endereco.raise_()
        self.lb_FormFornecedor_26.raise_()
        self.lb_FormFornecedor_27.raise_()
        self.tx_BairroEmpresa.raise_()
        self.lb_FormFornecedor_28.raise_()
        self.lb_FormFornecedor_29.raise_()
        self.tx_NomeFantasia.raise_()
        self.tx_EstadoEmpresa.raise_()
        self.lb_FormFornecedor_30.raise_()
        self.lb_FormFornecedor_31.raise_()
        self.tx_idEmpresa.raise_()
        self.lb_FormFornecedor.raise_()
        self.lb_LogoEmpresa.raise_()
        self.tx_Titulo.raise_()
        self.lb_FormFornecedor_21.raise_()
        self.lb_FormFornecedor_23.raise_()
        self.tx_SubTitulo.raise_()
        self.bt_DelLogo.raise_()
        self.bt_AddLogo.raise_()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_Config.addTab(self.tab_empresa, icon, "")
        self.tab_database = QtWidgets.QWidget()
        self.tab_database.setObjectName("tab_database")
        self.fr_BotoesDataBase = QtWidgets.QFrame(self.tab_database)
        self.fr_BotoesDataBase.setGeometry(QtCore.QRect(0, 463, 1000, 30))
        self.fr_BotoesDataBase.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesDataBase.setObjectName("fr_BotoesDataBase")
        self.bt_SalvarConfigDB = QtWidgets.QPushButton(self.fr_BotoesDataBase)
        self.bt_SalvarConfigDB.setEnabled(False)
        self.bt_SalvarConfigDB.setGeometry(QtCore.QRect(880, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_SalvarConfigDB.setFont(font)
        self.bt_SalvarConfigDB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_SalvarConfigDB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_SalvarConfigDB.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_SalvarConfigDB.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: #CCC;\n"
"\n"
"}")
        self.bt_SalvarConfigDB.setIconSize(QtCore.QSize(75, 35))
        self.bt_SalvarConfigDB.setObjectName("bt_SalvarConfigDB")
        self.lb_FormFornecedor_2 = QtWidgets.QLabel(self.tab_database)
        self.lb_FormFornecedor_2.setGeometry(QtCore.QRect(20, 10, 950, 30))
        self.lb_FormFornecedor_2.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor_2.setObjectName("lb_FormFornecedor_2")
        self.tx_IpServer = QtWidgets.QLineEdit(self.tab_database)
        self.tx_IpServer.setGeometry(QtCore.QRect(20, 85, 120, 25))
        self.tx_IpServer.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_IpServer.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_IpServer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_IpServer.setObjectName("tx_IpServer")
        self.lb_FormFornecedor_24 = QtWidgets.QLabel(self.tab_database)
        self.lb_FormFornecedor_24.setGeometry(QtCore.QRect(20, 60, 180, 20))
        self.lb_FormFornecedor_24.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_24.setObjectName("lb_FormFornecedor_24")
        self.lb_FormFornecedor_32 = QtWidgets.QLabel(self.tab_database)
        self.lb_FormFornecedor_32.setGeometry(QtCore.QRect(20, 120, 180, 25))
        self.lb_FormFornecedor_32.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_32.setObjectName("lb_FormFornecedor_32")
        self.tx_DbName = QtWidgets.QLineEdit(self.tab_database)
        self.tx_DbName.setGeometry(QtCore.QRect(20, 145, 180, 25))
        self.tx_DbName.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_DbName.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_DbName.setInputMask("")
        self.tx_DbName.setText("")
        self.tx_DbName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_DbName.setObjectName("tx_DbName")
        self.lb_FormFornecedor_33 = QtWidgets.QLabel(self.tab_database)
        self.lb_FormFornecedor_33.setGeometry(QtCore.QRect(20, 180, 180, 25))
        self.lb_FormFornecedor_33.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_33.setObjectName("lb_FormFornecedor_33")
        self.tx_DbUser = QtWidgets.QLineEdit(self.tab_database)
        self.tx_DbUser.setGeometry(QtCore.QRect(20, 205, 180, 25))
        self.tx_DbUser.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_DbUser.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_DbUser.setInputMask("")
        self.tx_DbUser.setText("")
        self.tx_DbUser.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_DbUser.setObjectName("tx_DbUser")
        self.tx_DbPass = QtWidgets.QLineEdit(self.tab_database)
        self.tx_DbPass.setGeometry(QtCore.QRect(20, 260, 180, 25))
        self.tx_DbPass.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_DbPass.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_DbPass.setInputMask("")
        self.tx_DbPass.setText("")
        self.tx_DbPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_DbPass.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_DbPass.setObjectName("tx_DbPass")
        self.lb_FormFornecedor_34 = QtWidgets.QLabel(self.tab_database)
        self.lb_FormFornecedor_34.setGeometry(QtCore.QRect(20, 235, 180, 25))
        self.lb_FormFornecedor_34.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_34.setObjectName("lb_FormFornecedor_34")
        self.bt_TestarConexao = QtWidgets.QPushButton(self.tab_database)
        self.bt_TestarConexao.setGeometry(QtCore.QRect(20, 300, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.bt_TestarConexao.setFont(font)
        self.bt_TestarConexao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_TestarConexao.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_TestarConexao.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_TestarConexao.setStyleSheet("QPushButton{\n"
"background: #40A286 ;\n"
"border: none;\n"
"color: #FFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover {\n"
"background: #7AB32E\n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E\n"
"}")
        self.bt_TestarConexao.setIconSize(QtCore.QSize(75, 35))
        self.bt_TestarConexao.setObjectName("bt_TestarConexao")
        self.lb_StatusTesteDb = QtWidgets.QLabel(self.tab_database)
        self.lb_StatusTesteDb.setGeometry(QtCore.QRect(210, 300, 30, 30))
        self.lb_StatusTesteDb.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_StatusTesteDb.setText("")
        self.lb_StatusTesteDb.setObjectName("lb_StatusTesteDb")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/icon/sql.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_Config.addTab(self.tab_database, icon1, "")
        self.fr_TopoConfig = QtWidgets.QFrame(self.frameMainConfig)
        self.fr_TopoConfig.setGeometry(QtCore.QRect(0, 60, 1000, 45))
        self.fr_TopoConfig.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_TopoConfig.setObjectName("fr_TopoConfig")
        self.fr_TituloConfig.raise_()
        self.fr_TopoConfig.raise_()
        self.tab_Config.raise_()

        self.tradMainConfig(ct_MainConfig)
        self.tab_Config.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ct_MainConfig)

    def tradMainConfig(self, ct_MainConfig):
        _translate = QtCore.QCoreApplication.translate
        ct_MainConfig.setWindowTitle(_translate("ct_MainConfig", "Frame"))
        self.lb_tituloConfig.setText(_translate("ct_MainConfig", "CONFIGURAÇÃO"))
        self.bt_SalvarDadosEmpresa.setText(_translate("ct_MainConfig", "SALVAR"))
        self.lb_FormFornecedor_6.setText(_translate("ct_MainConfig", "IE"))
        self.lb_FormFornecedor_16.setText(_translate("ct_MainConfig", "ESTADO"))
        self.lb_FormFornecedor_25.setText(_translate("ct_MainConfig", "Email"))
        self.lb_FormFornecedor_9.setText(_translate("ct_MainConfig", "TELEFONE "))
        self.lb_FormFornecedor_17.setText(_translate("ct_MainConfig", "NOME FANTASIA"))
        self.tx_ObsEmpresa.setPlaceholderText(_translate("ct_MainConfig", "Observação"))
        self.lb_FormFornecedor_18.setText(_translate("ct_MainConfig", "CNPJ"))
        self.lb_FormFornecedor_19.setText(_translate("ct_MainConfig", "OBSERVAÇÃO"))
        self.lb_FormFornecedor_22.setText(_translate("ct_MainConfig", "RAZÃO SOCIAL"))
        self.lb_FormFornecedor_20.setText(_translate("ct_MainConfig", "BAIRRO"))
        self.tx_RazaoSocial.setPlaceholderText(_translate("ct_MainConfig", "Razão Social"))
        self.tx_TelefoneEmpresa.setInputMask(_translate("ct_MainConfig", "(00) 0000-0000"))
        self.tx_TelefoneEmpresa.setText(_translate("ct_MainConfig", "() -"))
        self.tx_CepEmpresa.setInputMask(_translate("ct_MainConfig", "99999-999"))
        self.tx_CepEmpresa.setPlaceholderText(_translate("ct_MainConfig", "123456789"))
        self.lb_FormFornecedor_26.setText(_translate("ct_MainConfig", "CIDADE"))
        self.lb_FormFornecedor_27.setText(_translate("ct_MainConfig", "Nº"))
        self.lb_FormFornecedor_28.setText(_translate("ct_MainConfig", "CEP"))
        self.lb_FormFornecedor_29.setText(_translate("ct_MainConfig", "ENDEREÇO"))
        self.tx_NomeFantasia.setPlaceholderText(_translate("ct_MainConfig", "NOME FANTASIA"))
        self.lb_FormFornecedor_30.setText(_translate("ct_MainConfig", "SITE"))
        self.lb_FormFornecedor_31.setText(_translate("ct_MainConfig", "ENDEREÇO"))
        self.lb_FormFornecedor.setText(_translate("ct_MainConfig", "DADOS DA EMPRESA"))
        self.bt_AddLogo.setToolTip(_translate("ct_MainConfig", "<html><head/><body><p>CADASTRAR IMGEM</p></body></html>"))
        self.tx_Titulo.setPlaceholderText(_translate("ct_MainConfig", "TITULO "))
        self.lb_FormFornecedor_21.setText(_translate("ct_MainConfig", "TITULO"))
        self.lb_FormFornecedor_23.setText(_translate("ct_MainConfig", "SUB-TITULO"))
        self.tx_SubTitulo.setPlaceholderText(_translate("ct_MainConfig", "SUB-TITULO"))
        self.bt_DelLogo.setToolTip(_translate("ct_MainConfig", "<html><head/><body><p>Deletar Imagem</p></body></html>"))
        self.tab_Config.setTabText(self.tab_Config.indexOf(self.tab_empresa), _translate("ct_MainConfig", "Dados da Empresa"))
        self.bt_SalvarConfigDB.setText(_translate("ct_MainConfig", "SALVAR"))
        self.lb_FormFornecedor_2.setText(_translate("ct_MainConfig", "CONFIGURAÇÃO BANCO DE DADOS"))
        self.tx_IpServer.setInputMask(_translate("ct_MainConfig", "000.000.000.000"))
        self.tx_IpServer.setText(_translate("ct_MainConfig", "..."))
        self.tx_IpServer.setPlaceholderText(_translate("ct_MainConfig", "127.0.0.1"))
        self.lb_FormFornecedor_24.setText(_translate("ct_MainConfig", "ENDEREÇO IP SERVIDOR"))
        self.lb_FormFornecedor_32.setText(_translate("ct_MainConfig", "NOME DO BANCO DE DADOS"))
        self.tx_DbName.setPlaceholderText(_translate("ct_MainConfig", "DB NAME"))
        self.lb_FormFornecedor_33.setText(_translate("ct_MainConfig", "USUÁRIO"))
        self.tx_DbUser.setPlaceholderText(_translate("ct_MainConfig", "DB USER"))
        self.tx_DbPass.setPlaceholderText(_translate("ct_MainConfig", "DB PASS"))
        self.lb_FormFornecedor_34.setText(_translate("ct_MainConfig", "SENHA "))
        self.bt_TestarConexao.setText(_translate("ct_MainConfig", "TESTAR"))
        self.tab_Config.setTabText(self.tab_Config.indexOf(self.tab_database), _translate("ct_MainConfig", "Banco de dados"))
