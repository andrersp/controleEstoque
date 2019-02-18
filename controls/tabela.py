# -*- codding: utf-8 -*-
from PySide2 import QtWidgets


class ControlTabela(object):

    # DateEdit Tabela usado
    def dt_tabela(self, tabela, row, col, data, status):
        item = QtWidgets.QDateEdit()
        # item.setGeometry(QtCore.QRect(120, 18, 140, 18))
        item.setFixedWidth(90)
        if status == 1:
            item.setReadOnly(True)
        item.setStyleSheet("QDateEdit {\n"
                           "background: #FFF;\n"
                           "border: none;\n"
                           "font-family: \"Arial\";\n"
                           "font-size: 12px;\n"
                           "font-weight: bold;\n"
                           "color: rgb(80,79,79)\n"
                           "}\n"
                           " QDateEdit::drop-down {\n"
                           "     subcontrol-origin: padding;\n"
                           "     subcontrol-position: top right;\n"
                           "     width: 20px;\n"
                           "     border-left-width: 1px;\n"
                           "     border-left-color: darkgray;\n"
                           "     border-left-style: solid; \n"
                           "     border-top-right-radius: 3px; \n"
                           "     border-bottom-right-radius: 3px;\n"
                           " }\n"
                           "QDateEdit::down-arrow {\n"
                           "     image: url(" +
                           self.resourcepath('Images/down.png')+");\n"
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
        item.setCalendarPopup(True)
        item.setDate(data)
        tabela.setCellWidget(row, col, item)

    def TabelaNomeTelefone(self, tabela, row, col, nome, telefone):
        item = QtWidgets.QTextBrowser()
        # item.setFixedSize(250, 60)
        item.setStyleSheet('background: #FFF')
        item.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        item.setOpenLinks(False)
        html = (("""<p align="center">
        <strong>
        <span style="font-size:15px;">{}</span>
        </strong><br />
        <span style="font-size:12px; color: #000;"> {}</span>
        </p>
        """)).format(nome, telefone)
        item.setHtml(html)
        tabela.setCellWidget(row, col, item)
