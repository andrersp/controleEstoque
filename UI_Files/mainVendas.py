from PySide2 import QtCore, QtGui, QtWidgets


class Completer(QtWidgets.QCompleter):

    def __init__(self, *args, **kwargs):
        super(Completer, self).__init__(*args, **kwargs)
        self.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.setWrapAround(False)

    # Add texts instead of replace
    def pathFromIndex(self, index):
        path = QtWidgets.QCompleter.pathFromIndex(self, index)
        lst = str(self.widget().text()).split(',')
        if len(lst) > 1:
            path = '%s, %s' % (','.join(lst[:-1]), path)
        return path

    def splitPath(self, path):
        path = str(path.split(',')[-1]).lstrip(' ')
        return [path]


class TextEdit(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        words = ["alpha", "omega", "omicron", "zeta"]
        self.setPlaceholderText("example : ")
        self._completer = Completer(words, self)
        self.setCompleter(self._completer)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = TextEdit()
    w.show()
    sys.exit(app.exec_())
