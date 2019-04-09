# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainConfig.ui',
# licensing of 'mainConfig.ui' applies.
#
# Created: Sat Mar 23 13:32:36 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_MainConfig(object):
    def setMainConfig(self, ct_MainConfig):
        ct_MainConfig.setObjectName("ct_MainConfig")
        ct_MainConfig.resize(1000, 600)
        ct_MainConfig.setStyleSheet("border:none")
        self.frameMainConfig = QtWidgets.QFrame(ct_MainConfig)
        self.frameMainConfig.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainConfig.setObjectName("frameMainConfig")
        self.fr_TituloConfig = QtWidgets.QFrame(self.frameMainConfig)
        self.fr_TituloConfig.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloConfig.setStyleSheet("border: none")
        self.fr_TituloConfig.setObjectName("fr_TituloConfig")
        self.lb_tituloConfig = QtWidgets.QLabel(self.fr_TituloConfig)
        self.lb_tituloConfig.setGeometry(QtCore.QRect(10, 15, 271, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.lb_tituloConfig.setFont(font)
        self.lb_tituloConfig.setStyleSheet("color: #FFF")
        self.lb_tituloConfig.setObjectName("lb_tituloConfig")
        self.ct_config = QtWidgets.QFrame(self.frameMainConfig)
        self.ct_config.setGeometry(QtCore.QRect(0, 100, 1000, 500))
        self.ct_config.setStyleSheet("background: #FFF;\n"
                                     "border: none")
        self.ct_config.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ct_config.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ct_config.setObjectName("ct_config")
        self.fr_menuConfig = QtWidgets.QFrame(self.frameMainConfig)
        self.fr_menuConfig.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_menuConfig.setStyleSheet("background:#E1DFE0;\n"
                                         "border: none;\n"
                                         "border-bottom: 2px solid #069;")
        self.fr_menuConfig.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_menuConfig.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_menuConfig.setObjectName("fr_menuConfig")
        self.bt_confEmpresa = QtWidgets.QPushButton(self.fr_menuConfig)
        self.bt_confEmpresa.setGeometry(QtCore.QRect(5, 2, 170, 36))
        font = QtGui.QFont()
        font.setFamily("Arial [Mono]")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_confEmpresa.setFont(font)
        self.bt_confEmpresa.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_confEmpresa.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_confEmpresa.setAutoFillBackground(False)
        self.bt_confEmpresa.setStyleSheet("QPushButton{\n"
                                          "background: #40A286 ;\n"
                                          "border: none;\n"
                                          "color: #FFF;\n"
                                          "border-top-left-radius: 4px;\n"
                                          "border-top-right-radius: 4px;\n"
                                          "margin-top: 7px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background: #7AB32E;\n"
                                          "margin-top: 0;\n"
                                          "}\n"
                                          "QPushButton:disabled {\n"
                                          "background: #7AB32E;\n"
                                          "margin-top: 0;\n"
                                          "}\n"
                                          "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../../RSP/Images/icon/tag-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_confEmpresa.setIcon(icon)
        self.bt_confEmpresa.setIconSize(QtCore.QSize(25, 25))
        self.bt_confEmpresa.setFlat(True)
        self.bt_confEmpresa.setObjectName("bt_confEmpresa")
        self.bt_confUser = QtWidgets.QPushButton(self.fr_menuConfig)
        self.bt_confUser.setGeometry(QtCore.QRect(185, 2, 170, 36))
        font = QtGui.QFont()
        font.setFamily("Arial [Mono]")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_confUser.setFont(font)
        self.bt_confUser.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_confUser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_confUser.setAutoFillBackground(False)
        self.bt_confUser.setStyleSheet("QPushButton{\n"
                                       "background: #40A286 ;\n"
                                       "border: none;\n"
                                       "color: #FFF;\n"
                                       "border-top-left-radius: 4px;\n"
                                       "border-top-right-radius: 4px;\n"
                                       "margin-top: 7px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "background: #7AB32E;\n"
                                       "margin-top: 0;\n"
                                       "}\n"
                                       "QPushButton:disabled {\n"
                                       "background: #7AB32E;\n"
                                       "margin-top: 0;\n"
                                       "}\n"
                                       "")
        self.bt_confUser.setIcon(icon)
        self.bt_confUser.setIconSize(QtCore.QSize(25, 25))
        self.bt_confUser.setFlat(True)
        self.bt_confUser.setObjectName("bt_confUser")
        self.bt_confDB = QtWidgets.QPushButton(self.fr_menuConfig)
        self.bt_confDB.setEnabled(True)
        self.bt_confDB.setGeometry(QtCore.QRect(365, 2, 170, 36))
        font = QtGui.QFont()
        font.setFamily("Arial [Mono]")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_confDB.setFont(font)
        self.bt_confDB.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_confDB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_confDB.setAutoFillBackground(False)
        self.bt_confDB.setStyleSheet("QPushButton{\n"
                                     "background: #40A286 ;\n"
                                     "border: none;\n"
                                     "color: #FFF;\n"
                                     "border-top-left-radius: 4px;\n"
                                     "border-top-right-radius: 4px;\n"
                                     "margin-top: 7px;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "background: #7AB32E;\n"
                                     "margin-top: 0;\n"
                                     "}\n"
                                     "QPushButton:disabled {\n"
                                     "background: #7AB32E;\n"
                                     "margin-top: 0;\n"
                                     "}\n"
                                     "")
        self.bt_confDB.setIcon(icon)
        self.bt_confDB.setIconSize(QtCore.QSize(25, 25))
        self.bt_confDB.setFlat(True)
        self.bt_confDB.setObjectName("bt_confDB")

        self.tradMainConfig(ct_MainConfig)
        QtCore.QMetaObject.connectSlotsByName(ct_MainConfig)

    def tradMainConfig(self, ct_MainConfig):
        ct_MainConfig.setWindowTitle(QtWidgets.QApplication.translate(
            "ct_MainConfig", "Frame", None, -1))
        self.lb_tituloConfig.setText(QtWidgets.QApplication.translate(
            "ct_MainConfig", "CONFIGURAÇÃO", None, -1))
        self.bt_confEmpresa.setText(QtWidgets.QApplication.translate(
            "ct_MainConfig", "EMPRESA", None, -1))
        self.bt_confEmpresa.setShortcut(
            QtWidgets.QApplication.translate("ct_MainConfig", "F7", None, -1))
        self.bt_confUser.setText(QtWidgets.QApplication.translate(
            "ct_MainConfig", "USUÁRIOS", None, -1))
        self.bt_confUser.setShortcut(
            QtWidgets.QApplication.translate("ct_MainConfig", "F7", None, -1))
        self.bt_confDB.setText(QtWidgets.QApplication.translate(
            "ct_MainConfig", "BANCO DE DADOS", None, -1))
        self.bt_confDB.setShortcut(
            QtWidgets.QApplication.translate("ct_MainConfig", "F7", None, -1))
