# -*- coding: utf-8 -*-
from PySide2 import QtGui, QtCore, QtWidgets


class Funcao(object):

    def LimpaFrame(self, frame):
        for i in range(len(frame.children())):
            frame.children()[i].deleteLater()

    def DesativaBotao(self, frame, botao):
        for filho in frame.findChildren(QtWidgets.QPushButton):
            filho.setEnabled(True)

        botao.setEnabled(False)

    def ativaBotoes(self, frame):
        for filho in frame.findChildren(QtWidgets.QPushButton):
            filho.setEnabled(True)

    def IconeBotaoTopo(self, botao, imagem):

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imagem),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap((os.path.join(caminho, imagem)),
        #                              QtGui.QIcon.Normal, QtGui.QIcon.Off))
        botao.setIcon(icon)
        botao.setIconSize(QtCore.QSize(50, 35))

    def IconeBotaoMenu(self, botao, imagem):

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imagem),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QtCore.QSize(25, 25))

    def IconeBotaoForm(self, botao, imagem):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imagem),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QtCore.QSize(80, 35))
