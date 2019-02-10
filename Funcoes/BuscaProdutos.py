import sys
import sqlite3
import time
import datetime
from PySide2 import QtCore, QtGui, QtWidgets
import mysql.connector
conn = mysql.connector.connect(host="127.0.0.1", database="sistema", user="andre",
                               password="rsp", charset="utf8", use_unicode=True)
c = conn.cursor()


class window(QtGui.QMainWindow):

    # Defines Initial Window Settings
    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(650, 300, 500, 400)  # window geometry
        self.home()

    def home(self):
        self.edit = QtWidgets.QPushButton(self)
        self.edit.move(250, 250)
        self.completer = QtWidgets.QCompleter(self)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setCompletionMode(1)
        self.edit.setCompleter(self.completer)
        self.model = QtCore.QStringListModel(self)
        self.completer.setModel(self.model)
        self.edit.textEdited.connect(self.get_data)
        self.edit.returnPressed.connect(self.teste)
        # self.get_data()
        self.show()

    def get_data(self):
        nome = self.edit.text()
        c.execute(
            """ SELECT apelido FROM clientes WHERE apelido LIKE '%{}%' """.format(nome))
        results = c.fetchall()
        new_list = [i[0] for i in results]
        print(new_list)  # Test print
        # From here up I was able to get the
        self.model.setStringList(new_list)
        # code to work but there's no auto completion in the QLineEdit.

    def teste(self):
        nome = self.edit.text()
        c.execute(
            """ SELECT * FROM clientes WHERE apelido LIKE '%{}%' """.format(nome))
        busca = c.fetchone()
        print busca[0]


def run():
    app = QtGui.QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
