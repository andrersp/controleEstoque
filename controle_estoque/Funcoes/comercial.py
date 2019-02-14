# -*- coding: utf-8 -*-
from PySide2 import QtGui, QtCore, QtWidgets
from functools import partial
from Crud.CrudProdutos import CrudProdutos


class Comercial(object):
    """ Funcoes das Telas de Venda e Compra """

    def validaCampos(self):
        # Setando Validadot Int nos campos
        validaInt = QtGui.QIntValidator(0, 9999)
        self.tx_QntdItem.setValidator(validaInt)
        self.tx_IdBuscaItem.setValidator(validaInt)
        self.tx_Id.setValidator(validaInt)
        # Setando Validador float nos campos
        validarValor = QtGui.QDoubleValidator(0.00, 999.99, 2)
        validarValor.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validarValor.setDecimals(2)
        self.tx_Desconto.setValidator(validarValor)
        self.tx_Frete.setValidator(validarValor)

    # Setando Datas Padrão
    def setDatas(self):
        self.dt_Emissao.setDate(QtCore.QDate.currentDate())
        self.dt_Prazo.setDate(QtCore.QDate.currentDate().addDays(2))
        self.dt_Entrega.setDate(QtCore.QDate.currentDate())
        self.dt_Vencimento.setDate(QtCore.QDate.currentDate())

    # Setando Icone dos Botoes
    def setIcones(self):
        # Icone Botoes
        self.IconeBotaoMenu(self.bt_Salvar,
                            self.resourcepath('Images/salvar.png'))

        self.IconeBotaoMenu(self.bt_Voltar,
                            self.resourcepath('Images/cancelar.png'))

        self.IconeBotaoMenu(
            self.bt_Entregar, self.resourcepath('Images/ico_entrega.png'))

        self.IconeBotaoMenu(self.bt_Imprimir,
                            self.resourcepath('Images/gtk-print.png'))

        self.IconeBotaoMenu(self.bt_GerarParcela,
                            self.resourcepath('Images/ico_conta.png'))

        self.IconeBotaoForm(self.bt_IncluirItem,
                            self.resourcepath('Images/addPedido.svg'))

    # Definindo Tamanho das tabelas
    def tamanhoTabelas(self):
        # Tamanho das Colunas Tabela Itens
        self.tb_Itens.blockSignals(True)
        self.tb_Itens.setColumnHidden(0, True)
        self.tb_Itens.setColumnHidden(7, True)
        self.tb_Itens.resizeRowsToContents()
        self.tb_Itens.setColumnWidth(1, 165)
        self.tb_Itens.setColumnWidth(2, 150)
        self.tb_Itens.setColumnWidth(3, 75)
        self.tb_Itens.setColumnWidth(4, 75)
        self.tb_Itens.setColumnWidth(5, 75)
        self.tb_Itens.setColumnWidth(6, 45)

        # Tamanho tabela parcelas
        self.tb_Parcelas.blockSignals(True)
        self.tb_Parcelas.setColumnHidden(0, True)
        self.tb_Parcelas.setColumnWidth(1, 90)
        self.tb_Parcelas.setColumnWidth(2, 60)
        self.tb_Parcelas.setColumnWidth(3, 80)
        self.tb_Parcelas.setColumnWidth(4, 90)

    def acaoCalculo(self):
        # calculando com desconto
        self.tx_Desconto.returnPressed.connect(self.TotalFinal)
        self.tx_Desconto.returnPressed.connect(self.tx_Frete.setFocus)
        self.tx_Desconto.returnPressed.connect(self.tx_Frete.selectAll)

        # calculando com frete
        self.tx_Frete.returnPressed.connect(self.TotalFinal)
        self.tx_Frete.returnPressed.connect(self.tx_valorRecebido.setFocus)
        self.tx_Frete.returnPressed.connect(self.tx_valorRecebido.selectAll)

    def ValidaFormAdd(self):
        if not self.tx_Id.text():
            self.tx_Id.setFocus()
        elif not self.tx_BuscaItem.text():
            self.tx_BuscaItem.setFocus()
        elif not self.tx_BuscaItem.text():
            self.tx_BuscaItem.setFocus()
        elif not self.tx_QntdItem.text():
            self.tx_QntdItem.setFocus()
        elif not self.tx_NomeFantasia.text():
            self.tx_NomeFantasia.setFocus()
        else:
            self.AddItemTabela()

    # Adiciona Item a tabela
    def AddItemTabela(self):
        row = self.tb_Itens.rowCount()
        self.tb_Itens.insertRow(row)
        self.conteudoTabela(self.tb_Itens, row, 0,
                            self.tx_IdBuscaItem.text())
        self.conteudoTabelaLeft(self.tb_Itens, row, 1,
                                self.tx_BuscaItem.text())
        self.conteudoTabelaLeft(self.tb_Itens, row, 2,
                                self.tx_ObsItem.text())

        self.conteudoTabela(self.tb_Itens, row, 3,
                            self.tx_QntdItem.text())
        self.conteudoTabela(self.tb_Itens, row, 4,
                            self.tx_ValorUnitarioItem.text())
        self.conteudoTabela(self.tb_Itens, row, 5,
                            self.tx_ValorTotalItem.text())
        self.botaoRemoveItem(self.tb_Itens, row, 6,
                             partial(self.RemoveLInha, row), "#005099")

        self.conteudoTabela(self.tb_Itens, row, 7, str(
            QtCore.QDateTime.toMSecsSinceEpoch(QtCore.QDateTime.currentDateTime())))

        self.TotalFinal()
        self.LimpaCampoAddProduto()
        self.bt_GerarParcela.setEnabled(True)

    # Calcular total de Venda e Compra
    def TotalFinal(self):
        total = 0

        if not int(self.tb_Itens.rowCount()) == 0 and self.tb_Itens.item(0, 5).text():
            for row in range(self.tb_Itens.rowCount()):
                total = float(self.tb_Itens.item(row, 5).text()) + total
        self.lb_SubTotal.setText(format(total, ".2f"))
        self.tx_TotalFinal.setText(format(total, ".2f"))
        self.lb_ValorPendente.setText(format(total, ".2f"))

        if self.tx_Desconto.text():
            desconto = self.tx_Desconto.text().replace(',', '.')
            TotalFinal = float(total) - float(desconto)
            self.tx_TotalFinal.setText(format(TotalFinal, ".2f"))
            self.tx_Desconto.setText(
                format(float(desconto), ".2f"))
            self.lb_ValorPendente.setText(format(TotalFinal, ".2f"))

        if self.tx_Frete.text():
            frete = self.tx_Frete.text().replace(',', '.')
            TotalFinal = float(
                total) - float(self.tx_Desconto.text()) + float(frete)
            self.tx_Frete.setText(format(float(frete), ".2f"))
            self.tx_TotalFinal.setText(format(TotalFinal, ".2f"))
            self.lb_ValorPendente.setText(format(TotalFinal, ".2f"))

        if self.tx_valorRecebido.text():
            recebido = self.tx_valorRecebido.text().replace(",", ".")
            TotalFinal = float(self.tx_TotalFinal.text()) - \
                float(recebido)
            self.tx_valorRecebido.setText(
                format(float(recebido), ".2f"))
            self.lb_ValorPendente.setText(format(TotalFinal, ".2f"))
            pass

    # Limpando campos após adicionar produdo
    def LimpaCampoAddProduto(self):
        for filho in self.fr_addProduto.findChildren(QtWidgets.QLineEdit):
            filho.clear()
        self.bt_IncluirItem.setDisabled(True)
        self.tx_IdBuscaItem.setFocus()

    # Gerando parcelas Venda e Compra
    def gerarParcela(self, acao):
        numParcela = self.cb_QtdeParcela.currentIndex()
        valorTotal = self.tx_TotalFinal.text()
        valor_parcela = float(valorTotal) / int(numParcela)

        while self.tb_Parcelas.rowCount() > 0:
            self.tb_Parcelas.removeRow(0)
            pass
        for i in range(numParcela):

            self.tb_Parcelas.insertRow(i)
            self.dt_tabela(self.tb_Parcelas, i, 1, QtCore.QDate.addMonths(
                self.dt_Vencimento.date(), i), 2)
            self.conteudoTabela(self.tb_Parcelas, i, 2,
                                format(valor_parcela, ".2f"))
            self.botaoReceberParcela(self.tb_Parcelas, i, 4,
                                     partial(self.Receber, i), acao, 1)
            self.tx_tabelaReceber(self.tb_Parcelas, i, 3, 2, '')

        pass

    # Validar valor Recebido
    def validarRecebimento(self):
        valorRecebido = float(self.tx_ValorPago.text().replace(',', '.'))
        valorPendente = float(self.lb_ValorPendente.text().replace(',', '.'))
        if valorRecebido > valorPendente:
            self.tx_ValorPago.setText(format(valorPendente, '.2f'))

    # Setando auto complete
    def setAutocomplete(self):
        # Setando Auto complete
        self.completer = QtWidgets.QCompleter(self)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.model = QtCore.QStringListModel(self)
        self.completer.setModel(self.model)
        self.tx_BuscaItem.setCompleter(self.completer)
        self.tx_NomeFantasia.setCompleter(self.completer)

    # AutoComplete Produtos
    def autocompleteProduto(self):
        produto = self.tx_BuscaItem.text()
        busca = CrudProdutos()
        busca.ListaProdutoTabela(produto)
        lista = busca.descricaoProduto
        if produto:
            self.model.setStringList(lista)

    # Busca Produto por nome
    def BuscaProdutoNome(self):
        produto = self.tx_BuscaItem.text()
        busca = CrudProdutos()
        busca.ListaProdutoTabela(produto)
        self.tx_IdBuscaItem.setText(str(busca.idProduto[0]))
        self.BuscaProdutoId()
