# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainClientes.ui'
#
# Created by: PySide2 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_MainClientes(object):
    def setMainClientes(self, ct_MainClientes):
        ct_MainClientes.setObjectName("ct_MainClientes")
        ct_MainClientes.resize(1000, 600)
        ct_MainClientes.setStyleSheet("border:none")
        self.frameMainClientes = QtWidgets.QFrame(ct_MainClientes)
        self.frameMainClientes.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainClientes.setObjectName("frameMainClientes")
        self.fr_TopoMenuClientes = QtWidgets.QFrame(self.frameMainClientes)
        self.fr_TopoMenuClientes.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_TopoMenuClientes.setStyleSheet("background:#E1DFE0;\n"
                                               "border: none;")
        self.fr_TopoMenuClientes.setObjectName("fr_TopoMenuClientes")
        self.bt_BuscaClientes = QtWidgets.QPushButton(self.fr_TopoMenuClientes)
        self.bt_BuscaClientes.setGeometry(QtCore.QRect(830, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_BuscaClientes.setFont(font)
        self.bt_BuscaClientes.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_BuscaClientes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaClientes.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaClientes.setText("")
        self.bt_BuscaClientes.setObjectName("bt_BuscaClientes")
        self.bt_AddNovoClientes = QtWidgets.QPushButton(
            self.fr_TopoMenuClientes)
        self.bt_AddNovoClientes.setGeometry(QtCore.QRect(900, 0, 100, 40))
        self.bt_AddNovoClientes.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_AddNovoClientes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddNovoClientes.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_AddNovoClientes.setStyleSheet("QPushButton {\n"
                                              "background-color: #7AB32E;\n"
                                              " }\n"
                                              "QPushButton:hover{\n"
                                              "background-color: #40a286\n"
                                              "}")
        self.bt_AddNovoClientes.setText("")
        self.bt_AddNovoClientes.setIconSize(QtCore.QSize(75, 35))
        self.bt_AddNovoClientes.setObjectName("bt_AddNovoClientes")
        self.tx_BuscaClientes = QtWidgets.QLineEdit(self.fr_TopoMenuClientes)
        self.tx_BuscaClientes.setGeometry(QtCore.QRect(0, 5, 830, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_BuscaClientes.setFont(font)
        self.tx_BuscaClientes.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_BuscaClientes.setStyleSheet("QLineEdit {\n"
                                            "color: #000\n"
                                            "}\n"
                                            "")
        self.tx_BuscaClientes.setObjectName("tx_BuscaClientes")
        self.bt_PrintRelatCliente = QtWidgets.QPushButton(
            self.fr_TopoMenuClientes)
        self.bt_PrintRelatCliente.setGeometry(QtCore.QRect(870, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_PrintRelatCliente.setFont(font)
        self.bt_PrintRelatCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_PrintRelatCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_PrintRelatCliente.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_PrintRelatCliente.setText("")
        self.bt_PrintRelatCliente.setObjectName("bt_PrintRelatCliente")
        self.ct_containerClientes = QtWidgets.QFrame(self.frameMainClientes)
        self.ct_containerClientes.setGeometry(QtCore.QRect(0, 100, 1000, 500))
        self.ct_containerClientes.setStyleSheet("border: none")
        self.ct_containerClientes.setObjectName("ct_containerClientes")
        self.tb_Clientes = QtWidgets.QTableWidget(self.ct_containerClientes)
        self.tb_Clientes.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tb_Clientes.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Clientes.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Clientes.setStyleSheet("QTableView{\n"
                                       "color: #797979;\n"
                                       "font-weight: bold;\n"
                                       "font-size: 13px;\n"
                                       "background: #FFF;\n"
                                       "padding: 0 0 0 5px;\n"
                                       "}\n"
                                       "QHeaderView:section{\n"
                                       "background: #FFF;\n"
                                       "padding: 5px 0 ;\n"
                                       "font-size: 12px;\n"
                                       "font-family: \"Arial\";\n"
                                       "font-weight: bold;\n"
                                       "color: #797979;\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid #CCC;\n"
                                       "text-transform: uppercase\n"
                                       "}\n"
                                       "QTableView::item {\n"
                                       "border-bottom: 2px solid #CCC;\n"
                                       "padding: 2px;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.tb_Clientes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Clientes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Clientes.setAutoScrollMargin(20)
        self.tb_Clientes.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Clientes.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Clientes.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Clientes.setShowGrid(False)
        self.tb_Clientes.setGridStyle(QtCore.Qt.NoPen)
        self.tb_Clientes.setWordWrap(False)
        self.tb_Clientes.setRowCount(0)
        self.tb_Clientes.setObjectName("tb_Clientes")
        self.tb_Clientes.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Clientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter |
                              QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
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
        self.tb_Clientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Clientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Clientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Clientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter |
                              QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_Clientes.setHorizontalHeaderItem(5, item)
        self.tb_Clientes.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Clientes.horizontalHeader().setHighlightSections(False)
        self.tb_Clientes.horizontalHeader().setStretchLastSection(True)
        self.tb_Clientes.verticalHeader().setVisible(False)
        self.tb_Clientes.verticalHeader().setDefaultSectionSize(50)
        self.tb_Clientes.verticalHeader().setMinimumSectionSize(20)
        self.fr_TituloClientes = QtWidgets.QFrame(self.frameMainClientes)
        self.fr_TituloClientes.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloClientes.setStyleSheet("border: none")
        self.fr_TituloClientes.setObjectName("fr_TituloClientes")
        self.lb_tituloClientes = QtWidgets.QLabel(self.fr_TituloClientes)
        self.lb_tituloClientes.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes.setFont(font)
        self.lb_tituloClientes.setStyleSheet("color: #FFF")
        self.lb_tituloClientes.setObjectName("lb_tituloClientes")
        self.ct_containerClientes.raise_()
        self.fr_TopoMenuClientes.raise_()
        self.fr_TituloClientes.raise_()

        self.tradMainClientes(ct_MainClientes)
        QtCore.QMetaObject.connectSlotsByName(ct_MainClientes)

    def tradMainClientes(self, ct_MainClientes):
        _translate = QtCore.QCoreApplication.translate
        ct_MainClientes.setWindowTitle(_translate("ct_MainClientes", "Frame"))
        self.bt_BuscaClientes.setToolTip(
            _translate("ct_MainClientes", "BUSCAR"))
        self.tx_BuscaClientes.setPlaceholderText(
            _translate("ct_MainClientes", "PROCURAR POR..."))
        self.bt_PrintRelatCliente.setToolTip(
            _translate("ct_MainClientes", "IMPRIMIR"))
        item = self.tb_Clientes.horizontalHeaderItem(1)
        item.setText(_translate("ct_MainClientes", "ID"))
        item = self.tb_Clientes.horizontalHeaderItem(2)
        item.setText(_translate("ct_MainClientes", "NOME"))
        item = self.tb_Clientes.horizontalHeaderItem(3)
        item.setText(_translate("ct_MainClientes", "EMAIL"))
        item = self.tb_Clientes.horizontalHeaderItem(4)
        item.setText(_translate("ct_MainClientes", "TELEFONE"))
        item = self.tb_Clientes.horizontalHeaderItem(5)
        item.setText(_translate("ct_MainClientes", "EDITAR"))
        self.lb_tituloClientes.setText(
            _translate("ct_MainClientes", "CLIENTES"))
