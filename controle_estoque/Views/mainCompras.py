# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainCompras.ui'
#
# Created by: PySide2 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_MainCompras(object):
    def setMainCompras(self, ct_MainCompras):
        ct_MainCompras.setObjectName("ct_MainCompras")
        ct_MainCompras.resize(1000, 600)
        ct_MainCompras.setStyleSheet("border:none")
        self.frameMainCompras = QtWidgets.QFrame(ct_MainCompras)
        self.frameMainCompras.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainCompras.setObjectName("frameMainCompras")
        self.fr_TopoMenuCompras = QtWidgets.QFrame(self.frameMainCompras)
        self.fr_TopoMenuCompras.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_TopoMenuCompras.setStyleSheet("background:#E1DFE0;\n"
                                              "border: none;")
        self.fr_TopoMenuCompras.setObjectName("fr_TopoMenuCompras")
        self.bt_BuscaCompras = QtWidgets.QPushButton(self.fr_TopoMenuCompras)
        self.bt_BuscaCompras.setGeometry(QtCore.QRect(820, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_BuscaCompras.setFont(font)
        self.bt_BuscaCompras.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_BuscaCompras.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaCompras.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaCompras.setText("")
        self.bt_BuscaCompras.setObjectName("bt_BuscaCompras")
        self.bt_AddNovaCompra = QtWidgets.QPushButton(self.fr_TopoMenuCompras)
        self.bt_AddNovaCompra.setGeometry(QtCore.QRect(900, 0, 100, 40))
        self.bt_AddNovaCompra.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_AddNovaCompra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddNovaCompra.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_AddNovaCompra.setStyleSheet("QPushButton {\n"
                                            "background-color: #7AB32E;\n"
                                            " }\n"
                                            "QPushButton:hover{\n"
                                            "background-color: #40a286\n"
                                            "}")
        self.bt_AddNovaCompra.setText("")
        self.bt_AddNovaCompra.setObjectName("bt_AddNovaCompra")
        self.tx_BuscaCompras = QtWidgets.QLineEdit(self.fr_TopoMenuCompras)
        self.tx_BuscaCompras.setGeometry(QtCore.QRect(0, 5, 500, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_BuscaCompras.setFont(font)
        self.tx_BuscaCompras.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_BuscaCompras.setStyleSheet("QLineEdit {\n"
                                           "color: #000\n"
                                           "}\n"
                                           "")
        self.tx_BuscaCompras.setObjectName("tx_BuscaCompras")
        self.bt_PrintRelatCompras = QtWidgets.QPushButton(
            self.fr_TopoMenuCompras)
        self.bt_PrintRelatCompras.setGeometry(QtCore.QRect(860, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_PrintRelatCompras.setFont(font)
        self.bt_PrintRelatCompras.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_PrintRelatCompras.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_PrintRelatCompras.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_PrintRelatCompras.setText("")
        self.bt_PrintRelatCompras.setObjectName("bt_PrintRelatCompras")
        self.lb_FormVenda_22 = QtWidgets.QLabel(self.fr_TopoMenuCompras)
        self.lb_FormVenda_22.setGeometry(QtCore.QRect(670, 2, 120, 16))
        self.lb_FormVenda_22.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_22.setObjectName("lb_FormVenda_22")
        self.dt_InicioCompra = QtWidgets.QDateEdit(self.fr_TopoMenuCompras)
        self.dt_InicioCompra.setGeometry(QtCore.QRect(520, 16, 140, 20))
        self.dt_InicioCompra.setStyleSheet("QDateEdit {\n"
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
                                           "     image: url("+self.resourcepath(
                                               'Images/down.png')+");\n"
                                           " }")
        self.dt_InicioCompra.setCalendarPopup(True)
        self.dt_InicioCompra.setObjectName("dt_InicioCompra")
        self.lb_FormVenda_21 = QtWidgets.QLabel(self.fr_TopoMenuCompras)
        self.lb_FormVenda_21.setGeometry(QtCore.QRect(520, 2, 120, 16))
        self.lb_FormVenda_21.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_21.setObjectName("lb_FormVenda_21")
        self.dt_FimCompra = QtWidgets.QDateEdit(self.fr_TopoMenuCompras)
        self.dt_FimCompra.setGeometry(QtCore.QRect(670, 16, 140, 20))
        self.dt_FimCompra.setStyleSheet("QDateEdit {\n"
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
                                        "     image: url("+self.resourcepath(
                                            'Images/down.png')+");\n"
                                        " }")
        self.dt_FimCompra.setCalendarPopup(True)
        self.dt_FimCompra.setObjectName("dt_FimCompra")
        self.ct_containerCompras = QtWidgets.QFrame(self.frameMainCompras)
        self.ct_containerCompras.setGeometry(QtCore.QRect(0, 100, 1000, 500))
        self.ct_containerCompras.setStyleSheet("border: none")
        self.ct_containerCompras.setObjectName("ct_containerCompras")
        self.tb_Compras = QtWidgets.QTableWidget(self.ct_containerCompras)
        self.tb_Compras.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tb_Compras.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Compras.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Compras.setStyleSheet("QTableView{\n"
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
        self.tb_Compras.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Compras.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Compras.setAutoScrollMargin(20)
        self.tb_Compras.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Compras.setTabKeyNavigation(False)
        self.tb_Compras.setProperty("showDropIndicator", False)
        self.tb_Compras.setDragDropOverwriteMode(False)
        self.tb_Compras.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Compras.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Compras.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_Compras.setShowGrid(False)
        self.tb_Compras.setCornerButtonEnabled(False)
        self.tb_Compras.setRowCount(0)
        self.tb_Compras.setObjectName("tb_Compras")
        self.tb_Compras.setColumnCount(7)
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
        self.tb_Compras.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Compras.setHorizontalHeaderItem(1, item)
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
        self.tb_Compras.setHorizontalHeaderItem(2, item)
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
        self.tb_Compras.setHorizontalHeaderItem(3, item)
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
        self.tb_Compras.setHorizontalHeaderItem(4, item)
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
        self.tb_Compras.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_Compras.setHorizontalHeaderItem(6, item)
        self.tb_Compras.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Compras.horizontalHeader().setStretchLastSection(True)
        self.tb_Compras.verticalHeader().setVisible(False)
        self.tb_Compras.verticalHeader().setCascadingSectionResizes(True)
        self.tb_Compras.verticalHeader().setDefaultSectionSize(40)
        self.fr_TituloCompras = QtWidgets.QFrame(self.frameMainCompras)
        self.fr_TituloCompras.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloCompras.setStyleSheet("border: none")
        self.fr_TituloCompras.setObjectName("fr_TituloCompras")
        self.lb_tituloCompras = QtWidgets.QLabel(self.fr_TituloCompras)
        self.lb_tituloCompras.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloCompras.setFont(font)
        self.lb_tituloCompras.setStyleSheet("color: #FFF")
        self.lb_tituloCompras.setObjectName("lb_tituloCompras")
        self.ct_containerCompras.raise_()
        self.fr_TopoMenuCompras.raise_()
        self.fr_TituloCompras.raise_()

        self.tradMainCompras(ct_MainCompras)
        QtCore.QMetaObject.connectSlotsByName(ct_MainCompras)

    def tradMainCompras(self, ct_MainCompras):
        _translate = QtCore.QCoreApplication.translate
        ct_MainCompras.setWindowTitle(_translate("ct_MainCompras", "Frame"))
        self.bt_BuscaCompras.setToolTip(_translate("ct_MainCompras", "BUSCAR"))
        self.tx_BuscaCompras.setPlaceholderText(
            _translate("ct_MainCompras", "PROCURAR POR..."))
        self.bt_PrintRelatCompras.setToolTip(
            _translate("ct_MainCompras", "IMPRIMIR"))
        self.lb_FormVenda_22.setText(_translate("ct_MainCompras", "DATA FIM"))
        self.dt_InicioCompra.setDisplayFormat(
            _translate("ct_MainCompras", "dd/MM/yyyy"))
        self.lb_FormVenda_21.setText(
            _translate("ct_MainCompras", "DATA ÍNICIO"))
        self.dt_FimCompra.setDisplayFormat(
            _translate("ct_MainCompras", "dd/MM/yyyy"))
        item = self.tb_Compras.horizontalHeaderItem(0)
        item.setText(_translate("ct_MainCompras", "ID"))
        item = self.tb_Compras.horizontalHeaderItem(2)
        item.setText(_translate("ct_MainCompras", "FORNECEDOR"))
        item = self.tb_Compras.horizontalHeaderItem(3)
        item.setText(_translate("ct_MainCompras", "EMISSÂO"))
        item = self.tb_Compras.horizontalHeaderItem(4)
        item.setText(_translate("ct_MainCompras", "ENTREGA"))
        item = self.tb_Compras.horizontalHeaderItem(5)
        item.setText(_translate("ct_MainCompras", "VALOR"))
        item = self.tb_Compras.horizontalHeaderItem(6)
        item.setText(_translate("ct_MainCompras", "EDITAR"))
        self.lb_tituloCompras.setText(_translate("ct_MainCompras", "Compras"))
