# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aReceber.ui',
# licensing of 'aReceber.ui' applies.
#
# Created: Fri Mar 15 08:46:39 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_AReceber(object):
    def setAReceber(self, ct_AReceber):
        ct_AReceber.setObjectName("ct_AReceber")
        ct_AReceber.resize(1000, 500)
        ct_AReceber.setStyleSheet("border: none;\n"
                                  "background: #FFF")
        self.fr_AReceber = QtWidgets.QFrame(ct_AReceber)
        self.fr_AReceber.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_AReceber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_AReceber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_AReceber.setObjectName("fr_AReceber")
        self.fr_TopoMenuAReceber = QtWidgets.QFrame(self.fr_AReceber)
        self.fr_TopoMenuAReceber.setGeometry(QtCore.QRect(0, 0, 1000, 40))
        self.fr_TopoMenuAReceber.setStyleSheet("background:#E1DFE0;\n"
                                               "border: none;")
        self.fr_TopoMenuAReceber.setObjectName("fr_TopoMenuAReceber")
        self.bt_Busca = QtWidgets.QPushButton(self.fr_TopoMenuAReceber)
        self.bt_Busca.setGeometry(QtCore.QRect(820, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_Busca.setFont(font)
        self.bt_Busca.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Busca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Busca.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_Busca.setStyleSheet("")
        self.bt_Busca.setText("")
        self.bt_Busca.setObjectName("bt_Busca")
        self.bt_Print = QtWidgets.QPushButton(self.fr_TopoMenuAReceber)
        self.bt_Print.setGeometry(QtCore.QRect(860, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_Print.setFont(font)
        self.bt_Print.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Print.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Print.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_Print.setText("")
        self.bt_Print.setObjectName("bt_Print")
        self.dt_Inicio = QtWidgets.QDateEdit(self.fr_TopoMenuAReceber)
        self.dt_Inicio.setGeometry(QtCore.QRect(370, 16, 140, 20))
        self.dt_Inicio.setStyleSheet("QDateEdit {\n"
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
                                     "image: url("+self.resourcepath('Images/down.png')+");\n"
                                     " }\n"
                                     "")
        self.dt_Inicio.setCalendarPopup(True)
        self.dt_Inicio.setObjectName("dt_Inicio")
        self.lb_FormVenda_25 = QtWidgets.QLabel(self.fr_TopoMenuAReceber)
        self.lb_FormVenda_25.setGeometry(QtCore.QRect(370, 2, 120, 16))
        self.lb_FormVenda_25.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_25.setObjectName("lb_FormVenda_25")
        self.lb_FormVenda_26 = QtWidgets.QLabel(self.fr_TopoMenuAReceber)
        self.lb_FormVenda_26.setGeometry(QtCore.QRect(530, 2, 120, 16))
        self.lb_FormVenda_26.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_26.setObjectName("lb_FormVenda_26")
        self.dt_Fim = QtWidgets.QDateEdit(self.fr_TopoMenuAReceber)
        self.dt_Fim.setGeometry(QtCore.QRect(530, 16, 140, 20))
        self.dt_Fim.setStyleSheet("QDateEdit {\n"
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
                                  "image: url("+self.resourcepath('Images/down.png')+");\n"
                                  " }\n"
                                  "")
        self.dt_Fim.setCalendarPopup(True)
        self.dt_Fim.setObjectName("dt_Fim")
        self.cb_Situacao = QtWidgets.QComboBox(self.fr_TopoMenuAReceber)
        self.cb_Situacao.setGeometry(QtCore.QRect(690, 16, 120, 20))
        self.cb_Situacao.setStyleSheet("QComboBox{\n"
                                       "background: #E1DFE0;\n"
                                       "border: none;\n"
                                       "font-family: \"Arial\";\n"
                                       "font-size: 14px;\n"
                                       "font-weight: bold;\n"
                                       "color: rgb(80,79,79)\n"
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
                                       "     image: url("+self.resourcepath(
                                           'Images/down.png')+");\n"
                                       " }\n"
                                       "")
        self.cb_Situacao.setObjectName("cb_Situacao")
        self.cb_Situacao.addItem("")
        self.cb_Situacao.addItem("")
        self.lb_FormVenda_29 = QtWidgets.QLabel(self.fr_TopoMenuAReceber)
        self.lb_FormVenda_29.setGeometry(QtCore.QRect(690, 2, 120, 16))
        self.lb_FormVenda_29.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_29.setObjectName("lb_FormVenda_29")
        self.bt_AddConta = QtWidgets.QPushButton(self.fr_TopoMenuAReceber)
        self.bt_AddConta.setGeometry(QtCore.QRect(900, 0, 100, 40))
        self.bt_AddConta.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_AddConta.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddConta.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_AddConta.setStyleSheet("QPushButton {\n"
                                       "background-color: #7AB32E;\n"
                                       " }\n"
                                       "QPushButton:hover{\n"
                                       "background-color: #40a286\n"
                                       "}")
        self.bt_AddConta.setText("")
        self.bt_AddConta.setObjectName("bt_AddConta")
        self.tx_Buscar = QtWidgets.QLineEdit(self.fr_TopoMenuAReceber)
        self.tx_Buscar.setGeometry(QtCore.QRect(0, 5, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_Buscar.setFont(font)
        self.tx_Buscar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_Buscar.setStyleSheet("QLineEdit {\n"
                                     "color: #000\n"
                                     "}\n"
                                     "")
        self.tx_Buscar.setObjectName("tx_Buscar")
        self.tb_AReceber = QtWidgets.QTableWidget(self.fr_AReceber)
        self.tb_AReceber.setGeometry(QtCore.QRect(0, 40, 1000, 455))
        self.tb_AReceber.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tb_AReceber.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_AReceber.setStyleSheet("QTableView{\n"
                                       "color: #797979;\n"
                                       "font-weight: bold;\n"
                                       "font-size: 13px;\n"
                                       "background: #FFF;\n"
                                       "padding: 0 0 0 5px;\n"
                                       "}\n"
                                       "QHeaderView:section{\n"
                                       "background: #FFF;\n"
                                       "padding: 5px 0 ;\n"
                                       "font-size: 13px;\n"
                                       "font-family: \"Arial\";\n"
                                       "font-weight: bold;\n"
                                       "color: #797979;\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid #CCC;\n"
                                       "}\n"
                                       "QTableView::item {\n"
                                       "border-bottom: 2px solid #CCC;\n"
                                       "padding: 2px;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.tb_AReceber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_AReceber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_AReceber.setAutoScrollMargin(20)
        self.tb_AReceber.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_AReceber.setTabKeyNavigation(False)
        self.tb_AReceber.setProperty("showDropIndicator", False)
        self.tb_AReceber.setDragDropOverwriteMode(False)
        self.tb_AReceber.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.tb_AReceber.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_AReceber.setShowGrid(False)
        self.tb_AReceber.setCornerButtonEnabled(False)
        self.tb_AReceber.setRowCount(0)
        self.tb_AReceber.setObjectName("tb_AReceber")
        self.tb_AReceber.setColumnCount(8)
        self.tb_AReceber.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AReceber.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AReceber.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AReceber.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AReceber.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AReceber.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AReceber.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AReceber.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AReceber.setHorizontalHeaderItem(7, item)
        self.tb_AReceber.horizontalHeader().setDefaultSectionSize(120)
        self.tb_AReceber.horizontalHeader().setStretchLastSection(True)
        self.tb_AReceber.verticalHeader().setVisible(False)
        self.tb_AReceber.verticalHeader().setCascadingSectionResizes(True)
        self.tb_AReceber.verticalHeader().setDefaultSectionSize(50)

        self.tradAReceber(ct_AReceber)
        QtCore.QMetaObject.connectSlotsByName(ct_AReceber)

    def tradAReceber(self, ct_AReceber):
        ct_AReceber.setWindowTitle(QtWidgets.QApplication.translate(
            "ct_AReceber", "Frame", None, -1))
        self.bt_Busca.setToolTip(QtWidgets.QApplication.translate(
            "ct_AReceber", "BUSCAR", None, -1))
        self.bt_Print.setToolTip(QtWidgets.QApplication.translate(
            "ct_AReceber", "IMPRIMIR", None, -1))
        self.dt_Inicio.setDisplayFormat(QtWidgets.QApplication.translate(
            "ct_AReceber", "dd/MM/yyyy", None, -1))
        self.lb_FormVenda_25.setText(QtWidgets.QApplication.translate(
            "ct_AReceber", "DATA ÍNICIO", None, -1))
        self.lb_FormVenda_26.setText(QtWidgets.QApplication.translate(
            "ct_AReceber", "DATA FIM", None, -1))
        self.dt_Fim.setDisplayFormat(QtWidgets.QApplication.translate(
            "ct_AReceber", "dd/MM/yyyy", None, -1))
        self.cb_Situacao.setItemText(0, QtWidgets.QApplication.translate(
            "ct_AReceber", "PENDENTE", None, -1))
        self.cb_Situacao.setItemText(1, QtWidgets.QApplication.translate(
            "ct_AReceber", "RECEBIDO", None, -1))
        self.lb_FormVenda_29.setText(QtWidgets.QApplication.translate(
            "ct_AReceber", "SITUAÇÃO", None, -1))
        self.tx_Buscar.setPlaceholderText(QtWidgets.QApplication.translate(
            "ct_AReceber", "PROCURAR POR...", None, -1))
        self.tb_AReceber.horizontalHeaderItem(0).setText(
            QtWidgets.QApplication.translate("ct_AReceber", "ID", None, -1))
        self.tb_AReceber.horizontalHeaderItem(2).setText(
            QtWidgets.QApplication.translate("ct_AReceber", "CLIENTE", None, -1))
        self.tb_AReceber.horizontalHeaderItem(3).setText(
            QtWidgets.QApplication.translate("ct_AReceber", "DESCRIÇÃO", None, -1))
        self.tb_AReceber.horizontalHeaderItem(4).setText(
            QtWidgets.QApplication.translate("ct_AReceber", "VENCIMENTO", None, -1))
        self.tb_AReceber.horizontalHeaderItem(5).setText(
            QtWidgets.QApplication.translate("ct_AReceber", "VALOR", None, -1))
        self.tb_AReceber.horizontalHeaderItem(6).setText(
            QtWidgets.QApplication.translate("ct_AReceber", "SALDO", None, -1))
        self.tb_AReceber.horizontalHeaderItem(7).setText(
            QtWidgets.QApplication.translate("ct_AReceber", "RECEBER", None, -1))
