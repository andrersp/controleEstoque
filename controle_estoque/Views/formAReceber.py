# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formAReceber.ui',
# licensing of 'formAReceber.ui' applies.
#
# Created: Wed Feb 13 14:11:39 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ct_FormReceber(object):
    def setFormAReceber(self, ct_FormReceber):
        ct_FormReceber.setObjectName("ct_FormReceber")
        ct_FormReceber.resize(1000, 500)
        self.fr_FormReceber = QtWidgets.QFrame(ct_FormReceber)
        self.fr_FormReceber.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormReceber.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormReceber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_FormReceber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormReceber.setObjectName("fr_FormReceber")
        self.lb_FormProdutos = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(100, 10, 880, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.tx_Cod = QtWidgets.QLineEdit(self.fr_FormReceber)
        self.tx_Cod.setEnabled(False)
        self.tx_Cod.setGeometry(QtCore.QRect(20, 10, 50, 30))
        self.tx_Cod.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border: 1px solid #A2A2A2;\n"
"color: #000;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.tx_Cod.setText("")
        self.tx_Cod.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Cod.setObjectName("tx_Cod")
        self.lb_FormCompra_5 = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormCompra_5.setGeometry(QtCore.QRect(510, 60, 110, 20))
        self.lb_FormCompra_5.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_5.setObjectName("lb_FormCompra_5")
        self.tx_Id = QtWidgets.QLineEdit(self.fr_FormReceber)
        self.tx_Id.setGeometry(QtCore.QRect(20, 80, 100, 30))
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
        self.lb_FormCompra_2 = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormCompra_2.setGeometry(QtCore.QRect(140, 60, 120, 20))
        self.lb_FormCompra_2.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_2.setObjectName("lb_FormCompra_2")
        self.tx_NomeFantasia = QtWidgets.QLineEdit(self.fr_FormReceber)
        self.tx_NomeFantasia.setGeometry(QtCore.QRect(140, 80, 350, 30))
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
        self.lb_FormCompra_3 = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormCompra_3.setGeometry(QtCore.QRect(20, 60, 100, 20))
        self.lb_FormCompra_3.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_3.setObjectName("lb_FormCompra_3")
        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormReceber)
        self.tx_Telefone.setGeometry(QtCore.QRect(510, 80, 110, 30))
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
        self.tx_descricao = QtWidgets.QLineEdit(self.fr_FormReceber)
        self.tx_descricao.setGeometry(QtCore.QRect(20, 140, 600, 30))
        self.tx_descricao.setMouseTracking(True)
        self.tx_descricao.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_descricao.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_descricao.setText("")
        self.tx_descricao.setFrame(False)
        self.tx_descricao.setCursorPosition(0)
        self.tx_descricao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_descricao.setReadOnly(False)
        self.tx_descricao.setObjectName("tx_descricao")
        self.lb_FormCompra_4 = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormCompra_4.setGeometry(QtCore.QRect(20, 120, 120, 20))
        self.lb_FormCompra_4.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_4.setObjectName("lb_FormCompra_4")
        self.lb_FormCompra_6 = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormCompra_6.setGeometry(QtCore.QRect(20, 180, 120, 20))
        self.lb_FormCompra_6.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_6.setObjectName("lb_FormCompra_6")
        self.cb_categoria = QtWidgets.QComboBox(self.fr_FormReceber)
        self.cb_categoria.setGeometry(QtCore.QRect(20, 200, 180, 30))
        self.cb_categoria.setStyleSheet("QComboBox{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url(Images/down.png);\n"
" }\n"
"")
        self.cb_categoria.setObjectName("cb_categoria")
        self.bt_AddCategoriaProduto = QtWidgets.QPushButton(self.fr_FormReceber)
        self.bt_AddCategoriaProduto.setGeometry(QtCore.QRect(200, 200, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.bt_AddCategoriaProduto.setFont(font)
        self.bt_AddCategoriaProduto.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_AddCategoriaProduto.setText("")
        self.bt_AddCategoriaProduto.setObjectName("bt_AddCategoriaProduto")
        self.bt_CancelAddCatergoria = QtWidgets.QPushButton(self.fr_FormReceber)
        self.bt_CancelAddCatergoria.setGeometry(QtCore.QRect(200, 200, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.bt_CancelAddCatergoria.setFont(font)
        self.bt_CancelAddCatergoria.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_CancelAddCatergoria.setText("")
        self.bt_CancelAddCatergoria.setObjectName("bt_CancelAddCatergoria")
        self.dt_Vencimento = QtWidgets.QDateEdit(self.fr_FormReceber)
        self.dt_Vencimento.setGeometry(QtCore.QRect(250, 200, 180, 30))
        self.dt_Vencimento.setStyleSheet("QDateEdit {\n"
"background: #CFCFCF;\n"
"border: none;\n"
"font-family: \"Arial\";\n"
"font-size: 16px;\n"
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
"     image: url(Images/down.png);\n"
" }\n"
"\n"
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
"}")
        self.dt_Vencimento.setCalendarPopup(True)
        self.dt_Vencimento.setObjectName("dt_Vencimento")
        self.lb_FormCompra_7 = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormCompra_7.setGeometry(QtCore.QRect(250, 180, 150, 20))
        self.lb_FormCompra_7.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_7.setObjectName("lb_FormCompra_7")
        self.tx_Obs = QtWidgets.QTextEdit(self.fr_FormReceber)
        self.tx_Obs.setGeometry(QtCore.QRect(20, 260, 600, 100))
        self.tx_Obs.setStyleSheet("QTextEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QTextEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Obs.setObjectName("tx_Obs")
        self.lb_FormCompra_8 = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormCompra_8.setGeometry(QtCore.QRect(20, 240, 120, 20))
        self.lb_FormCompra_8.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_8.setObjectName("lb_FormCompra_8")
        self.fr_financeiroCompra = QtWidgets.QFrame(self.fr_FormReceber)
        self.fr_financeiroCompra.setGeometry(QtCore.QRect(640, 60, 340, 360))
        self.fr_financeiroCompra.setStyleSheet("background: #F1F1F1;\n"
"border-top: 4px solid #277298;\n"
"border-bottom: 4px solid #277298;")
        self.fr_financeiroCompra.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_financeiroCompra.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_financeiroCompra.setObjectName("fr_financeiroCompra")
        self.lb_FormVenda_14 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_14.setGeometry(QtCore.QRect(20, 20, 130, 30))
        self.lb_FormVenda_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_14.setObjectName("lb_FormVenda_14")
        self.dt_dataPagamento = QtWidgets.QDateEdit(self.fr_financeiroCompra)
        self.dt_dataPagamento.setGeometry(QtCore.QRect(160, 20, 150, 30))
        self.dt_dataPagamento.setStyleSheet("QDateEdit {\n"
"background: #FFF;\n"
"border: none;\n"
"font-family: \"Arial\";\n"
"font-size: 14px;\n"
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
"     image: url(Images/down.png);\n"
" }\n"
"\n"
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
"}")
        self.dt_dataPagamento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dt_dataPagamento.setCalendarPopup(True)
        self.dt_dataPagamento.setObjectName("dt_dataPagamento")
        self.lb_FormVenda_22 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_22.setGeometry(QtCore.QRect(20, 320, 130, 30))
        self.lb_FormVenda_22.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_22.setObjectName("lb_FormVenda_22")
        self.lb_ValorPendente = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_ValorPendente.setGeometry(QtCore.QRect(160, 320, 125, 30))
        self.lb_ValorPendente.setStyleSheet("QLabel{\n"
"font-size: 20px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_ValorPendente.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_ValorPendente.setObjectName("lb_ValorPendente")
        self.tx_valorPago = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_valorPago.setGeometry(QtCore.QRect(160, 100, 125, 30))
        self.tx_valorPago.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_valorPago.setStyleSheet("QLineEdit{\n"
"background: #FFF;\n"
"border: none;\n"
"font-family: \"Arial\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color: rgb(80,79,79)\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_valorPago.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_valorPago.setObjectName("tx_valorPago")
        self.lb_FormVenda_27 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_27.setGeometry(QtCore.QRect(20, 60, 130, 30))
        self.lb_FormVenda_27.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_27.setObjectName("lb_FormVenda_27")
        self.cb_formaPagamento = QtWidgets.QComboBox(self.fr_financeiroCompra)
        self.cb_formaPagamento.setGeometry(QtCore.QRect(160, 60, 150, 30))
        self.cb_formaPagamento.setStyleSheet("QComboBox{\n"
"background: #FFF;\n"
"border: none;\n"
"font-family: \"Arial\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color: rgb(80,79,79)\n"
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
"     image: url(down.png);\n"
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
        self.cb_formaPagamento.setObjectName("cb_formaPagamento")
        self.lb_FormVenda_28 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_28.setGeometry(QtCore.QRect(20, 100, 130, 30))
        self.lb_FormVenda_28.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.lb_FormVenda_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_28.setObjectName("lb_FormVenda_28")
        self.bt_receber = QtWidgets.QPushButton(self.fr_financeiroCompra)
        self.bt_receber.setEnabled(True)
        self.bt_receber.setGeometry(QtCore.QRect(160, 140, 125, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_receber.setFont(font)
        self.bt_receber.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_receber.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_receber.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_receber.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF;\n"
"border: none;\n"
"border-radius: 2px\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_receber.setIconSize(QtCore.QSize(75, 35))
        self.bt_receber.setObjectName("bt_receber")
        self.lb_FormCompra_9 = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_FormCompra_9.setGeometry(QtCore.QRect(450, 180, 100, 20))
        self.lb_FormCompra_9.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_FormCompra_9.setObjectName("lb_FormCompra_9")
        self.tx_valor = QtWidgets.QLineEdit(self.fr_FormReceber)
        self.tx_valor.setGeometry(QtCore.QRect(450, 200, 170, 30))
        self.tx_valor.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_valor.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border: none;\n"
"font-family: \"Arial\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: rgb(80,79,79)\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_valor.setObjectName("tx_valor")
        self.cb_repetir = QtWidgets.QComboBox(self.fr_FormReceber)
        self.cb_repetir.setGeometry(QtCore.QRect(20, 390, 180, 30))
        self.cb_repetir.setStyleSheet("QComboBox{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url(Images/down.png);\n"
" }\n"
"")
        self.cb_repetir.setObjectName("cb_repetir")
        self.lb_Repetir = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_Repetir.setGeometry(QtCore.QRect(20, 370, 110, 20))
        self.lb_Repetir.setStyleSheet("QLabel{\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #A2A2A2;\n"
"}")
        self.lb_Repetir.setObjectName("lb_Repetir")
        self.fr_BotoesFormCompra = QtWidgets.QFrame(self.fr_FormReceber)
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
        self.lb_obsRepetir = QtWidgets.QLabel(self.fr_FormReceber)
        self.lb_obsRepetir.setGeometry(QtCore.QRect(210, 390, 410, 30))
        self.lb_obsRepetir.setStyleSheet("   QLabel \n"
"{\n"
"font-family: \"Arial\";\n"
"color: #a3a3a3;\n"
" font-size: 12px;\n"
"text-align: center\n"
"   \n"
"\n"
"}")
        self.lb_obsRepetir.setMargin(0)
        self.lb_obsRepetir.setObjectName("lb_obsRepetir")
        self.tx_addCategoria = QtWidgets.QLineEdit(self.fr_FormReceber)
        self.tx_addCategoria.setGeometry(QtCore.QRect(20, 200, 180, 30))
        self.tx_addCategoria.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_addCategoria.setObjectName("tx_addCategoria")

        self.tradFormAReceber(ct_FormReceber)
        QtCore.QMetaObject.connectSlotsByName(ct_FormReceber)

    def tradFormAReceber(self, ct_FormReceber):
        ct_FormReceber.setWindowTitle(QtWidgets.QApplication.translate("ct_FormReceber", "Frame", None, -1))
        self.lb_FormProdutos.setText(QtWidgets.QApplication.translate("ct_FormReceber", "CADASTRO CONTA A RECEBER", None, -1))
        self.lb_FormCompra_5.setText(QtWidgets.QApplication.translate("ct_FormReceber", "TELEFONE", None, -1))
        self.tx_Id.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormReceber", "0", None, -1))
        self.lb_FormCompra_2.setText(QtWidgets.QApplication.translate("ct_FormReceber", "CLIENTE", None, -1))
        self.tx_NomeFantasia.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormReceber", "NOME CLIENTE", None, -1))
        self.lb_FormCompra_3.setText(QtWidgets.QApplication.translate("ct_FormReceber", "CÓD. CLIENTE", None, -1))
        self.tx_Telefone.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormReceber", "(00) 00000-00", None, -1))
        self.tx_descricao.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormReceber", "DESCRIçÃO ", None, -1))
        self.lb_FormCompra_4.setText(QtWidgets.QApplication.translate("ct_FormReceber", "DESCRIÇÃO", None, -1))
        self.lb_FormCompra_6.setText(QtWidgets.QApplication.translate("ct_FormReceber", "CATEGORIA", None, -1))
        self.bt_CancelAddCatergoria.setToolTip(QtWidgets.QApplication.translate("ct_FormReceber", "<html><head/><body><p>Cancelar</p></body></html>", None, -1))
        self.dt_Vencimento.setDisplayFormat(QtWidgets.QApplication.translate("ct_FormReceber", "dd/MM/yyyy", None, -1))
        self.lb_FormCompra_7.setText(QtWidgets.QApplication.translate("ct_FormReceber", "VENCIMENTO", None, -1))
        self.lb_FormCompra_8.setText(QtWidgets.QApplication.translate("ct_FormReceber", "OBSERVAÇÕES", None, -1))
        self.lb_FormVenda_14.setText(QtWidgets.QApplication.translate("ct_FormReceber", "DATA PAGAMENTO", None, -1))
        self.dt_dataPagamento.setDisplayFormat(QtWidgets.QApplication.translate("ct_FormReceber", "dd/MM/yyyy", None, -1))
        self.lb_FormVenda_22.setText(QtWidgets.QApplication.translate("ct_FormReceber", "VALOR PENDENTE", None, -1))
        self.lb_ValorPendente.setText(QtWidgets.QApplication.translate("ct_FormReceber", "0.00", None, -1))
        self.tx_valorPago.setText(QtWidgets.QApplication.translate("ct_FormReceber", "0.00", None, -1))
        self.tx_valorPago.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormReceber", "R$ 0.00", None, -1))
        self.lb_FormVenda_27.setText(QtWidgets.QApplication.translate("ct_FormReceber", "FORMA PAGAMENTO", None, -1))
        self.lb_FormVenda_28.setText(QtWidgets.QApplication.translate("ct_FormReceber", "VALOR PAGO", None, -1))
        self.bt_receber.setText(QtWidgets.QApplication.translate("ct_FormReceber", "RECEBER", None, -1))
        self.lb_FormCompra_9.setText(QtWidgets.QApplication.translate("ct_FormReceber", "VALOR", None, -1))
        self.tx_valor.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormReceber", "R$ 0,00", None, -1))
        self.lb_Repetir.setText(QtWidgets.QApplication.translate("ct_FormReceber", "REPETIR", None, -1))
        self.bt_Voltar.setText(QtWidgets.QApplication.translate("ct_FormReceber", "VOLTAR", None, -1))
        self.bt_Salvar.setText(QtWidgets.QApplication.translate("ct_FormReceber", "SALVAR", None, -1))
        self.bt_Imprimir.setText(QtWidgets.QApplication.translate("ct_FormReceber", "IMPRIMIR", None, -1))
        self.lb_obsRepetir.setText(QtWidgets.QApplication.translate("ct_FormReceber", "Utilize esta opção caso esta conta for se repetir nos próximos meses,  \n"
"para efetuar os lançamentos futuros", None, -1))

