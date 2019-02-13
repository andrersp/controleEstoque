# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtWidgets, QtGui
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
        self.IconeBotaoMenu(self.bt_AddCategoriaProduto,
                            self.resourcepath('Images/edit-add.png'))
        self.IconeBotaoMenu(self.bt_CancelAddCatergoria,
                            self.resourcepath('Images/edit-delete.png'))
        self.bt_CancelAddCatergoria.setHidden(True)
        self.tx_addCategoria.setHidden(True)

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
        self.cb_categoria.setDisabled(True)
        self.dt_Vencimento.setDisabled(True)
        self.bt_AddCategoriaProduto.setDisabled(True)
        self.bt_CancelAddCatergoria.setDisabled(True)

    def cboxRepedir(self, cbox):
        cbox.addItem("Não Repetir", str(1))
        for i in range(2, 13):
            cbox.addItem("{} Vezes".format(i), str(i))

    # Ocultando e mostando campo add categoria
    def AddCategoriaFinanceiro(self):
        self.cb_categoria.setHidden(True)
        self.bt_AddCategoriaProduto.setHidden(True)
        self.bt_CancelAddCatergoria.setVisible(True)
        self.tx_addCategoria.setVisible(True)
        self.tx_addCategoria.setFocus()
    # Fim Botoes Categoria e Marca

    # Cancelado Add Marca / Categoria
    def CalcelAddFinanceiro(self, *args):
        args[0].setHidden(True)
        args[1].setVisible(True)
        args[2].setHidden(True)
        args[3].setVisible(True)
        args[3].setFocus()

    def ValidaInputInt(self, campo):
        # Setando Validadot Int nos campos
        validaInt = QtGui.QIntValidator(0, 9999)
        campo.setValidator(validaInt)

    def ValidaInputFloat(self, campo):
        validarValor = QtGui.QDoubleValidator(0.00, 999.99, 2)
        validarValor.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validarValor.setDecimals(2)
        campo.setValidator(validarValor)
