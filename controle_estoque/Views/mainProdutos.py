# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainProdutos.ui'
#
# Created by: PySide2 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_MainProdutos(object):
    def setMainProdutos(self, ct_MainProdutos):
        ct_MainProdutos.setObjectName("ct_MainProdutos")
        ct_MainProdutos.resize(1000, 600)
        ct_MainProdutos.setStyleSheet("border:none")
        self.frameMainProdutos = QtWidgets.QFrame(ct_MainProdutos)
        self.frameMainProdutos.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainProdutos.setObjectName("frameMainProdutos")
        self.fr_TopoMenuProdutos = QtWidgets.QFrame(self.frameMainProdutos)
        self.fr_TopoMenuProdutos.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_TopoMenuProdutos.setStyleSheet("background:#E1DFE0;\n"
                                               "border: none;")
        self.fr_TopoMenuProdutos.setObjectName("fr_TopoMenuProdutos")
        self.bt_BuscaProduto = QtWidgets.QPushButton(self.fr_TopoMenuProdutos)
        self.bt_BuscaProduto.setGeometry(QtCore.QRect(830, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_BuscaProduto.setFont(font)
        self.bt_BuscaProduto.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_BuscaProduto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaProduto.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaProduto.setText("")
        self.bt_BuscaProduto.setObjectName("bt_BuscaProduto")
        self.bt_AddNovoProduto = QtWidgets.QPushButton(
            self.fr_TopoMenuProdutos)
        self.bt_AddNovoProduto.setGeometry(QtCore.QRect(900, 0, 100, 40))
        self.bt_AddNovoProduto.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_AddNovoProduto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddNovoProduto.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_AddNovoProduto.setStyleSheet("QPushButton {\n"
                                             "background-color: #7AB32E;\n"
                                             " }\n"
                                             "QPushButton:hover{\n"
                                             "background-color: #40a286\n"
                                             "}")
        self.bt_AddNovoProduto.setText("")
        self.bt_AddNovoProduto.setObjectName("bt_AddNovoProduto")
        self.tx_BuscaProduto = QtWidgets.QLineEdit(self.fr_TopoMenuProdutos)
        self.tx_BuscaProduto.setGeometry(QtCore.QRect(0, 5, 830, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_BuscaProduto.setFont(font)
        self.tx_BuscaProduto.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_BuscaProduto.setStyleSheet("QLineEdit {\n"
                                           "color: #000\n"
                                           "}\n"
                                           "")
        self.tx_BuscaProduto.setObjectName("tx_BuscaProduto")
        self.bt_PrintRelatProdutos = QtWidgets.QPushButton(
            self.fr_TopoMenuProdutos)
        self.bt_PrintRelatProdutos.setGeometry(QtCore.QRect(870, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_PrintRelatProdutos.setFont(font)
        self.bt_PrintRelatProdutos.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_PrintRelatProdutos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_PrintRelatProdutos.setContextMenuPolicy(
            QtCore.Qt.NoContextMenu)
        self.bt_PrintRelatProdutos.setText("")
        self.bt_PrintRelatProdutos.setObjectName("bt_PrintRelatProdutos")
        self.ct_containerProdutos = QtWidgets.QFrame(self.frameMainProdutos)
        self.ct_containerProdutos.setGeometry(QtCore.QRect(0, 100, 1000, 500))
        self.ct_containerProdutos.setStyleSheet("border: none")
        self.ct_containerProdutos.setObjectName("ct_containerProdutos")
        self.tb_produtos = QtWidgets.QTableWidget(self.ct_containerProdutos)
        self.tb_produtos.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.tb_produtos.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_produtos.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_produtos.setStyleSheet("QTableView{\n"
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
        self.tb_produtos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_produtos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_produtos.setAutoScrollMargin(20)
        self.tb_produtos.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_produtos.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.tb_produtos.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_produtos.setShowGrid(False)
        self.tb_produtos.setGridStyle(QtCore.Qt.NoPen)
        self.tb_produtos.setRowCount(0)
        self.tb_produtos.setObjectName("tb_produtos")
        self.tb_produtos.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(1, item)
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
        self.tb_produtos.setHorizontalHeaderItem(2, item)
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
        self.tb_produtos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter |
                              QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_produtos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter |
                              QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_produtos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter |
                              QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_produtos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter |
                              QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_produtos.setHorizontalHeaderItem(7, item)
        self.tb_produtos.horizontalHeader().setDefaultSectionSize(120)
        self.tb_produtos.horizontalHeader().setHighlightSections(False)
        self.tb_produtos.horizontalHeader().setStretchLastSection(True)
        self.tb_produtos.verticalHeader().setVisible(False)
        self.tb_produtos.verticalHeader().setDefaultSectionSize(40)
        self.fr_TituloProdutos = QtWidgets.QFrame(self.frameMainProdutos)
        self.fr_TituloProdutos.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloProdutos.setStyleSheet("border: none")
        self.fr_TituloProdutos.setObjectName("fr_TituloProdutos")
        self.lb_tituloProdutos = QtWidgets.QLabel(self.fr_TituloProdutos)
        self.lb_tituloProdutos.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloProdutos.setFont(font)
        self.lb_tituloProdutos.setStyleSheet("color: #FFF")
        self.lb_tituloProdutos.setObjectName("lb_tituloProdutos")
        self.ct_containerProdutos.raise_()
        self.fr_TopoMenuProdutos.raise_()
        self.fr_TituloProdutos.raise_()

        self.tradMainProdutos(ct_MainProdutos)
        QtCore.QMetaObject.connectSlotsByName(ct_MainProdutos)

    def tradMainProdutos(self, ct_MainProdutos):
        _translate = QtCore.QCoreApplication.translate
        ct_MainProdutos.setWindowTitle(_translate("ct_MainProdutos", "Frame"))
        self.tx_BuscaProduto.setPlaceholderText(
            _translate("ct_MainProdutos", "PROCURAR POR..."))
        self.bt_PrintRelatProdutos.setToolTip(
            _translate("ct_MainProdutos", "IMPRIMIR"))
        item = self.tb_produtos.horizontalHeaderItem(2)
        item.setText(_translate("ct_MainProdutos", "ID"))
        item = self.tb_produtos.horizontalHeaderItem(3)
        item.setText(_translate("ct_MainProdutos", "Descrição"))
        item = self.tb_produtos.horizontalHeaderItem(4)
        item.setText(_translate("ct_MainProdutos", "Estoque"))
        item = self.tb_produtos.horizontalHeaderItem(5)
        item.setText(_translate("ct_MainProdutos", "Valor Unitário"))
        item = self.tb_produtos.horizontalHeaderItem(6)
        item.setText(_translate("ct_MainProdutos", "Valor Quantidade"))
        item = self.tb_produtos.horizontalHeaderItem(7)
        item.setText(_translate("ct_MainProdutos", "EDITAR"))
        self.lb_tituloProdutos.setText(
            _translate("ct_MainProdutos", "PRODUTOS"))
