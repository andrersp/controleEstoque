# -*- coding: utf-8 -*-
from functools import partial

from PySide2.QtCore import QDate, QUrl
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWebEngineWidgets import QWebEngineView


from Views.mainCompras import Ui_ct_MainCompras
from Views.formCompras import Ui_ct_FormCompra

from orm.CrudCompra import CrudCompra
from orm.CrudFornecedor import CrudFornecedor
from orm.CrudProduto import CrudProduto
from orm.CrudRelCompra import CrudRelCompra
from orm.CrudContaAPagar import CrudContaAPagar

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
        busca = CrudCompra()
        busca.dataEmissao = QDate.toString(
            self.dt_InicioCompra.date(), "yyyy-MM-dd")
        busca.dataFim = QDate.toString(self.dt_FimCompra.date(),
                                              "yyyy-MM-dd")
        busca.listaCompra(cliente)

        while self.tb_Compras.rowCount() > 0:
            self.tb_Compras.removeRow(0)

        i = 0
        while i < len(busca.fornecedor):
            self.tb_Compras.insertRow(i)
            self.conteudoTabela(self.tb_Compras, i, 0, str(busca.id[i]))

            self.TabelaStatus(self.tb_Compras, i, 1,
                              self.StatusEntrega(busca.idStatusEntrega[i],
                                                 busca.idStatusPagamento[i]))

            self.TabelaNomeTelefone(
                self.tb_Compras, i, 2, busca.fornecedor[i],
                self.formatoNumTelefone(busca.telefone[i]))
            self.TabelaEntrega(self.tb_Compras, i, 3,
                               busca.dataEmissao[i],
                               self.StatusEntrega(busca.idStatusEntrega[i]), "")
            self.TabelaEntrega(self.tb_Compras, i, 4,
                               busca.prazoEntrega[i],
                               self.StatusEntrega(busca.idStatusEntrega[i]),
                               busca.statusEntrega[i].upper())
            self.TabelaEntrega(self.tb_Compras, i, 5,
                                 "R$ "+str(busca.valorTotal[i]),
                                 self.StatusEntrega(
                                     busca.idStatusPagamento[i]),
                                 busca.statusPagamento[i].upper())

            self.botaoTabela(self.tb_Compras, i, 6,
                             partial(self.SelectCompraId, busca.id[i]), "#005099")

            i += 1

    # Janela Form Compras
    def FormCompras(self):
        self.DesativaBotaoCompras()
        self.LimpaFrame(self.ct_containerCompras)
        super(MainCompras, self).setFormCompras(self.ct_containerCompras)
        self.fr_FormCompra.show()

        # Setando Foco no Cliente id TX
        self.tx_Id.setFocus()

        # Checando se existe ID válido
        self.IdCheckCompra()

        """ Chamanda de funções localizadas no arquivo comercial.py na pasta Funcoes """
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

        # Gerar Parcelas
        self.bt_GerarParcela.clicked.connect(
            partial(self.gerarParcela,
                    "Pagar"))

        # Auto COmplete Produto
        self.tx_BuscaItem.textEdited.connect(self.autocompleteProduto)

        # Add Item Tabela
        self.tx_ObsItem.returnPressed.connect(self.ValidaFormAdd)
        self.bt_IncluirItem.clicked.connect(self.ValidaFormAdd)
        """ Fim das chamandas comercial.py"""

        """ Chamanda de funções localizadas no arquivo fornecedor.py na pasta Funcoes """
        # Campo Busca por nome e Autocompletar Fornecedor
        self.tx_NomeFantasia.textEdited.connect(self.autocompleFornecedor)
        self.tx_NomeFantasia.returnPressed.connect(
            partial(self.BuscaFornecedorNome, self.tx_IdBuscaItem))

        # Return Press Busca Id Fornecedor
        self.tx_Id.returnPressed.connect(
            partial(self.BuscaFornecedorId, self.tx_IdBuscaItem))
        """ Fim chamada fornecedor.py """

        """ Chamanda de funções localizadas no arquivo FormaPagamento.py na pasta Funcoes """
        # Populando combobox Forma de Pagamento
        self.CboxFPagamento(self.cb_FormaPagamento)
        """ Fim Chamanda FormaPagamento.py  """

        # Adicionando numero parcelas
        self.cboxParcelas(self.cb_QtdeParcela)

        # Return Press Busca Id Produto
        self.tx_IdBuscaItem.returnPressed.connect(self.BuscaProdutoIdCompra)

        # Busca Produto por nome
        self.tx_BuscaItem.returnPressed.connect(self.BuscaProdutoNomeCompra)

        # Calculo total produto por qtde item
        self.tx_QntdItem.returnPressed.connect(self.TotalItemCompra)
        self.tx_ValorUnitarioItem.returnPressed.connect(self.TotalItemCompra)

        # Focando campos Obs apos valor do Item
        self.tx_ValorUnitarioItem.returnPressed.connect(
            self.tx_ObsItem.setFocus)

        # Entregar
        self.bt_Entregar.clicked.connect(self.ReceberProduto)

        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.CadCompra)

        # Botao Cancelar
        self.bt_Voltar.clicked.connect(self.janelaCompras)

        #Bota Imprimir
        self.bt_Imprimir.clicked.connect(self.imprimirCompra)

    # checando campo Id se é Edicao ou Nova Venda

    def IdCheckCompra(self):
        if not self.tx_Cod.text():
            busca = CrudCompra()
            self.tx_Cod.setText(str(busca.lastIdCompra()))
            # setando dataAtual campo entrega e emissão

    # Busca Produto por nome
    def BuscaProdutoNomeCompra(self):
        produto = self.tx_BuscaItem.text()
        busca = CrudProduto()
        busca.ListaProdutoTabela(produto)
        self.tx_IdBuscaItem.setText(str(busca.idProduto[0]))
        self.BuscaProdutoIdCompra()

    # Busca produtos por ID
    def BuscaProdutoIdCompra(self):
        id = int(self.tx_IdBuscaItem.text())
        busca = CrudProduto()
        busca.id = id
        busca.selectProdutoId()
        if busca.produto:
            self.tx_BuscaItem.setText(busca.produto)
            self.tx_ValorUnitarioItem.setText(str(busca.valorCompra))
            self.tx_QntdItem.setFocus()
        else:
            self.tx_BuscaItem.setText("Produto não encontrado")
            self.tx_IdBuscaItem.clear()
            self.tx_IdBuscaItem.setFocus()
        pass



    # Calculo ValorTotalItem
    def TotalItemCompra(self):

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
        
        pass

    # Removendo item da tabela e banco de dados se ouver
    def RemoveLInhaCompra(self, linha):
        REMOVE = CrudRelCompra()
        REMOVE.id = self.tb_Itens.item(linha, 7).text()
        REMOVE.delItem()
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

    
    # Salvar Compra
    def CadCompra(self):
        if not int(self.tb_Itens.rowCount()) < 1:
            INSERI = CrudCompra()
            INSERI.id = self.tx_Cod.text()
            INSERI.idFornecedor = self.tx_Id.text()
            INSERI.dataEmissao = QDate.toString(
                self.dt_Emissao.date(), 'yyyy-MM-dd')
            INSERI.prazoEntrega = QDate.toString(
                self.dt_Prazo.date(), 'yyyy-MM-dd')
            INSERI.desconto = self.tx_Desconto.text()
            INSERI.categoria = 1
            INSERI.frete = self.tx_Frete.text()
            INSERI.valorTotal = self.tx_TotalFinal.text()
            INSERI.valorPendente = self.lb_ValorPendente.text()
            INSERI.inseriCompra()
            self.CadItemCompra()

        pass

    def CadItemCompra(self):
        INSERI = CrudRelCompra()
        i = 0
        while i < self.tb_Itens.rowCount():
            INSERI.idProduto = self.tb_Itens.item(i, 0).text()
            INSERI.idCompra = self.tx_Cod.text()
            INSERI.id = self.tb_Itens.item(i, 7).text()
            INSERI.qtde = self.tb_Itens.item(i, 3).text().replace(',', '.')
            INSERI.valorUnitario = self.tb_Itens.item(i, 4).text()
            INSERI.valorTotal = self.tb_Itens.item(i, 5).text()
            INSERI.obs = self.tb_Itens.item(i, 2).text()
            INSERI.inseriItens()
            i += 1
        self.CadContaCompra()
        self.SelectCompraId(self.tx_Cod.text())

        pass

    # Cadastro Parcelas
    def CadContaCompra(self):
        INSERI = CrudContaAPagar()

        if self.tb_Parcelas.rowCount() > 0:
            for i in range(self.tb_Parcelas.rowCount()):
                try:
                    self.tb_Parcelas.item(i, 0).text()
                    INSERI.id = self.tb_Parcelas.item(i, 0).text()
                except:
                    INSERI.id =  INSERI.lastIdContaAPagar()
                INSERI.idCompra = self.tx_Cod.text()
                INSERI.idFornecedor = self.tx_Id.text()
                INSERI.descricao = """Pedido de Compra {}. Parcela {} de {} """.format(
                    self.tx_Cod.text(), i + 1, self.tb_Parcelas.rowCount())
                INSERI.categoria = 1
                INSERI.dataVencimento = QDate.toString(
                    self.tb_Parcelas.cellWidget(i, 1).date(), "yyyy-MM-dd")
                INSERI.valor = self.tb_Parcelas.item(i, 2).text()
                INSERI.formaPagamento = self.cb_FormaPagamento.currentData()
                INSERI.inseriParcelaCompra()


    
    # Selecionando Venda pela tabela
    def SelectCompraId(self, id):
        busca = CrudCompra()
        self.FormCompras()
        self.tx_Cod.setText(str(id))
        busca.id = id
        busca.selectCompraId()

        self.tx_Id.setText(str(busca.idFornecedor))
        self.BuscaFornecedorId(self.tx_IdBuscaItem)
        self.tx_Desconto.setText(str(busca.desconto))
        self.tx_Frete.setText(str(busca.frete))
        self.dt_Prazo.setDate(busca.prazoEntrega)
        if busca.valorPago:
            self.tx_valorRecebido.setText(str(busca.valorPago))
        if busca.idStatusPagamento == 2:
            self.bt_GerarParcela.setEnabled(True)
        if busca.idStatusEntrega == 2:
            self.bt_Entregar.setEnabled(True)
        if busca.idStatusEntrega == 1:
            self.tb_Itens.setColumnHidden(6, True)
            for item in self.fr_addProduto.findChildren(QLineEdit):
                item.setReadOnly(True)


        # Listando itens referente a compra
        busca = CrudRelCompra()
        busca.idCompra = id
        busca.listaItens()

        i = 0
        while i < len(busca.produto):

            self.tb_Itens.insertRow(i)
            self.conteudoTabela(self.tb_Itens, i, 0,
                                str(busca.idProduto[i]))
            self.conteudoTabelaLeft(self.tb_Itens, i, 1,
                                    busca.produto[i])
            self.conteudoTabelaLeft(self.tb_Itens, i, 2,
                                    str(busca.obs[i]))
            self.conteudoTabela(self.tb_Itens, i, 3,
                                str(busca.qtde[i]))
            self.conteudoTabela(self.tb_Itens, i, 4,
                                str(busca.valorUnitario[i]))
            self.conteudoTabela(self.tb_Itens, i, 5,
                                str(busca.valorTotal[i]))
            self.botaoRemoveItem(self.tb_Itens, i, 6,
                                 partial(self.RemoveLInhaCompra, i), "#005099")
            self.conteudoTabela(self.tb_Itens, i, 7,
                                str(busca.id[i]))
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

        busca = CrudContaAPagar()
        busca.idCompra = self.tx_Cod.text()
        busca.listaParcelas()

        if busca.dataVencimento:
            self.bt_GerarParcela.setDisabled(True)
            self.tb_Itens.setColumnHidden(6, True)
            for item in self.fr_addProduto.findChildren(QLineEdit):
                item.setDisabled(True)
            self.bt_Salvar.setDisabled(True)

        for i in range(len(busca.dataVencimento)):
            self.tb_Parcelas.insertRow(i)
            self.conteudoTabela(self.tb_Parcelas, i,
                                0, str(busca.id[i]))
            self.dt_tabela(self.tb_Parcelas, i,
                           1, busca.dataVencimento[i], busca.idStatusPagamento[i])
            self.conteudoTabela(self.tb_Parcelas, i,
                                2, str(busca.valor[i]))
            self.tx_tabelaReceber(self.tb_Parcelas, i, 3, busca.idStatusPagamento[
                                  i], str(busca.valor[i] - busca.valorPago[i]))
            self.botaoReceberParcela(self.tb_Parcelas, i, 4,
                                     partial(self.Pagar, i), "Pagar", 
                                     busca.idStatusPagamento[i])
            self.cb_QtdeParcela.setCurrentIndex(
                self.cb_QtdeParcela.findData(len(busca.dataVencimento)))
            self.cb_FormaPagamento.setCurrentIndex(
                self.cb_FormaPagamento.findData(
                    busca.idFormaPagamento[0]))

    
    # Pagando Parcela Compra
    def Pagar(self, id):
        # print(self.tb_Parcelas.item(id, 0).text())

        if self.tb_Parcelas.cellWidget(id, 3).text():
            INSERI = CrudContaAPagar()
            INSERI.id = self.tb_Parcelas.item(id, 0).text()
            INSERI.valorPago = self.tb_Parcelas.cellWidget(
                id, 3).text().replace(",", ".")
            INSERI.formaPagamento = self.cb_FormaPagamento.currentData()
            INSERI.dataPagamento = QDate.toString(
                QDate.currentDate(), "yyyy-MM-dd")

            # Inserindo Pagamento no DB
            INSERI.pagarConta()

            # Atualizando valor Recebido
            INSERI = CrudCompra()
            INSERI.id = self.tx_Cod.text()
            INSERI.valorPago = self.tb_Parcelas.cellWidget(
                id, 3).text().replace(",", ".")
            

            # Executando o update no DB
            INSERI.Pagar()

            # Recalculando valores
            if self.tx_valorRecebido.text():
                valorPago = float(
                    self.tx_valorRecebido.text()) + float(INSERI.valorPago)
            else:
                valorPago = float(INSERI.valorPago)

            self.tx_valorRecebido.setText(format(valorPago, '.2f'))
            self.TotalFinal()

            self.ParcelasAPagar()

    # Recebendo Produtos DB
    def ReceberProduto(self):
        INSERI = CrudCompra()
        INSERI.dataEntrega = QDate.toString(
            self.dt_Entrega.date(), "yyyy-MM-dd")
        INSERI.id = self.tx_Cod.text()
        INSERI.receberProduto()
        self.EntradaEstoque()
        self.SelectCompraId(self.tx_Cod.text())

    # Dando Entrada no Estoque
    def EntradaEstoque(self):
        INSERI = CrudProduto()
        i = 0
        while i < self.tb_Itens.rowCount():
            INSERI.id = self.tb_Itens.item(i, 0).text()
            INSERI.valorCompra = self.tb_Itens.item(
                i, 4).text().replace(",", ".")
            INSERI.qtdeProduto = self.tb_Itens.item(i, 3).text()
            INSERI.obsProduto = self.tb_Itens.item(i, 2).text()
            
            INSERI.entradaEstoque()
            i += 1


    def imprimirCompra(self):
        self.documento = QWebEngineView()

        headertable = ["Produto", "Obs. ", "Qnte.", "$ Unitário", "$ Total"]
        produto = []
        qtde = []
        obs = []
        valorUnitario = []
        totalItem = []
        for i in range(self.tb_Itens.rowCount()):
            produto.append(self.tb_Itens.item(i, 1).text())
            obs.append(self.tb_Itens.item(i, 2).text())
            qtde.append(self.tb_Itens.item(i, 3).text())
            valorUnitario.append(self.tb_Itens.item(i, 4).text())
            totalItem.append(self.tb_Itens.item(i, 5).text())
        

        # Consulta Venda Banco de Dados
        busca = CrudCompra()
        busca.id = self.tx_Cod.text()
        busca.selectCompraId()

        # Consulta Cliente banco de dados
        cliente = CrudFornecedor()
        cliente.id = self.tx_Id.text()
        cliente.SelectFornecedorId()

        # Consulta Financeiro banco de dados
        financeiro= CrudContaAPagar()
        financeiro.idCompra = self.tx_Cod.text()
        financeiro.listaParcelas()
    
        html = self.renderTemplate(
            "venda.html",
            estilo=self.resourcepath('Template/estilo.css'),
            titulo="Pedido de Compra Nº:",
            idPedido=self.tx_Cod.text(),
            cliente = cliente.nomeFantasia,
            endCliente= [cliente.endereco, cliente.numero],
            cepCliente = cliente.cep,
            emailEcliente = cliente.email,
            cpfCliente = cliente.cnpj,
            cidadeCliente = cliente.cidade,
            telefoneCliente = self.formatoNumTelefone(cliente.telefone),
            rgCliente = cliente.inscEstadual,
            bairroCliente = cliente.bairro,
            estadoCliente = cliente.estado,
            celularCliente = "",
            dataEmissao = QDate.toString(self.dt_Emissao.date(), 
                                                "dd-MM-yyyy"),
            prazoEntrega= QDate.toString(self.dt_Prazo.date(), 
                                                "dd-MM-yyyy"),
            dataEntrega=QDate.toString(self.dt_Entrega.date(), 
                                                "dd-MM-yyyy"),
            statusEntrega=[busca.idStatusEntrega, busca.statusEntrega],
            statusFinanceiro=busca.statusPagamento,
            headertable=headertable,
            descProduto=produto,
            observacao = obs,
            quantidade=qtde,
            valUnit=valorUnitario,
            valTotalItens = totalItem,
            subtotal = self.lb_SubTotal.text(),
            frete = self.tx_Frete.text(),
            desconto = self.tx_Desconto.text(),
            total = self.tx_TotalFinal.text(),
            formaPagamento = self.cb_FormaPagamento.currentText(),
            condicao = self.cb_QtdeParcela.currentText(),
            descParcela = financeiro.descricao,
            vencimentoparcela = financeiro.dataVencimento,
            valorParcela = financeiro.valor,
            situacao= financeiro.statusPagamento,
            formaPagamentoParcela= financeiro.formaPagamento
            
        )

        self.documento.load(QUrl("file:///" +
                                        self.resourcepath("report.html")))
        self.documento.loadFinished['bool'].connect(self.previaImpressao)
