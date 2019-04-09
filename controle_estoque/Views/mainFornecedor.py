# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFornecedor.ui',
# licensing of 'mainFornecedor.ui' applies.
#
# Created: Mon Feb 18 09:34:27 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_MainFornecedor(object):
    def setMainFornecedor(self, ct_MainFornecedor):
        ct_MainFornecedor.setObjectName("ct_MainFornecedor")
        ct_MainFornecedor.resize(1000, 600)
        ct_MainFornecedor.setStyleSheet("border:none")
        self.frameMainFornecedor = QtWidgets.QFrame(ct_MainFornecedor)
        self.frameMainFornecedor.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainFornecedor.setObjectName("frameMainFornecedor")
        self.fr_TopoMenuFornecedor = QtWidgets.QFrame(self.frameMainFornecedor)
        self.fr_TopoMenuFornecedor.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_TopoMenuFornecedor.setStyleSheet("background:#E1DFE0;\n"
                                                 "border: none;")
        self.fr_TopoMenuFornecedor.setObjectName("fr_TopoMenuFornecedor")
        self.bt_BuscaFornecedor = QtWidgets.QPushButton(
            self.fr_TopoMenuFornecedor)
        self.bt_BuscaFornecedor.setGeometry(QtCore.QRect(830, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_BuscaFornecedor.setFont(font)
        self.bt_BuscaFornecedor.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_BuscaFornecedor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaFornecedor.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaFornecedor.setText("")
        self.bt_BuscaFornecedor.setObjectName("bt_BuscaFornecedor")
        self.bt_AddNovoFornecedor = QtWidgets.QPushButton(
            self.fr_TopoMenuFornecedor)
        self.bt_AddNovoFornecedor.setGeometry(QtCore.QRect(900, 0, 100, 40))
        self.bt_AddNovoFornecedor.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_AddNovoFornecedor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddNovoFornecedor.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_AddNovoFornecedor.setStyleSheet("QPushButton {\n"
                                                "background-color: #7AB32E;\n"
                                                " }\n"
                                                "QPushButton:hover{\n"
                                                "background-color: #40a286\n"
                                                "}")
        self.bt_AddNovoFornecedor.setText("")
        self.bt_AddNovoFornecedor.setObjectName("bt_AddNovoFornecedor")
        self.tx_BuscaFornecedor = QtWidgets.QLineEdit(
            self.fr_TopoMenuFornecedor)
        self.tx_BuscaFornecedor.setGeometry(QtCore.QRect(0, 5, 830, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_BuscaFornecedor.setFont(font)
        self.tx_BuscaFornecedor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_BuscaFornecedor.setStyleSheet("QLineEdit {\n"
                                              "color: #000\n"
                                              "}\n"
                                              "")
        self.tx_BuscaFornecedor.setObjectName("tx_BuscaFornecedor")
        self.bt_PrintRelatForn = QtWidgets.QPushButton(
            self.fr_TopoMenuFornecedor)
        self.bt_PrintRelatForn.setGeometry(QtCore.QRect(870, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_PrintRelatForn.setFont(font)
        self.bt_PrintRelatForn.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_PrintRelatForn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_PrintRelatForn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_PrintRelatForn.setText("")
        self.bt_PrintRelatForn.setObjectName("bt_PrintRelatForn")
        self.ct_containerFornecedor = QtWidgets.QFrame(
            self.frameMainFornecedor)
        self.ct_containerFornecedor.setGeometry(
            QtCore.QRect(0, 100, 1000, 500))
        self.ct_containerFornecedor.setStyleSheet("border: none")
        self.ct_containerFornecedor.setObjectName("ct_containerFornecedor")
        self.tb_Fornecedor = QtWidgets.QTableWidget(
            self.ct_containerFornecedor)
        self.tb_Fornecedor.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tb_Fornecedor.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tb_Fornecedor.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Fornecedor.setStyleSheet("QTableView{\n"
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
        self.tb_Fornecedor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Fornecedor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Fornecedor.setAutoScrollMargin(20)
        self.tb_Fornecedor.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Fornecedor.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Fornecedor.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Fornecedor.setShowGrid(False)
        self.tb_Fornecedor.setGridStyle(QtCore.Qt.NoPen)
        self.tb_Fornecedor.setWordWrap(False)
        self.tb_Fornecedor.setRowCount(0)
        self.tb_Fornecedor.setObjectName("tb_Fornecedor")
        self.tb_Fornecedor.setColumnCount(7)
        self.tb_Fornecedor.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Fornecedor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Fornecedor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Fornecedor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Fornecedor.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Fornecedor.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Fornecedor.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Fornecedor.setHorizontalHeaderItem(6, item)
        self.tb_Fornecedor.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Fornecedor.horizontalHeader().setHighlightSections(False)
        self.tb_Fornecedor.horizontalHeader().setStretchLastSection(True)
        self.tb_Fornecedor.verticalHeader().setVisible(False)
        self.tb_Fornecedor.verticalHeader().setDefaultSectionSize(40)
        self.fr_TituloFornecedor = QtWidgets.QFrame(self.frameMainFornecedor)
        self.fr_TituloFornecedor.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloFornecedor.setStyleSheet("border: none")
        self.fr_TituloFornecedor.setObjectName("fr_TituloFornecedor")
        self.lb_tituloFornecedor = QtWidgets.QLabel(self.fr_TituloFornecedor)
        self.lb_tituloFornecedor.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.lb_tituloFornecedor.setFont(font)
        self.lb_tituloFornecedor.setStyleSheet("color: #FFF")
        self.lb_tituloFornecedor.setObjectName("lb_tituloFornecedor")

        self.tradmainFornecedor(ct_MainFornecedor)
        QtCore.QMetaObject.connectSlotsByName(ct_MainFornecedor)

    def tradmainFornecedor(self, ct_MainFornecedor):
        ct_MainFornecedor.setWindowTitle(QtWidgets.QApplication.translate(
            "ct_MainFornecedor", "Frame", None, -1))
        self.bt_BuscaFornecedor.setToolTip(
            QtWidgets.QApplication.translate("ct_MainFornecedor", "BUSCAR", None, -1))
        self.tx_BuscaFornecedor.setPlaceholderText(QtWidgets.QApplication.translate(
            "ct_MainFornecedor", "PROCURAR POR...", None, -1))
        self.bt_PrintRelatForn.setToolTip(QtWidgets.QApplication.translate(
            "ct_MainFornecedor", "IMPRIMIR", None, -1))
        self.tb_Fornecedor.horizontalHeaderItem(1).setText(
            QtWidgets.QApplication.translate("ct_MainFornecedor", "COD", None, -1))
        self.tb_Fornecedor.horizontalHeaderItem(2).setText(
            QtWidgets.QApplication.translate("ct_MainFornecedor", "FORNECEDOR", None, -1))
        self.tb_Fornecedor.horizontalHeaderItem(3).setText(
            QtWidgets.QApplication.translate("ct_MainFornecedor", "TELEFONE", None, -1))
        self.tb_Fornecedor.horizontalHeaderItem(4).setText(
            QtWidgets.QApplication.translate("ct_MainFornecedor", "EMAIL", None, -1))
        self.tb_Fornecedor.horizontalHeaderItem(5).setText(
            QtWidgets.QApplication.translate("ct_MainFornecedor", "SITE", None, -1))
        self.tb_Fornecedor.horizontalHeaderItem(6).setText(
            QtWidgets.QApplication.translate("ct_MainFornecedor", "EDITAR", None, -1))
        self.lb_tituloFornecedor.setText(QtWidgets.QApplication.translate(
            "ct_MainFornecedor", "FORNECEDOR", None, -1))
