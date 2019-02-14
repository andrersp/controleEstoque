# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFinanceiro.ui',
# licensing of 'mainFinanceiro.ui' applies.
#
# Created: Sat Feb  9 22:53:25 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_MainFinanceiro(object):
    def setMainFinanceiro(self, ct_MainFinanceiro):
        ct_MainFinanceiro.setObjectName("ct_MainFinanceiro")
        ct_MainFinanceiro.resize(1000, 600)
        ct_MainFinanceiro.setStyleSheet("border:none")
        self.frameMainFinanceiro = QtWidgets.QFrame(ct_MainFinanceiro)
        self.frameMainFinanceiro.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainFinanceiro.setObjectName("frameMainFinanceiro")
        self.fr_TituloFinanceiro = QtWidgets.QFrame(self.frameMainFinanceiro)
        self.fr_TituloFinanceiro.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloFinanceiro.setStyleSheet("border: none")
        self.fr_TituloFinanceiro.setObjectName("fr_TituloFinanceiro")
        self.lb_tituloFinanceiro = QtWidgets.QLabel(self.fr_TituloFinanceiro)
        self.lb_tituloFinanceiro.setGeometry(QtCore.QRect(10, 15, 271, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.lb_tituloFinanceiro.setFont(font)
        self.lb_tituloFinanceiro.setStyleSheet("color: #FFF")
        self.lb_tituloFinanceiro.setObjectName("lb_tituloFinanceiro")
        self.ct_financeiro = QtWidgets.QFrame(self.frameMainFinanceiro)
        self.ct_financeiro.setGeometry(QtCore.QRect(0, 100, 1000, 500))
        self.ct_financeiro.setStyleSheet("background: #FFF;\n"
                                         "border: none")
        self.ct_financeiro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ct_financeiro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ct_financeiro.setObjectName("ct_financeiro")
        self.fr_menuFinanceiro = QtWidgets.QFrame(self.frameMainFinanceiro)
        self.fr_menuFinanceiro.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_menuFinanceiro.setStyleSheet("background:#E1DFE0;\n"
                                             "border: none;\n"
                                             "border-bottom: 2px solid #069;")
        self.fr_menuFinanceiro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_menuFinanceiro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_menuFinanceiro.setObjectName("fr_menuFinanceiro")
        self.bt_MovCaixa = QtWidgets.QPushButton(self.fr_menuFinanceiro)
        self.bt_MovCaixa.setGeometry(QtCore.QRect(5, 2, 170, 36))
        font = QtGui.QFont()
        font.setFamily("Arial [Mono]")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_MovCaixa.setFont(font)
        self.bt_MovCaixa.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_MovCaixa.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_MovCaixa.setAutoFillBackground(False)
        self.bt_MovCaixa.setStyleSheet("QPushButton{\n"
                                       "background: #40A286 ;\n"
                                       "border: none;\n"
                                       "color: #FFF;\n"
                                       "border-top-left-radius: 4px;\n"
                                       "border-top-right-radius: 4px;\n"
                                       "margin-top: 7px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "background: #7AB32E;\n"
                                       "margin-top: 0;\n"
                                       "}\n"
                                       "QPushButton:disabled {\n"
                                       "background: #7AB32E;\n"
                                       "margin-top: 0;\n"
                                       "}\n"
                                       "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../../RSP/Images/icon/tag-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_MovCaixa.setIcon(icon)
        self.bt_MovCaixa.setIconSize(QtCore.QSize(25, 25))
        self.bt_MovCaixa.setFlat(True)
        self.bt_MovCaixa.setObjectName("bt_MovCaixa")
        self.bt_AReceber = QtWidgets.QPushButton(self.fr_menuFinanceiro)
        self.bt_AReceber.setGeometry(QtCore.QRect(185, 2, 170, 36))
        font = QtGui.QFont()
        font.setFamily("Arial [Mono]")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_AReceber.setFont(font)
        self.bt_AReceber.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_AReceber.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AReceber.setAutoFillBackground(False)
        self.bt_AReceber.setStyleSheet("QPushButton{\n"
                                       "background: #40A286 ;\n"
                                       "border: none;\n"
                                       "color: #FFF;\n"
                                       "border-top-left-radius: 4px;\n"
                                       "border-top-right-radius: 4px;\n"
                                       "margin-top: 7px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "background: #7AB32E;\n"
                                       "margin-top: 0;\n"
                                       "}\n"
                                       "QPushButton:disabled {\n"
                                       "background: #7AB32E;\n"
                                       "margin-top: 0;\n"
                                       "}\n"
                                       "")
        self.bt_AReceber.setIcon(icon)
        self.bt_AReceber.setIconSize(QtCore.QSize(25, 25))
        self.bt_AReceber.setFlat(True)
        self.bt_AReceber.setObjectName("bt_AReceber")
        self.bt_APagar = QtWidgets.QPushButton(self.fr_menuFinanceiro)
        self.bt_APagar.setEnabled(True)
        self.bt_APagar.setGeometry(QtCore.QRect(365, 2, 170, 36))
        font = QtGui.QFont()
        font.setFamily("Arial [Mono]")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_APagar.setFont(font)
        self.bt_APagar.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_APagar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_APagar.setAutoFillBackground(False)
        self.bt_APagar.setStyleSheet("QPushButton{\n"
                                     "background: #40A286 ;\n"
                                     "border: none;\n"
                                     "color: #FFF;\n"
                                     "border-top-left-radius: 4px;\n"
                                     "border-top-right-radius: 4px;\n"
                                     "margin-top: 7px;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "background: #7AB32E;\n"
                                     "margin-top: 0;\n"
                                     "}\n"
                                     "QPushButton:disabled {\n"
                                     "background: #7AB32E;\n"
                                     "margin-top: 0;\n"
                                     "}\n"
                                     "")
        self.bt_APagar.setIcon(icon)
        self.bt_APagar.setIconSize(QtCore.QSize(25, 25))
        self.bt_APagar.setFlat(True)
        self.bt_APagar.setObjectName("bt_APagar")

        self.tradMainFinanceiro(ct_MainFinanceiro)
        QtCore.QMetaObject.connectSlotsByName(ct_MainFinanceiro)

    def tradMainFinanceiro(self, ct_MainFinanceiro):
        ct_MainFinanceiro.setWindowTitle(QtWidgets.QApplication.translate(
            "ct_MainFinanceiro", "Frame", None, -1))
        self.lb_tituloFinanceiro.setText(QtWidgets.QApplication.translate(
            "ct_MainFinanceiro", "FINANCEIRO", None, -1))
        self.bt_MovCaixa.setText(QtWidgets.QApplication.translate(
            "ct_MainFinanceiro", "MOVIMENTO DE CAIXA", None, -1))
        self.bt_MovCaixa.setShortcut(QtWidgets.QApplication.translate(
            "ct_MainFinanceiro", "F7", None, -1))
        self.bt_AReceber.setText(QtWidgets.QApplication.translate(
            "ct_MainFinanceiro", "CONTAS A RECEBER", None, -1))
        self.bt_AReceber.setShortcut(QtWidgets.QApplication.translate(
            "ct_MainFinanceiro", "F7", None, -1))
        self.bt_APagar.setText(QtWidgets.QApplication.translate(
            "ct_MainFinanceiro", "CONTAS A PAGAR", None, -1))
        self.bt_APagar.setShortcut(QtWidgets.QApplication.translate(
            "ct_MainFinanceiro", "F7", None, -1))
