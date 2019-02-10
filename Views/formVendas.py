# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formVendas.ui'
#
# Created by: PySide2 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ct_FormVenda(object):
    def setFormVenda(self, ct_FormVenda):
        ct_FormVenda.setObjectName("ct_FormVenda")
        ct_FormVenda.resize(1000, 500)
        ct_FormVenda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormVenda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormVenda = QtWidgets.QFrame(ct_FormVenda)
        self.fr_FormVenda.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormVenda.setStyleSheet("background: #FFF;\n"
                                        "border: none")
        self.fr_FormVenda.setObjectName("fr_FormVenda")
        self.lb_FormVenda = QtWidgets.QLabel(self.fr_FormVenda)
        self.lb_FormVenda.setGeometry(QtCore.QRect(20, 10, 960, 20))
        self.lb_FormVenda.setStyleSheet("QLabel{\n"
                                        "font-size: 14px;\n"
                                        "font-family: \"Arial\";\n"
                                        "font-weight: bold;\n"
                                        "color: #A2A2A2;\n"
                                        "}")
        self.lb_FormVenda.setObjectName("lb_FormVenda")
        self.fr_BotoesFormVenda = QtWidgets.QFrame(self.fr_FormVenda)
        self.fr_BotoesFormVenda.setGeometry(QtCore.QRect(0, 460, 1000, 40))
        self.fr_BotoesFormVenda.setStyleSheet("background:#E1DFE0;\n"
                                              "border: none;")
        self.fr_BotoesFormVenda.setObjectName("fr_BotoesFormVenda")
        self.bt_CancelarVenda = QtWidgets.QPushButton(self.fr_BotoesFormVenda)
        self.bt_CancelarVenda.setGeometry(QtCore.QRect(870, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_CancelarVenda.setFont(font)
        self.bt_CancelarVenda.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_CancelarVenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_CancelarVenda.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_CancelarVenda.setStyleSheet("QPushButton {\n"
                                            "background-color: #1E87F0;\n"
                                            "color: #FFF\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color: #40a286\n"
                                            "}")
        self.bt_CancelarVenda.setObjectName("bt_CancelarVenda")
        self.bt_SalvarVenda = QtWidgets.QPushButton(self.fr_BotoesFormVenda)
        self.bt_SalvarVenda.setGeometry(QtCore.QRect(610, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_SalvarVenda.setFont(font)
        self.bt_SalvarVenda.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_SalvarVenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_SalvarVenda.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_SalvarVenda.setStyleSheet("QPushButton {\n"
                                          "background-color: #7AB32E;\n"
                                          "color: #FFF\n"
                                          " }\n"
                                          "QPushButton:hover{\n"
                                          "background-color: #40a286\n"
                                          "}")
        self.bt_SalvarVenda.setObjectName("bt_SalvarVenda")
        self.bt_ImprimirVenda = QtWidgets.QPushButton(self.fr_BotoesFormVenda)
        self.bt_ImprimirVenda.setEnabled(False)
        self.bt_ImprimirVenda.setGeometry(QtCore.QRect(740, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_ImprimirVenda.setFont(font)
        self.bt_ImprimirVenda.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_ImprimirVenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_ImprimirVenda.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_ImprimirVenda.setStyleSheet("QPushButton {\n"
                                            "background-color: #5C9BBC;\n"
                                            "color: #FFF\n"
                                            " }\n"
                                            "QPushButton:hover{\n"
                                            "background-color: #40a286\n"
                                            "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../../../../home/andre/.designer/Images/gtk-print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_ImprimirVenda.setIcon(icon)
        self.bt_ImprimirVenda.setObjectName("bt_ImprimirVenda")
        self.tx_ClienteVenda = QtWidgets.QLineEdit(self.fr_FormVenda)
        self.tx_ClienteVenda.setGeometry(QtCore.QRect(140, 110, 350, 30))
        self.tx_ClienteVenda.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ClienteVenda.setStyleSheet("QLineEdit{\n"
                                           "background: #CFCFCF;\n"
                                           "border-radius: 2px;\n"
                                           "color: #000;\n"
                                           "font: 13px \"Arial\" ;\n"
                                           "text-transform: uppercase;\n"
                                           "}\n"
                                           "QLineEdit:Focus {\n"
                                           "border: 1px solid red;\n"
                                           "}")
        self.tx_ClienteVenda.setObjectName("tx_ClienteVenda")
        self.fr_topoPedido = QtWidgets.QFrame(self.fr_FormVenda)
        self.fr_topoPedido.setGeometry(QtCore.QRect(20, 30, 960, 40))
        self.fr_topoPedido.setStyleSheet("QFrame{\n"
                                         "background: #FFF;\n"
                                         "border: 1px solid #1E87F0;\n"
                                         "}\n"
                                         "")
        self.fr_topoPedido.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_topoPedido.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_topoPedido.setObjectName("fr_topoPedido")
        self.tx_CodPedido = QtWidgets.QLineEdit(self.fr_topoPedido)
        self.tx_CodPedido.setGeometry(QtCore.QRect(0, 0, 100, 40))
        self.tx_CodPedido.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_CodPedido.setStyleSheet("QLineEdit{\n"
                                        "background: #0884C2;\n"
                                        "border-radius: 2px;\n"
                                        "color: #000;\n"
                                        "font: 16px \"Arial\" ;\n"
                                        "font-weight: bold;\n"
                                        "color: #FFF\n"
                                        "}\n"
                                        "")
        self.tx_CodPedido.setText("")
        self.tx_CodPedido.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_CodPedido.setReadOnly(True)
        self.tx_CodPedido.setPlaceholderText("")
        self.tx_CodPedido.setObjectName("tx_CodPedido")
        self.dt_EmissaoPedido = QtWidgets.QDateEdit(self.fr_topoPedido)
        self.dt_EmissaoPedido.setGeometry(QtCore.QRect(120, 18, 140, 18))
        self.dt_EmissaoPedido.setStyleSheet("QDateEdit {\n"
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
        self.dt_EmissaoPedido.setCalendarPopup(True)
        self.dt_EmissaoPedido.setObjectName("dt_EmissaoPedido")
        self.lb_FormVenda_21 = QtWidgets.QLabel(self.fr_topoPedido)
        self.lb_FormVenda_21.setGeometry(QtCore.QRect(120, 2, 120, 18))
        self.lb_FormVenda_21.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_21.setObjectName("lb_FormVenda_21")
        self.dt_PrazoEntrega = QtWidgets.QDateEdit(self.fr_topoPedido)
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
        self.dt_PrazoEntrega.setCalendarPopup(True)
        self.dt_PrazoEntrega.setObjectName("dt_PrazoEntrega")
        self.lb_FormVenda_22 = QtWidgets.QLabel(self.fr_topoPedido)
        self.lb_FormVenda_22.setGeometry(QtCore.QRect(300, 2, 120, 18))
        self.lb_FormVenda_22.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_22.setObjectName("lb_FormVenda_22")
        self.bt_Entregar = QtWidgets.QPushButton(self.fr_topoPedido)
        self.bt_Entregar.setEnabled(False)
        self.bt_Entregar.setGeometry(QtCore.QRect(820, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_Entregar.setFont(font)
        self.bt_Entregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Entregar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Entregar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Entregar.setStyleSheet("QPushButton {\n"
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
        self.bt_Entregar.setIconSize(QtCore.QSize(75, 35))
        self.bt_Entregar.setObjectName("bt_Entregar")
        self.lb_FormVenda_23 = QtWidgets.QLabel(self.fr_topoPedido)
        self.lb_FormVenda_23.setGeometry(QtCore.QRect(480, 2, 120, 18))
        self.lb_FormVenda_23.setStyleSheet("QLabel{\n"
                                           "font-size: 12px;\n"
                                           "font-family: \"Arial Unicode MS\";\n"
                                           "\n"
                                           "color:#1E87F0;\n"
                                           "border: none;\n"
                                           "}")
        self.lb_FormVenda_23.setObjectName("lb_FormVenda_23")
        self.dt_EntregaPedido = QtWidgets.QDateEdit(self.fr_topoPedido)
        self.dt_EntregaPedido.setGeometry(QtCore.QRect(480, 18, 140, 18))
        self.dt_EntregaPedido.setStyleSheet("QDateEdit {\n"
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
        self.dt_EntregaPedido.setCalendarPopup(True)
        self.dt_EntregaPedido.setObjectName("dt_EntregaPedido")
        self.lb_FormVenda_2 = QtWidgets.QLabel(self.fr_FormVenda)
        self.lb_FormVenda_2.setGeometry(QtCore.QRect(140, 90, 120, 20))
        self.lb_FormVenda_2.setStyleSheet("QLabel{\n"
                                          "font-size: 12px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #A2A2A2;\n"
                                          "}")
        self.lb_FormVenda_2.setObjectName("lb_FormVenda_2")
        self.lb_FormVenda_3 = QtWidgets.QLabel(self.fr_FormVenda)
        self.lb_FormVenda_3.setGeometry(QtCore.QRect(20, 90, 100, 20))
        self.lb_FormVenda_3.setStyleSheet("QLabel{\n"
                                          "font-size: 12px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #A2A2A2;\n"
                                          "}")
        self.lb_FormVenda_3.setObjectName("lb_FormVenda_3")
        self.tx_CodClienteVenda = QtWidgets.QLineEdit(self.fr_FormVenda)
        self.tx_CodClienteVenda.setGeometry(QtCore.QRect(20, 110, 100, 30))
        self.tx_CodClienteVenda.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_CodClienteVenda.setStyleSheet("QLineEdit{\n"
                                              "background: #CFCFCF;\n"
                                              "border-radius: 2px;\n"
                                              "color: #000;\n"
                                              "font: 13px \"Arial\" ;\n"
                                              "text-transform: uppercase;\n"
                                              "}\n"
                                              "QLineEdit:Focus {\n"
                                              "border: 1px solid red;\n"
                                              "}")
        self.tx_CodClienteVenda.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_CodClienteVenda.setObjectName("tx_CodClienteVenda")
        self.lb_FormVenda_4 = QtWidgets.QLabel(self.fr_FormVenda)
        self.lb_FormVenda_4.setGeometry(QtCore.QRect(20, 150, 120, 20))
        self.lb_FormVenda_4.setStyleSheet("QLabel{\n"
                                          "font-size: 13px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #A2A2A2;\n"
                                          "}")
        self.lb_FormVenda_4.setObjectName("lb_FormVenda_4")
        self.fr_addProduto = QtWidgets.QFrame(self.fr_FormVenda)
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
        self.lb_FormVenda_6 = QtWidgets.QLabel(self.fr_addProduto)
        self.lb_FormVenda_6.setGeometry(QtCore.QRect(350, 0, 75, 15))
        self.lb_FormVenda_6.setStyleSheet("QLabel{\n"
                                          "font-size: 9px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #A2A2A2;\n"
                                          "border: none;\n"
                                          "}")
        self.lb_FormVenda_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FormVenda_6.setObjectName("lb_FormVenda_6")
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
        self.tx_ValorUnitarioItem.setReadOnly(True)
        self.tx_ValorUnitarioItem.setObjectName("tx_ValorUnitarioItem")
        self.lb_FormVenda_7 = QtWidgets.QLabel(self.fr_addProduto)
        self.lb_FormVenda_7.setGeometry(QtCore.QRect(425, 0, 75, 15))
        self.lb_FormVenda_7.setStyleSheet("QLabel{\n"
                                          "font-size: 9px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #A2A2A2;\n"
                                          "border: none;\n"
                                          "}")
        self.lb_FormVenda_7.setObjectName("lb_FormVenda_7")
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
        self.bt_IncluirItemPedido = QtWidgets.QPushButton(self.fr_addProduto)
        self.bt_IncluirItemPedido.setEnabled(False)
        self.bt_IncluirItemPedido.setGeometry(QtCore.QRect(500, 0, 100, 70))
        self.bt_IncluirItemPedido.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_IncluirItemPedido.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_IncluirItemPedido.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_IncluirItemPedido.setStyleSheet("QPushButton {\n"
                                                "background: #025682;\n"
                                                "\n"
                                                " }\n"
                                                "QPushButton:hover{\n"
                                                "background-color: #5C9BBC\n"
                                                "}")
        self.bt_IncluirItemPedido.setText("")
        self.bt_IncluirItemPedido.setIconSize(QtCore.QSize(75, 35))
        self.bt_IncluirItemPedido.setObjectName("bt_IncluirItemPedido")
        self.tx_ObsItemPedido = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ObsItemPedido.setGeometry(QtCore.QRect(0, 40, 500, 30))
        self.tx_ObsItemPedido.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ObsItemPedido.setStyleSheet("QLineEdit{\n"
                                            "background: #1E87F0;\n"
                                            "border-radius: 2px;\n"
                                            "color: #000;\n"
                                            "font: 12px \"Arial\" ;\n"
                                            "font-weight: bold;\n"
                                            "color: #FFF\n"
                                            "}\n"
                                            "\n"
                                            "")
        self.tx_ObsItemPedido.setText("")
        self.tx_ObsItemPedido.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ObsItemPedido.setReadOnly(False)
        self.tx_ObsItemPedido.setObjectName("tx_ObsItemPedido")
        self.tx_IdBuscaItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_IdBuscaItem.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.tx_IdBuscaItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_IdBuscaItem.setStyleSheet("QLineEdit{\n"
                                          "background: #5C9BBC;\n"
                                          "border-radius: 2px;\n"
                                          "color: #000;\n"
                                          "font: 10px \"Arial\" ;\n"
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
        self.lb_FormVenda_5 = QtWidgets.QLabel(self.fr_FormVenda)
        self.lb_FormVenda_5.setGeometry(QtCore.QRect(510, 90, 120, 20))
        self.lb_FormVenda_5.setStyleSheet("QLabel{\n"
                                          "font-size: 12px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #A2A2A2;\n"
                                          "}")
        self.lb_FormVenda_5.setObjectName("lb_FormVenda_5")
        self.tx_TelefoneClienteVenda = QtWidgets.QLineEdit(self.fr_FormVenda)
        self.tx_TelefoneClienteVenda.setGeometry(
            QtCore.QRect(510, 110, 110, 30))
        self.tx_TelefoneClienteVenda.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_TelefoneClienteVenda.setStyleSheet("QLineEdit{\n"
                                                   "background: #CFCFCF;\n"
                                                   "border-radius: 2px;\n"
                                                   "color: #000;\n"
                                                   "font: 13px \"Arial\" ;\n"
                                                   "text-transform: uppercase;\n"
                                                   "}\n"
                                                   "QLineEdit:Focus {\n"
                                                   "border: 1px solid red;\n"
                                                   "}")
        self.tx_TelefoneClienteVenda.setReadOnly(True)
        self.tx_TelefoneClienteVenda.setObjectName("tx_TelefoneClienteVenda")
        self.tb_Itens = QtWidgets.QTableWidget(self.fr_FormVenda)
        self.tb_Itens.setGeometry(QtCore.QRect(20, 250, 600, 200))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tb_Itens.sizePolicy().hasHeightForWidth())
        self.tb_Itens.setSizePolicy(sizePolicy)
        self.tb_Itens.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Itens.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Itens.setStyleSheet("QTableView{\n"
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
        self.tb_Itens.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Itens.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Itens.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Itens.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Itens.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb_Itens.setAutoScrollMargin(20)
        self.tb_Itens.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Itens.setTabKeyNavigation(False)
        self.tb_Itens.setProperty("showDropIndicator", False)
        self.tb_Itens.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Itens.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Itens.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_Itens.setShowGrid(False)
        self.tb_Itens.setCornerButtonEnabled(False)
        self.tb_Itens.setRowCount(0)
        self.tb_Itens.setObjectName("tb_Itens")
        self.tb_Itens.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Itens.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Itens.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Itens.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Itens.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_Itens.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tb_Itens.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(7, item)
        self.tb_Itens.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Itens.horizontalHeader().setStretchLastSection(True)
        self.tb_Itens.verticalHeader().setVisible(False)
        self.tb_Itens.verticalHeader().setCascadingSectionResizes(True)
        self.tb_Itens.verticalHeader().setDefaultSectionSize(40)
        self.fr_financeiroPedido = QtWidgets.QFrame(self.fr_FormVenda)
        self.fr_financeiroPedido.setGeometry(QtCore.QRect(640, 110, 340, 340))
        self.fr_financeiroPedido.setStyleSheet("background: #F1F1F1;\n"
                                               "border-top: 4px solid #277298;\n"
                                               "border-bottom: 4px solid #277298;")
        self.fr_financeiroPedido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_financeiroPedido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_financeiroPedido.setObjectName("fr_financeiroPedido")
        self.tx_Desconto = QtWidgets.QLineEdit(self.fr_financeiroPedido)
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
        self.tx_Desconto.setInputMask("")
        self.tx_Desconto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_Desconto.setObjectName("tx_Desconto")
        self.lb_FormVenda_9 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_9.setGeometry(QtCore.QRect(120, 5, 90, 20))
        self.lb_FormVenda_9.setStyleSheet("QLabel{\n"
                                          "font-size: 13px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #7B7A7A;\n"
                                          "border: none\n"
                                          "}")
        self.lb_FormVenda_9.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_9.setObjectName("lb_FormVenda_9")
        self.tx_Frete = QtWidgets.QLineEdit(self.fr_financeiroPedido)
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
        self.lb_FormVenda_10 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_10.setGeometry(QtCore.QRect(230, 5, 90, 20))
        self.lb_FormVenda_10.setStyleSheet("QLabel{\n"
                                           "font-size: 13px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #7B7A7A;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_10.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_10.setObjectName("lb_FormVenda_10")
        self.lb_SubTotalVenda = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_SubTotalVenda.setGeometry(QtCore.QRect(0, 25, 100, 25))
        self.lb_SubTotalVenda.setStyleSheet("QLabel{\n"
                                            "font-size: 20px;\n"
                                            "font-family: \"Arial\";\n"
                                            "font-weight: bold;\n"
                                            "color: #277298;\n"
                                            "border: none\n"
                                            "}")
        self.lb_SubTotalVenda.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_SubTotalVenda.setObjectName("lb_SubTotalVenda")
        self.lb_FormVenda_8 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_8.setGeometry(QtCore.QRect(0, 5, 100, 20))
        self.lb_FormVenda_8.setStyleSheet("QLabel{\n"
                                          "font-size: 10px;\n"
                                          "font-family: \"Arial\";\n"
                                          "font-weight: bold;\n"
                                          "color: #277298;\n"
                                          "border: none\n"
                                          "}")
        self.lb_FormVenda_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_8.setObjectName("lb_FormVenda_8")
        self.lb_FormVenda_12 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_12.setGeometry(QtCore.QRect(10, 55, 100, 20))
        self.lb_FormVenda_12.setStyleSheet("QLabel{\n"
                                           "font-size: 10px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #277298;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_12.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_12.setObjectName("lb_FormVenda_12")
        self.bt_GerarParcelaVenda = QtWidgets.QPushButton(
            self.fr_financeiroPedido)
        self.bt_GerarParcelaVenda.setEnabled(False)
        self.bt_GerarParcelaVenda.setGeometry(QtCore.QRect(180, 165, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_GerarParcelaVenda.setFont(font)
        self.bt_GerarParcelaVenda.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_GerarParcelaVenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_GerarParcelaVenda.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)
        self.bt_GerarParcelaVenda.setStyleSheet("QPushButton {\n"
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
        self.bt_GerarParcelaVenda.setIconSize(QtCore.QSize(75, 35))
        self.bt_GerarParcelaVenda.setObjectName("bt_GerarParcelaVenda")
        self.tx_TotalFinal = QtWidgets.QLineEdit(self.fr_financeiroPedido)
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
            self.fr_financeiroPedido)
        self.cb_FormaPagamentoVenda.setGeometry(QtCore.QRect(10, 125, 150, 25))
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
        self.lb_FormVenda_15 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_15.setGeometry(QtCore.QRect(10, 110, 150, 15))
        self.lb_FormVenda_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_FormVenda_15.setStyleSheet("QLabel{\n"
                                           "font-size: 10px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #277298;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_15.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_15.setObjectName("lb_FormVenda_15")
        self.cb_ParcelamentoVenda = QtWidgets.QComboBox(
            self.fr_financeiroPedido)
        self.cb_ParcelamentoVenda.setGeometry(QtCore.QRect(180, 125, 150, 25))
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
        self.lb_FormVenda_16 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_16.setGeometry(QtCore.QRect(180, 110, 150, 15))
        self.lb_FormVenda_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_FormVenda_16.setStyleSheet("QLabel{\n"
                                           "font-size: 10px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #277298;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_16.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_16.setObjectName("lb_FormVenda_16")
        self.dt_VencimentoVenda = QtWidgets.QDateEdit(self.fr_financeiroPedido)
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
        self.lb_FormVenda_24 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_24.setGeometry(QtCore.QRect(10, 155, 150, 15))
        self.lb_FormVenda_24.setStyleSheet("QLabel{\n"
                                           "font-size: 10px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #277298;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_24.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_24.setObjectName("lb_FormVenda_24")
        self.lb_FormVenda_11 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_11.setGeometry(QtCore.QRect(230, 55, 100, 20))
        self.lb_FormVenda_11.setStyleSheet("QLabel{\n"
                                           "font-size: 10px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #277298;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_11.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_11.setObjectName("lb_FormVenda_11")
        self.lb_ValorPendente = QtWidgets.QLabel(self.fr_financeiroPedido)
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
            self.fr_financeiroPedido)
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
        self.tx_valorRecebido = QtWidgets.QLineEdit(self.fr_financeiroPedido)
        self.tx_valorRecebido.setEnabled(False)
        self.tx_valorRecebido.setGeometry(QtCore.QRect(120, 75, 100, 25))
        self.tx_valorRecebido.setStyleSheet("\n"
                                            "font-size: 24px;\n"
                                            "font-family: \"Arial\";\n"
                                            "font-weight: bold;\n"
                                            "color: #277298;\n"
                                            "border: none\n"
                                            "\n"
                                            "")
        self.tx_valorRecebido.setText("")
        self.tx_valorRecebido.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_valorRecebido.setReadOnly(True)
        self.tx_valorRecebido.setObjectName("tx_valorRecebido")
        self.lb_FormVenda_13 = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_FormVenda_13.setGeometry(QtCore.QRect(120, 55, 100, 20))
        self.lb_FormVenda_13.setStyleSheet("QLabel{\n"
                                           "font-size: 10px;\n"
                                           "font-family: \"Arial\";\n"
                                           "font-weight: bold;\n"
                                           "color: #277298;\n"
                                           "border: none\n"
                                           "}")
        self.lb_FormVenda_13.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lb_FormVenda_13.setObjectName("lb_FormVenda_13")

        self.tradFormVenda(ct_FormVenda)
        QtCore.QMetaObject.connectSlotsByName(ct_FormVenda)
        ct_FormVenda.setTabOrder(self.tx_CodPedido, self.tx_CodClienteVenda)
        ct_FormVenda.setTabOrder(self.tx_CodClienteVenda, self.tx_ClienteVenda)
        ct_FormVenda.setTabOrder(self.tx_ClienteVenda,
                                 self.tx_TelefoneClienteVenda)
        ct_FormVenda.setTabOrder(
            self.tx_TelefoneClienteVenda, self.tx_IdBuscaItem)
        ct_FormVenda.setTabOrder(self.tx_IdBuscaItem, self.tx_BuscaItem)
        ct_FormVenda.setTabOrder(self.tx_BuscaItem, self.tx_QntdItem)
        ct_FormVenda.setTabOrder(self.tx_QntdItem, self.tx_ValorUnitarioItem)
        ct_FormVenda.setTabOrder(
            self.tx_ValorUnitarioItem, self.tx_ObsItemPedido)
        ct_FormVenda.setTabOrder(self.tx_ObsItemPedido, self.tx_Desconto)
        ct_FormVenda.setTabOrder(self.tx_Desconto, self.tx_Frete)

        ct_FormVenda.setTabOrder(self.dt_EmissaoPedido, self.dt_PrazoEntrega)
        ct_FormVenda.setTabOrder(self.dt_PrazoEntrega, self.tx_ValorTotalItem)
        ct_FormVenda.setTabOrder(self.tx_ValorTotalItem, self.tb_Itens)
        ct_FormVenda.setTabOrder(self.tb_Itens, self.tx_TotalFinal)

    def tradFormVenda(self, ct_FormVenda):
        _translate = QtCore.QCoreApplication.translate
        ct_FormVenda.setWindowTitle(_translate("ct_FormVenda", "Frame"))
        self.lb_FormVenda.setText(_translate("ct_FormVenda", "PEDIDO"))
        self.bt_CancelarVenda.setText(_translate("ct_FormVenda", "CANCELAR"))
        self.bt_SalvarVenda.setText(_translate("ct_FormVenda", "SALVAR"))
        self.bt_ImprimirVenda.setText(_translate("ct_FormVenda", "IMPRIMIR"))
        self.tx_ClienteVenda.setPlaceholderText(
            _translate("ct_FormVenda", "NOME CLIENTE"))
        self.dt_EmissaoPedido.setDisplayFormat(
            _translate("ct_FormVenda", "dd/MM/yyyy"))
        self.lb_FormVenda_21.setText(
            _translate("ct_FormVenda", "DATA EMISSÃO"))
        self.dt_PrazoEntrega.setDisplayFormat(
            _translate("ct_FormVenda", "dd/MM/yyyy"))
        self.lb_FormVenda_22.setText(
            _translate("ct_FormVenda", "PRAZO ENTREGA"))
        self.bt_Entregar.setText(_translate("ct_FormVenda", "ENTREGAR"))
        self.lb_FormVenda_23.setText(
            _translate("ct_FormVenda", "DATA ENTREGA"))
        self.dt_EntregaPedido.setDisplayFormat(
            _translate("ct_FormVenda", "dd/MM/yyyy"))
        self.lb_FormVenda_2.setText(_translate("ct_FormVenda", "CLIENTE"))
        self.lb_FormVenda_3.setText(_translate("ct_FormVenda", "CÓD. CLIENTE"))
        self.tx_CodClienteVenda.setPlaceholderText(
            _translate("ct_FormVenda", "0"))
        self.lb_FormVenda_4.setText(_translate("ct_FormVenda", "ITENS"))
        self.tx_BuscaItem.setPlaceholderText(
            _translate("ct_FormVenda", "DIGITE O NOME  DO ITEM"))
        self.lb_FormVenda_6.setText(
            _translate("ct_FormVenda", "UNITÁRIO (R$)"))
        self.tx_ValorUnitarioItem.setPlaceholderText(
            _translate("ct_FormVenda", "0,00"))
        self.lb_FormVenda_7.setText(_translate("ct_FormVenda", "TOTAL (R$)"))
        self.tx_ValorTotalItem.setPlaceholderText(
            _translate("ct_FormVenda", "0,00"))
        self.tx_ObsItemPedido.setPlaceholderText(
            _translate("ct_FormVenda", "OBSERVAÇÃO"))
        self.tx_IdBuscaItem.setPlaceholderText(
            _translate("ct_FormVenda", "CÓD"))
        self.tx_QntdItem.setPlaceholderText(
            _translate("ct_FormVenda", "QTDE."))
        self.lb_FormVenda_5.setText(_translate("ct_FormVenda", "TELEFONE"))
        self.tx_TelefoneClienteVenda.setPlaceholderText(
            _translate("ct_FormVenda", "(00) 00000-00"))
        item = self.tb_Itens.horizontalHeaderItem(1)
        item.setText(_translate("ct_FormVenda", "PRODUTO"))
        item = self.tb_Itens.horizontalHeaderItem(2)
        item.setText(_translate("ct_FormVenda", "OBS"))
        item = self.tb_Itens.horizontalHeaderItem(3)
        item.setText(_translate("ct_FormVenda", "QUANTIDADE"))
        item = self.tb_Itens.horizontalHeaderItem(4)
        item.setText(_translate("ct_FormVenda", "UNITÁRIO (R$)"))
        item = self.tb_Itens.horizontalHeaderItem(5)
        item.setText(_translate("ct_FormVenda", "TOTAL (R$)"))
        item = self.tb_Itens.horizontalHeaderItem(6)
        item.setText(_translate("ct_FormVenda", "EXCLUIR"))
        self.tx_Desconto.setText(_translate("ct_FormVenda", "0.00"))
        self.tx_Desconto.setPlaceholderText(
            _translate("ct_FormVenda", "R$ 0.00"))
        self.lb_FormVenda_9.setText(_translate("ct_FormVenda", "DESCONTO"))
        self.tx_Frete.setText(_translate("ct_FormVenda", "0.00"))
        self.tx_Frete.setPlaceholderText(_translate("ct_FormVenda", "R$ 0.00"))
        self.lb_FormVenda_10.setText(_translate("ct_FormVenda", "FRETE"))
        self.lb_SubTotalVenda.setText(_translate("ct_FormVenda", "0"))
        self.lb_FormVenda_8.setText(
            _translate("ct_FormVenda", "SUBTOTAL (R$)"))
        self.lb_FormVenda_12.setText(_translate(
            "ct_FormVenda", "TOTAL FINAL (R$)"))
        self.bt_GerarParcelaVenda.setText(
            _translate("ct_FormVenda", "GERAR  CONTAS"))
        self.tx_TotalFinal.setPlaceholderText(
            _translate("ct_FormVenda", "0.00"))
        self.cb_FormaPagamentoVenda.setItemText(
            1, _translate("ct_FormVenda", "DINHEIRO"))
        self.cb_FormaPagamentoVenda.setItemText(
            2, _translate("ct_FormVenda", "CARTÂO"))
        self.lb_FormVenda_15.setText(_translate(
            "ct_FormVenda", "FORMA DE PAGAMENTO"))
        self.cb_ParcelamentoVenda.setItemText(
            1, _translate("ct_FormVenda", "À VISTA"))
        self.cb_ParcelamentoVenda.setItemText(
            2, _translate("ct_FormVenda", "ENTRADA + 01"))
        self.cb_ParcelamentoVenda.setItemText(
            3, _translate("ct_FormVenda", "ENTRADA + 02"))
        self.cb_ParcelamentoVenda.setItemText(
            4, _translate("ct_FormVenda", "ENTRADA + 03"))
        self.lb_FormVenda_16.setText(
            _translate("ct_FormVenda", "PARCELAMENTO"))
        self.dt_VencimentoVenda.setDisplayFormat(
            _translate("ct_FormVenda", "dd/MM/yyyy"))
        self.lb_FormVenda_24.setText(_translate("ct_FormVenda", "VENCIMENTO"))
        self.lb_FormVenda_11.setText(
            _translate("ct_FormVenda", "VALOR PENDENTE"))
        self.lb_ValorPendente.setText(_translate("ct_FormVenda", "0.00"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(0)
        item.setText(_translate("ct_FormVenda", "idConta"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(1)
        item.setText(_translate("ct_FormVenda", "Vencimento"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(2)
        item.setText(_translate("ct_FormVenda", "Valor"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(3)
        item.setText(_translate("ct_FormVenda", "Saldo"))
        item = self.tb_parcelasVenda.horizontalHeaderItem(4)
        item.setText(_translate("ct_FormVenda", "Receber"))
        self.tx_valorRecebido.setPlaceholderText(
            _translate("ct_FormVenda", "0.00"))
        self.lb_FormVenda_13.setText(
            _translate("ct_FormVenda", "VALOR RECEBIDO"))
