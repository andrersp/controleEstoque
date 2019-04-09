# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Mon Mar 18 01:06:11 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
"}")
        self.fr_VendasAbertas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_VendasAbertas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_VendasAbertas.setObjectName("fr_VendasAbertas")
        self.bt_addCompra = QtWidgets.QPushButton(self.fr_VendasAbertas)
        self.bt_addCompra.setGeometry(QtCore.QRect(265, 150, 150, 110))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.bt_addCompra.setFont(font)
        self.bt_addCompra.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_addCompra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_addCompra.setAutoFillBackground(False)
        self.bt_addCompra.setStyleSheet("QPushButton{\n"
"border: none;\n"
"color: #FFF;\n"
"background: #7AB32E ;\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover {\n"
"background: #40A286 \n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E\n"
"}")
        self.bt_addCompra.setText("")
        self.bt_addCompra.setFlat(True)
        self.bt_addCompra.setObjectName("bt_addCompra")
        self.bt_addItem = QtWidgets.QPushButton(self.fr_VendasAbertas)
        self.bt_addItem.setGeometry(QtCore.QRect(265, 10, 150, 110))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.bt_addItem.setFont(font)
        self.bt_addItem.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_addItem.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_addItem.setAutoFillBackground(False)
        self.bt_addItem.setStyleSheet("QPushButton{\n"
"border: none;\n"
"color: #FFF;\n"
"background: #7AB32E ;\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover {\n"
"background: #40A286 \n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E\n"
"}")
        self.bt_addItem.setText("")
        self.bt_addItem.setFlat(True)
        self.bt_addItem.setObjectName("bt_addItem")
        self.label = QtWidgets.QLabel(self.fr_VendasAbertas)
        self.label.setGeometry(QtCore.QRect(75, 20, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.fr_VendasAbertas)
        self.label_2.setGeometry(QtCore.QRect(75, 45, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.fr_VendasAbertas)
        self.line.setGeometry(QtCore.QRect(20, 85, 210, 2))
        self.line.setStyleSheet("background: #CCC")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.fr_VendasAbertas)
        self.line_2.setGeometry(QtCore.QRect(20, 170, 210, 2))
        self.line_2.setStyleSheet("background: #CCC")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.fr_VendasAbertas)
        self.label_3.setGeometry(QtCore.QRect(75, 107, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.fr_VendasAbertas)
        self.label_4.setGeometry(QtCore.QRect(75, 132, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.fr_VendasAbertas)
        self.label_5.setGeometry(QtCore.QRect(50, 255, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.fr_VendasAbertas)
        self.label_6.setGeometry(QtCore.QRect(50, 230, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.bt_estoqueBaixo = QtWidgets.QPushButton(self.fr_VendasAbertas)
        self.bt_estoqueBaixo.setGeometry(QtCore.QRect(20, 20, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Arial [TMC ]")
        font.setPointSize(35)
        font.setWeight(75)
        font.setBold(True)
        self.bt_estoqueBaixo.setFont(font)
        self.bt_estoqueBaixo.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_estoqueBaixo.setStyleSheet("QPushButton {\n"
"background: none;\n"
"color: #ffff00;\n"
"text-align: right\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:pressed {\n"
"     background: none;\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }")
        self.bt_estoqueBaixo.setText("")
        self.bt_estoqueBaixo.setFlat(True)
        self.bt_estoqueBaixo.setObjectName("bt_estoqueBaixo")
        self.bt_pedidosHoje = QtWidgets.QPushButton(self.fr_VendasAbertas)
        self.bt_pedidosHoje.setGeometry(QtCore.QRect(20, 107, 50, 45))
        font = QtGui.QFont()
        font.setFamily("Arial [TMC ]")
        font.setPointSize(35)
        font.setWeight(75)
        font.setBold(True)
        self.bt_pedidosHoje.setFont(font)
        self.bt_pedidosHoje.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_pedidosHoje.setStyleSheet("QPushButton {\n"
"background: none;\n"
"color: #ffff00;\n"
"text-align: right\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:pressed {\n"
"     background: none;\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }")
        self.bt_pedidosHoje.setText("")
        self.bt_pedidosHoje.setFlat(True)
        self.bt_pedidosHoje.setObjectName("bt_pedidosHoje")
        self.bt_produtosAtivos = QtWidgets.QPushButton(self.fr_VendasAbertas)
        self.bt_produtosAtivos.setGeometry(QtCore.QRect(90, 190, 70, 45))
        font = QtGui.QFont()
        font.setFamily("Arial [TMC ]")
        font.setPointSize(35)
        font.setWeight(75)
        font.setBold(True)
        self.bt_produtosAtivos.setFont(font)
        self.bt_produtosAtivos.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_produtosAtivos.setStyleSheet("QPushButton {\n"
"background: none;\n"
"color: #ffff00;\n"
"text-align: center\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:pressed {\n"
"     background: none;\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }")
        self.bt_produtosAtivos.setText("")
        self.bt_produtosAtivos.setFlat(True)
        self.bt_produtosAtivos.setObjectName("bt_produtosAtivos")
        self.fr_VendasAbertas_2 = QtWidgets.QFrame(self.HomeFrame)
        self.fr_VendasAbertas_2.setGeometry(QtCore.QRect(510, 10, 470, 280))
        self.fr_VendasAbertas_2.setStyleSheet("QFrame {\n"
"background: rgba(0, 0, 0, 30%);\n"
"border: none;\n"
"border-radius: 20px\n"
"}")
        self.fr_VendasAbertas_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_VendasAbertas_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_VendasAbertas_2.setObjectName("fr_VendasAbertas_2")
        self.bt_addCliente = QtWidgets.QPushButton(self.fr_VendasAbertas_2)
        self.bt_addCliente.setGeometry(QtCore.QRect(265, 10, 150, 110))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.bt_addCliente.setFont(font)
        self.bt_addCliente.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_addCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_addCliente.setAutoFillBackground(False)
        self.bt_addCliente.setStyleSheet("QPushButton{\n"
"border: none;\n"
"color: #FFF;\n"
"background: #7AB32E ;\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover {\n"
"background: #40A286 \n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E\n"
"}")
        self.bt_addCliente.setText("")
        self.bt_addCliente.setFlat(True)
        self.bt_addCliente.setObjectName("bt_addCliente")
        self.bt_addVenda = QtWidgets.QPushButton(self.fr_VendasAbertas_2)
        self.bt_addVenda.setGeometry(QtCore.QRect(265, 150, 150, 110))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.bt_addVenda.setFont(font)
        self.bt_addVenda.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_addVenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_addVenda.setAutoFillBackground(False)
        self.bt_addVenda.setStyleSheet("QPushButton{\n"
"border: none;\n"
"color: #FFF;\n"
"background: #7AB32E ;\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover {\n"
"background: #40A286 \n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E\n"
"}")
        self.bt_addVenda.setText("")
        self.bt_addVenda.setFlat(True)
        self.bt_addVenda.setObjectName("bt_addVenda")
        self.line_3 = QtWidgets.QFrame(self.fr_VendasAbertas_2)
        self.line_3.setGeometry(QtCore.QRect(20, 85, 210, 2))
        self.line_3.setStyleSheet("background: #CCC")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.fr_VendasAbertas_2)
        self.line_4.setGeometry(QtCore.QRect(20, 170, 210, 2))
        self.line_4.setStyleSheet("background: #CCC")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_11 = QtWidgets.QLabel(self.fr_VendasAbertas_2)
        self.label_11.setGeometry(QtCore.QRect(50, 255, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.fr_VendasAbertas_2)
        self.label_12.setGeometry(QtCore.QRect(50, 230, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.lb_mesAtual = QtWidgets.QLabel(self.fr_VendasAbertas_2)
        self.lb_mesAtual.setGeometry(QtCore.QRect(50, 140, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.lb_mesAtual.setFont(font)
        self.lb_mesAtual.setStyleSheet("background: None;\n"
"color: #FFF")
        self.lb_mesAtual.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_mesAtual.setObjectName("lb_mesAtual")
        self.lb_produtosAtivos_4 = QtWidgets.QLabel(self.fr_VendasAbertas_2)
        self.lb_produtosAtivos_4.setGeometry(QtCore.QRect(45, 115, 20, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_produtosAtivos_4.setFont(font)
        self.lb_produtosAtivos_4.setStyleSheet("background: none")
        self.lb_produtosAtivos_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produtosAtivos_4.setOpenExternalLinks(True)
        self.lb_produtosAtivos_4.setObjectName("lb_produtosAtivos_4")
        self.label_15 = QtWidgets.QLabel(self.fr_VendasAbertas_2)
        self.label_15.setGeometry(QtCore.QRect(50, 60, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.lb_produtosAtivos_6 = QtWidgets.QLabel(self.fr_VendasAbertas_2)
        self.lb_produtosAtivos_6.setGeometry(QtCore.QRect(45, 35, 20, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_produtosAtivos_6.setFont(font)
        self.lb_produtosAtivos_6.setStyleSheet("background: none")
        self.lb_produtosAtivos_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produtosAtivos_6.setOpenExternalLinks(True)
        self.lb_produtosAtivos_6.setObjectName("lb_produtosAtivos_6")
        self.bt_vendidoHoje = QtWidgets.QPushButton(self.fr_VendasAbertas_2)
        self.bt_vendidoHoje.setGeometry(QtCore.QRect(70, 20, 130, 45))
        font = QtGui.QFont()
        font.setFamily("Arial [TMC ]")
        font.setPointSize(35)
        font.setWeight(75)
        font.setBold(True)
        self.bt_vendidoHoje.setFont(font)
        self.bt_vendidoHoje.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_vendidoHoje.setStyleSheet("QPushButton {\n"
"background: none;\n"
"color: #ffff00;\n"
"text-align: left\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:pressed {\n"
"     background: none;\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }")
        self.bt_vendidoHoje.setText("")
        self.bt_vendidoHoje.setFlat(True)
        self.bt_vendidoHoje.setObjectName("bt_vendidoHoje")
        self.bt_vendidoMes = QtWidgets.QPushButton(self.fr_VendasAbertas_2)
        self.bt_vendidoMes.setGeometry(QtCore.QRect(70, 100, 130, 45))
        font = QtGui.QFont()
        font.setFamily("Arial [TMC ]")
        font.setPointSize(35)
        font.setWeight(75)
        font.setBold(True)
        self.bt_vendidoMes.setFont(font)
        self.bt_vendidoMes.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_vendidoMes.setStyleSheet("QPushButton {\n"
"background: none;\n"
"color: #ffff00;\n"
"text-align: left\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:pressed {\n"
"     background: none;\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }")
        self.bt_vendidoMes.setText("")
        self.bt_vendidoMes.setFlat(True)
        self.bt_vendidoMes.setObjectName("bt_vendidoMes")
        self.bt_clientesAtendidos = QtWidgets.QPushButton(self.fr_VendasAbertas_2)
        self.bt_clientesAtendidos.setGeometry(QtCore.QRect(90, 190, 70, 45))
        font = QtGui.QFont()
        font.setFamily("Arial [TMC ]")
        font.setPointSize(35)
        font.setWeight(75)
        font.setBold(True)
        self.bt_clientesAtendidos.setFont(font)
        self.bt_clientesAtendidos.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_clientesAtendidos.setStyleSheet("QPushButton {\n"
"background: none;\n"
"color: #ffff00;\n"
"text-align: center\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:pressed {\n"
"     background: none;\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* no border for a flat push button */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }")
        self.bt_clientesAtendidos.setText("")
        self.bt_clientesAtendidos.setFlat(True)
        self.bt_clientesAtendidos.setObjectName("bt_clientesAtendidos")
        self.fr_VendasAbertas_3 = QtWidgets.QFrame(self.HomeFrame)
        self.fr_VendasAbertas_3.setGeometry(QtCore.QRect(20, 310, 470, 280))
        self.fr_VendasAbertas_3.setStyleSheet("QFrame {\n"
"background: rgba(0, 0, 0, 30%);\n"
"border: none;\n"
"border-radius: 20px\n"
"}")
        self.fr_VendasAbertas_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_VendasAbertas_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_VendasAbertas_3.setObjectName("fr_VendasAbertas_3")
        self.bt_apagarHoje = QtWidgets.QPushButton(self.fr_VendasAbertas_3)
        self.bt_apagarHoje.setGeometry(QtCore.QRect(265, 150, 150, 110))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.bt_apagarHoje.setFont(font)
        self.bt_apagarHoje.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_apagarHoje.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_apagarHoje.setAutoFillBackground(False)
        self.bt_apagarHoje.setStyleSheet("QPushButton{\n"
"border: none;\n"
"color: #FFF;\n"
"background: #7AB32E ;\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover {\n"
"background: #40A286 \n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E\n"
"}")
        self.bt_apagarHoje.setText("")
        self.bt_apagarHoje.setFlat(True)
        self.bt_apagarHoje.setObjectName("bt_apagarHoje")
        self.bt_areceberHoje = QtWidgets.QPushButton(self.fr_VendasAbertas_3)
        self.bt_areceberHoje.setGeometry(QtCore.QRect(265, 10, 150, 110))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.bt_areceberHoje.setFont(font)
        self.bt_areceberHoje.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_areceberHoje.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_areceberHoje.setAutoFillBackground(False)
        self.bt_areceberHoje.setStyleSheet("QPushButton{\n"
"border: none;\n"
"color: #FFF;\n"
"background: #7AB32E ;\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover {\n"
"background: #40A286 \n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E\n"
"}")
        self.bt_areceberHoje.setText("")
        self.bt_areceberHoje.setFlat(True)
        self.bt_areceberHoje.setObjectName("bt_areceberHoje")
        self.line_5 = QtWidgets.QFrame(self.fr_VendasAbertas_3)
        self.line_5.setGeometry(QtCore.QRect(20, 85, 210, 2))
        self.line_5.setStyleSheet("background: #CCC")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.fr_VendasAbertas_3)
        self.line_6.setGeometry(QtCore.QRect(20, 170, 210, 2))
        self.line_6.setStyleSheet("background: #CCC")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_13 = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.label_13.setGeometry(QtCore.QRect(50, 255, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.label_16.setGeometry(QtCore.QRect(50, 230, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.lb_apagarHoje = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.lb_apagarHoje.setGeometry(QtCore.QRect(70, 100, 130, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_apagarHoje.setFont(font)
        self.lb_apagarHoje.setStyleSheet("background: none")
        self.lb_apagarHoje.setText("")
        self.lb_apagarHoje.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_apagarHoje.setOpenExternalLinks(True)
        self.lb_apagarHoje.setObjectName("lb_apagarHoje")
        self.label_17 = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.label_17.setGeometry(QtCore.QRect(50, 140, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.lb_produtosAtivos_9 = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.lb_produtosAtivos_9.setGeometry(QtCore.QRect(45, 115, 20, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_produtosAtivos_9.setFont(font)
        self.lb_produtosAtivos_9.setStyleSheet("background: none")
        self.lb_produtosAtivos_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produtosAtivos_9.setOpenExternalLinks(True)
        self.lb_produtosAtivos_9.setObjectName("lb_produtosAtivos_9")
        self.label_18 = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.label_18.setGeometry(QtCore.QRect(50, 60, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background: None;\n"
"color: #FFF")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.lb_areceberHoje = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.lb_areceberHoje.setGeometry(QtCore.QRect(70, 20, 130, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_areceberHoje.setFont(font)
        self.lb_areceberHoje.setStyleSheet("background: none")
        self.lb_areceberHoje.setText("")
        self.lb_areceberHoje.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_areceberHoje.setOpenExternalLinks(True)
        self.lb_areceberHoje.setObjectName("lb_areceberHoje")
        self.lb_produtosAtivos_11 = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.lb_produtosAtivos_11.setGeometry(QtCore.QRect(45, 35, 20, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_produtosAtivos_11.setFont(font)
        self.lb_produtosAtivos_11.setStyleSheet("background: none")
        self.lb_produtosAtivos_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produtosAtivos_11.setOpenExternalLinks(True)
        self.lb_produtosAtivos_11.setObjectName("lb_produtosAtivos_11")
        self.lb_saldoHoje = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.lb_saldoHoje.setGeometry(QtCore.QRect(70, 190, 130, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_saldoHoje.setFont(font)
        self.lb_saldoHoje.setStyleSheet("background: none")
        self.lb_saldoHoje.setText("")
        self.lb_saldoHoje.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_saldoHoje.setOpenExternalLinks(True)
        self.lb_saldoHoje.setObjectName("lb_saldoHoje")
        self.lb_produtosAtivos_13 = QtWidgets.QLabel(self.fr_VendasAbertas_3)
        self.lb_produtosAtivos_13.setGeometry(QtCore.QRect(45, 205, 20, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_produtosAtivos_13.setFont(font)
        self.lb_produtosAtivos_13.setStyleSheet("background: none")
        self.lb_produtosAtivos_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produtosAtivos_13.setOpenExternalLinks(True)
        self.lb_produtosAtivos_13.setObjectName("lb_produtosAtivos_13")
        self.fr_VendasAbertas_4 = QtWidgets.QFrame(self.HomeFrame)
        self.fr_VendasAbertas_4.setGeometry(QtCore.QRect(510, 310, 470, 280))
        self.fr_VendasAbertas_4.setStyleSheet("QFrame {\n"
"background: rgba(0, 0, 0, 30%);\n"
"border: none;\n"
"border-radius: 20px\n"
"}")
        self.fr_VendasAbertas_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_VendasAbertas_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_VendasAbertas_4.setObjectName("fr_VendasAbertas_4")
        self.line_7 = QtWidgets.QFrame(self.fr_VendasAbertas_4)
        self.line_7.setGeometry(QtCore.QRect(20, 85, 430, 2))
        self.line_7.setStyleSheet("background: #CCC")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.fr_VendasAbertas_4)
        self.line_8.setGeometry(QtCore.QRect(20, 170, 430, 2))
        self.line_8.setStyleSheet("background: #CCC")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.lb_DataAtual = QtWidgets.QLabel(self.fr_VendasAbertas_4)
        self.lb_DataAtual.setGeometry(QtCore.QRect(85, 20, 300, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_DataAtual.setFont(font)
        self.lb_DataAtual.setStyleSheet("background: none")
        self.lb_DataAtual.setText("")
        self.lb_DataAtual.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_DataAtual.setOpenExternalLinks(True)
        self.lb_DataAtual.setObjectName("lb_DataAtual")
        self.lb_semanaDia = QtWidgets.QLabel(self.fr_VendasAbertas_4)
        self.lb_semanaDia.setGeometry(QtCore.QRect(85, 105, 300, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_semanaDia.setFont(font)
        self.lb_semanaDia.setStyleSheet("background: none")
        self.lb_semanaDia.setText("")
        self.lb_semanaDia.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_semanaDia.setOpenExternalLinks(True)
        self.lb_semanaDia.setObjectName("lb_semanaDia")
        self.lb_produtosAtivos_16 = QtWidgets.QLabel(self.fr_VendasAbertas_4)
        self.lb_produtosAtivos_16.setGeometry(QtCore.QRect(85, 190, 300, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_produtosAtivos_16.setFont(font)
        self.lb_produtosAtivos_16.setStyleSheet("background: none")
        self.lb_produtosAtivos_16.setText("")
        self.lb_produtosAtivos_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_produtosAtivos_16.setOpenExternalLinks(True)
        self.lb_produtosAtivos_16.setObjectName("lb_produtosAtivos_16")

        self.tradHome(ct_Home)
        QtCore.QMetaObject.connectSlotsByName(ct_Home)

    def tradHome(self, ct_Home):
        ct_Home.setWindowTitle(QtWidgets.QApplication.translate("ct_Home", "Frame", None, -1))
        self.bt_addCompra.setToolTip(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p>Nova Compra</p></body></html>", None, -1))
        self.bt_addCompra.setShortcut(QtWidgets.QApplication.translate("ct_Home", "F7", None, -1))
        self.bt_addItem.setToolTip(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p>Adicioar Item</p></body></html>", None, -1))
        self.bt_addItem.setWhatsThis(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p><br/></p></body></html>", None, -1))
        self.bt_addItem.setShortcut(QtWidgets.QApplication.translate("ct_Home", "F2", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ct_Home", "PRODUTOS", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ct_Home", "COM ESTOQUE BAIXO", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ct_Home", "PEDIDOS", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("ct_Home", "PARA RECEBER HOJE", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("ct_Home", "ATIVOS CADASTRADOS", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("ct_Home", "PRODUTOS", None, -1))
        self.bt_addCliente.setToolTip(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p>Novo Cliente</p></body></html>", None, -1))
        self.bt_addCliente.setShortcut(QtWidgets.QApplication.translate("ct_Home", "F7", None, -1))
        self.bt_addVenda.setToolTip(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p>Nova Venda</p></body></html>", None, -1))
        self.bt_addVenda.setWhatsThis(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p><br/></p></body></html>", None, -1))
        self.bt_addVenda.setShortcut(QtWidgets.QApplication.translate("ct_Home", "F2", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("ct_Home", "ATENDIDOS HOJE", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("ct_Home", "CLIENTES", None, -1))
        self.lb_mesAtual.setText(QtWidgets.QApplication.translate("ct_Home", "VENDIDO EM SETEMBRO", None, -1))
        self.lb_produtosAtivos_4.setText(QtWidgets.QApplication.translate("ct_Home", "<span style=\"font-family:\'Arial\'; font-size:15px;\n"
"                font-weight: bold;color:#ffff00; \">R$</span>", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("ct_Home", "VENDIDO HOJE", None, -1))
        self.lb_produtosAtivos_6.setText(QtWidgets.QApplication.translate("ct_Home", "<span style=\"font-family:\'Arial\'; font-size:15px;\n"
"                font-weight: bold;color:#ffff00; \">R$</span>", None, -1))
        self.bt_apagarHoje.setToolTip(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p>Conta a pagar hoje</p></body></html>", None, -1))
        self.bt_apagarHoje.setShortcut(QtWidgets.QApplication.translate("ct_Home", "F7", None, -1))
        self.bt_areceberHoje.setToolTip(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p>Conta a receber hoje</p></body></html>", None, -1))
        self.bt_areceberHoje.setWhatsThis(QtWidgets.QApplication.translate("ct_Home", "<html><head/><body><p><br/></p></body></html>", None, -1))
        self.bt_areceberHoje.setShortcut(QtWidgets.QApplication.translate("ct_Home", "F2", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("ct_Home", "FINAL HOJE", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("ct_Home", "SALDO", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("ct_Home", "A PAGAR HOJE", None, -1))
        self.lb_produtosAtivos_9.setText(QtWidgets.QApplication.translate("ct_Home", "<span style=\"font-family:\'Arial\'; font-size:15px;\n"
"                font-weight: bold;color:#ffff00; \">R$</span>", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("ct_Home", "A RECEBER HOJE", None, -1))
        self.lb_produtosAtivos_11.setText(QtWidgets.QApplication.translate("ct_Home", "<span style=\"font-family:\'Arial\'; font-size:15px;\n"
"                font-weight: bold;color:#ffff00; \">R$</span>", None, -1))
        self.lb_produtosAtivos_13.setText(QtWidgets.QApplication.translate("ct_Home", "<span style=\"font-family:\'Arial\'; font-size:15px;\n"
"                font-weight: bold;color:#ffff00; \">R$</span>", None, -1))

