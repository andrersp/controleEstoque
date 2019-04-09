# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDbConfig.ui',
# licensing of 'mainDbConfig.ui' applies.
#
# Created: Fri Mar 15 09:57:40 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_dbConf(object):
    def setDbConf(self, ct_dbConf):
        ct_dbConf.setObjectName("ct_dbConf")
        ct_dbConf.resize(1000, 500)
        ct_dbConf.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_dbConf = QtWidgets.QFrame(ct_dbConf)
        self.fr_dbConf.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_dbConf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_dbConf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_dbConf.setObjectName("fr_dbConf")
        self.fr_BotoesDataBase = QtWidgets.QFrame(self.fr_dbConf)
        self.fr_BotoesDataBase.setGeometry(QtCore.QRect(0, 460, 1000, 40))
        self.fr_BotoesDataBase.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesDataBase.setObjectName("fr_BotoesDataBase")
        self.bt_SalvarConfigDB = QtWidgets.QPushButton(self.fr_BotoesDataBase)
        self.bt_SalvarConfigDB.setEnabled(False)
        self.bt_SalvarConfigDB.setGeometry(QtCore.QRect(880, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_SalvarConfigDB.setFont(font)
        self.bt_SalvarConfigDB.setCursor(QtCore.Qt.PointingHandCursor)
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
        self.lb_FormFornecedor_3 = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_FormFornecedor_3.setGeometry(QtCore.QRect(20, 10, 950, 30))
        self.lb_FormFornecedor_3.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor_3.setObjectName("lb_FormFornecedor_3")
        self.lb_FormFornecedor_25 = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_FormFornecedor_25.setGeometry(QtCore.QRect(20, 60, 180, 20))
        self.lb_FormFornecedor_25.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_25.setObjectName("lb_FormFornecedor_25")
        self.lb_FormFornecedor_46 = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_FormFornecedor_46.setGeometry(QtCore.QRect(20, 120, 180, 25))
        self.lb_FormFornecedor_46.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_46.setObjectName("lb_FormFornecedor_46")
        self.lb_FormFornecedor_47 = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_FormFornecedor_47.setGeometry(QtCore.QRect(20, 180, 180, 25))
        self.lb_FormFornecedor_47.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_47.setObjectName("lb_FormFornecedor_47")
        self.tx_DbPass = QtWidgets.QLineEdit(self.fr_dbConf)
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
        self.lb_FormFornecedor_48 = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_FormFornecedor_48.setGeometry(QtCore.QRect(20, 235, 180, 25))
        self.lb_FormFornecedor_48.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_48.setObjectName("lb_FormFornecedor_48")
        self.tx_DbUser = QtWidgets.QLineEdit(self.fr_dbConf)
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
        self.tx_IpServer = QtWidgets.QLineEdit(self.fr_dbConf)
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
        self.tx_DbName = QtWidgets.QLineEdit(self.fr_dbConf)
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
        self.bt_TestarConexao = QtWidgets.QPushButton(self.fr_dbConf)
        self.bt_TestarConexao.setGeometry(QtCore.QRect(20, 300, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setWeight(50)
        font.setBold(False)
        self.bt_TestarConexao.setFont(font)
        self.bt_TestarConexao.setCursor(QtCore.Qt.PointingHandCursor)
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
        self.lb_StatusTesteDb = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_StatusTesteDb.setGeometry(QtCore.QRect(210, 300, 30, 30))
        self.lb_StatusTesteDb.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_StatusTesteDb.setText("")
        self.lb_StatusTesteDb.setObjectName("lb_StatusTesteDb")
        self.lb_status_db = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_status_db.setGeometry(QtCore.QRect(210, 145, 240, 25))
        self.lb_status_db.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_status_db.setText("")
        self.lb_status_db.setObjectName("lb_status_db")
        self.lb_status_user = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_status_user.setGeometry(QtCore.QRect(210, 205, 240, 25))
        self.lb_status_user.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_status_user.setText("")
        self.lb_status_user.setObjectName("lb_status_user")
        self.lb_status_senha = QtWidgets.QLabel(self.fr_dbConf)
        self.lb_status_senha.setGeometry(QtCore.QRect(210, 260, 240, 25))
        self.lb_status_senha.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_status_senha.setText("")
        self.lb_status_senha.setObjectName("lb_status_senha")

        self.traddBConf(ct_dbConf)
        QtCore.QMetaObject.connectSlotsByName(ct_dbConf)
        ct_dbConf.setTabOrder(self.tx_IpServer, self.tx_DbName)
        ct_dbConf.setTabOrder(self.tx_DbName, self.tx_DbUser)
        ct_dbConf.setTabOrder(self.tx_DbUser, self.tx_DbPass)

    def traddBConf(self, ct_dbConf):
        ct_dbConf.setWindowTitle(QtWidgets.QApplication.translate("ct_dbConf", "Frame", None, -1))
        self.bt_SalvarConfigDB.setText(QtWidgets.QApplication.translate("ct_dbConf", "SALVAR", None, -1))
        self.lb_FormFornecedor_3.setText(QtWidgets.QApplication.translate("ct_dbConf", "CONFIGURAÇÃO BANCO DE DADOS", None, -1))
        self.lb_FormFornecedor_25.setText(QtWidgets.QApplication.translate("ct_dbConf", "ENDEREÇO IP SERVIDOR", None, -1))
        self.lb_FormFornecedor_46.setText(QtWidgets.QApplication.translate("ct_dbConf", "NOME DO BANCO DE DADOS", None, -1))
        self.lb_FormFornecedor_47.setText(QtWidgets.QApplication.translate("ct_dbConf", "USUÁRIO", None, -1))
        self.tx_DbPass.setPlaceholderText(QtWidgets.QApplication.translate("ct_dbConf", "DB PASS", None, -1))
        self.lb_FormFornecedor_48.setText(QtWidgets.QApplication.translate("ct_dbConf", "SENHA ", None, -1))
        self.tx_DbUser.setPlaceholderText(QtWidgets.QApplication.translate("ct_dbConf", "DB USER", None, -1))
        self.tx_IpServer.setInputMask(QtWidgets.QApplication.translate("ct_dbConf", "000.000.000.000", None, -1))
        self.tx_IpServer.setText(QtWidgets.QApplication.translate("ct_dbConf", "...", None, -1))
        self.tx_IpServer.setPlaceholderText(QtWidgets.QApplication.translate("ct_dbConf", "127.0.0.1", None, -1))
        self.tx_DbName.setPlaceholderText(QtWidgets.QApplication.translate("ct_dbConf", "DB NAME", None, -1))
        self.bt_TestarConexao.setText(QtWidgets.QApplication.translate("ct_dbConf", "TESTAR", None, -1))

