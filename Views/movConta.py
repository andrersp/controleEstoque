# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movConta.ui',
# licensing of 'movConta.ui' applies.
#
# Created: Sat Feb  9 22:19:14 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ct_movimento(object):
    def setMovConta(self, ct_movimento):
        ct_movimento.setObjectName("ct_movimento")
        ct_movimento.resize(1000, 500)
        ct_movimento.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_movimento = QtWidgets.QFrame(ct_movimento)
        self.fr_movimento.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_movimento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_movimento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_movimento.setObjectName("fr_movimento")
        self.fr_TopoMenuMovimento = QtWidgets.QFrame(self.fr_movimento)
        self.fr_TopoMenuMovimento.setGeometry(QtCore.QRect(0, 0, 1000, 40))
        self.fr_TopoMenuMovimento.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_TopoMenuMovimento.setObjectName("fr_TopoMenuMovimento")
        self.bt_BuscaMovimento = QtWidgets.QPushButton(self.fr_TopoMenuMovimento)
        self.bt_BuscaMovimento.setGeometry(QtCore.QRect(920, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_BuscaMovimento.setFont(font)
        self.bt_BuscaMovimento.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_BuscaMovimento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaMovimento.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaMovimento.setStyleSheet("")
        self.bt_BuscaMovimento.setText("")
        self.bt_BuscaMovimento.setObjectName("bt_BuscaMovimento")
        self.bt_PrintMovimento = QtWidgets.QPushButton(self.fr_TopoMenuMovimento)
        self.bt_PrintMovimento.setGeometry(QtCore.QRect(960, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_PrintMovimento.setFont(font)
        self.bt_PrintMovimento.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_PrintMovimento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_PrintMovimento.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_PrintMovimento.setText("")
        self.bt_PrintMovimento.setObjectName("bt_PrintMovimento")
        self.dt_inicio = QtWidgets.QDateEdit(self.fr_TopoMenuMovimento)
        self.dt_inicio.setGeometry(QtCore.QRect(620, 16, 140, 20))
        self.dt_inicio.setStyleSheet("QDateEdit {\n"
"background: #E1DFE0;\n"
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
"     image: url(down.png);\n"
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
"}")
        self.dt_inicio.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dt_inicio.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dt_inicio.setCalendarPopup(True)
        self.dt_inicio.setTimeSpec(QtCore.Qt.TimeZone)
        self.dt_inicio.setObjectName("dt_inicio")
        self.lb_FormVenda_21 = QtWidgets.QLabel(self.fr_TopoMenuMovimento)
        self.lb_FormVenda_21.setGeometry(QtCore.QRect(620, 2, 120, 16))
        self.lb_FormVenda_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"\n"
"color:#1E87F0;\n"
"border: none;\n"
"}")
        self.lb_FormVenda_21.setObjectName("lb_FormVenda_21")
        self.lb_FormVenda_22 = QtWidgets.QLabel(self.fr_TopoMenuMovimento)
        self.lb_FormVenda_22.setGeometry(QtCore.QRect(770, 2, 120, 16))
        self.lb_FormVenda_22.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"\n"
"color:#1E87F0;\n"
"border: none;\n"
"}")
        self.lb_FormVenda_22.setObjectName("lb_FormVenda_22")
        self.dt_fim = QtWidgets.QDateEdit(self.fr_TopoMenuMovimento)
        self.dt_fim.setGeometry(QtCore.QRect(770, 16, 140, 20))
        self.dt_fim.setStyleSheet("QDateEdit {\n"
"background: #E1DFE0;\n"
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
"     image: url(down.png);\n"
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
"}")
        self.dt_fim.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dt_fim.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dt_fim.setCalendarPopup(True)
        self.dt_fim.setObjectName("dt_fim")
        self.fr_Receita = QtWidgets.QFrame(self.fr_movimento)
        self.fr_Receita.setGeometry(QtCore.QRect(20, 50, 470, 100))
        self.fr_Receita.setStyleSheet("QFrame {\n"
"background: rgba(139, 194, 74, 100%);\n"
"border: none;\n"
"}\n"
"")
        self.fr_Receita.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Receita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Receita.setObjectName("fr_Receita")
        self.pr_receita = QtWidgets.QProgressBar(self.fr_Receita)
        self.pr_receita.setGeometry(QtCore.QRect(10, 65, 450, 30))
        self.pr_receita.setStyleSheet("QProgressBar {\n"
"     border: 2px solid grey;\n"
"     border-radius: 5px;\n"
"    text-align: center;\n"
"    font: 14px \"Tahoma\";\n"
"    font-weight: bold;\n"
"    color: #000;\n"
"    background-color: #FFF\n"
"\n"
" }\n"
" QProgressBar::chunk {\n"
"     background: rgb(122, 179, 46, 60%);\n"
"     width: 8px;\n"
"     margin: 0.5px;\n"
"    border-radius: 3px\n"
" }")
        self.pr_receita.setProperty("value", 0)
        self.pr_receita.setObjectName("pr_receita")
        self.lb_FormVenda_20 = QtWidgets.QLabel(self.fr_Receita)
        self.lb_FormVenda_20.setGeometry(QtCore.QRect(10, 5, 150, 20))
        self.lb_FormVenda_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_FormVenda_20.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"border: none;\n"
"background: none\n"
"}")
        self.lb_FormVenda_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_20.setObjectName("lb_FormVenda_20")
        self.label_3 = QtWidgets.QLabel(self.fr_Receita)
        self.label_3.setGeometry(QtCore.QRect(10, 35, 25, 20))
        self.label_3.setStyleSheet("background: none;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 18px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.lb_entradaRecebido = QtWidgets.QLabel(self.fr_Receita)
        self.lb_entradaRecebido.setGeometry(QtCore.QRect(35, 30, 100, 25))
        self.lb_entradaRecebido.setStyleSheet("background: none;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 25px \"Arial\" ;\n"
"\n"
"color: #FFF;\n"
"")
        self.lb_entradaRecebido.setText("")
        self.lb_entradaRecebido.setObjectName("lb_entradaRecebido")
        self.lb_entradaPendente = QtWidgets.QLabel(self.fr_Receita)
        self.lb_entradaPendente.setGeometry(QtCore.QRect(155, 30, 100, 25))
        self.lb_entradaPendente.setStyleSheet("background: none;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 25px \"Arial\" ;\n"
"\n"
"color: #FFF;\n"
"")
        self.lb_entradaPendente.setText("")
        self.lb_entradaPendente.setObjectName("lb_entradaPendente")
        self.label_8 = QtWidgets.QLabel(self.fr_Receita)
        self.label_8.setGeometry(QtCore.QRect(130, 35, 25, 20))
        self.label_8.setStyleSheet("background: none;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 18px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.fr_Receita)
        self.line.setGeometry(QtCore.QRect(120, 30, 2, 30))
        self.line.setStyleSheet("background: #FFF")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lb_inicioMovimento = QtWidgets.QLabel(self.fr_Receita)
        self.lb_inicioMovimento.setGeometry(QtCore.QRect(280, 5, 80, 20))
        self.lb_inicioMovimento.setStyleSheet("QLabel{\n"
"font-size: 15px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"border: none;\n"
"background: none\n"
"}")
        self.lb_inicioMovimento.setText("")
        self.lb_inicioMovimento.setObjectName("lb_inicioMovimento")
        self.label_2 = QtWidgets.QLabel(self.fr_Receita)
        self.label_2.setGeometry(QtCore.QRect(365, 5, 10, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"border: none;\n"
"background: none\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lb_fimMovimento = QtWidgets.QLabel(self.fr_Receita)
        self.lb_fimMovimento.setGeometry(QtCore.QRect(380, 5, 80, 20))
        self.lb_fimMovimento.setStyleSheet("QLabel{\n"
"font-size: 15px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"border: none;\n"
"background: none\n"
"}")
        self.lb_fimMovimento.setText("")
        self.lb_fimMovimento.setObjectName("lb_fimMovimento")
        self.fr_Despesa = QtWidgets.QFrame(self.fr_movimento)
        self.fr_Despesa.setGeometry(QtCore.QRect(510, 50, 470, 100))
        self.fr_Despesa.setStyleSheet("QFrame {\n"
"background: rgba(251, 90, 84, 100%);\n"
"border: none;\n"
"\n"
"\n"
"}")
        self.fr_Despesa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Despesa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Despesa.setObjectName("fr_Despesa")
        self.pr_despesa = QtWidgets.QProgressBar(self.fr_Despesa)
        self.pr_despesa.setGeometry(QtCore.QRect(10, 65, 450, 30))
        self.pr_despesa.setStyleSheet("QProgressBar {\n"
"     border: 2px solid grey;\n"
"     border-radius: 5px;\n"
"    text-align: center;\n"
"    font: 14px \"Tahoma\";\n"
"    font-weight: bold;\n"
"    color: #000;\n"
"    background: #FFF \n"
"\n"
" }\n"
" QProgressBar::chunk {\n"
"     background: rgb(251, 90, 84, 60%);\n"
"     width: 8px;\n"
"     margin: 0.5px;\n"
"    border-radius: 3px\n"
" }")
        self.pr_despesa.setProperty("value", 0)
        self.pr_despesa.setObjectName("pr_despesa")
        self.lb_FormVenda_24 = QtWidgets.QLabel(self.fr_Despesa)
        self.lb_FormVenda_24.setGeometry(QtCore.QRect(10, 5, 150, 20))
        self.lb_FormVenda_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_FormVenda_24.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"border: none;\n"
"background: none\n"
"}")
        self.lb_FormVenda_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_24.setObjectName("lb_FormVenda_24")
        self.label_6 = QtWidgets.QLabel(self.fr_Despesa)
        self.label_6.setGeometry(QtCore.QRect(10, 35, 25, 20))
        self.label_6.setStyleSheet("background: none;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 18px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.lb_despesaPaga = QtWidgets.QLabel(self.fr_Despesa)
        self.lb_despesaPaga.setGeometry(QtCore.QRect(35, 30, 100, 25))
        self.lb_despesaPaga.setStyleSheet("background: none;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 25px \"Arial\" ;\n"
"\n"
"color: #FFF;\n"
"")
        self.lb_despesaPaga.setText("")
        self.lb_despesaPaga.setObjectName("lb_despesaPaga")
        self.line_3 = QtWidgets.QFrame(self.fr_Despesa)
        self.line_3.setGeometry(QtCore.QRect(120, 30, 2, 30))
        self.line_3.setStyleSheet("background: #FFF")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lb_despesaAPagar = QtWidgets.QLabel(self.fr_Despesa)
        self.lb_despesaAPagar.setGeometry(QtCore.QRect(155, 30, 100, 25))
        self.lb_despesaAPagar.setStyleSheet("background: none;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 25px \"Arial\" ;\n"
"\n"
"color: #FFF;\n"
"")
        self.lb_despesaAPagar.setText("")
        self.lb_despesaAPagar.setObjectName("lb_despesaAPagar")
        self.label_10 = QtWidgets.QLabel(self.fr_Despesa)
        self.label_10.setGeometry(QtCore.QRect(130, 35, 25, 20))
        self.label_10.setStyleSheet("background: none;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 18px \"Arial\" ;\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_10.setObjectName("label_10")
        self.lb_fimDespesa = QtWidgets.QLabel(self.fr_Despesa)
        self.lb_fimDespesa.setGeometry(QtCore.QRect(380, 5, 80, 20))
        self.lb_fimDespesa.setStyleSheet("QLabel{\n"
"font-size: 15px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"border: none;\n"
"background: none\n"
"}")
        self.lb_fimDespesa.setText("")
        self.lb_fimDespesa.setObjectName("lb_fimDespesa")
        self.label_12 = QtWidgets.QLabel(self.fr_Despesa)
        self.label_12.setGeometry(QtCore.QRect(365, 5, 10, 20))
        self.label_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"border: none;\n"
"background: none\n"
"}")
        self.label_12.setObjectName("label_12")
        self.lb_inicioDespesa = QtWidgets.QLabel(self.fr_Despesa)
        self.lb_inicioDespesa.setGeometry(QtCore.QRect(280, 5, 80, 20))
        self.lb_inicioDespesa.setStyleSheet("QLabel{\n"
"font-size: 15px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"border: none;\n"
"background: none\n"
"}")
        self.lb_inicioDespesa.setText("")
        self.lb_inicioDespesa.setObjectName("lb_inicioDespesa")
        self.tb_receita = QtWidgets.QTableWidget(self.fr_movimento)
        self.tb_receita.setGeometry(QtCore.QRect(20, 200, 470, 200))
        self.tb_receita.setStyleSheet("QTableView{\n"
"color: #797979;\n"
"font-weight: bold;\n"
"font-size: 13px;\n"
"background: #FFF;\n"
"padding: 0 0 0 5px;\n"
"}\n"
"")
        self.tb_receita.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_receita.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_receita.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_receita.setTabKeyNavigation(False)
        self.tb_receita.setProperty("showDropIndicator", False)
        self.tb_receita.setDragDropOverwriteMode(False)
        self.tb_receita.setAlternatingRowColors(True)
        self.tb_receita.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_receita.setShowGrid(False)
        self.tb_receita.setRowCount(0)
        self.tb_receita.setObjectName("tb_receita")
        self.tb_receita.setColumnCount(2)
        self.tb_receita.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_receita.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_receita.setHorizontalHeaderItem(1, item)
        self.tb_receita.horizontalHeader().setVisible(False)
        self.tb_receita.horizontalHeader().setDefaultSectionSize(200)
        self.tb_receita.horizontalHeader().setStretchLastSection(True)
        self.tb_receita.verticalHeader().setVisible(False)
        self.tb_receita.verticalHeader().setDefaultSectionSize(25)
        self.tb_despesa = QtWidgets.QTableWidget(self.fr_movimento)
        self.tb_despesa.setGeometry(QtCore.QRect(510, 200, 470, 200))
        self.tb_despesa.setStyleSheet("QTableView{\n"
"color: #797979;\n"
"font-weight: bold;\n"
"font-size: 13px;\n"
"background: #FFF;\n"
"padding: 0 0 0 5px;\n"
"}\n"
"")
        self.tb_despesa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_despesa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_despesa.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_despesa.setTabKeyNavigation(False)
        self.tb_despesa.setProperty("showDropIndicator", False)
        self.tb_despesa.setDragDropOverwriteMode(False)
        self.tb_despesa.setAlternatingRowColors(True)
        self.tb_despesa.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_despesa.setShowGrid(False)
        self.tb_despesa.setRowCount(1)
        self.tb_despesa.setObjectName("tb_despesa")
        self.tb_despesa.setColumnCount(2)
        self.tb_despesa.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tb_despesa.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_despesa.setHorizontalHeaderItem(1, item)
        self.tb_despesa.horizontalHeader().setVisible(False)
        self.tb_despesa.horizontalHeader().setDefaultSectionSize(200)
        self.tb_despesa.horizontalHeader().setStretchLastSection(True)
        self.tb_despesa.verticalHeader().setVisible(False)
        self.tb_despesa.verticalHeader().setDefaultSectionSize(25)
        self.frameTotalmov = QtWidgets.QFrame(self.fr_movimento)
        self.frameTotalmov.setGeometry(QtCore.QRect(0, 460, 1000, 40))
        self.frameTotalmov.setStyleSheet("border-bottom: 2px solid #CCC;\n"
"background: #F7F7F7")
        self.frameTotalmov.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTotalmov.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTotalmov.setObjectName("frameTotalmov")
        self.label = QtWidgets.QLabel(self.frameTotalmov)
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 20))
        self.label.setStyleSheet("QLabel{\n"
"font-size: 16px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #072D06;\n"
"border: none;\n"
"background: none\n"
"}")
        self.label.setObjectName("label")
        self.lb_totalMovimento = QtWidgets.QLabel(self.frameTotalmov)
        self.lb_totalMovimento.setGeometry(QtCore.QRect(830, 5, 150, 30))
        self.lb_totalMovimento.setStyleSheet("QLabel{\n"
"font-size: 26px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #072D06;\n"
"border: none;\n"
"background: none\n"
"}")
        self.lb_totalMovimento.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_totalMovimento.setObjectName("lb_totalMovimento")

        self.tradMovConta(ct_movimento)
        QtCore.QMetaObject.connectSlotsByName(ct_movimento)

    def tradMovConta(self, ct_movimento):
        ct_movimento.setWindowTitle(QtWidgets.QApplication.translate("ct_movimento", "Frame", None, -1))
        self.bt_BuscaMovimento.setToolTip(QtWidgets.QApplication.translate("ct_movimento", "BUSCAR", None, -1))
        self.bt_PrintMovimento.setToolTip(QtWidgets.QApplication.translate("ct_movimento", "IMPRIMIR", None, -1))
        self.dt_inicio.setDisplayFormat(QtWidgets.QApplication.translate("ct_movimento", "dd-MM-yyyy", None, -1))
        self.lb_FormVenda_21.setText(QtWidgets.QApplication.translate("ct_movimento", "DATA ÍNICIO", None, -1))
        self.lb_FormVenda_22.setText(QtWidgets.QApplication.translate("ct_movimento", "DATA FIM", None, -1))
        self.dt_fim.setDisplayFormat(QtWidgets.QApplication.translate("ct_movimento", "dd-MM-yyyy", None, -1))
        self.lb_FormVenda_20.setText(QtWidgets.QApplication.translate("ct_movimento", "TOTAL DE RECEITAS", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ct_movimento", "R$", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("ct_movimento", "R$", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ct_movimento", "à", None, -1))
        self.pr_despesa.setFormat(QtWidgets.QApplication.translate("ct_movimento", "%p%", None, -1))
        self.lb_FormVenda_24.setText(QtWidgets.QApplication.translate("ct_movimento", "TOTAL DE DESPESAS", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("ct_movimento", "R$", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("ct_movimento", "R$", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("ct_movimento", "à", None, -1))
        self.tb_receita.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ct_movimento", "New Column", None, -1))
        self.tb_receita.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ct_movimento", "New Column", None, -1))
        self.tb_despesa.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ct_movimento", "New Column", None, -1))
        self.tb_despesa.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ct_movimento", "New Column", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ct_movimento", "LUCRO / PREJUÍZO", None, -1))
        self.lb_totalMovimento.setText(QtWidgets.QApplication.translate("ct_movimento", "R$ 250,00", None, -1))

