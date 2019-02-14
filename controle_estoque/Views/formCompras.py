# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formCompras.ui',
# licensing of 'formCompras.ui' applies.
#
# Created: Mon Feb 11 12:24:19 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ct_FormCompra(object):
    def setFormCompras(self, ct_FormCompra):
        ct_FormCompra.setObjectName("ct_FormCompra")
        ct_FormCompra.resize(1000, 500)
        ct_FormCompra.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormCompra.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormCompra = QtWidgets.QFrame(ct_FormCompra)
        self.fr_FormCompra.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormCompra.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormCompra.setObjectName("fr_FormCompra")
        self.lb_FormCompra = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra.setGeometry(QtCore.QRect(20, 10, 960, 20))
        self.lb_FormCompra.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra.setObjectName("lb_FormCompra")
        self.fr_BotoesFormCompra = QtWidgets.QFrame(self.fr_FormCompra)
        self.fr_BotoesFormCompra.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormCompra.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormCompra.setObjectName("fr_BotoesFormCompra")
        self.bt_Voltar = QtWidgets.QPushButton(self.fr_BotoesFormCompra)
        self.bt_Voltar.setGeometry(QtCore.QRect(870, 0, 120, 30))
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
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_Voltar.setIconSize(QtCore.QSize(75, 35))
        self.bt_Voltar.setObjectName("bt_Voltar")
        self.bt_Salvar = QtWidgets.QPushButton(self.fr_BotoesFormCompra)
        self.bt_Salvar.setGeometry(QtCore.QRect(610, 0, 120, 30))
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
        self.bt_Imprimir = QtWidgets.QPushButton(self.fr_BotoesFormCompra)
        self.bt_Imprimir.setEnabled(False)
        self.bt_Imprimir.setGeometry(QtCore.QRect(740, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_Imprimir.setFont(font)
        self.bt_Imprimir.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Imprimir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Imprimir.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Imprimir.setStyleSheet("QPushButton {\n"
"background-color: #5C9BBC;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_Imprimir.setIconSize(QtCore.QSize(75, 35))
        self.bt_Imprimir.setObjectName("bt_Imprimir")
        self.tx_NomeFantasia = QtWidgets.QLineEdit(self.fr_FormCompra)
        self.tx_NomeFantasia.setGeometry(QtCore.QRect(140, 110, 350, 30))
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
        self.fr_topoCompra = QtWidgets.QFrame(self.fr_FormCompra)
        self.fr_topoCompra.setGeometry(QtCore.QRect(20, 30, 960, 40))
        self.fr_topoCompra.setStyleSheet("QFrame{\n"
"background: #FFF;\n"
"border: 1px solid #1E87F0;\n"
"}\n"
"")
        self.fr_topoCompra.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_topoCompra.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_topoCompra.setObjectName("fr_topoCompra")
        self.tx_Cod = QtWidgets.QLineEdit(self.fr_topoCompra)
        self.tx_Cod.setGeometry(QtCore.QRect(0, 0, 100, 40))
        self.tx_Cod.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Cod.setStyleSheet("QLineEdit{\n"
"background: #0884C2;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 16px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF\n"
"}\n"
"")
        self.tx_Cod.setText("")
        self.tx_Cod.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Cod.setReadOnly(True)
        self.tx_Cod.setPlaceholderText("")
        self.tx_Cod.setObjectName("tx_Cod")
        self.dt_Emissao = QtWidgets.QDateEdit(self.fr_topoCompra)
        self.dt_Emissao.setGeometry(QtCore.QRect(120, 18, 140, 18))
        self.dt_Emissao.setStyleSheet("QDateEdit {\n"
"background: #FFF;\n"
"border: none;\n"
"font-family: \"Arial\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: rgb(80,79,79)\n"
"}\n"
" QDateEdit::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QDateEdit::down-arrow {\n"
"     image: url("+self.resourcepath('Images/down.png')+");\n"
" }")
        self.dt_Emissao.setCalendarPopup(True)
        self.dt_Emissao.setObjectName("dt_Emissao")
        self.lb_FormCompra_21 = QtWidgets.QLabel(self.fr_topoCompra)
        self.lb_FormCompra_21.setGeometry(QtCore.QRect(120, 2, 120, 18))
        self.lb_FormCompra_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"\n"
"color:#1E87F0;\n"
"border: none;\n"
"}")
        self.lb_FormCompra_21.setObjectName("lb_FormCompra_21")
        self.dt_Prazo = QtWidgets.QDateEdit(self.fr_topoCompra)
        self.dt_Prazo.setGeometry(QtCore.QRect(300, 18, 140, 18))
        self.dt_Prazo.setStyleSheet("QDateEdit {\n"
"background: #FFF;\n"
"border: none;\n"
"font-family: \"Arial\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: rgb(80,79,79)\n"
"}\n"
" QDateEdit::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QDateEdit::down-arrow {\n"
"     image: url("+self.resourcepath('Images/down.png')+");\n"
" }")
        self.dt_Prazo.setCalendarPopup(True)
        self.dt_Prazo.setObjectName("dt_Prazo")
        self.lb_FormCompra_22 = QtWidgets.QLabel(self.fr_topoCompra)
        self.lb_FormCompra_22.setGeometry(QtCore.QRect(300, 2, 120, 18))
        self.lb_FormCompra_22.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"\n"
"color:#1E87F0;\n"
"border: none;\n"
"}")
        self.lb_FormCompra_22.setObjectName("lb_FormCompra_22")
        self.bt_Entregar = QtWidgets.QPushButton(self.fr_topoCompra)
        self.bt_Entregar.setEnabled(False)
        self.bt_Entregar.setGeometry(QtCore.QRect(820, 5, 120, 30))
        self.bt_Entregar.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Entregar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Entregar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Entregar.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: #CACACA;\n"
"\n"
" }\n"
"")
        self.bt_Entregar.setIconSize(QtCore.QSize(75, 35))
        self.bt_Entregar.setObjectName("bt_Entregar")
        self.lb_FormCompra_23 = QtWidgets.QLabel(self.fr_topoCompra)
        self.lb_FormCompra_23.setGeometry(QtCore.QRect(480, 2, 120, 18))
        self.lb_FormCompra_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"\n"
"color:#1E87F0;\n"
"border: none;\n"
"}")
        self.lb_FormCompra_23.setObjectName("lb_FormCompra_23")
        self.dt_Entrega = QtWidgets.QDateEdit(self.fr_topoCompra)
        self.dt_Entrega.setGeometry(QtCore.QRect(480, 18, 140, 18))
        self.dt_Entrega.setStyleSheet("QDateEdit {\n"
"background: #FFF;\n"
"border: none;\n"
"font-family: \"Arial\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: rgb(80,79,79)\n"
"}\n"
" QDateEdit::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QDateEdit::down-arrow {\n"
"     image: url("+self.resourcepath('Images/down.png')+");\n"
" }")
        self.dt_Entrega.setCalendarPopup(True)
        self.dt_Entrega.setObjectName("dt_Entrega")
        self.lb_FormCompra_2 = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra_2.setGeometry(QtCore.QRect(140, 90, 120, 20))
        self.lb_FormCompra_2.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_2.setObjectName("lb_FormCompra_2")
        self.lb_FormCompra_3 = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra_3.setGeometry(QtCore.QRect(20, 90, 100, 20))
        self.lb_FormCompra_3.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_3.setObjectName("lb_FormCompra_3")
        self.tx_Id = QtWidgets.QLineEdit(self.fr_FormCompra)
        self.tx_Id.setGeometry(QtCore.QRect(20, 110, 100, 30))
        self.tx_Id.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Id.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Id.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Id.setObjectName("tx_Id")
        self.lb_FormCompra_4 = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra_4.setGeometry(QtCore.QRect(20, 150, 120, 20))
        self.lb_FormCompra_4.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_4.setObjectName("lb_FormCompra_4")
        self.fr_addProduto = QtWidgets.QFrame(self.fr_FormCompra)
        self.fr_addProduto.setGeometry(QtCore.QRect(20, 170, 600, 70))
        self.fr_addProduto.setStyleSheet("QFrame{\n"
"background: #1D76A2;\n"
"border: 1px solid #1E87F0;\n"
"}\n"
"")
        self.fr_addProduto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_addProduto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_addProduto.setObjectName("fr_addProduto")
        self.tx_BuscaItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_BuscaItem.setGeometry(QtCore.QRect(40, 0, 270, 40))
        self.tx_BuscaItem.setMouseTracking(True)
        self.tx_BuscaItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_BuscaItem.setStyleSheet("QLineEdit{\n"
"background: #5C9BBC;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 10px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"text-transform: uppercase\n"
"}\n"
"\n"
"")
        self.tx_BuscaItem.setText("")
        self.tx_BuscaItem.setFrame(False)
        self.tx_BuscaItem.setCursorPosition(0)
        self.tx_BuscaItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_BuscaItem.setReadOnly(False)
        self.tx_BuscaItem.setObjectName("tx_BuscaItem")
        self.lb_FormCompra_6 = QtWidgets.QLabel(self.fr_addProduto)
        self.lb_FormCompra_6.setGeometry(QtCore.QRect(350, 0, 75, 15))
        self.lb_FormCompra_6.setStyleSheet("QLabel{\n"
"font-size: 9px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"border: none;\n"
"}")
        self.lb_FormCompra_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FormCompra_6.setObjectName("lb_FormCompra_6")
        self.tx_ValorUnitarioItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ValorUnitarioItem.setGeometry(QtCore.QRect(350, 15, 75, 25))
        self.tx_ValorUnitarioItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorUnitarioItem.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"color: #FFF;\n"
"border: none\n"
"}\n"
"QLineEdit::placeholder{\n"
"color: red;\n"
"}")
        self.tx_ValorUnitarioItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ValorUnitarioItem.setObjectName("tx_ValorUnitarioItem")
        self.lb_FormCompra_7 = QtWidgets.QLabel(self.fr_addProduto)
        self.lb_FormCompra_7.setGeometry(QtCore.QRect(425, 0, 75, 15))
        self.lb_FormCompra_7.setStyleSheet("QLabel{\n"
"font-size: 9px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"border: none;\n"
"}")
        self.lb_FormCompra_7.setObjectName("lb_FormCompra_7")
        self.tx_ValorTotalItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ValorTotalItem.setGeometry(QtCore.QRect(425, 15, 75, 25))
        self.tx_ValorTotalItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorTotalItem.setStyleSheet("QLineEdit{\n"
"background:transparent;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"color: #FFF;\n"
"border: none\n"
"}\n"
"QLineEdit::placeholder{\n"
"color: red;\n"
"}")
        self.tx_ValorTotalItem.setText("")
        self.tx_ValorTotalItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ValorTotalItem.setReadOnly(True)
        self.tx_ValorTotalItem.setObjectName("tx_ValorTotalItem")
        self.bt_IncluirItem = QtWidgets.QPushButton(self.fr_addProduto)
        self.bt_IncluirItem.setEnabled(False)
        self.bt_IncluirItem.setGeometry(QtCore.QRect(500, 0, 100, 70))
        self.bt_IncluirItem.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_IncluirItem.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_IncluirItem.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_IncluirItem.setStyleSheet("QPushButton {\n"
"background: #025682;\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #5C9BBC\n"
"}")
        self.bt_IncluirItem.setText("")
        self.bt_IncluirItem.setIconSize(QtCore.QSize(75, 35))
        self.bt_IncluirItem.setObjectName("bt_IncluirItem")
        self.tx_ObsItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ObsItem.setGeometry(QtCore.QRect(0, 40, 500, 30))
        self.tx_ObsItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ObsItem.setStyleSheet("QLineEdit{\n"
"background: #1E87F0;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF\n"
"}\n"
"\n"
"")
        self.tx_ObsItem.setText("")
        self.tx_ObsItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ObsItem.setReadOnly(False)
        self.tx_ObsItem.setObjectName("tx_ObsItem")
        self.tx_IdBuscaItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_IdBuscaItem.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.tx_IdBuscaItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_IdBuscaItem.setStyleSheet("QLineEdit{\n"
"background: #5C9BBC;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 11px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF\n"
"}\n"
"\n"
"")
        self.tx_IdBuscaItem.setText("")
        self.tx_IdBuscaItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_IdBuscaItem.setReadOnly(False)
        self.tx_IdBuscaItem.setObjectName("tx_IdBuscaItem")
        self.tx_QntdItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_QntdItem.setGeometry(QtCore.QRect(310, 0, 40, 40))
        self.tx_QntdItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_QntdItem.setStyleSheet("\n"
"QLineEdit{\n"
"background: #4088AC;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 11px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF\n"
"}\n"
"\n"
"\n"
"")
        self.tx_QntdItem.setText("")
        self.tx_QntdItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_QntdItem.setReadOnly(False)
        self.tx_QntdItem.setObjectName("tx_QntdItem")
        self.lb_FormCompra_5 = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra_5.setGeometry(QtCore.QRect(510, 90, 110, 20))
        self.lb_FormCompra_5.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_5.setObjectName("lb_FormCompra_5")
        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormCompra)
        self.tx_Telefone.setGeometry(QtCore.QRect(510, 110, 110, 30))
        self.tx_Telefone.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Telefone.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Telefone.setReadOnly(True)
        self.tx_Telefone.setObjectName("tx_Telefone")
        self.tb_Itens = QtWidgets.QTableWidget(self.fr_FormCompra)
        self.tb_Itens.setGeometry(QtCore.QRect(20, 250, 600, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_Itens.sizePolicy().hasHeightForWidth())
        self.tb_Itens.setSizePolicy(sizePolicy)
        self.tb_Itens.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tb_Itens.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Itens.setStyleSheet("QTableView{\n"
"color: #28292A;\n"
"font-weight: bold;\n"
"font-size: 11px;\n"
"background: #FFF;\n"
"padding: 0 0 0 5px;\n"
"}\n"
"QHeaderView:section{\n"
"background: #FFF;\n"
"padding: 5px 0 ;\n"
"font-size: 11px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #797979;\n"
"border: none;\n"
"border-bottom: 2px solid #CCC;\n"
"text-transform: uppercase;\n"
"margin: 0 2px 0 0;\n"
"}\n"
"QTableView::item {\n"
"border-bottom: 2px solid #CCC;\n"
"padding: 2px;\n"
"margin: 0 2px 0 0;\n"
"}\n"
"\n"
"")
        self.tb_Itens.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Itens.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Itens.setAutoScrollMargin(20)
        self.tb_Itens.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Itens.setTabKeyNavigation(False)
        self.tb_Itens.setProperty("showDropIndicator", False)
        self.tb_Itens.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Itens.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Itens.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_Itens.setShowGrid(False)
        self.tb_Itens.setCornerButtonEnabled(False)
        self.tb_Itens.setRowCount(0)
        self.tb_Itens.setObjectName("tb_Itens")
        self.tb_Itens.setColumnCount(8)
        self.tb_Itens.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(7, item)
        self.tb_Itens.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Itens.horizontalHeader().setStretchLastSection(True)
        self.tb_Itens.verticalHeader().setVisible(False)
        self.tb_Itens.verticalHeader().setCascadingSectionResizes(True)
        self.tb_Itens.verticalHeader().setDefaultSectionSize(40)
        self.fr_financeiroCompra = QtWidgets.QFrame(self.fr_FormCompra)
        self.fr_financeiroCompra.setGeometry(QtCore.QRect(640, 110, 340, 340))
        self.fr_financeiroCompra.setStyleSheet("background: #F1F1F1;\n"
"border-top: 4px solid #277298;\n"
"border-bottom: 4px solid #277298;")
        self.fr_financeiroCompra.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_financeiroCompra.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_financeiroCompra.setObjectName("fr_financeiroCompra")
        self.tx_Desconto = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_Desconto.setGeometry(QtCore.QRect(120, 25, 90, 25))
        self.tx_Desconto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Desconto.setStyleSheet("QLineEdit{\n"
"background: #F1F1F1;\n"
"border: 2px solid #CFCFCF;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Desconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_Desconto.setObjectName("tx_Desconto")
        self.lb_FormVenda_14 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_14.setGeometry(QtCore.QRect(120, 5, 90, 20))
        self.lb_FormVenda_14.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #7B7A7A;\n"
"border: none\n"
"}")
        self.lb_FormVenda_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_14.setObjectName("lb_FormVenda_14")
        self.tx_Frete = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_Frete.setGeometry(QtCore.QRect(230, 25, 90, 25))
        self.tx_Frete.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Frete.setStyleSheet("QLineEdit{\n"
"background: #F1F1F1;\n"
"border: 2px solid #CFCFCF;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Frete.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_Frete.setObjectName("tx_Frete")
        self.lb_FormVenda_17 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_17.setGeometry(QtCore.QRect(230, 5, 90, 20))
        self.lb_FormVenda_17.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #7B7A7A;\n"
"border: none\n"
"}")
        self.lb_FormVenda_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_17.setObjectName("lb_FormVenda_17")
        self.lb_SubTotal = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_SubTotal.setGeometry(QtCore.QRect(0, 25, 100, 25))
        self.lb_SubTotal.setStyleSheet("QLabel{\n"
"font-size: 20px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_SubTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_SubTotal.setObjectName("lb_SubTotal")
        self.lb_FormVenda_18 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_18.setGeometry(QtCore.QRect(0, 5, 100, 20))
        self.lb_FormVenda_18.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_18.setObjectName("lb_FormVenda_18")
        self.lb_FormVenda_19 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_19.setGeometry(QtCore.QRect(10, 55, 100, 20))
        self.lb_FormVenda_19.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_19.setObjectName("lb_FormVenda_19")
        self.bt_GerarParcela = QtWidgets.QPushButton(self.fr_financeiroCompra)
        self.bt_GerarParcela.setEnabled(False)
        self.bt_GerarParcela.setGeometry(QtCore.QRect(180, 165, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_GerarParcela.setFont(font)
        self.bt_GerarParcela.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_GerarParcela.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_GerarParcela.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_GerarParcela.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
" }\n"
"QPushButton:disabled{\n"
"background-color: #CACACA;\n"
"\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_GerarParcela.setIconSize(QtCore.QSize(75, 35))
        self.bt_GerarParcela.setObjectName("bt_GerarParcela")
        self.tx_TotalFinal = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_TotalFinal.setEnabled(False)
        self.tx_TotalFinal.setGeometry(QtCore.QRect(10, 75, 100, 25))
        self.tx_TotalFinal.setStyleSheet("\n"
"font-size: 24px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"\n"
"")
        self.tx_TotalFinal.setText("")
        self.tx_TotalFinal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_TotalFinal.setReadOnly(True)
        self.tx_TotalFinal.setObjectName("tx_TotalFinal")
        self.cb_FormaPagamento = QtWidgets.QComboBox(self.fr_financeiroCompra)
        self.cb_FormaPagamento.setGeometry(QtCore.QRect(10, 125, 150, 25))
        self.cb_FormaPagamento.setStyleSheet("QComboBox{\n"
"background: #F1F1F1;\n"
"border: 2px solid #CFCFCF;\n"
"color: #000;\n"
"font: 12px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"\n"
"}\n"
"QCombobox:on {\n"
"color: #000;\n"
"font: 10px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url("+self.resourcepath('Images/down.png')+");\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid darkgray;\n"
"    selection-background-color: #40a286;\n"
"color: #000;\n"
"font: 10px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"}\n"
"")
        self.cb_FormaPagamento.setObjectName("cb_FormaPagamento")
        self.cb_FormaPagamento.addItem("")
        self.cb_FormaPagamento.addItem("")
        self.lb_FormVenda_20 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_20.setGeometry(QtCore.QRect(10, 110, 150, 15))
        self.lb_FormVenda_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_FormVenda_20.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_20.setObjectName("lb_FormVenda_20")
        self.cb_QtdeParcela = QtWidgets.QComboBox(self.fr_financeiroCompra)
        self.cb_QtdeParcela.setGeometry(QtCore.QRect(180, 125, 150, 25))
        self.cb_QtdeParcela.setStyleSheet("QComboBox{\n"
"background: #F1F1F1;\n"
"border: 2px solid #CFCFCF;\n"
"color: #000;\n"
"font: 12px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"\n"
"}\n"
"QCombobox:on {\n"
"color: #000;\n"
"font: 10px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url("+self.resourcepath('Images/down.png')+");\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid darkgray;\n"
"    selection-background-color: #40a286;\n"
"color: #000;\n"
"font: 10px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold;\n"
"}\n"
"")
        self.cb_QtdeParcela.setObjectName("cb_QtdeParcela")
        self.cb_QtdeParcela.addItem("")
        self.cb_QtdeParcela.addItem("")
        self.cb_QtdeParcela.addItem("")
        self.cb_QtdeParcela.addItem("")
        self.lb_FormVenda_21 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_21.setGeometry(QtCore.QRect(180, 110, 150, 15))
        self.lb_FormVenda_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_FormVenda_21.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_21.setObjectName("lb_FormVenda_21")
        self.dt_Vencimento = QtWidgets.QDateEdit(self.fr_financeiroCompra)
        self.dt_Vencimento.setGeometry(QtCore.QRect(10, 170, 150, 25))
        self.dt_Vencimento.setStyleSheet("QDateEdit {\n"
"background: #F1F1F1;\n"
"border: 2px solid #CFCFCF;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"font-weight: bold\n"
"}\n"
" QDateEdit::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
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
"}\n"
"")
        self.dt_Vencimento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dt_Vencimento.setCalendarPopup(True)
        self.dt_Vencimento.setObjectName("dt_Vencimento")
        self.lb_FormVenda_25 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_25.setGeometry(QtCore.QRect(10, 155, 150, 15))
        self.lb_FormVenda_25.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_25.setObjectName("lb_FormVenda_25")
        self.lb_FormVenda_22 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_22.setGeometry(QtCore.QRect(230, 55, 100, 20))
        self.lb_FormVenda_22.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_22.setObjectName("lb_FormVenda_22")
        self.lb_ValorPendente = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_ValorPendente.setGeometry(QtCore.QRect(230, 75, 100, 25))
        self.lb_ValorPendente.setStyleSheet("QLabel{\n"
"font-size: 20px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_ValorPendente.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_ValorPendente.setObjectName("lb_ValorPendente")
        self.tb_Parcelas = QtWidgets.QTableWidget(self.fr_financeiroCompra)
        self.tb_Parcelas.setGeometry(QtCore.QRect(10, 200, 320, 130))
        self.tb_Parcelas.setStyleSheet("QTableView{\n"
"font-family: \"Tahoma\";\n"
"color: #28292A;\n"
"font-size: 12px;\n"
"background: #F1F1F1;\n"
"border: none\n"
"}\n"
"QHeaderView:section{\n"
"background: #F1F1F1;\n"
"padding: 3px 0 ;\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #000;\n"
"border: none;\n"
"border-bottom: 2px solid #CCC;\n"
"text-transform: uppercase;\n"
"margin: 0 1px 0 0;\n"
"}\n"
"QTableView::item {\n"
"border-bottom: 1px solid #CCC;\n"
"padding: 1px;\n"
"margin: 0 1px 0 0;\n"
"\n"
"}\n"
"QTableView QAbstractItemView {\n"
"    border: none;\n"
"    background: #F1F1F1;\n"
"\n"
"}\n"
"")
        self.tb_Parcelas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Parcelas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Parcelas.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb_Parcelas.setShowGrid(False)
        self.tb_Parcelas.setObjectName("tb_Parcelas")
        self.tb_Parcelas.setColumnCount(5)
        self.tb_Parcelas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Parcelas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Parcelas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Parcelas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Parcelas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Parcelas.setHorizontalHeaderItem(4, item)
        self.tb_Parcelas.horizontalHeader().setDefaultSectionSize(80)
        self.tb_Parcelas.horizontalHeader().setMinimumSectionSize(40)
        self.tb_Parcelas.verticalHeader().setVisible(False)
        self.tb_Parcelas.verticalHeader().setDefaultSectionSize(25)
        self.tx_valorRecebido = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_valorRecebido.setEnabled(False)
        self.tx_valorRecebido.setGeometry(QtCore.QRect(120, 75, 100, 25))
        self.tx_valorRecebido.setStyleSheet("\n"
"font-size: 24px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"\n"
"")
        self.tx_valorRecebido.setText("")
        self.tx_valorRecebido.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_valorRecebido.setReadOnly(True)
        self.tx_valorRecebido.setObjectName("tx_valorRecebido")
        self.lb_FormVenda_23 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_23.setGeometry(QtCore.QRect(120, 55, 100, 20))
        self.lb_FormVenda_23.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_23.setObjectName("lb_FormVenda_23")

        self.tradFormCompras(ct_FormCompra)
        QtCore.QMetaObject.connectSlotsByName(ct_FormCompra)
        ct_FormCompra.setTabOrder(self.tx_Cod, self.tx_Id)
        ct_FormCompra.setTabOrder(self.tx_Id, self.tx_NomeFantasia)
        ct_FormCompra.setTabOrder(self.tx_NomeFantasia, self.tx_Telefone)
        ct_FormCompra.setTabOrder(self.tx_Telefone, self.tx_IdBuscaItem)
        ct_FormCompra.setTabOrder(self.tx_IdBuscaItem, self.tx_BuscaItem)
        ct_FormCompra.setTabOrder(self.tx_BuscaItem, self.tx_QntdItem)
        ct_FormCompra.setTabOrder(self.tx_QntdItem, self.tx_ValorUnitarioItem)
        ct_FormCompra.setTabOrder(self.tx_ValorUnitarioItem, self.tx_ObsItem)
        ct_FormCompra.setTabOrder(self.tx_ObsItem, self.dt_Emissao)
        ct_FormCompra.setTabOrder(self.dt_Emissao, self.dt_Prazo)
        ct_FormCompra.setTabOrder(self.dt_Prazo, self.tx_ValorTotalItem)
        ct_FormCompra.setTabOrder(self.tx_ValorTotalItem, self.tb_Itens)

    def tradFormCompras(self, ct_FormCompra):
        ct_FormCompra.setWindowTitle(QtWidgets.QApplication.translate("ct_FormCompra", "Frame", None, -1))
        self.lb_FormCompra.setText(QtWidgets.QApplication.translate("ct_FormCompra", "COMPRA", None, -1))
        self.bt_Voltar.setText(QtWidgets.QApplication.translate("ct_FormCompra", "VOLTAR", None, -1))
        self.bt_Salvar.setText(QtWidgets.QApplication.translate("ct_FormCompra", "SALVAR", None, -1))
        self.bt_Imprimir.setText(QtWidgets.QApplication.translate("ct_FormCompra", "IMPRIMIR", None, -1))
        self.tx_NomeFantasia.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "NOME CLIENTE", None, -1))
        self.dt_Emissao.setDisplayFormat(QtWidgets.QApplication.translate("ct_FormCompra", "dd/MM/yyyy", None, -1))
        self.lb_FormCompra_21.setText(QtWidgets.QApplication.translate("ct_FormCompra", "DATA EMISSÃO", None, -1))
        self.dt_Prazo.setDisplayFormat(QtWidgets.QApplication.translate("ct_FormCompra", "dd/MM/yyyy", None, -1))
        self.lb_FormCompra_22.setText(QtWidgets.QApplication.translate("ct_FormCompra", "PRAZO ENTREGA", None, -1))
        self.bt_Entregar.setText(QtWidgets.QApplication.translate("ct_FormCompra", "RECEBER", None, -1))
        self.lb_FormCompra_23.setText(QtWidgets.QApplication.translate("ct_FormCompra", "DATA ENTREGA", None, -1))
        self.dt_Entrega.setDisplayFormat(QtWidgets.QApplication.translate("ct_FormCompra", "dd/MM/yyyy", None, -1))
        self.lb_FormCompra_2.setText(QtWidgets.QApplication.translate("ct_FormCompra", "FORNECEDOR", None, -1))
        self.lb_FormCompra_3.setText(QtWidgets.QApplication.translate("ct_FormCompra", "CÓD. FORNEC.", None, -1))
        self.tx_Id.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "0", None, -1))
        self.lb_FormCompra_4.setText(QtWidgets.QApplication.translate("ct_FormCompra", "ITENS", None, -1))
        self.tx_BuscaItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "DIGITE O NOME  DO ITEM", None, -1))
        self.lb_FormCompra_6.setText(QtWidgets.QApplication.translate("ct_FormCompra", "UNITÁRIO (R$)", None, -1))
        self.tx_ValorUnitarioItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "0,00", None, -1))
        self.lb_FormCompra_7.setText(QtWidgets.QApplication.translate("ct_FormCompra", "TOTAL (R$)", None, -1))
        self.tx_ValorTotalItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "0,00", None, -1))
        self.tx_ObsItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "OBSERVAÇÃO", None, -1))
        self.tx_IdBuscaItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "CÓD", None, -1))
        self.tx_QntdItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "QTDE.", None, -1))
        self.lb_FormCompra_5.setText(QtWidgets.QApplication.translate("ct_FormCompra", "TELEFONE", None, -1))
        self.tx_Telefone.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "(00) 00000-00", None, -1))
        self.tb_Itens.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ct_FormCompra", "PRODUTO", None, -1))
        self.tb_Itens.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ct_FormCompra", "OBS", None, -1))
        self.tb_Itens.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("ct_FormCompra", "QUANTIDADE", None, -1))
        self.tb_Itens.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("ct_FormCompra", "UNITÁRIO (R$)", None, -1))
        self.tb_Itens.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("ct_FormCompra", "TOTAL (R$)", None, -1))
        self.tb_Itens.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("ct_FormCompra", "EXCLUIR", None, -1))
        self.tx_Desconto.setText(QtWidgets.QApplication.translate("ct_FormCompra", "0.00", None, -1))
        self.tx_Desconto.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "R$ 0.00", None, -1))
        self.lb_FormVenda_14.setText(QtWidgets.QApplication.translate("ct_FormCompra", "DESCONTO", None, -1))
        self.tx_Frete.setText(QtWidgets.QApplication.translate("ct_FormCompra", "0.00", None, -1))
        self.tx_Frete.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "R$ 0.00", None, -1))
        self.lb_FormVenda_17.setText(QtWidgets.QApplication.translate("ct_FormCompra", "FRETE", None, -1))
        self.lb_SubTotal.setText(QtWidgets.QApplication.translate("ct_FormCompra", "0", None, -1))
        self.lb_FormVenda_18.setText(QtWidgets.QApplication.translate("ct_FormCompra", "SUBTOTAL (R$)", None, -1))
        self.lb_FormVenda_19.setText(QtWidgets.QApplication.translate("ct_FormCompra", "TOTAL FINAL (R$)", None, -1))
        self.bt_GerarParcela.setText(QtWidgets.QApplication.translate("ct_FormCompra", "GERAR  CONTAS", None, -1))
        self.tx_TotalFinal.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "0.00", None, -1))
        self.cb_FormaPagamento.setItemText(0, QtWidgets.QApplication.translate("ct_FormCompra", "DINHEIRO", None, -1))
        self.cb_FormaPagamento.setItemText(1, QtWidgets.QApplication.translate("ct_FormCompra", "CARTÂO", None, -1))
        self.lb_FormVenda_20.setText(QtWidgets.QApplication.translate("ct_FormCompra", "FORMA DE PAGAMENTO", None, -1))
        self.cb_QtdeParcela.setItemText(0, QtWidgets.QApplication.translate("ct_FormCompra", "À VISTA", None, -1))
        self.cb_QtdeParcela.setItemText(1, QtWidgets.QApplication.translate("ct_FormCompra", "ENTRADA + 01", None, -1))
        self.cb_QtdeParcela.setItemText(2, QtWidgets.QApplication.translate("ct_FormCompra", "ENTRADA + 02", None, -1))
        self.cb_QtdeParcela.setItemText(3, QtWidgets.QApplication.translate("ct_FormCompra", "ENTRADA + 03", None, -1))
        self.lb_FormVenda_21.setText(QtWidgets.QApplication.translate("ct_FormCompra", "PARCELAMENTO", None, -1))
        self.dt_Vencimento.setDisplayFormat(QtWidgets.QApplication.translate("ct_FormCompra", "dd/MM/yyyy", None, -1))
        self.lb_FormVenda_25.setText(QtWidgets.QApplication.translate("ct_FormCompra", "VENCIMENTO", None, -1))
        self.lb_FormVenda_22.setText(QtWidgets.QApplication.translate("ct_FormCompra", "VALOR PENDENTE", None, -1))
        self.lb_ValorPendente.setText(QtWidgets.QApplication.translate("ct_FormCompra", "0.00", None, -1))
        self.tb_Parcelas.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ct_FormCompra", "idConta", None, -1))
        self.tb_Parcelas.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ct_FormCompra", "Vencimento", None, -1))
        self.tb_Parcelas.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ct_FormCompra", "Valor", None, -1))
        self.tb_Parcelas.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("ct_FormCompra", "Saldo", None, -1))
        self.tb_Parcelas.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("ct_FormCompra", "Receber", None, -1))
        self.tx_valorRecebido.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormCompra", "0.00", None, -1))
        self.lb_FormVenda_23.setText(QtWidgets.QApplication.translate("ct_FormCompra", "VALOR PAGO", None, -1))

