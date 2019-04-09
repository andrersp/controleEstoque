# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formProdutos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_FormProdutos(object):

    def setFormProdutos(self, ct_FormProdutos):
        ct_FormProdutos.setObjectName("ct_FormProdutos")
        ct_FormProdutos.resize(1000, 500)
        ct_FormProdutos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormProdutos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormProdutos = QtWidgets.QFrame(ct_FormProdutos)
        self.fr_FormProdutos.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormProdutos.setStyleSheet("background: #FFF;\n"
                                           "border: none")
        self.fr_FormProdutos.setObjectName("fr_FormProdutos")
        self.lb_FormProdutos = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(200, 10, 780, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
                                           "font-size: 14px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "\n"
                                           "border-bottom: 2px solid #A2A2A2\n"
                                           "}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.tx_idProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_idProduto.setEnabled(False)
        self.tx_idProduto.setGeometry(QtCore.QRect(20, 85, 150, 25))
        self.tx_idProduto.setStyleSheet("QLineEdit{\n"
                                        "background: #CFCFCF;\n"
                                        "border: 1px solid #A2A2A2;\n"
                                        "color: #000;\n"
                                        "font-size: 14px;\n"
                                        "font-family: \"Arial\";\n"
                                        "font-weight: bold;\n"
                                        "\n"
                                        "}")
        self.tx_idProduto.setText("")
        self.tx_idProduto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_idProduto.setObjectName("tx_idProduto")
        self.lb_FotoProduto = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FotoProduto.setGeometry(QtCore.QRect(20, 110, 150, 150))
        self.lb_FotoProduto.setStyleSheet("border: 1px solid #A2A2A2;\n"
                                          "background: url(\'Images/icon/Photo.svg\') center no-repeat \n"
                                          "")
        self.lb_FotoProduto.setText("")
        self.lb_FotoProduto.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FotoProduto.setObjectName("lb_FotoProduto")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(200, 60, 150, 20))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
                                             "font-size: 12px;\n"
                                             "font-family: \"Arial Unicode MS\";\n"
                                             "font-weight: bold;\n"
                                             "color: #797979\n"
                                             "}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_DescricaoProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_DescricaoProduto.setGeometry(QtCore.QRect(200, 85, 450, 25))
        self.tx_DescricaoProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_DescricaoProduto.setStyleSheet("QLineEdit{\n"
                                               "background: #CFCFCF;\n"
                                               "border-radius: 2px;\n"
                                               "color: #000;\n"
                                               "font: 13px \"Arial\" ;\n"
                                               "text-transform: uppercase;\n"
                                               "}\n"
                                               "QLineEdit:Focus {\n"
                                               "border: 1px solid red;\n"
                                               "}")
        self.tx_DescricaoProduto.setObjectName("tx_DescricaoProduto")
        self.lb_FormProdutos_3 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_3.setGeometry(QtCore.QRect(200, 120, 215, 20))
        self.lb_FormProdutos_3.setStyleSheet("QLabel{\n"
                                             "font-size: 12px;\n"
                                             "font-family: \"Arial Unicode MS\";\n"
                                             "font-weight: bold;\n"
                                             "color: #797979\n"
                                             "}")
        self.lb_FormProdutos_3.setObjectName("lb_FormProdutos_3")
        self.cb_CategoriaProduto = QtWidgets.QComboBox(self.fr_FormProdutos)
        self.cb_CategoriaProduto.setGeometry(QtCore.QRect(200, 145, 190, 25))
        self.cb_CategoriaProduto.setStyleSheet("QComboBox{\n"
                                               "background: #CFCFCF;\n"
                                               "border-radius: 2px;\n"
                                               "color: #000;\n"
                                               "font: 13px \"Arial\" ;\n"
                                               "text-transform: uppercase\n"
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
                                               "     image: url("+self.resourcepath('Images/down.png')+");\n"
                                               " }\n"
                                               "")
        self.cb_CategoriaProduto.setObjectName("cb_CategoriaProduto")
        self.cb_CategoriaProduto.addItem("")
        self.bt_AddCategoriaProduto = QtWidgets.QPushButton(
            self.fr_FormProdutos)
        self.bt_AddCategoriaProduto.setGeometry(QtCore.QRect(390, 145, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
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
        self.lb_FormProdutos_4 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_4.setGeometry(QtCore.QRect(435, 120, 215, 20))
        self.lb_FormProdutos_4.setStyleSheet("QLabel{\n"
                                             "font-size: 12px;\n"
                                             "font-family: \"Arial Unicode MS\";\n"
                                             "font-weight: bold;\n"
                                             "color: #797979\n"
                                             "}")
        self.lb_FormProdutos_4.setObjectName("lb_FormProdutos_4")
        self.cb_MarcaProduto = QtWidgets.QComboBox(self.fr_FormProdutos)
        self.cb_MarcaProduto.setGeometry(QtCore.QRect(435, 145, 190, 25))
        self.cb_MarcaProduto.setStyleSheet("QComboBox{\n"
                                           "background: #CFCFCF;\n"
                                           "border-radius: 2px;\n"
                                           "color: #000;\n"
                                           "font: 13px \"Arial\" ;\n"
                                           "text-transform: uppercase\n"
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
                                           "     image: url("+self.resourcepath('Images/down.png')+");\n"
                                           " }\n"
                                           "")
        self.cb_MarcaProduto.setInsertPolicy(
            QtWidgets.QComboBox.InsertAtBottom)
        self.cb_MarcaProduto.setFrame(False)
        self.cb_MarcaProduto.setObjectName("cb_MarcaProduto")
        self.cb_MarcaProduto.addItem("")
        self.bt_AddMarcaProduto = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_AddMarcaProduto.setGeometry(QtCore.QRect(625, 145, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_AddMarcaProduto.setFont(font)
        self.bt_AddMarcaProduto.setStyleSheet("QPushButton{\n"
                                              "background: #7AB32E;\n"
                                              "color: #FFF\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background-color: #40a286\n"
                                              "}")
        self.bt_AddMarcaProduto.setText("")
        self.bt_AddMarcaProduto.setObjectName("bt_AddMarcaProduto")
        self.lb_FormProdutos_5 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_5.setGeometry(QtCore.QRect(200, 180, 215, 20))
        self.lb_FormProdutos_5.setStyleSheet("QLabel{\n"
                                             "font-size: 12px;\n"
                                             "font-family: \"Arial Unicode MS\";\n"
                                             "font-weight: bold;\n"
                                             "color: #797979\n"
                                             "}")
        self.lb_FormProdutos_5.setObjectName("lb_FormProdutos_5")
        self.lb_FormProdutos_6 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(435, 180, 215, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
                                             "font-size: 12px;\n"
                                             "font-family: \"Arial Unicode MS\";\n"
                                             "font-weight: bold;\n"
                                             "color: #797979\n"
                                             "}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_EstoqueMinimoProduto = QtWidgets.QLineEdit(
            self.fr_FormProdutos)
        self.tx_EstoqueMinimoProduto.setGeometry(
            QtCore.QRect(200, 205, 215, 25))
        self.tx_EstoqueMinimoProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_EstoqueMinimoProduto.setStyleSheet("QLineEdit{\n"
                                                   "background: #CFCFCF;\n"
                                                   "border-radius: 2px;\n"
                                                   "color: #000;\n"
                                                   "font: 13px \"Arial\" \n"
                                                   "}\n"
                                                   "QLineEdit:Focus {\n"
                                                   "border: 1px solid red;\n"
                                                   "}")
        self.tx_EstoqueMinimoProduto.setText("")
        self.tx_EstoqueMinimoProduto.setPlaceholderText("")
        self.tx_EstoqueMinimoProduto.setObjectName("tx_EstoqueMinimoProduto")
        self.tx_EstoqueMaximoProduto = QtWidgets.QLineEdit(
            self.fr_FormProdutos)
        self.tx_EstoqueMaximoProduto.setGeometry(
            QtCore.QRect(435, 205, 215, 25))
        self.tx_EstoqueMaximoProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_EstoqueMaximoProduto.setStyleSheet("QLineEdit{\n"
                                                   "background: #CFCFCF;\n"
                                                   "border-radius: 2px;\n"
                                                   "color: #000;\n"
                                                   "font: 13px \"Arial\" \n"
                                                   "}\n"
                                                   "QLineEdit:Focus {\n"
                                                   "border: 1px solid red;\n"
                                                   "}")
        self.tx_EstoqueMaximoProduto.setPlaceholderText("")
        self.tx_EstoqueMaximoProduto.setObjectName("tx_EstoqueMaximoProduto")
        self.tx_ObsProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_ObsProduto.setGeometry(QtCore.QRect(200, 260, 450, 25))
        self.tx_ObsProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ObsProduto.setStyleSheet("QLineEdit{\n"
                                         "background: #CFCFCF;\n"
                                         "border-radius: 2px;\n"
                                         "color: #000;\n"
                                         "font: 13px \"Arial\" ;\n"
                                         "text-transform: uppercase\n"
                                         "}\n"
                                         "QLineEdit:Focus {\n"
                                         "border: 1px solid red;\n"
                                         "}")
        self.tx_ObsProduto.setObjectName("tx_ObsProduto")
        self.lb_FormProdutos_7 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_7.setGeometry(QtCore.QRect(200, 235, 150, 20))
        self.lb_FormProdutos_7.setStyleSheet("QLabel{\n"
                                             "font-size: 12px;\n"
                                             "font-family: \"Arial Unicode MS\";\n"
                                             "font-weight: bold;\n"
                                             "color: #797979\n"
                                             "}")
        self.lb_FormProdutos_7.setObjectName("lb_FormProdutos_7")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(20, 290, 960, 30))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
                                             "font-size: 14px;\n"
                                             "font-family: \"Arial\";\n"
                                             "font-weight: normal;\n"
                                             "\n"
                                             "border-bottom: 2px solid #A2A2A2;\n"
                                             "color: #797979\n"
                                             "}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tb_HistoricoComprasProduto = QtWidgets.QTableWidget(
            self.fr_FormProdutos)
        self.tb_HistoricoComprasProduto.setGeometry(
            QtCore.QRect(670, 85, 310, 200))
        self.tb_HistoricoComprasProduto.setStyleSheet("QTableView{\n"
                                                      "color: #797979;\n"
                                                      "font-family: \"Arial\";\n"
                                                      "font-weight: bold;\n"
                                                      "font-size: 12px;\n"
                                                      "background: #FFF;\n"
                                                      "}\n"
                                                      "QHeaderView:section{\n"
                                                      "background: #FFF;\n"
                                                      "font-size: 12px;\n"
                                                      "font-family: \"Arial\";\n"
                                                      "font-weight: bold;\n"
                                                      "color: #797979;\n"
                                                      "border: none;\n"
                                                      "border-bottom: 1px solid #CCC;\n"
                                                      "height: 25px;\n"
                                                      "}\n"
                                                      "")
        self.tb_HistoricoComprasProduto.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_HistoricoComprasProduto.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_HistoricoComprasProduto.setShowGrid(False)
        self.tb_HistoricoComprasProduto.setObjectName(
            "tb_HistoricoComprasProduto")
        self.tb_HistoricoComprasProduto.setColumnCount(3)
        self.tb_HistoricoComprasProduto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.tb_HistoricoComprasProduto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.tb_HistoricoComprasProduto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.tb_HistoricoComprasProduto.setHorizontalHeaderItem(2, item)
        self.tb_HistoricoComprasProduto.verticalHeader().setVisible(False)
        self.tb_HistoricoComprasProduto.verticalHeader().setHighlightSections(False)
        self.lb_FormProdutos_9 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_9.setGeometry(QtCore.QRect(670, 60, 310, 20))
        self.lb_FormProdutos_9.setStyleSheet("QLabel{\n"
                                             "font-size: 12px;\n"
                                             "font-family: \"Arial Unicode MS\";\n"
                                             "font-weight: bold;\n"
                                             "color: #797979\n"
                                             "}")
        self.lb_FormProdutos_9.setObjectName("lb_FormProdutos_9")
        self.tx_ValorCompraProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_ValorCompraProduto.setGeometry(QtCore.QRect(20, 360, 150, 30))
        self.tx_ValorCompraProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorCompraProduto.setStyleSheet("QLineEdit{\n"
                                                 "background: #CFCFCF;\n"
                                                 "border-radius: 2px;\n"
                                                 "color: #000;\n"
                                                 "font: 14px \"Arial\" ;\n"
                                                 "text-transform: uppercase;\n"
                                                 "}\n"
                                                 "QLineEdit:Focus {\n"
                                                 "border: 1px solid red;\n"
                                                 "}")
        self.tx_ValorCompraProduto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_ValorCompraProduto.setObjectName("tx_ValorCompraProduto")
        self.lb_FormProdutos_10 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(20, 335, 50, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
                                              "font-size: 12px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: bold;\n"
                                              "color: #797979\n"
                                              "}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.lb_FormProdutos_11 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_11.setGeometry(QtCore.QRect(80, 335, 90, 20))
        self.lb_FormProdutos_11.setStyleSheet("QLabel{\n"
                                              "font-size: 9px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: bold;\n"
                                              "color: #797979;\n"
                                              "\n"
                                              "}")
        self.lb_FormProdutos_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FormProdutos_11.setObjectName("lb_FormProdutos_11")
        self.tx_ValorUnitarioProduto = QtWidgets.QLineEdit(
            self.fr_FormProdutos)
        self.tx_ValorUnitarioProduto.setGeometry(
            QtCore.QRect(200, 360, 150, 30))
        self.tx_ValorUnitarioProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorUnitarioProduto.setStyleSheet("QLineEdit{\n"
                                                   "background: #CFCFCF;\n"
                                                   "border-radius: 2px;\n"
                                                   "color: #000;\n"
                                                   "font: 14px \"Arial\" ;\n"
                                                   "text-transform: uppercase;\n"
                                                   "}\n"
                                                   "QLineEdit:Focus {\n"
                                                   "border: 1px solid red;\n"
                                                   "}")
        self.tx_ValorUnitarioProduto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_ValorUnitarioProduto.setObjectName("tx_ValorUnitarioProduto")
        self.lb_FormProdutos_12 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(200, 335, 150, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
                                              "font-size: 12px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: bold;\n"
                                              "color: #797979\n"
                                              "}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.lb_FormProdutos_13 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_13.setGeometry(QtCore.QRect(200, 395, 150, 20))
        self.lb_FormProdutos_13.setStyleSheet("QLabel{\n"
                                              "font-size: 12px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: bold;\n"
                                              "color: #797979\n"
                                              "}")
        self.lb_FormProdutos_13.setObjectName("lb_FormProdutos_13")
        self.tx_ValorAtacadoProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_ValorAtacadoProduto.setGeometry(
            QtCore.QRect(200, 420, 150, 30))
        self.tx_ValorAtacadoProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorAtacadoProduto.setStyleSheet("QLineEdit{\n"
                                                  "background: #CFCFCF;\n"
                                                  "border-radius: 2px;\n"
                                                  "color: #000;\n"
                                                  "font: 14px \"Arial\" ;\n"
                                                  "text-transform: uppercase;\n"
                                                  "}\n"
                                                  "QLineEdit:Focus {\n"
                                                  "border: 1px solid red;\n"
                                                  "}")
        self.tx_ValorAtacadoProduto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_ValorAtacadoProduto.setObjectName("tx_ValorAtacadoProduto")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_FormProdutos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background:#E1DFE0;\n"
                                                 "border: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")
        self.bt_CancelarProdutos = QtWidgets.QPushButton(
            self.fr_BotoesFormProdutos)
        self.bt_CancelarProdutos.setGeometry(QtCore.QRect(880, 0, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_CancelarProdutos.setFont(font)
        self.bt_CancelarProdutos.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_CancelarProdutos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_CancelarProdutos.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_CancelarProdutos.setStyleSheet("QPushButton {\n"
                                               "background-color: #1E87F0;\n"
                                               "color: #FFF\n"
                                               " }\n"
                                               "QPushButton:hover{\n"
                                               "background-color: #40a286\n"
                                               "}")
        self.bt_CancelarProdutos.setIconSize(QtCore.QSize(75, 35))
        self.bt_CancelarProdutos.setObjectName("bt_CancelarProdutos")
        self.bt_SalvarProdutos = QtWidgets.QPushButton(
            self.fr_BotoesFormProdutos)
        self.bt_SalvarProdutos.setGeometry(QtCore.QRect(750, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_SalvarProdutos.setFont(font)
        self.bt_SalvarProdutos.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_SalvarProdutos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_SalvarProdutos.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_SalvarProdutos.setStyleSheet("QPushButton {\n"
                                             "background-color: #7AB32E;\n"
                                             "color: #FFF\n"
                                             " }\n"
                                             "QPushButton:hover{\n"
                                             "background-color: #40a286\n"
                                             "}")
        self.bt_SalvarProdutos.setIconSize(QtCore.QSize(75, 35))
        self.bt_SalvarProdutos.setObjectName("bt_SalvarProdutos")
        self.lb_qtdeMin = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_qtdeMin.setGeometry(QtCore.QRect(890, 350, 40, 35))
        self.lb_qtdeMin.setText("")
        self.lb_qtdeMin.setObjectName("lb_qtdeMin")
        self.tx_MinimoAtacado = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_MinimoAtacado.setGeometry(QtCore.QRect(860, 405, 100, 30))
        self.tx_MinimoAtacado.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_MinimoAtacado.setStyleSheet("QLineEdit{\n"
                                            "background: #CFCFCF;\n"
                                            "border-radius: 2px;\n"
                                            "color: #000;\n"
                                            "font: 12px \"Arial\" ;\n"
                                            "text-transform: uppercase\n"
                                            "}\n"
                                            "QLineEdit:Focus {\n"
                                            "border: 1px solid red;\n"
                                            "}")
        self.tx_MinimoAtacado.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_MinimoAtacado.setPlaceholderText("")
        self.tx_MinimoAtacado.setObjectName("tx_MinimoAtacado")
        self.lb_FormProdutos_14 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(840, 385, 140, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
                                              "font-size: 10px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: normal;\n"
                                              "color: red\n"
                                              "}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")
        self.lb_FormProdutos_15 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_15.setGeometry(QtCore.QRect(445, 360, 150, 20))
        self.lb_FormProdutos_15.setStyleSheet("QLabel{\n"
                                              "font-size: 12px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: bold;\n"
                                              "color: #000\n"
                                              "}")
        self.lb_FormProdutos_15.setObjectName("lb_FormProdutos_15")
        self.tx_PorcentagemVarejo = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_PorcentagemVarejo.setGeometry(QtCore.QRect(360, 360, 60, 30))
        self.tx_PorcentagemVarejo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_PorcentagemVarejo.setStyleSheet("QLineEdit{\n"
                                                "background: #FFF;\n"
                                                "border-radius: 2px;\n"
                                                "color: #7AB32E;\n"
                                                "font: 20px \"Arial\" ;\n"
                                                "font-weight: bold\n"
                                                "}\n"
                                                "QLineEdit:Focus {\n"
                                                "border: 1px solid red;\n"
                                                "}")
        self.tx_PorcentagemVarejo.setText("")
        self.tx_PorcentagemVarejo.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_PorcentagemVarejo.setReadOnly(True)
        self.tx_PorcentagemVarejo.setObjectName("tx_PorcentagemVarejo")
        self.lb_FormProdutos_17 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_17.setGeometry(QtCore.QRect(445, 380, 150, 10))
        self.lb_FormProdutos_17.setStyleSheet("QLabel{\n"
                                              "font-size: 8px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: normal;\n"
                                              "color: #000\n"
                                              "}")
        self.lb_FormProdutos_17.setObjectName("lb_FormProdutos_17")
        self.lb_porcVar = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_porcVar.setGeometry(QtCore.QRect(420, 360, 20, 30))
        self.lb_porcVar.setStyleSheet("QLabel{\n"
                                      "font-size: 20px;\n"
                                      "font-family: \"Arial Unicode MS\";\n"
                                      "font-weight: bold;\n"
                                      "color: #7AB32E\n"
                                      "}")
        self.lb_porcVar.setObjectName("lb_porcVar")
        self.lb_FormProdutos_16 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_16.setGeometry(QtCore.QRect(445, 420, 150, 20))
        self.lb_FormProdutos_16.setStyleSheet("QLabel{\n"
                                              "font-size: 12px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: bold;\n"
                                              "color: #000\n"
                                              "}")
        self.lb_FormProdutos_16.setObjectName("lb_FormProdutos_16")
        self.lb_FormProdutos_19 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_19.setGeometry(QtCore.QRect(445, 440, 150, 10))
        self.lb_FormProdutos_19.setStyleSheet("QLabel{\n"
                                              "font-size: 8px;\n"
                                              "font-family: \"Arial Unicode MS\";\n"
                                              "font-weight: normal;\n"
                                              "color: #000\n"
                                              "}")
        self.lb_FormProdutos_19.setObjectName("lb_FormProdutos_19")
        self.lb_porcAtac = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_porcAtac.setGeometry(QtCore.QRect(420, 420, 20, 30))
        self.lb_porcAtac.setStyleSheet("QLabel{\n"
                                       "font-size: 20px;\n"
                                       "font-family: \"Arial Unicode MS\";\n"
                                       "font-weight: bold;\n"
                                       "color: #7AB32E\n"
                                       "}")
        self.lb_porcAtac.setObjectName("lb_porcAtac")
        self.tx_PorcentagemAtacado = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_PorcentagemAtacado.setGeometry(QtCore.QRect(360, 420, 60, 30))
        self.tx_PorcentagemAtacado.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_PorcentagemAtacado.setStyleSheet("QLineEdit{\n"
                                                 "background: #FFF;\n"
                                                 "border-radius: 2px;\n"
                                                 "color: #7AB32E;\n"
                                                 "font: 20px \"Arial\" ;\n"
                                                 "font-weight: bold\n"
                                                 "}\n"
                                                 "QLineEdit:Focus {\n"
                                                 "border: 1px solid red;\n"
                                                 "}")
        self.tx_PorcentagemAtacado.setText("")
        self.tx_PorcentagemAtacado.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_PorcentagemAtacado.setReadOnly(True)
        self.tx_PorcentagemAtacado.setObjectName("tx_PorcentagemAtacado")
        self.label_2 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 150, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Images/CodBarra.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tx_AddMarca = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_AddMarca.setGeometry(QtCore.QRect(435, 145, 190, 25))
        self.tx_AddMarca.setStyleSheet("QLineEdit{\n"
                                       "background: #CFCFCF;\n"
                                       "border-radius: 2px;\n"
                                       "color: #000;\n"
                                       "font: 13px \"Arial\" ;\n"
                                       "text-transform: uppercase;\n"
                                       "}\n"
                                       "QLineEdit:Focus {\n"
                                       "border: 1px solid red;\n"
                                       "}")
        self.tx_AddMarca.setObjectName("tx_AddMarca")
        self.tx_AddCategoria = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_AddCategoria.setGeometry(QtCore.QRect(200, 145, 190, 25))
        self.tx_AddCategoria.setStyleSheet("QLineEdit{\n"
                                           "background: #CFCFCF;\n"
                                           "border-radius: 2px;\n"
                                           "color: #000;\n"
                                           "font: 13px \"Arial\" ;\n"
                                           "text-transform: uppercase;\n"
                                           "}\n"
                                           "QLineEdit:Focus {\n"
                                           "border: 1px solid red;\n"
                                           "}")
        self.tx_AddCategoria.setInputMask("")
        self.tx_AddCategoria.setObjectName("tx_AddCategoria")
        self.bt_CancelAddCatergoria = QtWidgets.QPushButton(
            self.fr_FormProdutos)
        self.bt_CancelAddCatergoria.setGeometry(QtCore.QRect(390, 145, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
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
        self.bt_CalcelAddMarca = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_CalcelAddMarca.setGeometry(QtCore.QRect(625, 145, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_CalcelAddMarca.setFont(font)
        self.bt_CalcelAddMarca.setStyleSheet("QPushButton{\n"
                                             "background: #7AB32E;\n"
                                             "color: #FFF\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color: #40a286\n"
                                             "}")
        self.bt_CalcelAddMarca.setText("")
        self.bt_CalcelAddMarca.setObjectName("bt_CalcelAddMarca")
        self.bt_AddImagem = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_AddImagem.setGeometry(QtCore.QRect(140, 230, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_AddImagem.setFont(font)
        self.bt_AddImagem.setStyleSheet("QPushButton{\n"
                                        "background: #7AB32E;\n"
                                        "color: #FFF\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: #40a286\n"
                                        "}")
        self.bt_AddImagem.setText("")
        self.bt_AddImagem.setObjectName("bt_AddImagem")
        self.bt_DelImagem = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_DelImagem.setGeometry(QtCore.QRect(140, 230, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_DelImagem.setFont(font)
        self.bt_DelImagem.setStyleSheet("QPushButton{\n"
                                        "background: #7AB32E;\n"
                                        "color: #FFF\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: #40a286\n"
                                        "}")
        self.bt_DelImagem.setText("")
        self.bt_DelImagem.setObjectName("bt_DelImagem")
        self.tx_AddMarca.raise_()
        self.tx_AddCategoria.raise_()
        self.bt_CancelAddCatergoria.raise_()
        self.bt_CalcelAddMarca.raise_()
        self.lb_FormProdutos.raise_()
        self.tx_idProduto.raise_()
        self.lb_FotoProduto.raise_()
        self.lb_FormProdutos_2.raise_()
        self.tx_DescricaoProduto.raise_()
        self.lb_FormProdutos_3.raise_()
        self.cb_CategoriaProduto.raise_()
        self.bt_AddCategoriaProduto.raise_()
        self.lb_FormProdutos_4.raise_()
        self.cb_MarcaProduto.raise_()
        self.bt_AddMarcaProduto.raise_()
        self.lb_FormProdutos_5.raise_()
        self.lb_FormProdutos_6.raise_()
        self.tx_EstoqueMinimoProduto.raise_()
        self.tx_EstoqueMaximoProduto.raise_()
        self.tx_ObsProduto.raise_()
        self.lb_FormProdutos_7.raise_()
        self.lb_FormProdutos_8.raise_()
        self.tb_HistoricoComprasProduto.raise_()
        self.lb_FormProdutos_9.raise_()
        self.tx_ValorCompraProduto.raise_()
        self.lb_FormProdutos_10.raise_()
        self.lb_FormProdutos_11.raise_()
        self.tx_ValorUnitarioProduto.raise_()
        self.lb_FormProdutos_12.raise_()
        self.lb_FormProdutos_13.raise_()
        self.tx_ValorAtacadoProduto.raise_()
        self.fr_BotoesFormProdutos.raise_()
        self.lb_qtdeMin.raise_()
        self.tx_MinimoAtacado.raise_()
        self.lb_FormProdutos_14.raise_()
        self.lb_FormProdutos_15.raise_()
        self.tx_PorcentagemVarejo.raise_()
        self.lb_FormProdutos_17.raise_()
        self.lb_porcVar.raise_()
        self.lb_FormProdutos_16.raise_()
        self.lb_FormProdutos_19.raise_()
        self.lb_porcAtac.raise_()
        self.tx_PorcentagemAtacado.raise_()
        self.label_2.raise_()
        self.bt_DelImagem.raise_()
        self.bt_AddImagem.raise_()

        self.tradFormProdutos(ct_FormProdutos)
        QtCore.QMetaObject.connectSlotsByName(ct_FormProdutos)
        ct_FormProdutos.setTabOrder(
            self.tx_idProduto, self.tx_DescricaoProduto)
        ct_FormProdutos.setTabOrder(
            self.tx_DescricaoProduto, self.cb_CategoriaProduto)
        ct_FormProdutos.setTabOrder(
            self.cb_CategoriaProduto, self.bt_AddCategoriaProduto)
        ct_FormProdutos.setTabOrder(
            self.bt_AddCategoriaProduto, self.cb_MarcaProduto)
        ct_FormProdutos.setTabOrder(
            self.cb_MarcaProduto, self.bt_AddMarcaProduto)
        ct_FormProdutos.setTabOrder(
            self.bt_AddMarcaProduto, self.tx_EstoqueMinimoProduto)
        ct_FormProdutos.setTabOrder(
            self.tx_EstoqueMinimoProduto, self.tx_EstoqueMaximoProduto)
        ct_FormProdutos.setTabOrder(
            self.tx_EstoqueMaximoProduto, self.tx_ObsProduto)
        ct_FormProdutos.setTabOrder(
            self.tx_ObsProduto, self.tx_ValorCompraProduto)
        ct_FormProdutos.setTabOrder(
            self.tx_ValorCompraProduto, self.tx_ValorUnitarioProduto)
        ct_FormProdutos.setTabOrder(
            self.tx_ValorUnitarioProduto, self.tx_ValorAtacadoProduto)
        ct_FormProdutos.setTabOrder(
            self.tx_ValorAtacadoProduto, self.tx_MinimoAtacado)
        ct_FormProdutos.setTabOrder(
            self.tx_MinimoAtacado, self.tx_PorcentagemVarejo)
        ct_FormProdutos.setTabOrder(
            self.tx_PorcentagemVarejo, self.tx_PorcentagemAtacado)
        ct_FormProdutos.setTabOrder(
            self.tx_PorcentagemAtacado, self.tx_AddMarca)
        ct_FormProdutos.setTabOrder(self.tx_AddMarca, self.tx_AddCategoria)
        ct_FormProdutos.setTabOrder(
            self.tx_AddCategoria, self.bt_CancelAddCatergoria)
        ct_FormProdutos.setTabOrder(
            self.bt_CancelAddCatergoria, self.bt_CalcelAddMarca)
        ct_FormProdutos.setTabOrder(
            self.bt_CalcelAddMarca, self.tb_HistoricoComprasProduto)

    def tradFormProdutos(self, ct_FormProdutos):
        _translate = QtCore.QCoreApplication.translate
        ct_FormProdutos.setWindowTitle(_translate("ct_FormProdutos", "Frame"))
        self.lb_FormProdutos.setText(_translate(
            "ct_FormProdutos", "CADASTRAR PRODUTO"))
        self.lb_FormProdutos_2.setText(
            _translate("ct_FormProdutos", "DESCRIÇÃO"))
        self.tx_DescricaoProduto.setPlaceholderText(
            _translate("ct_FormProdutos", "Descrição Produto"))
        self.lb_FormProdutos_3.setText(
            _translate("ct_FormProdutos", "CATEGORIA"))
        self.cb_CategoriaProduto.setItemText(
            0, _translate("ct_FormProdutos", "SELECIONE"))
        self.lb_FormProdutos_4.setText(_translate("ct_FormProdutos", "MARCA"))
        self.cb_MarcaProduto.setItemText(
            0, _translate("ct_FormProdutos", "SELECIONE"))
        self.lb_FormProdutos_5.setText(
            _translate("ct_FormProdutos", "ESTOQUE MÍNIMO"))
        self.lb_FormProdutos_6.setText(
            _translate("ct_FormProdutos", "ESTOQUE MÁXIMO"))
        self.tx_ObsProduto.setPlaceholderText(
            _translate("ct_FormProdutos", "Observação"))
        self.lb_FormProdutos_7.setText(
            _translate("ct_FormProdutos", "OBSERVAÇÃO"))
        self.lb_FormProdutos_8.setText(_translate("ct_FormProdutos", "PREÇOS"))
        item = self.tb_HistoricoComprasProduto.horizontalHeaderItem(0)
        item.setText(_translate("ct_FormProdutos", "DATA"))
        item = self.tb_HistoricoComprasProduto.horizontalHeaderItem(1)
        item.setText(_translate("ct_FormProdutos", "QTDE"))
        item = self.tb_HistoricoComprasProduto.horizontalHeaderItem(2)
        item.setText(_translate("ct_FormProdutos", "VALOR"))
        self.lb_FormProdutos_9.setText(_translate(
            "ct_FormProdutos", "HISTÓRICO DE COMPRAS"))
        self.tx_ValorCompraProduto.setPlaceholderText(
            _translate("ct_FormProdutos", "R$ 0.00"))
        self.lb_FormProdutos_10.setText(_translate("ct_FormProdutos", "CUSTO"))
        self.lb_FormProdutos_11.setText(
            _translate("ct_FormProdutos", "(ÚLTIMA COMPRA)"))
        self.tx_ValorUnitarioProduto.setPlaceholderText(
            _translate("ct_FormProdutos", "R$ 0.00"))
        self.lb_FormProdutos_12.setText(
            _translate("ct_FormProdutos", "VENDA VAREJO"))
        self.lb_FormProdutos_13.setText(
            _translate("ct_FormProdutos", "VENDA ATACADO"))
        self.tx_ValorAtacadoProduto.setPlaceholderText(
            _translate("ct_FormProdutos", "R$ 0.00"))
        self.bt_CancelarProdutos.setText(
            _translate("ct_FormProdutos", "CANCELAR"))
        self.bt_SalvarProdutos.setText(_translate("ct_FormProdutos", "SALVAR"))
        self.lb_FormProdutos_14.setText(_translate(
            "ct_FormProdutos", "QTDE. MÍNIMA P/ ATACADO"))
        self.lb_FormProdutos_15.setText(
            _translate("ct_FormProdutos", "MARGEM LUCRO"))
        self.lb_FormProdutos_17.setText(_translate(
            "ct_FormProdutos", "(APROXIMADA NO VAREJO)"))
        self.lb_porcVar.setText(_translate("ct_FormProdutos", "%"))
        self.lb_FormProdutos_16.setText(
            _translate("ct_FormProdutos", "MARGEM LUCRO"))
        self.lb_FormProdutos_19.setText(_translate(
            "ct_FormProdutos", "(APROXIMADA NO ATACADO"))
        self.lb_porcAtac.setText(_translate("ct_FormProdutos", "%"))
        self.tx_AddMarca.setPlaceholderText(
            _translate("ct_FormProdutos", "NOVA MARCA"))
        self.tx_AddCategoria.setPlaceholderText(
            _translate("ct_FormProdutos", "NOVA CATEGORIA"))
        self.bt_CancelAddCatergoria.setToolTip(_translate(
            "ct_FormProdutos", "<html><head/><body><p>Cancelar</p></body></html>"))
        self.bt_CalcelAddMarca.setToolTip(_translate(
            "ct_FormProdutos", "<html><head/><body><p>Cancelar</p></body></html>"))
        self.bt_AddImagem.setToolTip(_translate(
            "ct_FormProdutos", "<html><head/><body><p>CADASTRAR IMGEM</p></body></html>"))
        self.bt_DelImagem.setToolTip(_translate(
            "ct_FormProdutos", "<html><head/><body><p>Deletar Imagem</p></body></html>"))
