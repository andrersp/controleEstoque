# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui',
# licensing of 'login.ui' applies.
#
# Created: Fri Mar 22 09:40:29 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_login(object):
    def setLogin(self, ct_login):
        ct_login.setObjectName("ct_login")
        ct_login.resize(1000, 600)
        self.frame_login = QtWidgets.QFrame(ct_login)
        self.frame_login.setGeometry(QtCore.QRect(300, 150, 400, 300))
        self.frame_login.setStyleSheet("QFrame {\n"
                                       "background: rgba(0, 0, 0, 30%);\n"
                                       "border: none;\n"
                                       "border-radius: 20px\n"
                                       "}")
        self.frame_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login.setObjectName("frame_login")
        self.lb_FormCompra_4 = QtWidgets.QLabel(self.frame_login)
        self.lb_FormCompra_4.setGeometry(QtCore.QRect(20, 40, 120, 20))
        self.lb_FormCompra_4.setStyleSheet("QLabel{\n"
                                           "font-size: 13px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #FFF;\n"
                                           "background: none\n"
                                           "}")
        self.lb_FormCompra_4.setObjectName("lb_FormCompra_4")
        self.tx_user = QtWidgets.QLineEdit(self.frame_login)
        self.tx_user.setGeometry(QtCore.QRect(20, 60, 360, 30))
        self.tx_user.setMouseTracking(True)
        self.tx_user.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_user.setStyleSheet("QLineEdit{\n"
                                   "background: #CFCFCF;\n"
                                   "border-radius: 2px;\n"
                                   "color: #000;\n"
                                   "font: 13px \"Arial\" ;\n"
                                   "background: url(" + self.resourcepath('Images/user.png') +
                                   ") right center no-repeat\n"
                                   "}\n"
                                   "QLineEdit:Focus {\n"
                                   "border: 1px solid red;\n"
                                   "}")
        self.tx_user.setText("")
        self.tx_user.setFrame(False)
        self.tx_user.setCursorPosition(0)
        self.tx_user.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tx_user.setReadOnly(False)
        self.tx_user.setObjectName("tx_user")
        self.lb_FormCompra_5 = QtWidgets.QLabel(self.frame_login)
        self.lb_FormCompra_5.setGeometry(QtCore.QRect(20, 110, 120, 20))
        self.lb_FormCompra_5.setStyleSheet("QLabel{\n"
                                           "font-size: 13px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #FFF;\n"
                                           "background: none\n"
                                           "}")
        self.lb_FormCompra_5.setObjectName("lb_FormCompra_5")
        self.tx_senha = QtWidgets.QLineEdit(self.frame_login)
        self.tx_senha.setGeometry(QtCore.QRect(20, 130, 360, 30))
        self.tx_senha.setMouseTracking(True)
        self.tx_senha.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_senha.setStyleSheet("QLineEdit{\n"
                                    "background: #CFCFCF;\n"
                                    "border-radius: 2px;\n"
                                    "color: #000;\n"
                                    "font: 13px \"Arial\" ;\n"
                                    "background: url(" + self.resourcepath(
                                        'Images/senha.png')+") right center no-repeat\n"
                                    "\n"
                                    "}\n"
                                    "QLineEdit:Focus {\n"
                                    "border: 1px solid red;\n"
                                    "}")
        self.tx_senha.setText("")
        self.tx_senha.setFrame(False)
        self.tx_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_senha.setCursorPosition(0)
        self.tx_senha.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tx_senha.setReadOnly(False)
        self.tx_senha.setObjectName("tx_senha")
        self.bt_login = QtWidgets.QPushButton(self.frame_login)
        self.bt_login.setGeometry(QtCore.QRect(20, 180, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_login.setFont(font)
        self.bt_login.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_login.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_login.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_login.setStyleSheet("QPushButton {\n"
                                    "background-color: #7AB32E;\n"
                                    "color: #FFF\n"
                                    " }\n"
                                    "QPushButton:hover{\n"
                                    "background-color: #40a286\n"
                                    "}")
        self.bt_login.setIconSize(QtCore.QSize(75, 35))
        self.bt_login.setObjectName("bt_login")
        self.lb_alert = QtWidgets.QLabel(self.frame_login)
        self.lb_alert.setGeometry(QtCore.QRect(20, 220, 360, 30))
        self.lb_alert.setStyleSheet("QLabel{\n"
                                    "font-size: 13px;\n"
                                    "font-family: \"Arial\";\n"
                                    "font-weight: bold;\n"
                                    "color: #FFF;\n"
                                    "background: none\n"
                                    "}")
        self.lb_alert.setText("")
        self.lb_alert.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_alert.setObjectName("lb_alert")

        self.tradLogin(ct_login)
        QtCore.QMetaObject.connectSlotsByName(ct_login)

    def tradLogin(self, ct_login):
        ct_login.setWindowTitle(QtWidgets.QApplication.translate(
            "ct_login", "Frame", None, -1))
        self.lb_FormCompra_4.setText(
            QtWidgets.QApplication.translate("ct_login", "USUÁRIO", None, -1))
        self.tx_user.setPlaceholderText(
            QtWidgets.QApplication.translate("ct_login", "Seu Usuário", None, -1))
        self.lb_FormCompra_5.setText(
            QtWidgets.QApplication.translate("ct_login", "SENHA", None, -1))
        self.tx_senha.setPlaceholderText(
            QtWidgets.QApplication.translate("ct_login", "Sua Senha", None, -1))
        self.bt_login.setText(QtWidgets.QApplication.translate(
            "ct_login", "LOGIN", None, -1))
