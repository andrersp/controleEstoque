# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PySide2 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_Home(object):
    def setHome(self, ct_Home):
        ct_Home.setObjectName("ct_Home")
        ct_Home.resize(1000, 600)
        ct_Home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.HomeFrame = QtWidgets.QFrame(ct_Home)
        self.HomeFrame.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.HomeFrame.setObjectName("HomeFrame")
        self.fr_VendasAbertas = QtWidgets.QFrame(self.HomeFrame)
        self.fr_VendasAbertas.setGeometry(QtCore.QRect(20, 10, 470, 280))
        self.fr_VendasAbertas.setStyleSheet("QFrame {\n"
                                            "background: rgba(0, 0, 0, 30%);\n"
                                            "border: none;\n"
                                            "border-radius: 20px\n"
                                            "\n"
                                            "}")
        self.fr_VendasAbertas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_VendasAbertas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_VendasAbertas.setObjectName("fr_VendasAbertas")
        self.fr_PedidosPendentes = QtWidgets.QFrame(self.HomeFrame)
        self.fr_PedidosPendentes.setGeometry(QtCore.QRect(510, 10, 470, 280))
        self.fr_PedidosPendentes.setStyleSheet("QFrame {\n"
                                               "background: rgba(0, 0, 0, 30%);\n"
                                               "border: none;\n"
                                               "border-radius: 20px\n"
                                               "}")
        self.fr_PedidosPendentes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_PedidosPendentes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_PedidosPendentes.setObjectName("fr_PedidosPendentes")
        self.fr_ListaEstoque_2 = QtWidgets.QFrame(self.HomeFrame)
        self.fr_ListaEstoque_2.setGeometry(QtCore.QRect(510, 310, 470, 280))
        self.fr_ListaEstoque_2.setStyleSheet("QFrame {\n"
                                             "background: rgba(0, 0, 0, 30%);\n"
                                             "border: none;\n"
                                             "border-radius: 20px\n"
                                             "}")
        self.fr_ListaEstoque_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_ListaEstoque_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_ListaEstoque_2.setObjectName("fr_ListaEstoque_2")
        self.fr_EstoqueAtual = QtWidgets.QFrame(self.HomeFrame)
        self.fr_EstoqueAtual.setGeometry(QtCore.QRect(20, 310, 470, 280))
        self.fr_EstoqueAtual.setStyleSheet("QFrame {\n"
                                           "background: rgba(0, 0, 0, 30%);\n"
                                           "border: none;\n"
                                           "border-radius: 20px\n"
                                           "\n"
                                           "}")
        self.fr_EstoqueAtual.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_EstoqueAtual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_EstoqueAtual.setObjectName("fr_EstoqueAtual")

        self.tradHome(ct_Home)
        QtCore.QMetaObject.connectSlotsByName(ct_Home)

    def tradHome(self, ct_Home):
        _translate = QtCore.QCoreApplication.translate
        ct_Home.setWindowTitle(_translate("ct_Home", "Frame"))
