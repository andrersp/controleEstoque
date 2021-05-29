# -*- coding: utf-8 -*-
from Views.mainFinanceiro import Ui_ct_MainFinanceiro
from movconta import MainMovimentoConta
from areceber import MainAReceber
from apagar import MainAPagar
from Funcoes.data import DataAtual


class MainFinanceiro(Ui_ct_MainFinanceiro, DataAtual, MainMovimentoConta,
                     MainAReceber, MainAPagar):

    def mainfinanceiro(self, frame):
        super(MainFinanceiro, self).setMainFinanceiro(frame)

        # Ocultando botoes ainda sem funcção
        self.bt_ajustesFinanceiro.setHidden(True)
        self.bt_relatCompras.setHidden(True)
        self.bt_relatVendas.setHidden(True)

        self.frameMainFinanceiro.show()

        """ Chamando funcoes ao clicar nos botoes """
        # Movimento Financeiro
        self.bt_MovCaixa.clicked.connect(self.JanelaMovimento)

        # Conta a Receber
        self.bt_AReceber.clicked.connect(self.JanelaAReceber)

        # Conta a Receber
        self.bt_APagar.clicked.connect(self.JanelaAPagar)

        # Abrindo janena Movimento Financeiro
        self.JanelaMovimento()

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
