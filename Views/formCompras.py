# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formCompras.ui'
#
# Created by: PySide2 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_FormCompra(object):

    def setFormCompra(self, ct_FormCompra):
        ct_FormCompra.setObjectName("ct_FormCompra")
        ct_FormCompra.resize(1000, 500)
        ct_FormCompra.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormCompra.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormCompra = QtWidgets.QFrame(ct_FormCompra)
        self.fr_FormCompra.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormCompra.setStyleSheet("background: #FFF;\n"
                                         "border: none")
        self.fr_FormCompra.setObjectName("fr_FormCompra")
        self.lb_FormCompra = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra.setGeometry(QtCore.QRect(20, 10, 960, 20))
        self.lb_FormCompra.setStyleSheet("QLabel{\n"
                                         "font-size: 14px;\n"
                                         "font-family: \"Arial\";\n"
                                         "font-weight: bold;\n"
                                         "color: #A2A2A2;\n"
                                         "}")
        self.lb_FormCompra.setObjectName("lb_FormCompra")
        self.fr_BotoesFormCompra = QtWidgets.QFrame(self.fr_FormCompra)
        self.fr_BotoesFormCompra.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormCompra.setStyleSheet("background:#E1DFE0;\n"
                                               "border: none;")
        self.fr_BotoesFormCompra.setObjectName("fr_BotoesFormCompra")
        self.bt_CancelarCompra = QtWidgets.QPushButton(
            self.fr_BotoesFormCompra)
        self.bt_CancelarCompra.setGeometry(QtCore.QRect(870, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_CancelarCompra.setFont(font)
        self.bt_CancelarCompra.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_CancelarCompra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_CancelarCompra.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_CancelarCompra.setStyleSheet("QPushButton {\n"
                                             "background-color: #1E87F0;\n"
                                             "color: #FFF\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color: #40a286\n"
                                             "}")
        self.bt_CancelarCompra.setIconSize(QtCore.QSize(75, 35))
        self.bt_CancelarCompra.setObjectName("bt_CancelarCompra")
        self.bt_SalvarCompra = QtWidgets.QPushButton(self.fr_BotoesFormCompra)
        self.bt_SalvarCompra.setGeometry(QtCore.QRect(610, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_SalvarCompra.setFont(font)
        self.bt_SalvarCompra.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_SalvarCompra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_SalvarCompra.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_SalvarCompra.setStyleSheet("QPushButton {\n"
                                           "background-color: #7AB32E;\n"
                                           "color: #FFF\n"
                                           " }\n"
                                           "QPushButton:hover{\n"
                                           "background-color: #40a286\n"
                                           "}")
        self.bt_SalvarCompra.setIconSize(QtCore.QSize(75, 35))
        self.bt_SalvarCompra.setObjectName("bt_SalvarCompra")
        self.bt_ImprimirCompra = QtWidgets.QPushButton(
            self.fr_BotoesFormCompra)
        self.bt_ImprimirCompra.setEnabled(False)
        self.bt_ImprimirCompra.setGeometry(QtCore.QRect(740, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_ImprimirCompra.setFont(font)
        self.bt_ImprimirCompra.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_ImprimirCompra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_ImprimirCompra.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_ImprimirCompra.setStyleSheet("QPushButton {\n"
                                             "background-color: #5C9BBC;\n"
                                             "color: #FFF\n"
                                             " }\n"
                                             "QPushButton:hover{\n"
                                             "background-color: #40a286\n"
                                             "}")
        self.bt_ImprimirCompra.setIconSize(QtCore.QSize(75, 35))
        self.bt_ImprimirCompra.setObjectName("bt_ImprimirCompra")
        self.tx_FornecedorCompra = QtWidgets.QLineEdit(self.fr_FormCompra)
        self.tx_FornecedorCompra.setGeometry(QtCore.QRect(140, 110, 350, 30))
        self.tx_FornecedorCompra.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_FornecedorCompra.setStyleSheet("QLineEdit{\n"
                                               "background: #CFCFCF;\n"
                                               "border-radius: 2px;\n"
                                               "color: #000;\n"
                                               "font: 13px \"Arial\" ;\n"
                                               "text-transform: uppercase;\n"
                                               "}\n"
                                               "QLineEdit:Focus {\n"
                                               "border: 1px solid red;\n"
                                               "}")
        self.tx_FornecedorCompra.setObjectName("tx_FornecedorCompra")
        self.fr_topoCompra = QtWidgets.QFrame(self.fr_FormCompra)
        self.fr_topoCompra.setGeometry(QtCore.QRect(20, 30, 960, 40))
        self.fr_topoCompra.setStyleSheet("QFrame{\n"
                                         "background: #FFF;\n"
                                         "border: 1px solid #1E87F0;\n"
                                         "}\n"
                                         "")
        self.fr_topoCompra.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_topoCompra.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_topoCompra.setObjectName("fr_topoCompra")
        self.tx_CodCompra = QtWidgets.QLineEdit(self.fr_topoCompra)
        self.tx_CodCompra.setGeometry(QtCore.QRect(0, 0, 100, 40))
        self.tx_CodCompra.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_CodCompra.setStyleSheet("QLineEdit{\n"
                                        "background: #0884C2;\n"
                                        "border-radius: 2px;\n"
                                        "color: #000;\n"
                                        "font: 16px \"Arial\" ;\n"
                                        "font-weight: bold;\n"
                                        "color: #FFF\n"
                                        "}\n"
                                        "")
        self.tx_CodCompra.setText("")
        self.tx_CodCompra.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_CodCompra.setReadOnly(True)
        self.tx_CodCompra.setPlaceholderText("")
        self.tx_CodCompra.setObjectName("tx_CodCompra")
        self.dt_EmissaoCompra = QtWidgets.QDateEdit(self.fr_topoCompra)
        self.dt_EmissaoCompra.setGeometry(QtCore.QRect(120, 18, 140, 18))
        self.dt_EmissaoCompra.setStyleSheet("QDateEdit {\n"
                                            "background: #FFF;\n"
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
                                            "     image: url(Images/down.png);\n"
                                            " }")
        self.dt_EmissaoCompra.setCalendarPopup(True)
        self.dt_EmissaoCompra.setObjectName("dt_EmissaoCompra")
        self.lb_FormCompra1 = QtWidgets.QLabel(self.fr_topoCompra)
        self.lb_FormCompra1.setGeometry(QtCore.QRect(120, 2, 120, 18))
        self.lb_FormCompra1.setStyleSheet("QLabel{\n"
                                          "font-size: 12px;\n"
                                          "font-family: \"Arial Unicode MS\";\n"
                                          "\n"
                                          "color:#1E87F0;\n"
                                          "border: none;\n"
                                          "}")
        self.lb_FormCompra1.setObjectName("lb_FormCompra1")
        self.dt_PrazoEntrega = QtWidgets.QDateEdit(self.fr_topoCompra)
        self.dt_PrazoEntrega.setGeometry(QtCore.QRect(300, 18, 140, 18))
        self.dt_PrazoEntrega.setStyleSheet("QDateEdit {\n"
                                           "background: #FFF;\n"
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
                                           "     image: url(Images/down.png);\n"
                                           " }")
        self.dt_PrazoEntrega.setCalendarPopup(True)
        self.dt_PrazoEntrega.setObjectName("dt_PrazoEntrega")
        self.lb_FormCompra2 = QtWidgets.QLabel(self.fr_topoCompra)
        self.lb_FormCompra2.setGeometry(QtCore.QRect(300, 2, 120, 18))
        self.lb_FormCompra2.setStyleSheet("QLabel{\n"
                                          "font-size: 12px;\n"
                                          "font-family: \"Arial Unicode MS\";\n"
                                          "\n"
                                          "color:#1E87F0;\n"
                                          "border: none;\n"
                                          "}")
        self.lb_FormCompra2.setObjectName("lb_FormCompra2")
        self.bt_ReceberProduto = QtWidgets.QPushButton(self.fr_topoCompra)
        self.bt_ReceberProduto.setEnabled(False)
        self.bt_ReceberProduto.setGeometry(QtCore.QRect(820, 5, 120, 30))
        self.bt_ReceberProduto.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_ReceberProduto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_ReceberProduto.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_ReceberProduto.setStyleSheet("QPushButton {\n"
                                             "background-color: #7AB32E;\n"
                                             "border-radius: 2px\n"
                                             " }\n"
                                             "QPushButton:disabled{\n"
                                             "background-color: #CACACA;\n"
                                             "border-radius: 5px\n"
                                             " }\n"
                                             "QPushButton:hover{\n"
                                             "background-color: #40a286\n"
                                             "}")
        self.bt_ReceberProduto.setText("")
        self.bt_ReceberProduto.setIconSize(QtCore.QSize(75, 35))
        self.bt_ReceberProduto.setObjectName("bt_ReceberProduto")
        self.lb_FormCompra3 = QtWidgets.QLabel(self.fr_topoCompra)
        self.lb_FormCompra3.setGeometry(QtCore.QRect(480, 2, 120, 18))
        self.lb_FormCompra3.setStyleSheet("QLabel{\n"
                                          "font-size: 12px;\n"
                                          "font-family: \"Arial Unicode MS\";\n"
                                          "\n"
                                          "color:#1E87F0;\n"
                                          "border: none;\n"
                                          "}")
        self.lb_FormCompra3.setObjectName("lb_FormCompra3")
        self.dt_EntregaCompra = QtWidgets.QDateEdit(self.fr_topoCompra)
        self.dt_EntregaCompra.setGeometry(QtCore.QRect(480, 18, 140, 18))
        self.dt_EntregaCompra.setStyleSheet("QDateEdit {\n"
                                            "background: #FFF;\n"
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
                                            "     image: url(Images/down.png);\n"
                                            " }")
        self.dt_EntregaCompra.setCalendarPopup(True)
        self.dt_EntregaCompra.setObjectName("dt_EntregaCompra")
        self.lb_FormCompra = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra.setGeometry(QtCore.QRect(140, 90, 120, 20))
        self.lb_FormCompra.setStyleSheet("QLabel{\n"
                                         "font-size: 13px;\n"
                                         "font-family: \"Arial\";\n"
                                         "font-weight: bold;\n"
                                         "color: #A2A2A2;\n"
                                         "}")
        self.lb_FormCompra.setObjectName("lb_FormCompra")
        self.lb_FormCompra_3 = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra_3.setGeometry(QtCore.QRect(20, 90, 100, 20))
        self.lb_FormCompra_3.setStyleSheet("QLabel{\n"
                                           "font-size: 13px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #A2A2A2;\n"
                                           "}")
        self.lb_FormCompra_3.setObjectName("lb_FormCompra_3")
        self.tx_CodFornecedorCompra = QtWidgets.QLineEdit(self.fr_FormCompra)
        self.tx_CodFornecedorCompra.setGeometry(QtCore.QRect(20, 110, 100, 30))
        self.tx_CodFornecedorCompra.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_CodFornecedorCompra.setStyleSheet("QLineEdit{\n"
                                                  "background: #CFCFCF;\n"
                                                  "border-radius: 2px;\n"
                                                  "color: #000;\n"
                                                  "font: 13px \"Arial\" ;\n"
                                                  "text-transform: uppercase;\n"
                                                  "}\n"
                                                  "QLineEdit:Focus {\n"
                                                  "border: 1px solid red;\n"
                                                  "}")
        self.tx_CodFornecedorCompra.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_CodFornecedorCompra.setObjectName("tx_CodFornecedorCompra")
        self.lb_FormCompra_4 = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra_4.setGeometry(QtCore.QRect(20, 150, 120, 20))
        self.lb_FormCompra_4.setStyleSheet("QLabel{\n"
                                           "font-size: 13px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #A2A2A2;\n"
                                           "}")
        self.lb_FormCompra_4.setObjectName("lb_FormCompra_4")
        self.fr_addProduto = QtWidgets.QFrame(self.fr_FormCompra)
        self.fr_addProduto.setGeometry(QtCore.QRect(20, 170, 600, 70))
        self.fr_addProduto.setStyleSheet("QFrame{\n"
                                         "background: #1D76A2;\n"
                                         "border: 1px solid #1E87F0;\n"
                                         "}\n"
                                         "")
        self.fr_addProduto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_addProduto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_addProduto.setObjectName("fr_addProduto")
        self.tx_BuscaItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_BuscaItem.setGeometry(QtCore.QRect(40, 0, 270, 40))
        self.tx_BuscaItem.setMouseTracking(True)
        self.tx_BuscaItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_BuscaItem.setStyleSheet("QLineEdit{\n"
                                        "background: #5C9BBC;\n"
                                        "border-radius: 2px;\n"
                                        "color: #000;\n"
                                        "font: 10px \"Arial\" ;\n"
                                        "font-weight: bold;\n"
                                        "color: #FFF;\n"
                                        "text-transform: uppercase\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.tx_BuscaItem.setText("")
        self.tx_BuscaItem.setFrame(False)
        self.tx_BuscaItem.setCursorPosition(0)
        self.tx_BuscaItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_BuscaItem.setReadOnly(False)
        self.tx_BuscaItem.setObjectName("tx_BuscaItem")
        self.lb_FormCompra_6 = QtWidgets.QLabel(self.fr_addProduto)
        self.lb_FormCompra_6.setGeometry(QtCore.QRect(350, 0, 75, 15))
        self.lb_FormCompra_6.setStyleSheet("QLabel{\n"
                                           "font-size: 9px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #A2A2A2;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormCompra_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FormCompra_6.setObjectName("lb_FormCompra_6")
        self.tx_ValorUnitarioItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ValorUnitarioItem.setGeometry(QtCore.QRect(350, 15, 75, 25))
        self.tx_ValorUnitarioItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorUnitarioItem.setStyleSheet("QLineEdit{\n"
                                                "background:transparent;\n"
                                                "border-radius: 2px;\n"
                                                "color: #000;\n"
                                                "font: 14px \"Arial\" ;\n"
                                                "text-transform: uppercase;\n"
                                                "color: #FFF;\n"
                                                "border: none\n"
                                                "}\n"
                                                "QLineEdit::placeholder{\n"
                                                "color: red;\n"
                                                "}")
        self.tx_ValorUnitarioItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ValorUnitarioItem.setObjectName("tx_ValorUnitarioItem")
        self.lb_FormCompra_7 = QtWidgets.QLabel(self.fr_addProduto)
        self.lb_FormCompra_7.setGeometry(QtCore.QRect(425, 0, 75, 15))
        self.lb_FormCompra_7.setStyleSheet("QLabel{\n"
                                           "font-size: 9px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #A2A2A2;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormCompra_7.setObjectName("lb_FormCompra_7")
        self.tx_ValorTotalItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ValorTotalItem.setGeometry(QtCore.QRect(425, 15, 75, 25))
        self.tx_ValorTotalItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorTotalItem.setStyleSheet("QLineEdit{\n"
                                             "background:transparent;\n"
                                             "border-radius: 2px;\n"
                                             "color: #000;\n"
                                             "font: 14px \"Arial\" ;\n"
                                             "text-transform: uppercase;\n"
                                             "color: #FFF;\n"
                                             "border: none\n"
                                             "}\n"
                                             "QLineEdit::placeholder{\n"
                                             "color: red;\n"
                                             "}")
        self.tx_ValorTotalItem.setText("")
        self.tx_ValorTotalItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ValorTotalItem.setReadOnly(True)
        self.tx_ValorTotalItem.setObjectName("tx_ValorTotalItem")
        self.bt_IncluirItemCompra = QtWidgets.QPushButton(self.fr_addProduto)
        self.bt_IncluirItemCompra.setEnabled(False)
        self.bt_IncluirItemCompra.setGeometry(QtCore.QRect(500, 0, 100, 70))
        self.bt_IncluirItemCompra.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_IncluirItemCompra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_IncluirItemCompra.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_IncluirItemCompra.setStyleSheet("QPushButton {\n"
                                                "background: #025682;\n"
                                                " }\n"
                                                "QPushButton:hover{\n"
                                                "background-color: #5C9BBC\n"
                                                "}")
        self.bt_IncluirItemCompra.setText("")
        self.bt_IncluirItemCompra.setIconSize(QtCore.QSize(75, 35))
        self.bt_IncluirItemCompra.setObjectName("bt_IncluirItemCompra")
        self.tx_ObsItemCompra = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ObsItemCompra.setGeometry(QtCore.QRect(0, 40, 500, 30))
        self.tx_ObsItemCompra.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ObsItemCompra.setStyleSheet("QLineEdit{\n"
                                            "background: #1E87F0;\n"
                                            "border-radius: 2px;\n"
                                            "color: #000;\n"
                                            "font: 13px \"Arial\" ;\n"
                                            "font-weight: bold;\n"
                                            "color: #FFF\n"
                                            "}\n"
                                            "\n"
                                            "")
        self.tx_ObsItemCompra.setText("")
        self.tx_ObsItemCompra.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ObsItemCompra.setReadOnly(False)
        self.tx_ObsItemCompra.setObjectName("tx_ObsItemCompra")
        self.tx_IdBuscaItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_IdBuscaItem.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.tx_IdBuscaItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_IdBuscaItem.setStyleSheet("QLineEdit{\n"
                                          "background: #5C9BBC;\n"
                                          "border-radius: 2px;\n"
                                          "color: #000;\n"
                                          "font: 11px \"Arial\" ;\n"
                                          "font-weight: bold;\n"
                                          "color: #FFF\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.tx_IdBuscaItem.setText("")
        self.tx_IdBuscaItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_IdBuscaItem.setReadOnly(False)
        self.tx_IdBuscaItem.setObjectName("tx_IdBuscaItem")
        self.tx_QntdItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_QntdItem.setGeometry(QtCore.QRect(310, 0, 40, 40))
        self.tx_QntdItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_QntdItem.setStyleSheet("\n"
                                       "QLineEdit{\n"
                                       "background: #4088AC;\n"
                                       "border-radius: 2px;\n"
                                       "color: #000;\n"
                                       "font: 11px \"Arial\" ;\n"
                                       "font-weight: bold;\n"
                                       "color: #FFF\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "")
        self.tx_QntdItem.setText("")
        self.tx_QntdItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_QntdItem.setReadOnly(False)
        self.tx_QntdItem.setObjectName("tx_QntdItem")
        self.lb_FormCompra_5 = QtWidgets.QLabel(self.fr_FormCompra)
        self.lb_FormCompra_5.setGeometry(QtCore.QRect(510, 90, 110, 20))
        self.lb_FormCompra_5.setStyleSheet("QLabel{\n"
                                           "font-size: 13px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #A2A2A2;\n"
                                           "}")
        self.lb_FormCompra_5.setObjectName("lb_FormCompra_5")
        self.tx_TelefoneFornecedorCompra = QtWidgets.QLineEdit(
            self.fr_FormCompra)
        self.tx_TelefoneFornecedorCompra.setGeometry(
            QtCore.QRect(510, 110, 110, 30))
        self.tx_TelefoneFornecedorCompra.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_TelefoneFornecedorCompra.setStyleSheet("QLineEdit{\n"
                                                       "background: #CFCFCF;\n"
                                                       "border-radius: 2px;\n"
                                                       "color: #000;\n"
                                                       "font: 13px \"Arial\" ;\n"
                                                       "text-transform: uppercase;\n"
                                                       "}\n"
                                                       "QLineEdit:Focus {\n"
                                                       "border: 1px solid red;\n"
                                                       "}")
        self.tx_TelefoneFornecedorCompra.setReadOnly(True)
        self.tx_TelefoneFornecedorCompra.setObjectName(
            "tx_TelefoneFornecedorCompra")
        self.tb_ItensCompra = QtWidgets.QTableWidget(self.fr_FormCompra)
        self.tb_ItensCompra.setGeometry(QtCore.QRect(20, 250, 600, 200))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tb_ItensCompra.sizePolicy().hasHeightForWidth())
        self.tb_ItensCompra.setSizePolicy(sizePolicy)
        self.tb_ItensCompra.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_ItensCompra.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_ItensCompra.setStyleSheet("QTableView{\n"
                                          "color: #28292A;\n"
                                          "font-weight: bold;\n"
                                          "font-size: 11px;\n"
                                          "background: #FFF;\n"
                                          "padding: 0 0 0 5px;\n"
                                          "}\n"
                                          "QHeaderView:section{\n"
                                          "background: #FFF;\n"
                                          "padding: 5px 0 ;\n"
                                          "font-size: 11px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #797979;\n"
                                          "border: none;\n"
                                          "border-bottom: 2px solid #CCC;\n"
                                          "text-transform: uppercase;\n"
                                          "margin: 0 2px 0 0;\n"
                                          "}\n"
                                          "QTableView::item {\n"
                                          "border-bottom: 2px solid #CCC;\n"
                                          "padding: 2px;\n"
                                          "margin: 0 2px 0 0;\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.tb_ItensCompra.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_ItensCompra.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_ItensCompra.setAutoScrollMargin(20)
        self.tb_ItensCompra.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_ItensCompra.setTabKeyNavigation(False)
        self.tb_ItensCompra.setProperty("showDropIndicator", False)
        self.tb_ItensCompra.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.tb_ItensCompra.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_ItensCompra.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_ItensCompra.setShowGrid(False)
        self.tb_ItensCompra.setCornerButtonEnabled(False)
        self.tb_ItensCompra.setRowCount(0)
        self.tb_ItensCompra.setObjectName("tb_ItensCompra")
        self.tb_ItensCompra.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ItensCompra.setHorizontalHeaderItem(0, item)
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
        self.tb_ItensCompra.setHorizontalHeaderItem(1, item)
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
        self.tb_ItensCompra.setHorizontalHeaderItem(2, item)
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
        self.tb_ItensCompra.setHorizontalHeaderItem(3, item)
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
        self.tb_ItensCompra.setHorizontalHeaderItem(4, item)
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
        self.tb_ItensCompra.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_ItensCompra.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ItensCompra.setHorizontalHeaderItem(7, item)
        self.tb_ItensCompra.horizontalHeader().setDefaultSectionSize(120)
        self.tb_ItensCompra.horizontalHeader().setStretchLastSection(True)
        self.tb_ItensCompra.verticalHeader().setVisible(False)
        self.tb_ItensCompra.verticalHeader().setCascadingSectionResizes(True)
        self.tb_ItensCompra.verticalHeader().setDefaultSectionSize(40)
        self.fr_financeiroCompra = QtWidgets.QFrame(self.fr_FormCompra)
        self.fr_financeiroCompra.setGeometry(QtCore.QRect(640, 110, 340, 340))
        self.fr_financeiroCompra.setStyleSheet("background: #F1F1F1;\n"
                                               "border-top: 4px solid #277298;\n"
                                               "border-bottom: 4px solid #277298;")
        self.fr_financeiroCompra.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_financeiroCompra.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_financeiroCompra.setObjectName("fr_financeiroCompra")
        self.tx_Desconto = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_Desconto.setGeometry(QtCore.QRect(120, 25, 90, 25))
        self.tx_Desconto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Desconto.setStyleSheet("QLineEdit{\n"
                                       "background: #F1F1F1;\n"
                                       "border: 2px solid #CFCFCF;\n"
                                       "color: #000;\n"
                                       "font: 14px \"Arial\" ;\n"
                                       "text-transform: uppercase;\n"
                                       "font-weight: bold\n"
                                       "}\n"
                                       "QLineEdit:Focus {\n"
                                       "border: 1px solid red;\n"
                                       "}")
        self.tx_Desconto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_Desconto.setObjectName("tx_Desconto")
        self.lb_FormVenda_14 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_14.setGeometry(QtCore.QRect(120, 5, 90, 20))
        self.lb_FormVenda_14.setStyleSheet("QLabel{\n"
                                           "font-size: 13px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #7B7A7A;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_14.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_14.setObjectName("lb_FormVenda_14")
        self.tx_Frete = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_Frete.setGeometry(QtCore.QRect(230, 25, 90, 25))
        self.tx_Frete.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Frete.setStyleSheet("QLineEdit{\n"
                                    "background: #F1F1F1;\n"
                                    "border: 2px solid #CFCFCF;\n"
                                    "color: #000;\n"
                                    "font: 14px \"Arial\" ;\n"
                                    "text-transform: uppercase;\n"
                                    "font-weight: bold\n"
                                    "}\n"
                                    "QLineEdit:Focus {\n"
                                    "border: 1px solid red;\n"
                                    "}")
        self.tx_Frete.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_Frete.setObjectName("tx_Frete")
        self.lb_FormVenda_17 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_17.setGeometry(QtCore.QRect(230, 5, 90, 20))
        self.lb_FormVenda_17.setStyleSheet("QLabel{\n"
                                           "font-size: 13px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #7B7A7A;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_17.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_17.setObjectName("lb_FormVenda_17")
        self.lb_SubTotalCompra = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_SubTotalCompra.setGeometry(QtCore.QRect(0, 25, 100, 25))
        self.lb_SubTotalCompra.setStyleSheet("QLabel{\n"
                                             "font-size: 20px;\n"
                                             "font-family: \"Arial\";\n"
                                             "font-weight: bold;\n"
                                             "color: #277298;\n"
                                             "border: none\n"
                                             "}")
        self.lb_SubTotalCompra.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_SubTotalCompra.setObjectName("lb_SubTotalCompra")
        self.lb_FormVenda_18 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_18.setGeometry(QtCore.QRect(0, 5, 100, 20))
        self.lb_FormVenda_18.setStyleSheet("QLabel{\n"
                                           "font-size: 10px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #277298;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_18.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_18.setObjectName("lb_FormVenda_18")
        self.lb_FormVenda_19 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda_19.setGeometry(QtCore.QRect(10, 55, 100, 20))
        self.lb_FormVenda_19.setStyleSheet("QLabel{\n"
                                           "font-size: 10px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #277298;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_19.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_19.setObjectName("lb_FormVenda_19")
        self.bt_GerarParcelaCompra = QtWidgets.QPushButton(
            self.fr_financeiroCompra)
        self.bt_GerarParcelaCompra.setEnabled(False)
        self.bt_GerarParcelaCompra.setGeometry(
            QtCore.QRect(180, 165, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_GerarParcelaCompra.setFont(font)
        self.bt_GerarParcelaCompra.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_GerarParcelaCompra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_GerarParcelaCompra.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_GerarParcelaCompra.setStyleSheet("QPushButton {\n"
                                                 "background-color: #7AB32E;\n"
                                                 "background-position: center;\n"
                                                 "background-repeat: no-repeat;\n"
                                                 "border: none;\n"
                                                 " }\n"
                                                 "QPushButton:disabled{\n"
                                                 "background-color: #CACACA;\n"
                                                 "\n"
                                                 " }\n"
                                                 "QPushButton:hover{\n"
                                                 "background-color: #40a286\n"
                                                 "}")
        self.bt_GerarParcelaCompra.setIconSize(QtCore.QSize(75, 35))
        self.bt_GerarParcelaCompra.setObjectName("bt_GerarParcelaCompra")
        self.tx_TotalFinal = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_TotalFinal.setEnabled(False)
        self.tx_TotalFinal.setGeometry(QtCore.QRect(10, 75, 100, 25))
        self.tx_TotalFinal.setStyleSheet("\n"
                                         "font-size: 24px;\n"
                                         "font-family: \"Arial\";\n"
                                         "font-weight: bold;\n"
                                         "color: #277298;\n"
                                         "border: none\n"
                                         "\n"
                                         "")
        self.tx_TotalFinal.setText("")
        self.tx_TotalFinal.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_TotalFinal.setReadOnly(True)
        self.tx_TotalFinal.setObjectName("tx_TotalFinal")
        self.cb_FormaPagamentoVenda = QtWidgets.QComboBox(
            self.fr_financeiroCompra)
        self.cb_FormaPagamentoVenda.setGeometry(
            QtCore.QRect(10, 125, 150, 25))
        self.cb_FormaPagamentoVenda.setStyleSheet("QComboBox{\n"
                                                  "background: #F1F1F1;\n"
                                                  "border: 2px solid #CFCFCF;\n"
                                                  "color: #000;\n"
                                                  "font: 12px \"Arial\" ;\n"
                                                  "text-transform: uppercase;\n"
                                                  "font-weight: bold;\n"
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
        self.cb_FormaPagamentoVenda.setObjectName("cb_FormaPagamentoVenda")
        self.cb_FormaPagamentoVenda.addItem("")
        self.cb_FormaPagamentoVenda.setItemText(0, "")
        self.cb_FormaPagamentoVenda.addItem("")
        self.cb_FormaPagamentoVenda.addItem("")
        self.lb_FormVenda0 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda0.setGeometry(QtCore.QRect(10, 110, 150, 15))
        self.lb_FormVenda0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_FormVenda0.setStyleSheet("QLabel{\n"
                                         "font-size: 10px;\n"
                                         "font-family: \"Arial\";\n"
                                         "font-weight: bold;\n"
                                         "color: #277298;\n"
                                         "border: none\n"
                                         "}")
        self.lb_FormVenda0.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda0.setObjectName("lb_FormVenda0")
        self.cb_ParcelamentoVenda = QtWidgets.QComboBox(
            self.fr_financeiroCompra)
        self.cb_ParcelamentoVenda.setGeometry(
            QtCore.QRect(180, 125, 150, 25))
        self.cb_ParcelamentoVenda.setStyleSheet("QComboBox{\n"
                                                "background: #F1F1F1;\n"
                                                "border: 2px solid #CFCFCF;\n"
                                                "color: #000;\n"
                                                "font: 12px \"Arial\" ;\n"
                                                "text-transform: uppercase;\n"
                                                "font-weight: bold;\n"
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
        self.cb_ParcelamentoVenda.setObjectName("cb_ParcelamentoVenda")
        self.cb_ParcelamentoVenda.addItem("")
        self.cb_ParcelamentoVenda.setItemText(0, "")
        self.cb_ParcelamentoVenda.addItem("")
        self.cb_ParcelamentoVenda.addItem("")
        self.cb_ParcelamentoVenda.addItem("")
        self.cb_ParcelamentoVenda.addItem("")
        self.lb_FormVenda1 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda1.setGeometry(QtCore.QRect(180, 110, 150, 15))
        self.lb_FormVenda1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_FormVenda1.setStyleSheet("QLabel{\n"
                                         "font-size: 10px;\n"
                                         "font-family: \"Arial\";\n"
                                         "font-weight: bold;\n"
                                         "color: #277298;\n"
                                         "border: none\n"
                                         "}")
        self.lb_FormVenda1.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda1.setObjectName("lb_FormVenda1")
        self.dt_VencimentoVenda = QtWidgets.QDateEdit(
            self.fr_financeiroCompra)
        self.dt_VencimentoVenda.setGeometry(QtCore.QRect(10, 170, 150, 25))
        self.dt_VencimentoVenda.setStyleSheet("QDateEdit {\n"
                                              "background: #F1F1F1;\n"
                                              "border: 2px solid #CFCFCF;\n"
                                              "color: #000;\n"
                                              "font: 14px \"Arial\" ;\n"
                                              "text-transform: uppercase;\n"
                                              "font-weight: bold\n"
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
                                              "}\n"
                                              "")
        self.dt_VencimentoVenda.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dt_VencimentoVenda.setCalendarPopup(True)
        self.dt_VencimentoVenda.setObjectName("dt_VencimentoVenda")
        self.lb_FormVenda5 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda5.setGeometry(QtCore.QRect(10, 155, 150, 15))
        self.lb_FormVenda5.setStyleSheet("QLabel{\n"
                                         "font-size: 10px;\n"
                                         "font-family: \"Arial\";\n"
                                         "font-weight: bold;\n"
                                         "color: #277298;\n"
                                         "border: none\n"
                                         "}")
        self.lb_FormVenda5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda5.setObjectName("lb_FormVenda5")
        self.lb_FormVenda2 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda2.setGeometry(QtCore.QRect(230, 55, 100, 20))
        self.lb_FormVenda2.setStyleSheet("QLabel{\n"
                                         "font-size: 10px;\n"
                                         "font-family: \"Arial\";\n"
                                         "font-weight: bold;\n"
                                         "color: #277298;\n"
                                         "border: none\n"
                                         "}")
        self.lb_FormVenda2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda2.setObjectName("lb_FormVenda2")
        self.lb_ValorPendente = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_ValorPendente.setGeometry(QtCore.QRect(230, 75, 100, 25))
        self.lb_ValorPendente.setStyleSheet("QLabel{\n"
                                            "font-size: 20px;\n"
                                            "font-family: \"Arial\";\n"
                                            "font-weight: bold;\n"
                                            "color: #277298;\n"
                                            "border: none\n"
                                            "}")
        self.lb_ValorPendente.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_ValorPendente.setObjectName("lb_ValorPendente")
        self.tb_parcelasVenda = QtWidgets.QTableWidget(
            self.fr_financeiroCompra)
        self.tb_parcelasVenda.setGeometry(QtCore.QRect(10, 200, 320, 130))
        self.tb_parcelasVenda.setStyleSheet("QTableView{\n"
                                            "font-family: \"Tahoma\";\n"
                                            "color: #28292A;\n"
                                            "font-size: 12px;\n"
                                            "background: #F1F1F1;\n"
                                            "border: none\n"
                                            "}\n"
                                            "QHeaderView:section{\n"
                                            "background: #F1F1F1;\n"
                                            "padding: 3px 0 ;\n"
                                            "font-size: 10px;\n"
                                            "font-family: \"Arial\";\n"
                                            "font-weight: bold;\n"
                                            "color: #000;\n"
                                            "border: none;\n"
                                            "border-bottom: 2px solid #CCC;\n"
                                            "text-transform: uppercase;\n"
                                            "margin: 0 1px 0 0;\n"
                                            "}\n"
                                            "QTableView::item {\n"
                                            "border-bottom: 1px solid #CCC;\n"
                                            "padding: 1px;\n"
                                            "margin: 0 1px 0 0;\n"
                                            "\n"
                                            "}\n"
                                            "QTableView QAbstractItemView {\n"
                                            "    border: none;\n"
                                            "    background: #F1F1F1;\n"
                                            "\n"
                                            "}\n"
                                            "")
        self.tb_parcelasVenda.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_parcelasVenda.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_parcelasVenda.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb_parcelasVenda.setShowGrid(False)
        self.tb_parcelasVenda.setObjectName("tb_parcelasVenda")
        self.tb_parcelasVenda.setColumnCount(5)
        self.tb_parcelasVenda.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_parcelasVenda.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_parcelasVenda.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_parcelasVenda.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_parcelasVenda.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_parcelasVenda.setHorizontalHeaderItem(4, item)
        self.tb_parcelasVenda.horizontalHeader().setDefaultSectionSize(80)
        self.tb_parcelasVenda.horizontalHeader().setMinimumSectionSize(40)
        self.tb_parcelasVenda.verticalHeader().setVisible(False)
        self.tb_parcelasVenda.verticalHeader().setDefaultSectionSize(25)
        self.tx_ValorPago = QtWidgets.QLineEdit(self.fr_financeiroCompra)
        self.tx_ValorPago.setEnabled(False)
        self.tx_ValorPago.setGeometry(QtCore.QRect(120, 75, 100, 25))
        self.tx_ValorPago.setStyleSheet("\n"
                                        "font-size: 24px;\n"
                                        "font-family: \"Arial\";\n"
                                        "font-weight: bold;\n"
                                        "color: #277298;\n"
                                        "border: none\n"
                                        "\n"
                                        "")
        self.tx_ValorPago.setText("")
        self.tx_ValorPago.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_ValorPago.setReadOnly(True)
        self.tx_ValorPago.setObjectName("tx_ValorPago")
        self.lb_FormVenda3 = QtWidgets.QLabel(self.fr_financeiroCompra)
        self.lb_FormVenda3.setGeometry(QtCore.QRect(120, 55, 100, 20))
        self.lb_FormVenda3.setStyleSheet("QLabel{\n"
                                         "font-size: 10px;\n"
                                         "font-family: \"Arial\";\n"
                                         "font-weight: bold;\n"
                                         "color: #277298;\n"
                                         "border: none\n"
                                         "}")
        self.lb_FormVenda3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda3.setObjectName("lb_FormVenda3")

        self.tradFormCompra(ct_FormCompra)
        QtCore.QMetaObject.connectSlotsByName(ct_FormCompra)
        ct_FormCompra.setTabOrder(
            self.tx_CodCompra, self.tx_CodFornecedorCompra)
        ct_FormCompra.setTabOrder(
            self.tx_CodFornecedorCompra, self.tx_FornecedorCompra)
        ct_FormCompra.setTabOrder(
            self.tx_FornecedorCompra, self.tx_TelefoneFornecedorCompra)
        ct_FormCompra.setTabOrder(
            self.tx_TelefoneFornecedorCompra, self.tx_IdBuscaItem)
        ct_FormCompra.setTabOrder(self.tx_IdBuscaItem, self.tx_BuscaItem)
        ct_FormCompra.setTabOrder(self.tx_BuscaItem, self.tx_QntdItem)
        ct_FormCompra.setTabOrder(self.tx_QntdItem, self.tx_ValorUnitarioItem)
        ct_FormCompra.setTabOrder(
            self.tx_ValorUnitarioItem, self.tx_ObsItemCompra)
        ct_FormCompra.setTabOrder(self.tx_ObsItemCompra, self.dt_EmissaoCompra)
        ct_FormCompra.setTabOrder(self.dt_EmissaoCompra, self.dt_PrazoEntrega)
        ct_FormCompra.setTabOrder(self.dt_PrazoEntrega, self.tx_ValorTotalItem)
        ct_FormCompra.setTabOrder(self.tx_ValorTotalItem, self.tb_ItensCompra)

    def tradFormCompra(self, ct_FormCompra):
        _translate = QtCore.QCoreApplication.translate
        ct_FormCompra.setWindowTitle(_translate("ct_FormCompra", "Frame"))
        self.lb_FormCompra.setText(_translate("ct_FormCompra", "COMPRA"))
        self.bt_CancelarCompra.setText(_translate("ct_FormCompra", "CANCELAR"))
        self.bt_SalvarCompra.setText(_translate("ct_FormCompra", "SALVAR"))
        self.bt_ImprimirCompra.setText(_translate("ct_FormCompra", "IMPRIMIR"))
        self.tx_FornecedorCompra.setPlaceholderText(
            _translate("ct_FormCompra", "NOME CLIENTE"))
        self.dt_EmissaoCompra.setDisplayFormat(
            _translate("ct_FormCompra", "dd/MM/yyyy"))
        self.lb_FormCompra1.setText(
            _translate("ct_FormCompra", "DATA EMISSÃO"))
        self.dt_PrazoEntrega.setDisplayFormat(
            _translate("ct_FormCompra", "dd/MM/yyyy"))
        self.lb_FormCompra2.setText(
            _translate("ct_FormCompra", "PRAZO ENTREGA"))
        self.lb_FormCompra3.setText(
            _translate("ct_FormCompra", "DATA ENTREGA"))
        self.dt_EntregaCompra.setDisplayFormat(
            _translate("ct_FormCompra", "dd/MM/yyyy"))
        self.lb_FormCompra.setText(_translate("ct_FormCompra", "FORNECEDOR"))
        self.lb_FormCompra_3.setText(
            _translate("ct_FormCompra", "CÓD. FORNEC."))
        self.tx_CodFornecedorCompra.setPlaceholderText(
            _translate("ct_FormCompra", "0"))
        self.lb_FormCompra_4.setText(_translate("ct_FormCompra", "ITENS"))
        self.tx_BuscaItem.setPlaceholderText(
            _translate("ct_FormCompra", "DIGITE O NOME  DO ITEM"))
        self.lb_FormCompra_6.setText(
            _translate("ct_FormCompra", "UNITÁRIO (R$)"))
        self.tx_ValorUnitarioItem.setPlaceholderText(
            _translate("ct_FormCompra", "0,00"))
        self.lb_FormCompra_7.setText(_translate("ct_FormCompra", "TOTAL (R$)"))
        self.tx_ValorTotalItem.setPlaceholderText(
            _translate("ct_FormCompra", "0,00"))
        self.tx_ObsItemCompra.setPlaceholderText(
            _translate("ct_FormCompra", "OBSERVAÇÃO"))
        self.tx_IdBuscaItem.setPlaceholderText(
            _translate("ct_FormCompra", "CÓD"))
        self.tx_QntdItem.setPlaceholderText(
            _translate("ct_FormCompra", "QTDE."))
        self.lb_FormCompra_5.setText(_translate("ct_FormCompra", "TELEFONE"))
        self.tx_TelefoneFornecedorCompra.setPlaceholderText(
            _translate("ct_FormCompra", "(00) 00000-00"))
        item = self.tb_ItensCompra.horizontalHeaderItem(1)
        item.setText(_translate("ct_FormCompra", "PRODUTO"))
        item = self.tb_ItensCompra.horizontalHeaderItem(2)
        item.setText(_translate("ct_FormCompra", "OBS"))
        item = self.tb_ItensCompra.horizontalHeaderItem(3)
        item.setText(_translate("ct_FormCompra", "QUANTIDADE"))
        item = self.tb_ItensCompra.horizontalHeaderItem(4)
        item.setText(_translate("ct_FormCompra", "UNITÁRIO (R$)"))
        item = self.tb_ItensCompra.horizontalHeaderItem(5)
        item.setText(_translate("ct_FormCompra", "TOTAL (R$)"))
        item = self.tb_ItensCompra.horizontalHeaderItem(6)
        item.setText(_translate("ct_FormCompra", "EXCLUIR"))
        self.tx_Desconto.setText(_translate("ct_FormCompra", "0.00"))
        self.tx_Desconto.setPlaceholderText(
            _translate("ct_FormCompra", "R$ 0.00"))
        self.lb_FormVenda_14.setText(_translate("ct_FormCompra", "DESCONTO"))
        self.tx_Frete.setText(_translate("ct_FormCompra", "0.00"))
        self.tx_Frete.setPlaceholderText(
            _translate("ct_FormCompra", "R$ 0.00"))
        self.lb_FormVenda_17.setText(_translate("ct_FormCompra", "FRETE"))
        self.lb_SubTotalCompra.setText(_translate("ct_FormCompra", "0"))
        self.lb_FormVenda_18.setText(
            _translate("ct_FormCompra", "SUBTOTAL (R$)"))
        self.lb_FormVenda_19.setText(_translate(
            "ct_FormCompra", "TOTAL FINAL (R$)"))
        self.bt_GerarParcelaCompra.setText(
            _translate("ct_FormCompra", "GERAR  CONTAS"))
        self.tx_TotalFinal.setPlaceholderText(
            _translate("ct_FormCompra", "0.00"))
        self.cb_FormaPagamentoVenda.setItemText(
            1, _translate("ct_FormCompra", "DINHEIRO"))
        self.cb_FormaPagamentoVenda.setItemText(
            2, _translate("ct_FormCompra", "CARTÂO"))
        self.lb_FormVenda0.setText(_translate(
            "ct_FormCompra", "FORMA DE PAGAMENTO"))
        self.cb_ParcelamentoVenda.setItemText(
            1, _translate("ct_FormCompra", "À VISTA"))
        self.cb_ParcelamentoVenda.setItemText(
            2, _translate("ct_FormCompra", "ENTRADA + 01"))
        self.cb_ParcelamentoVenda.setItemText(
            3, _translate("ct_FormCompra", "ENTRADA + 02"))
        self.cb_ParcelamentoVenda.setItemText(
            4, _translate("ct_FormCompra", "ENTRADA + 03"))
        self.lb_FormVenda1.setText(
            _translate("ct_FormCompra", "PARCELAMENTO"))
        self.dt_VencimentoVenda.setDisplayFormat(
            _translate("ct_FormCompra", "dd/MM/yyyy"))
        self.lb_FormVenda5.setText(_translate("ct_FormCompra", "VENCIMENTO"))
        self.lb_FormVenda2.setText(
            _translate("ct_FormCompra", "VALOR PENDENTE"))
        self.lb_ValorPendente.setText(_translate("ct_FormCompra", "0.00"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(0)
        item.setText(_translate("ct_FormCompra", "idConta"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(1)
        item.setText(_translate("ct_FormCompra", "Vencimento"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(2)
        item.setText(_translate("ct_FormCompra", "Valor"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(3)
        item.setText(_translate("ct_FormCompra", "Saldo"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(4)
        item.setText(_translate("ct_FormCompra", "Receber"))
        self.tx_ValorPago.setPlaceholderText(
            _translate("ct_FormCompra", "0.00"))
        self.lb_FormVenda3.setText(_translate("ct_FormCompra", "VALOR PAGO"))
