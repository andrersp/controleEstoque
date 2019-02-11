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
from Funcoes.comercial import Comercial


class MainCompras(Ui_ct_MainCompras, Ui_ct_FormCompra, DataAtual, Comercial):

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
        super(MainCompras, self).setFormCompras(self.ct_containerCompras)
        self.fr_FormCompra.show()

        """ Chamanda de funções localizadas no arquivo funcoes.py na pasta Funcoes """
        # Setando Datas
        self.setDatas()

        # Setando Validação
        self.validaCampos()

        # Definindo acao de calculo de frete e desconto
        self.acaoCalculo()

        # setando Icone Botoes
        self.setIcones()

        # Setando tamanho das tabelas
        self.tamanhoTabelas()

        # setando autocompleye
        self.setAutocomplete()
        """ Fim das chamandas """

        # Setando Foco no Cliente id TX
        self.tx_Id.setFocus()

        # Checando se existe ID válido
        self.IdCheckCompra()

        """ Definindo funcões widgets"""
        # Return Press Busca Id Produto
        self.tx_IdBuscaItem.returnPressed.connect(self.BuscaProdutoIdCompra)

        # Autocompletando on text edit
        self.tx_BuscaItem.textEdited.connect(self.autocompleteProduto)
        self.tx_BuscaItem.returnPressed.connect(self.BuscaProdutoNomeCompra)

        # Return Press Busca Id Cliente
        self.tx_Id.returnPressed.connect(
            self.BuscaFornecedorId)

        # Campo Busca por nome e Autocompletar Cliente
        self.tx_NomeFantasia.textEdited.connect(self.autocompleFornecedor)
        self.tx_NomeFantasia.returnPressed.connect(
            self.BuscaFornecedorNome)

        # Calculo total produto por qtde item
        self.tx_QntdItem.returnPressed.connect(self.TotalItemCompra)
        self.tx_ValorUnitarioItem.returnPressed.connect(self.TotalItemCompra)

        # Focando campos Obs apos valor do Item
        self.tx_ValorUnitarioItem.returnPressed.connect(
            self.tx_ObsItem.setFocus)

        # Entregar
        self.bt_Entregar.clicked.connect(self.ReceberProduto)

        # Add Item Tabela
        self.tx_ObsItem.returnPressed.connect(self.ValidaFormAdd)
        self.bt_IncluirItem.clicked.connect(self.ValidaFormAdd)

        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.CadCompra)
        # Botao Cancelar
        self.bt_Voltar.clicked.connect(self.janelaCompras)

        # Gerar Parcelas
        self.bt_GerarParcela.clicked.connect(
            partial(self.gerarParcela,
                    "Pagar"))

    # checando campo Id se é Edicao ou Nova Venda
    def IdCheckCompra(self):
        if not self.tx_Cod.text():
            busca = CrudCompras()
            self.tx_Cod.setText(str(busca.lastIdCompra()))
            # setando dataAtual campo entrega e emissão

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
        fornecedor = self.tx_NomeFantasia.text()
        busca = CrudFornecedor()
        busca.ListaFornecedorTabela(fornecedor)
        lista = busca.NomeFantasia
        if fornecedor:
            self.model.setStringList(lista)

    # Busca cliente por nome
    def BuscaFornecedorNome(self):
        cliente = self.tx_NomeFantasia.text()
        busca = CrudFornecedor()
        busca.ListaFornecedorTabela(cliente)
        self.tx_Id.setText(str(busca.idFornecedor[0]))
        self.BuscaFornecedorId()

    # Busca cliente por ID
    def BuscaFornecedorId(self):
        id = int(self.tx_Id.text())
        busca = CrudFornecedor()
        busca.SelectFornecedorId(id)
        if busca.NomeFantasia:
            self.tx_NomeFantasia.setText(busca.NomeFantasia)
            self.tx_Telefone.setText(busca.telefone)
            self.tx_IdBuscaItem.setFocus()
        else:
            self.tx_NomeFantasia.setText(
                "Cliente não encontrado".decode("utf8"))
            self.tx_Id.clear()
            self.tx_Id.setFocus()

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
            self.bt_IncluirItem.setEnabled(True)

    # Removendo item da tabela e banco de dados se ouver
    def RemoveLInhaCompra(self, linha):
        REMOVE = CrudCompras()
        REMOVE.idItemTabela = self.tb_Itens.item(linha, 7).text()
        REMOVE.DelItem()
        self.tb_Itens.removeRow(linha)
        for row in range(self.tb_Itens.rowCount()):
            self.botaoRemoveItem(self.tb_Itens, row, 6,
                                 partial(self.RemoveLInhaCompra, row), "#005099")
        self.TotalFinal()

    # Desativando Botões
    def DesativaBotaoCompras(self):
        self.bt_AddNovaCompra.setEnabled(False)
        self.tx_BuscaCompras.setEnabled(False)
        self.bt_BuscaCompras.setEnabled(False)

    def AtivaBotaoCompras(self):
        self.bt_AddNovaCompra.setEnabled(True)
        self.tx_BuscaCompras.setEnabled(True)
        self.bt_BuscaCompras.setEnabled(True)

        # Salvar Venda
    def CadCompra(self):
        if not int(self.tb_Itens.rowCount()) < 1:
            INSERI = CrudCompras()
            INSERI.idCompra = self.tx_Cod.text()
            INSERI.idFornecedor = self.tx_Id.text()
            INSERI.dataEmissao = QtCore.QDate.toString(
                self.dt_Emissao.date(), 'yyyy-MM-dd')
            INSERI.prazoEntrega = QtCore.QDate.toString(
                self.dt_Prazo.date(), 'yyyy-MM-dd')
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
        while i < self.tb_Itens.rowCount():
            INSERI.idItem = self.tb_Itens.item(i, 0).text()
            INSERI.idCompra = self.tx_Cod.text()
            INSERI.idItemTabela = self.tb_Itens.item(i, 7).text()
            INSERI.qtde = self.tb_Itens.item(i, 3).text()
            INSERI.valorItem = self.tb_Itens.item(i, 4).text()
            INSERI.totalItem = self.tb_Itens.item(i, 5).text()
            INSERI.obsItem = self.tb_Itens.item(i, 2).text()
            INSERI.CadItensCompra()
            i += 1
        self.CadContaCompra()
        self.SelectCompraId(self.tx_Cod.text())

        pass

    # Cadastro Parcelas
    def CadContaCompra(self):
        INSERI = CrudAPagar()

        if self.tb_Parcelas.rowCount() > 0:
            for i in range(self.tb_Parcelas.rowCount()):
                try:
                    self.tb_Parcelas.item(i, 0).text()
                    INSERI.idConta = self.tb_Parcelas.item(i, 0).text()
                except:
                    INSERI.idConta = ''
                INSERI.idCompra = self.tx_Cod.text()
                INSERI.idFornecedor = self.tx_Id.text()
                INSERI.descricao = """Pedido de Compra {}. Parcela {} de {} """.format(
                    self.tx_Cod.text(), i + 1, self.tb_Parcelas.rowCount())
                INSERI.obs = ""
                INSERI.categoria = 1
                INSERI.dataVencimento = QtCore.QDate.toString(
                    self.tb_Parcelas.cellWidget(i, 1).date(), "yyyy-MM-dd")
                INSERI.valor = self.tb_Parcelas.item(i, 2).text()
                INSERI.formaPagamento = self.cb_FormaPagamento.currentIndex()
                INSERI.cadContaPagar()

    # Pagando Parcela Compra
    def Pagar(self, id):
        # print(self.tb_Parcelas.item(id, 0).text())

        if self.tb_Parcelas.cellWidget(id, 3).text():
            INSERI = CrudAPagar()
            INSERI.idConta = self.tb_Parcelas.item(id, 0).text()
            INSERI.valorPago = self.tb_Parcelas.cellWidget(
                id, 3).text().replace(",", ".")

            INSERI.dataPagamento = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), "yyyy-MM-dd")

            INSERI.cadContaPagar()
            self.ParcelasAPagar()

    # Recebendo Produtos DB
    def ReceberProduto(self):
        INSERI = CrudCompras()
        INSERI.dataEntrega = QtCore.QDate.toString(
            self.dt_Entrega.date(), "yyyy-MM-dd")
        INSERI.idCompra = self.tx_Cod.text()
        INSERI.ReceberProduto()
        self.EntradaEstoque()
        self.SelectCompraId(self.tx_Cod.text())

    # Dando Entrada no Estoque
    def EntradaEstoque(self):
        INSERI = CrudProdutos()
        i = 0
        while i < self.tb_Itens.rowCount():
            INSERI.idProduto = self.tb_Itens.item(i, 0).text()
            INSERI.idRelacao = self.tb_Itens.item(i, 7).text()
            INSERI.valorCompra = self.tb_Itens.item(i, 4).text()
            INSERI.qtdeProduto = self.tb_Itens.item(i, 3).text()
            INSERI.obsProduto = self.tb_Itens.item(i, 2).text()
            INSERI.data = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), 'yyyy-MM-dd')

            INSERI.EntradaProduto()
            i += 1

    # Selecionando Venda pela tabela
    def SelectCompraId(self, id):
        busca = CrudCompras()
        self.FormCompras()
        self.tx_Cod.setText(str(id))
        busca.SelectCompraId(id)

        self.tx_Id.setText(str(busca.idFornecedor))
        self.BuscaFornecedorId()
        self.tx_Desconto.setText(str(busca.desconto))
        self.tx_Frete.setText(str(busca.frete))
        self.dt_Prazo.setDate(busca.prazoEntrega)
        if busca.valorRecebido:
            self.tx_valorRecebido.setText(str(busca.valorRecebido))
        if busca.statusPagamento == 2:
            self.bt_GerarParcela.setEnabled(True)
        if busca.statusEntrega == 2:
            self.bt_Entregar.setEnabled(True)

        if busca.statusPagamento == 1 or busca.statusEntrega == 1:
            self.tb_Parcelas.setColumnHidden(6, True)

            for item in self.fr_addProduto.findChildren(QtWidgets.QLineEdit):
                item.setReadOnly(True)

        i = 0
        while i < len(busca.itemDescricao):

            self.tb_Itens.insertRow(i)
            self.conteudoTabela(self.tb_Itens, i, 0,
                                str(busca.idItem[i]))
            self.conteudoTabelaLeft(self.tb_Itens, i, 1,
                                    busca.itemDescricao[i])
            self.conteudoTabelaLeft(self.tb_Itens, i, 2,
                                    str(busca.obsItem[i]))
            self.conteudoTabela(self.tb_Itens, i, 3,
                                str(busca.qtde[i]))
            self.conteudoTabela(self.tb_Itens, i, 4,
                                str(busca.valorItem[i]))
            self.conteudoTabela(self.tb_Itens, i, 5,
                                str(busca.totalItem[i]))
            self.botaoRemoveItem(self.tb_Itens, i, 6,
                                 partial(self.RemoveLInhaCompra, i), "#005099")
            self.conteudoTabela(self.tb_Itens, i, 7,
                                str(busca.idItemTabela[i]))
            self.TotalFinal()
            self.tx_valorRecebido.returnPressed.connect(self.Pagar)

            i += 1
        self.bt_Imprimir.setEnabled(True)
        self.ParcelasAPagar()

        pass
    # Populando tabela Parcelas

    def ParcelasAPagar(self):
        while self.tb_Parcelas.rowCount() > 0:
            self.tb_Parcelas.removeRow(0)

        busca = CrudAPagar()
        busca.idCompra = self.tx_Cod.text()
        busca.selectAPagarId()

        if busca.dataVencimento:
            self.bt_GerarParcela.setDisabled(True)

        for i in range(len(busca.dataVencimento)):
            self.tb_Parcelas.insertRow(i)
            self.conteudoTabela(self.tb_Parcelas, i,
                                0, str(busca.idConta[i]))
            self.dt_tabela(self.tb_Parcelas, i,
                           1, busca.dataVencimento[i], busca.status[i])
            self.conteudoTabela(self.tb_Parcelas, i,
                                2, str(busca.valor[i]))
            self.tx_tabelaReceber(self.tb_Parcelas, i, 3, busca.status[
                                  i], str(busca.valor[i] - busca.valorPago[i]))
            self.botaoReceberParcela(self.tb_Parcelas, i, 4,
                                     partial(self.Pagar, i), "Pagar", busca.status[i])
