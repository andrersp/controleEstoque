# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
from Views.mainCompras import Ui_ct_MainCompras
from Views.formCompras import Ui_ct_FormCompra
from Crud.CrudCompras import CrudCompras
from Crud.CrudProdutos import CrudProdutos
from Crud.CrudFornecedor import CrudFornecedor
from Crud.CrudAPagar import CrudAPagar
from functools import partial
from Funcoes.data import DataAtual


class MainCompras(Ui_ct_MainCompras, Ui_ct_FormCompra, DataAtual):

    def maincompras(self, frame):
        super(MainCompras, self).setMainCompras(frame)
        self.frameMainCompras.show()

        # Icone Botoes
        self.IconeBotaoForm(self.bt_AddNovaCompra,
                            self.resourcepath('Images/addCompra.svg'))
        self.IconeBotaoMenu(self.bt_BuscaCompras,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_PrintRelatCompras,
                            self.resourcepath('Images/gtk-print.png'))

        """ Definindo funcões widgets"""
        # Botao Adicionar Compra
        self.bt_AddNovaCompra.clicked.connect(self.FormCompras)

        # Busca Compras
        self.bt_BuscaCompras.clicked.connect(self.DataTabCompras)

        # Setando dat Inicio e Fim da consulta
        self.dt_InicioCompra.setDate(self.primeiroDiaMes())
        self.dt_FimCompra.setDate(self.ultimoDiaMes())

        # Tamanho das Colunas Tabela Compras
        self.tb_Compras.blockSignals(True)
        self.tb_Compras.setColumnHidden(0, True)

        self.tb_Compras.resizeRowsToContents()
        self.tb_Compras.setColumnWidth(1, 10)
        self.tb_Compras.setColumnWidth(2, 384)
        self.tb_Compras.setColumnWidth(3, 160)
        self.tb_Compras.setColumnWidth(4, 160)
        self.tb_Compras.setColumnWidth(5, 160)
        self.tb_Compras.setColumnWidth(6, 20)

        self.DataTabCompras()

    # Populando tabela vendas
    def DataTabCompras(self):
        cliente = self.tx_BuscaCompras.text()
        busca = CrudCompras()
        busca.dataEmissao = QtCore.QDate.toString(
            self.dt_InicioCompra.date(), "yyyy-MM-dd")
        busca.dataFim = QtCore.QDate.toString(self.dt_FimCompra.date(),
                                              "yyyy-MM-dd")
        busca.ListaCompratabela(cliente)

        while self.tb_Compras.rowCount() > 0:
            self.tb_Compras.removeRow(0)

        i = 0
        while i < len(busca.NomeFantasia):
            self.tb_Compras.insertRow(i)
            self.conteudoTabela(self.tb_Compras, i, 0, str(busca.idCompra[i]))

            self.TabelaStatus(self.tb_Compras, i, 1,
                              self.StatusEntrega(busca.idStatusEntrega[i],
                                                 busca.idStatusPagamento[i]))

            self.TabelaNomeTelefone(
                self.tb_Compras, i, 2, busca.NomeFantasia[i],
                busca.telefoneCliente[i])
            self.TabelaEntrega(self.tb_Compras, i, 3,
                               busca.dataEmissao[i],
                               self.StatusEntrega(busca.idStatusEntrega[i]), "")
            self.TabelaEntrega(self.tb_Compras, i, 4,
                               busca.prazoEntrega[i],
                               self.StatusEntrega(busca.idStatusEntrega[i]),
                               busca.statusEntrega[i].upper())
            self.TabelaPagamento(self.tb_Compras, i, 5,
                                 busca.valorTotal[i],
                                 self.StatusEntrega(
                                     busca.idStatusPagamento[i]),
                                 busca.statusPagamento[i].upper())

            self.botaoTabela(self.tb_Compras, i, 6,
                             partial(self.SelectCompraId, busca.idCompra[i]), "#005099")

            i += 1

    # Janela Form Compras
    def FormCompras(self):
        self.DesativaBotaoCompras()
        self.LimpaFrame(self.ct_containerCompras)
        super(MainCompras, self).setFormCompra(self.ct_containerCompras)
        self.fr_FormCompra.show()

        # Setando Datas
        self.dt_EmissaoCompra.setDate(QtCore.QDate.currentDate())
        self.dt_PrazoEntrega.setDate(QtCore.QDate.currentDate().addDays(2))
        self.dt_EntregaCompra.setDate(QtCore.QDate.currentDate())
        self.dt_VencimentoVenda.setDate(QtCore.QDate.currentDate())

        # Icone Botoes
        self.IconeBotaoMenu(self.bt_SalvarCompra,
                            self.resourcepath('Images/salvar.png'))
        self.IconeBotaoMenu(self.bt_CancelarCompra,
                            self.resourcepath('Images/cancelar.png'))
        self.IconeBotaoMenu(self.bt_ImprimirCompra,
                            self.resourcepath('Images/gtk-print.png'))
        self.IconeBotaoForm(
            self.bt_ReceberProduto, self.resourcepath('Images/Entregar.svg'))
        self.IconeBotaoForm(self.bt_IncluirItemCompra,
                            self.resourcepath('Images/addPedido.svg'))

        self.IconeBotaoMenu(self.bt_GerarParcelaCompra,
                            self.resourcepath('Images/ico_conta.png'))

        # Setando Foco no Cliente id TX
        self.tx_CodFornecedorCompra.setFocus()

        # Checando se existe ID válido
        self.IdCheckCompra()

        # Tamanho das Colunas Tabela Itens
        # Tamanho das Colunas Tabela Itens
        self.tb_ItensCompra.blockSignals(True)
        self.tb_ItensCompra.setColumnHidden(0, True)
        self.tb_ItensCompra.setColumnHidden(7, True)
        self.tb_ItensCompra.resizeRowsToContents()
        self.tb_ItensCompra.setColumnWidth(1, 165)
        self.tb_ItensCompra.setColumnWidth(2, 150)
        self.tb_ItensCompra.setColumnWidth(3, 75)
        self.tb_ItensCompra.setColumnWidth(4, 75)
        self.tb_ItensCompra.setColumnWidth(5, 75)
        self.tb_ItensCompra.setColumnWidth(6, 45)

        # Tamanho tabela parcelas
        self.tb_parcelasVenda.blockSignals(True)
        self.tb_parcelasVenda.setColumnHidden(0, True)
        self.tb_parcelasVenda.setColumnWidth(1, 90)
        self.tb_parcelasVenda.setColumnWidth(2, 55)
        self.tb_parcelasVenda.setColumnWidth(3, 65)
        self.tb_parcelasVenda.setColumnWidth(4, 70)

        """ Definindo funcões widgets"""
        # Return Press Busca Id Produto
        self.tx_IdBuscaItem.returnPressed.connect(self.BuscaProdutoIdCompra)

        # Campo Busca por nome e Autocompletar Produto
        self.completer = QtWidgets.QCompleter(self)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setCompletionMode(
            QtWidgets.QCompleter.PopupCompletion)
        self.model = QtCore.QStringListModel(self)
        self.completer.setModel(self.model)
        self.tx_BuscaItem.setCompleter(self.completer)
        self.tx_BuscaItem.textEdited.connect(self.autocomplete)
        self.tx_BuscaItem.returnPressed.connect(self.BuscaProdutoNomeCompra)

        # Return Press Busca Id Cliente
        self.tx_CodFornecedorCompra.returnPressed.connect(
            self.BuscaFornecedorId)

        # Campo Busca por nome e Autocompletar Cliente
        self.tx_FornecedorCompra.setCompleter(self.completer)
        self.tx_FornecedorCompra.textEdited.connect(self.autocompleFornecedor)
        self.tx_FornecedorCompra.returnPressed.connect(
            self.BuscaFornecedorNome)

        # Setando Validadot Int nos campos
        validaInt = QtGui.QIntValidator(0, 9999)
        # self.tx_QntdItem.setValidator(validaInt)
        self.tx_IdBuscaItem.setValidator(validaInt)
        self.tx_CodFornecedorCompra.setValidator(validaInt)
        # Setando Validador float nos campos
        validarValor = QtGui.QDoubleValidator()
        validarValor.setNotation(QtGui.QDoubleValidator.StandardNotation)
        validarValor.setRange(0, 9999.00, 2)
        self.tx_Desconto.setValidator(validarValor)
        self.tx_Frete.setValidator(validarValor)
        self.tx_ValorPago.setValidator(validarValor)

        # Calculo total produto por qtde item
        self.tx_QntdItem.returnPressed.connect(self.TotalItemCompra)
        self.tx_ValorUnitarioItem.returnPressed.connect(self.TotalItemCompra)

        # Focando campos Obs apos valor do Item
        self.tx_ValorUnitarioItem.returnPressed.connect(
            self.tx_ObsItemCompra.setFocus)

        # calculando com desconto
        self.tx_Desconto.returnPressed.connect(self.TotalFinalCompra)
        self.tx_Desconto.returnPressed.connect(self.tx_Frete.setFocus)
        self.tx_Desconto.returnPressed.connect(self.tx_Frete.selectAll)

        # calculando com frete
        self.tx_Frete.returnPressed.connect(self.TotalFinalCompra)
        self.tx_Frete.returnPressed.connect(self.tx_ValorPago.setFocus)
        self.tx_Frete.returnPressed.connect(self.tx_ValorPago.selectAll)

        # Calculo Valor Pendente
        self.tx_ValorPago.returnPressed.connect(self.TotalFinalCompra)

        # Validar valor Recebido
        self.tx_ValorPago.textEdited.connect(self.validarRecebimentoCompra)

        # Pagar

        # Entregar
        self.bt_ReceberProduto.clicked.connect(self.ReceberProduto)

        # Add Item Tabela
        self.tx_ObsItemCompra.returnPressed.connect(self.ValidaFormAddCompra)
        self.bt_IncluirItemCompra.clicked.connect(self.ValidaFormAddCompra)

        # Botao Salvar
        self.bt_SalvarCompra.clicked.connect(self.CadCompra)
        # Botao Cancelar
        self.bt_CancelarCompra.clicked.connect(self.janelaCompras)

        # Gerar Parcelas
        self.bt_GerarParcelaCompra.clicked.connect(self.gerarParcela)

    # checando campo Id se é Edicao ou Nova Venda
    def IdCheckCompra(self):
        if not self.tx_CodCompra.text():
            busca = CrudCompras()
            self.tx_CodCompra.setText(str(busca.lastIdCompra()))
            # setando dataAtual campo entrega e emissão

    # Autocomplete Produtos

    def autocomplete(self):
        produto = self.tx_BuscaItem.text()
        busca = CrudProdutos()
        busca.ListaProdutoTabela(produto)
        lista = busca.descricaoProduto
        if produto:
            self.model.setStringList(lista)

    # Busca Produto por nome
    def BuscaProdutoNomeCompra(self):
        produto = self.tx_BuscaItem.text()
        busca = CrudProdutos()
        busca.ListaProdutoTabela(produto)
        self.tx_IdBuscaItem.setText(str(busca.idProduto[0]))
        self.BuscaProdutoIdCompra()

    # Busca produtos por ID
    def BuscaProdutoIdCompra(self):
        id = int(self.tx_IdBuscaItem.text())
        busca = CrudProdutos()
        busca.SelectProdutoId(id)
        if busca.descricaoProduto:
            self.tx_BuscaItem.setText(busca.descricaoProduto)
            self.tx_ValorUnitarioItem.setText(busca.valorCompra)
            self.tx_QntdItem.setFocus()
        else:
            self.tx_BuscaItem.setText("Produto não encontrado")
            self.tx_IdBuscaItem.clear()
            self.tx_IdBuscaItem.setFocus()

    # AutoComplete Cliente
    def autocompleFornecedor(self):
        fornecedor = self.tx_FornecedorCompra.text()
        busca = CrudFornecedor()
        busca.ListaFornecedorTabela(fornecedor)
        lista = busca.NomeFantasia
        if fornecedor:
            self.model.setStringList(lista)

    # Busca cliente por nome
    def BuscaFornecedorNome(self):
        cliente = self.tx_FornecedorCompra.text()
        busca = CrudFornecedor()
        busca.ListaFornecedorTabela(cliente)
        self.tx_CodFornecedorCompra.setText(str(busca.idFornecedor[0]))
        self.BuscaFornecedorId()

    # Busca cliente por ID
    def BuscaFornecedorId(self):
        id = int(self.tx_CodFornecedorCompra.text())
        busca = CrudFornecedor()
        busca.SelectFornecedorId(id)
        if busca.NomeFantasia:
            self.tx_FornecedorCompra.setText(busca.NomeFantasia)
            self.tx_TelefoneFornecedorCompra.setText(busca.telefone)
            self.tx_IdBuscaItem.setFocus()
        else:
            self.tx_FornecedorCompra.setText(
                "Cliente não encontrado".decode("utf8"))
            self.tx_CodFornecedorCompra.clear()
            self.tx_CodFornecedorCompra.setFocus()

    # Calculo ValorTotalItem
    def TotalItemCompra(self):
        id = self.tx_IdBuscaItem.text()
        busca = CrudProdutos()
        busca.SelectProdutoId(id)

        if self.tx_QntdItem.text() and self.tx_ValorUnitarioItem.text():
            qtde = float(self.tx_QntdItem.text().replace(",", "."))
            valorUni = float(
                self.tx_ValorUnitarioItem.text().replace(",", "."))
            TotalItem = qtde * valorUni

            self.tx_ValorTotalItem.setText(format(TotalItem, ".2f"))
            self.tx_ValorUnitarioItem.setText(
                format(valorUni, ".2f"))
            self.tx_ValorUnitarioItem.setFocus()
            self.tx_ValorUnitarioItem.selectAll()
            self.bt_IncluirItemCompra.setEnabled(True)

    def TotalFinalCompra(self):
        total = 0

        if not int(self.tb_ItensCompra.rowCount()) == 0 and self.tb_ItensCompra.item(0, 5).text():
            for row in range(self.tb_ItensCompra.rowCount()):
                total = float(self.tb_ItensCompra.item(row, 5).text()) + total
        self.lb_SubTotalCompra.setText(format(total, ".2f"))
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

        if self.tx_ValorPago.text():
            recebido = self.tx_ValorPago.text().replace(",", ".")
            TotalFinal = float(self.tx_TotalFinal.text()) - float(recebido)
            self.tx_ValorPago.setText(
                format(float(recebido), ".2f"))
            self.lb_ValorPendente.setText(format(TotalFinal, ".2f"))

    def ValidaFormAddCompra(self):
        if not self.tx_CodFornecedorCompra.text():
            self.tx_CodFornecedorCompra.setFocus()
        elif not self.tx_IdBuscaItem.text():
            self.tx_IdBuscaItem.setFocus()
        elif not self.tx_BuscaItem.text():
            self.tx_BuscaItem.setFocus()
        elif not self.tx_QntdItem.text():
            self.tx_QntdItem.setFocus()
        elif not self.tx_FornecedorCompra.text():
            self.tx_FornecedorCompra.setFocus()
        else:
            self.AddItemTabelaCompra()

    # Adiciona Item a tabela
    def AddItemTabelaCompra(self):
        row = self.tb_ItensCompra.rowCount()
        self.tb_ItensCompra.insertRow(row)
        self.conteudoTabela(self.tb_ItensCompra, row, 0,
                            self.tx_IdBuscaItem.text())
        self.conteudoTabelaLeft(self.tb_ItensCompra, row, 1,
                                self.tx_BuscaItem.text())
        self.conteudoTabelaLeft(self.tb_ItensCompra, row, 2,
                                self.tx_ObsItemCompra.text())

        self.conteudoTabela(self.tb_ItensCompra, row, 3,
                            self.tx_QntdItem.text())
        self.conteudoTabela(self.tb_ItensCompra, row, 4,
                            self.tx_ValorUnitarioItem.text())
        self.conteudoTabela(self.tb_ItensCompra, row, 5,
                            self.tx_ValorTotalItem.text())
        self.botaoRemoveItem(self.tb_ItensCompra, row, 6,
                             partial(self.RemoveLInhaCompra, row), "#005099")

        self.conteudoTabela(self.tb_ItensCompra, row, 7, str(
            QtCore.QDateTime.toMSecsSinceEpoch(QtCore.QDateTime.currentDateTime())))

        self.TotalFinalCompra()
        self.LimpaCampoAddProdutoCompra()
        self.bt_GerarParcelaCompra.setEnabled(True)

    # Removendo item da tabela e banco de dados se ouver
    def RemoveLInhaCompra(self, linha):
        REMOVE = CrudCompras()
        REMOVE.idItemTabela = self.tb_ItensCompra.item(linha, 7).text()
        REMOVE.DelItem()
        self.tb_ItensCompra.removeRow(linha)
        for row in range(self.tb_ItensCompra.rowCount()):
            self.botaoRemoveItem(self.tb_ItensCompra, row, 6,
                                 partial(self.RemoveLInhaCompra, row), "#005099")
        self.TotalFinalCompra()

    # Desativando Botões
    def DesativaBotaoCompras(self):
        self.bt_AddNovaCompra.setEnabled(False)
        self.tx_BuscaCompras.setEnabled(False)
        self.bt_BuscaCompras.setEnabled(False)

    def AtivaBotaoCompras(self):
        self.bt_AddNovaCompra.setEnabled(True)
        self.tx_BuscaCompras.setEnabled(True)
        self.bt_BuscaCompras.setEnabled(True)

    def LimpaCampoAddProdutoCompra(self):
        for filho in self.fr_addProduto.findChildren(QtWidgets.QLineEdit):
            filho.clear()
        self.bt_IncluirItemCompra.setDisabled(True)
        self.tx_IdBuscaItem.setFocus()

        # Salvar Venda
    def CadCompra(self):
        if not int(self.tb_ItensCompra.rowCount()) < 1:
            INSERI = CrudCompras()
            INSERI.idCompra = self.tx_CodCompra.text()
            INSERI.idFornecedor = self.tx_CodFornecedorCompra.text()
            INSERI.dataEmissao = QtCore.QDate.toString(
                self.dt_EmissaoCompra.date(), 'yyyy-MM-dd')
            INSERI.prazoEntrega = QtCore.QDate.toString(
                self.dt_PrazoEntrega.date(), 'yyyy-MM-dd')
            INSERI.desconto = self.tx_Desconto.text()
            INSERI.frete = self.tx_Frete.text()
            INSERI.valorTotal = self.tx_TotalFinal.text()
            INSERI.valorPendente = self.lb_ValorPendente.text()
            if float(self.lb_ValorPendente.text()) == 0:
                INSERI.statusPagamento = 1
            else:
                INSERI.statusPagamento = 2
            INSERI.CadCompra()
            self.CadItemCompra()

        pass

    def CadItemCompra(self):
        INSERI = CrudCompras()
        i = 0
        while i < self.tb_ItensCompra.rowCount():
            INSERI.idItem = self.tb_ItensCompra.item(i, 0).text()
            INSERI.idCompra = self.tx_CodCompra.text()
            INSERI.idItemTabela = self.tb_ItensCompra.item(i, 7).text()
            INSERI.qtde = self.tb_ItensCompra.item(i, 3).text()
            INSERI.valorItem = self.tb_ItensCompra.item(i, 4).text()
            INSERI.totalItem = self.tb_ItensCompra.item(i, 5).text()
            INSERI.obsItem = self.tb_ItensCompra.item(i, 2).text()
            INSERI.CadItensCompra()
            i += 1
        self.CadContaCompra()
        self.SelectCompraId(self.tx_CodCompra.text())

        pass

    # Cadastro Parcelas
    def CadContaCompra(self):
        INSERI = CrudAPagar()

        if self.tb_parcelasVenda.rowCount() > 0:
            for i in range(self.tb_parcelasVenda.rowCount()):
                try:
                    self.tb_parcelasVenda.item(i, 0).text()
                    INSERI.idConta = self.tb_parcelasVenda.item(i, 0).text()
                except:
                    INSERI.idConta = ''
                INSERI.idCompra = self.tx_CodCompra.text()
                INSERI.idFornecedor = self.tx_CodFornecedorCompra.text()
                INSERI.descricao = """Pedido de Compra {}. Parcela {} de {} """.format(
                    self.tx_CodCompra.text(), i + 1, self.tb_parcelasVenda.rowCount())
                INSERI.obs = ""
                INSERI.categoria = 1
                INSERI.dataVencimento = QtCore.QDate.toString(
                    self.tb_parcelasVenda.cellWidget(i, 1).date(), "yyyy-MM-dd")
                INSERI.valor = self.tb_parcelasVenda.item(i, 2).text()
                INSERI.formaPagamento = self.cb_FormaPagamentoVenda.currentIndex()
                INSERI.cadContaPagar()

    # Validar valor Recebido
    def validarRecebimentoCompra(self):
        if not self.tx_ValorPago.text():
            valorRecebido = float(self.tx_ValorPago.text().replace(',', '.'))
            valorPendente = float(
                self.lb_ValorPendente.text().replace(',', '.'))
            if valorRecebido > valorPendente:
                self.tx_ValorPago.setText(format(valorPendente, '.2f'))

    # Pagando Compra
    def Pagar(self, id):
        # print(self.tb_parcelasVenda.item(id, 0).text())

        if self.tb_parcelasVenda.cellWidget(id, 3).text():
            INSERI = CrudAPagar()
            INSERI.idConta = self.tb_parcelasVenda.item(id, 0).text()
            INSERI.valorPago = self.tb_parcelasVenda.cellWidget(
                id, 3).text().replace(",", ".")

            INSERI.dataPagamento = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), "yyyy-MM-dd")

            INSERI.cadContaPagar()
            self.ParcelasAPagar()

    # Entregando Compra DB
    def ReceberProduto(self):
        INSERI = CrudCompras()
        INSERI.dataEntrega = QtCore.QDate.toString(
            self.dt_EntregaCompra.date(), "yyyy-MM-dd")
        INSERI.idCompra = self.tx_CodCompra.text()
        INSERI.ReceberProduto()
        self.EntradaEstoque()
        self.SelectCompraId(self.tx_CodCompra.text())

    # Dando Entrada no Estoque
    def EntradaEstoque(self):
        INSERI = CrudProdutos()
        i = 0
        while i < self.tb_ItensCompra.rowCount():
            INSERI.idProduto = self.tb_ItensCompra.item(i, 0).text()
            INSERI.idRelacao = self.tb_ItensCompra.item(i, 7).text()
            INSERI.valorCompra = self.tb_ItensCompra.item(i, 4).text()
            INSERI.qtdeProduto = self.tb_ItensCompra.item(i, 3).text()
            INSERI.obsProduto = self.tb_ItensCompra.item(i, 2).text()
            INSERI.data = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), 'yyyy-MM-dd')

            INSERI.EntradaProduto()
            i += 1

    # Selecionando Venda pela tabela
    def SelectCompraId(self, id):
        busca = CrudCompras()
        self.FormCompras()
        self.tx_CodCompra.setText(str(id))
        busca.SelectCompraId(id)

        self.tx_CodFornecedorCompra.setText(str(busca.idFornecedor))
        self.BuscaFornecedorId()
        self.tx_Desconto.setText(str(busca.desconto))
        self.tx_Frete.setText(str(busca.frete))
        self.dt_PrazoEntrega.setDate(busca.prazoEntrega)
        if busca.valorRecebido:
            self.tx_ValorPago.setText(str(busca.valorRecebido))
        if busca.statusPagamento == 2:
            self.bt_GerarParcelaCompra.setEnabled(True)
        if busca.statusEntrega == 2:
            self.bt_ReceberProduto.setEnabled(True)

        if busca.statusPagamento == 1 or busca.statusEntrega == 1:
            self.tb_parcelasVenda.setColumnHidden(6, True)

            for item in self.fr_addProduto.findChildren(QtWidgets.QLineEdit):
                item.setReadOnly(True)

        i = 0
        while i < len(busca.itemDescricao):

            self.tb_ItensCompra.insertRow(i)
            self.conteudoTabela(self.tb_ItensCompra, i, 0,
                                str(busca.idItem[i]))
            self.conteudoTabelaLeft(self.tb_ItensCompra, i, 1,
                                    busca.itemDescricao[i])
            self.conteudoTabelaLeft(self.tb_ItensCompra, i, 2,
                                    str(busca.obsItem[i]))
            self.conteudoTabela(self.tb_ItensCompra, i, 3,
                                str(busca.qtde[i]))
            self.conteudoTabela(self.tb_ItensCompra, i, 4,
                                str(busca.valorItem[i]))
            self.conteudoTabela(self.tb_ItensCompra, i, 5,
                                str(busca.totalItem[i]))
            self.botaoRemoveItem(self.tb_ItensCompra, i, 6,
                                 partial(self.RemoveLInhaCompra, i), "#005099")
            self.conteudoTabela(self.tb_ItensCompra, i, 7,
                                str(busca.idItemTabela[i]))
            self.TotalFinalCompra()
            self.tx_ValorPago.returnPressed.connect(self.Pagar)

            i += 1
        self.bt_ImprimirCompra.setEnabled(True)
        self.ParcelasAPagar()

        pass

    def ParcelasAPagar(self):
        while self.tb_parcelasVenda.rowCount() > 0:
            self.tb_parcelasVenda.removeRow(0)

        busca = CrudAPagar()
        busca.idCompra = self.tx_CodCompra.text()
        busca.selectAPagarId()

        if busca.dataVencimento:
            self.bt_GerarParcelaCompra.setDisabled(True)

        for i in range(len(busca.dataVencimento)):
            self.tb_parcelasVenda.insertRow(i)
            self.conteudoTabela(self.tb_parcelasVenda, i,
                                0, str(busca.idConta[i]))
            self.dt_tabela(self.tb_parcelasVenda, i,
                           1, busca.dataVencimento[i], busca.status[i])
            self.conteudoTabela(self.tb_parcelasVenda, i,
                                2, str(busca.valor[i]))
            self.tx_tabelaReceber(self.tb_parcelasVenda, i, 3, busca.status[
                                  i], str(busca.valor[i] - busca.valorPago[i]))
            self.botaoReceberParcela(self.tb_parcelasVenda, i, 4,
                                     partial(self.Pagar, i), "Pagar", busca.status[i])


# telefone = ("22997069161")
# print("({0:.2}) ").format(telefone)
