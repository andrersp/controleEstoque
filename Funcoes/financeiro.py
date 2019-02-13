# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtWidgets
from functools import partial
# from Crud.CrudProdutos import CrudProdutos


class Financeiro(object):
    # Setando Datas Padrão
    def setDataFinanceiro(self):
        # Setando Data Padrão
        self.dt_Inicio.setDate(self.primeiroDiaMes())
        self.dt_Fim.setDate(self.ultimoDiaMes())
        pass

    # Setando Data Vencimento e data Pagamento
    def setDataVencPgto(self):
        self.dt_Vencimento.setDate(QtCore.QDate.currentDate())
        self.dt_dataPagamento.setDate(QtCore.QDate.currentDate())

    def setIconFinanceiro(self):
        # Icone dos botoes
        self.IconeBotaoMenu(self.bt_Busca,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_Print,
                            self.resourcepath('Images/gtk-print.png'))
        self.IconeBotaoForm(self.bt_AddConta,
                            self.resourcepath('Images/addConta.svg'))

        pass

    def setIconFormFinanceiro(self):
        self.IconeBotaoMenu(self.bt_Salvar,
                            self.resourcepath('Images/salvar.png'))

        self.IconeBotaoMenu(self.bt_Voltar,
                            self.resourcepath('Images/cancelar.png'))

        self.IconeBotaoMenu(self.bt_Imprimir,
                            self.resourcepath('Images/gtk-print.png'))

    def tamanhoTabelaFinanceiro(self, frame):
        for tabela in frame.findChildren(QtWidgets.QTableWidget):
            tabela.blockSignals(True)
            tabela.setColumnHidden(0, True)
            tabela.setColumnWidth(1, 10)
            tabela.setColumnWidth(2, 270)
            tabela.setColumnWidth(3, 260)
            tabela.setColumnWidth(4, 120)
            tabela.setColumnWidth(5, 107)
            tabela.setColumnWidth(6, 107)
            tabela.setColumnWidth(7, 40)
        pass

    # Setando auto complete
    def setAutocompleteFinanceiro(self):
        # Setando Auto complete
        self.completer = QtWidgets.QCompleter(self)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.model = QtCore.QStringListModel(self)
        self.completer.setModel(self.model)
        self.tx_NomeFantasia.setCompleter(self.completer)

    def desabilitaLineEdit(self, frame):
        for filho in frame.findChildren(QtWidgets.QLineEdit):
            filho.setReadOnly(True)
