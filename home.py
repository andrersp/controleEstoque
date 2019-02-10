# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from Views.home import Ui_ct_Home


class MainHome(Ui_ct_Home):

    def main_home(self, frame):
        super(MainHome, self).setHome(frame)
        self.HomeFrame.show()
