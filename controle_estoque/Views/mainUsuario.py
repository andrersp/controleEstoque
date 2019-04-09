# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUsuario.ui',
# licensing of 'mainUsuario.ui' applies.
#
# Created: Fri Mar 22 13:47:16 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_Usuario(object):
    def setMainUsuario(self, ct_Usuario):
        ct_Usuario.setObjectName("ct_Usuario")
        ct_Usuario.resize(1000, 500)
        self.fr_Usurio = QtWidgets.QFrame(ct_Usuario)
        self.fr_Usurio.setGeometry(QtCore.QRect(0, 0, 1000, 5000))
        self.fr_Usurio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Usurio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Usurio.setObjectName("fr_Usurio")
        self.tb_Usuario = QtWidgets.QTableWidget(self.fr_Usurio)
        self.tb_Usuario.setGeometry(QtCore.QRect(0, 40, 1000, 455))
        self.tb_Usuario.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tb_Usuario.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Usuario.setStyleSheet("QTableView{\n"
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
        self.tb_Usuario.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Usuario.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Usuario.setAutoScrollMargin(20)
        self.tb_Usuario.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Usuario.setTabKeyNavigation(False)
        self.tb_Usuario.setProperty("showDropIndicator", False)
        self.tb_Usuario.setDragDropOverwriteMode(False)
        self.tb_Usuario.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Usuario.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Usuario.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_Usuario.setShowGrid(False)
        self.tb_Usuario.setCornerButtonEnabled(False)
        self.tb_Usuario.setRowCount(0)
        self.tb_Usuario.setObjectName("tb_Usuario")
        self.tb_Usuario.setColumnCount(6)
        self.tb_Usuario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Usuario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tb_Usuario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tb_Usuario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tb_Usuario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.tb_Usuario.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Usuario.setHorizontalHeaderItem(5, item)
        self.tb_Usuario.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Usuario.horizontalHeader().setStretchLastSection(True)
        self.tb_Usuario.verticalHeader().setVisible(False)
        self.tb_Usuario.verticalHeader().setCascadingSectionResizes(True)
        self.tb_Usuario.verticalHeader().setDefaultSectionSize(50)
        self.fr_TopoUsuarios = QtWidgets.QFrame(self.fr_Usurio)
        self.fr_TopoUsuarios.setGeometry(QtCore.QRect(0, 0, 1000, 40))
        self.fr_TopoUsuarios.setStyleSheet("background:#E1DFE0;\n"
                                           "border: none;")
        self.fr_TopoUsuarios.setObjectName("fr_TopoUsuarios")
        self.bt_BuscaUsurio = QtWidgets.QPushButton(self.fr_TopoUsuarios)
        self.bt_BuscaUsurio.setGeometry(QtCore.QRect(830, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_BuscaUsurio.setFont(font)
        self.bt_BuscaUsurio.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_BuscaUsurio.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaUsurio.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaUsurio.setText("")
        self.bt_BuscaUsurio.setObjectName("bt_BuscaUsurio")
        self.bt_AddNovoUsuario = QtWidgets.QPushButton(self.fr_TopoUsuarios)
        self.bt_AddNovoUsuario.setGeometry(QtCore.QRect(900, 0, 100, 40))
        self.bt_AddNovoUsuario.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_AddNovoUsuario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddNovoUsuario.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_AddNovoUsuario.setStyleSheet("QPushButton {\n"
                                             "background-color: #7AB32E;\n"
                                             " }\n"
                                             "QPushButton:hover{\n"
                                             "background-color: #40a286\n"
                                             "}")
        self.bt_AddNovoUsuario.setText("")
        self.bt_AddNovoUsuario.setIconSize(QtCore.QSize(75, 35))
        self.bt_AddNovoUsuario.setObjectName("bt_AddNovoUsuario")
        self.tx_BuscarUsuario = QtWidgets.QLineEdit(self.fr_TopoUsuarios)
        self.tx_BuscarUsuario.setGeometry(QtCore.QRect(0, 5, 830, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_BuscarUsuario.setFont(font)
        self.tx_BuscarUsuario.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_BuscarUsuario.setStyleSheet("QLineEdit {\n"
                                            "color: #000\n"
                                            "}\n"
                                            "")
        self.tx_BuscarUsuario.setObjectName("tx_BuscarUsuario")
        self.bt_PrintRelatUsuario = QtWidgets.QPushButton(self.fr_TopoUsuarios)
        self.bt_PrintRelatUsuario.setGeometry(QtCore.QRect(870, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_PrintRelatUsuario.setFont(font)
        self.bt_PrintRelatUsuario.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_PrintRelatUsuario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_PrintRelatUsuario.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_PrintRelatUsuario.setText("")
        self.bt_PrintRelatUsuario.setObjectName("bt_PrintRelatUsuario")

        self.tradMainUsuario(ct_Usuario)
        QtCore.QMetaObject.connectSlotsByName(ct_Usuario)

    def tradMainUsuario(self, ct_Usuario):
        ct_Usuario.setWindowTitle(QtWidgets.QApplication.translate(
            "ct_Usuario", "Frame", None, -1))
        self.tb_Usuario.horizontalHeaderItem(0).setText(
            QtWidgets.QApplication.translate("ct_Usuario", "ID", None, -1))
        self.tb_Usuario.horizontalHeaderItem(1).setText(
            QtWidgets.QApplication.translate("ct_Usuario", "NOME", None, -1))
        self.tb_Usuario.horizontalHeaderItem(2).setText(
            QtWidgets.QApplication.translate("ct_Usuario", "TELEFONE", None, -1))
        self.tb_Usuario.horizontalHeaderItem(3).setText(
            QtWidgets.QApplication.translate("ct_Usuario", "E-MAIL", None, -1))
        self.tb_Usuario.horizontalHeaderItem(4).setText(
            QtWidgets.QApplication.translate("ct_Usuario", "NIVEL / STATUS", None, -1))
        self.tb_Usuario.horizontalHeaderItem(5).setText(
            QtWidgets.QApplication.translate("ct_Usuario", "EDITAR", None, -1))
        self.bt_BuscaUsurio.setToolTip(
            QtWidgets.QApplication.translate("ct_Usuario", "BUSCAR", None, -1))
        self.tx_BuscarUsuario.setPlaceholderText(
            QtWidgets.QApplication.translate("ct_Usuario", "PROCURAR POR...", None, -1))
        self.bt_PrintRelatUsuario.setToolTip(
            QtWidgets.QApplication.translate("ct_Usuario", "IMPRIMIR", None, -1))
