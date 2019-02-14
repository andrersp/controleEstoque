# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainVendas.ui'
#
# Created by: PySide2 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_MainVendas(object):

    def setMainVendas(self, ct_MainVendas):
        ct_MainVendas.setObjectName("ct_MainVendas")
        ct_MainVendas.resize(1000, 600)
        ct_MainVendas.setStyleSheet("border:none")
        self.frameMainVendas = QtWidgets.QFrame(ct_MainVendas)
        self.frameMainVendas.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainVendas.setObjectName("frameMainVendas")
        self.fr_TopoMenuVendas = QtWidgets.QFrame(self.frameMainVendas)
        self.fr_TopoMenuVendas.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_TopoMenuVendas.setStyleSheet("background:#E1DFE0;\n"
                                             "border: none;")
        self.fr_TopoMenuVendas.setObjectName("fr_TopoMenuVendas")
        self.bt_BuscaVendas = QtWidgets.QPushButton(self.fr_TopoMenuVendas)
        self.bt_BuscaVendas.setGeometry(QtCore.QRect(820, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_BuscaVendas.setFont(font)
        self.bt_BuscaVendas.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_BuscaVendas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaVendas.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaVendas.setStyleSheet("")
        self.bt_BuscaVendas.setText("")
        self.bt_BuscaVendas.setObjectName("bt_BuscaVendas")
        self.bt_AddNovoVenda = QtWidgets.QPushButton(self.fr_TopoMenuVendas)
        self.bt_AddNovoVenda.setGeometry(QtCore.QRect(900, 0, 100, 40))
        self.bt_AddNovoVenda.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_AddNovoVenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddNovoVenda.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_AddNovoVenda.setStyleSheet("QPushButton {\n"
                                           "background-color: #7AB32E;\n"
                                           " }\n"
                                           "QPushButton:hover{\n"
                                           "background-color: #40a286\n"
                                           "}")
        self.bt_AddNovoVenda.setText("")
        self.bt_AddNovoVenda.setObjectName("bt_AddNovoVenda")
        self.tx_BuscaVendas = QtWidgets.QLineEdit(self.fr_TopoMenuVendas)
        self.tx_BuscaVendas.setGeometry(QtCore.QRect(0, 5, 500, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_BuscaVendas.setFont(font)
        self.tx_BuscaVendas.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_BuscaVendas.setStyleSheet("QLineEdit {\n"
                                          "color: #000\n"
                                          "}\n"
                                          "")
        self.tx_BuscaVendas.setObjectName("tx_BuscaVendas")
        self.bt_PrintRelatVendas = QtWidgets.QPushButton(
            self.fr_TopoMenuVendas)
        self.bt_PrintRelatVendas.setGeometry(QtCore.QRect(860, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_PrintRelatVendas.setFont(font)
        self.bt_PrintRelatVendas.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_PrintRelatVendas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_PrintRelatVendas.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_PrintRelatVendas.setText("")
        self.bt_PrintRelatVendas.setObjectName("bt_PrintRelatVendas")
        self.dt_InicioVenda = QtWidgets.QDateEdit(self.fr_TopoMenuVendas)
        self.dt_InicioVenda.setGeometry(QtCore.QRect(520, 16, 140, 20))
        self.dt_InicioVenda.setStyleSheet("QDateEdit {\n"
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
                                          "     image: url("+self.resourcepath('Images/down.png')+");\n"
                                          " }")
        self.dt_InicioVenda.setCalendarPopup(True)
        self.dt_InicioVenda.setObjectName("dt_InicioVenda")
        self.lb_FormVenda_21 = QtWidgets.QLabel(self.fr_TopoMenuVendas)
        self.lb_FormVenda_21.setGeometry(QtCore.QRect(520, 2, 120, 16))
        self.lb_FormVenda_21.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_21.setObjectName("lb_FormVenda_21")
        self.lb_FormVenda_22 = QtWidgets.QLabel(self.fr_TopoMenuVendas)
        self.lb_FormVenda_22.setGeometry(QtCore.QRect(670, 2, 120, 16))
        self.lb_FormVenda_22.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_22.setObjectName("lb_FormVenda_22")
        self.dt_FimVenda = QtWidgets.QDateEdit(self.fr_TopoMenuVendas)
        self.dt_FimVenda.setGeometry(QtCore.QRect(670, 16, 140, 20))
        self.dt_FimVenda.setStyleSheet("QDateEdit {\n"
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
                                       "     image: url("+self.resourcepath('Images/down.png')+");\n"
                                       " }")
        self.dt_FimVenda.setCalendarPopup(True)
        self.dt_FimVenda.setObjectName("dt_FimVenda")
        self.ct_containerVendas = QtWidgets.QFrame(self.frameMainVendas)
        self.ct_containerVendas.setGeometry(QtCore.QRect(0, 100, 1000, 500))
        self.ct_containerVendas.setStyleSheet("border: none")
        self.ct_containerVendas.setObjectName("ct_containerVendas")
        self.tb_Vendas = QtWidgets.QTableWidget(self.ct_containerVendas)
        self.tb_Vendas.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tb_Vendas.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Vendas.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Vendas.setStyleSheet("QTableView{\n"
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
        self.tb_Vendas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Vendas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Vendas.setAutoScrollMargin(20)
        self.tb_Vendas.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Vendas.setTabKeyNavigation(False)
        self.tb_Vendas.setProperty("showDropIndicator", False)
        self.tb_Vendas.setDragDropOverwriteMode(False)
        self.tb_Vendas.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Vendas.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Vendas.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_Vendas.setShowGrid(False)
        self.tb_Vendas.setCornerButtonEnabled(False)
        self.tb_Vendas.setRowCount(0)
        self.tb_Vendas.setObjectName("tb_Vendas")
        self.tb_Vendas.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Vendas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_Vendas.setHorizontalHeaderItem(6, item)
        self.tb_Vendas.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Vendas.horizontalHeader().setStretchLastSection(True)
        self.tb_Vendas.verticalHeader().setVisible(False)
        self.tb_Vendas.verticalHeader().setCascadingSectionResizes(True)
        self.tb_Vendas.verticalHeader().setDefaultSectionSize(50)
        self.fr_TituloVendas = QtWidgets.QFrame(self.frameMainVendas)
        self.fr_TituloVendas.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloVendas.setStyleSheet("border: none")
        self.fr_TituloVendas.setObjectName("fr_TituloVendas")
        self.lb_tituloVendas = QtWidgets.QLabel(self.fr_TituloVendas)
        self.lb_tituloVendas.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloVendas.setFont(font)
        self.lb_tituloVendas.setStyleSheet("color: #FFF")
        self.lb_tituloVendas.setObjectName("lb_tituloVendas")
        self.ct_containerVendas.raise_()
        self.fr_TopoMenuVendas.raise_()
        self.fr_TituloVendas.raise_()

        self.tradMainVendas(ct_MainVendas)
        QtCore.QMetaObject.connectSlotsByName(ct_MainVendas)

    def tradMainVendas(self, ct_MainVendas):
        _translate = QtCore.QCoreApplication.translate
        ct_MainVendas.setWindowTitle(_translate("ct_MainVendas", "Frame"))
        self.bt_BuscaVendas.setToolTip(_translate("ct_MainVendas", "BUSCAR"))
        self.tx_BuscaVendas.setPlaceholderText(
            _translate("ct_MainVendas", "PROCURAR POR..."))
        self.bt_PrintRelatVendas.setToolTip(
            _translate("ct_MainVendas", "IMPRIMIR"))
        self.dt_InicioVenda.setDisplayFormat(
            _translate("ct_MainVendas", "dd/MM/yyyy"))
        self.lb_FormVenda_21.setText(
            _translate("ct_MainVendas", "DATA ÍNICIO"))
        self.lb_FormVenda_22.setText(_translate("ct_MainVendas", "DATA FIM"))
        self.dt_FimVenda.setDisplayFormat(
            _translate("ct_MainVendas", "dd/MM/yyyy"))
        item = self.tb_Vendas.horizontalHeaderItem(0)
        item.setText(_translate("ct_MainVendas", "ID"))
        item = self.tb_Vendas.horizontalHeaderItem(2)
        item.setText(_translate("ct_MainVendas", "CLIENTE"))
        item = self.tb_Vendas.horizontalHeaderItem(3)
        item.setText(_translate("ct_MainVendas", "EMISSÂO"))
        item = self.tb_Vendas.horizontalHeaderItem(4)
        item.setText(_translate("ct_MainVendas", "ENTREGA"))
        item = self.tb_Vendas.horizontalHeaderItem(5)
        item.setText(_translate("ct_MainVendas", "VALOR"))
        item = self.tb_Vendas.horizontalHeaderItem(6)
        item.setText(_translate("ct_MainVendas", "EDITAR"))
        self.lb_tituloVendas.setText(_translate("ct_MainVendas", "VENDAS"))
