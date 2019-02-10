# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
from Views.mainFinanceiro import Ui_ct_MainFinanceiro
from movconta import MainMovimentoConta
from areceber import MainAReceber
from apagar import MainAPagar
from Funcoes.data import DataAtual


class MainFinanceiro(Ui_ct_MainFinanceiro, DataAtual, MainMovimentoConta,
                     MainAReceber, MainAPagar):

    def mainfinanceiro(self, frame):
        super(MainFinanceiro, self).setMainFinanceiro(frame)
        self.frameMainFinanceiro.show()

        # Abrindo janena Movimento Financeiro
        self.JanelaMovimento()

        """ Chamando funcoes ao clicar nos botoes """
        # Movimento Financeiro
        self.bt_MovCaixa.clicked.connect(self.JanelaMovimento)

        # Conta a Receber
        self.bt_AReceber.clicked.connect(self.JanelaAReceber)

        # Conta a Receber
        self.bt_APagar.clicked.connect(self.JanelaAPagar)

    def JanelaMovimento(self):
        self.LimpaFrame(self.ct_financeiro)
        self.DesativaBotao(self.fr_menuFinanceiro, self.bt_MovCaixa)
        self.mainmovconta(self.ct_financeiro)

    def JanelaAReceber(self):
        self.LimpaFrame(self.ct_financeiro)
        self.DesativaBotao(self.fr_menuFinanceiro, self.bt_AReceber)
        self.mainAReceber(self.ct_financeiro)

    def JanelaAPagar(self):
        self.LimpaFrame(self.ct_financeiro)
        self.DesativaBotao(self.fr_menuFinanceiro, self.bt_APagar)
        self.mainAPagar(self.ct_financeiro)
