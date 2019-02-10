# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
from Views.mainFinanceiro import Ui_ct_MainFinanceiro
from Crud.CrudAReceber import CrudAReceber
from Crud.CrudAPagar import CrudAPagar
import calendar
from Funcoes.data import DataAtual
from PySide2.QtWebEngineWidgets import QWebEngineView
from jinja2 import Environment, PackageLoader, FileSystemLoader
from functools import partial


class MainFinanceiro(Ui_ct_MainFinanceiro, DataAtual):

    def mainfinanceiro(self, frame):
        super(MainFinanceiro, self).setMainFinanceiro(frame)
        self.frameMainFinanceiro.show()

        # Icone dos botoes
        self.IconeBotaoMenu(self.bt_BuscaMovimento,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_BuscaAReceber,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_BuscaAPagar,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoForm(self.bt_AddContaAReceber,
                            self.resourcepath('Images/addConta.svg'))
        self.IconeBotaoForm(self.bt_AddContaAPagar,
                            self.resourcepath('Images/addConta.svg'))

        # Setando Padrão Campos de data
        self.dt_InicioMovimento.setDate(self.primeiroDiaMes())
        self.dt_FimMovimento.setDate(self.ultimoDiaMes())
        self.dt_InicioAPagar.setDate(self.primeiroDiaMes())
        self.dt_FimAPagar.setDate(self.ultimoDiaMes())
        self.dt_InicioAReceber.setDate(self.primeiroDiaMes())
        self.dt_FimAReceber.setDate(self.ultimoDiaMes())

        # Tamanho tabela
        self.tb_despesa.setColumnWidth(0, 360)
        self.tb_despesa.setColumnWidth(1, 100)
        self.tb_receita.setColumnWidth(0, 360)
        self.tb_receita.setColumnWidth(1, 100)

        self.tb_AReceber.blockSignals(True)
        self.tb_AReceber.setColumnHidden(0, True)
        self.tb_AReceber.resizeRowsToContents()
        self.tb_AReceber.setColumnWidth(1, 5)
        self.tb_AReceber.setColumnWidth(2, 250)
        self.tb_AReceber.setColumnWidth(3, 300)
        self.tb_AReceber.setColumnWidth(4, 120)
        self.tb_AReceber.setColumnWidth(5, 90)
        self.tb_AReceber.setColumnWidth(6, 90)
        self.tb_AReceber.setColumnWidth(7, 20)

        self.tb_APagar.blockSignals(True)
        self.tb_APagar.setColumnHidden(0, True)

        self.tb_APagar.resizeRowsToContents()
        self.tb_APagar.setColumnWidth(1, 5)
        self.tb_APagar.setColumnWidth(2, 250)
        self.tb_APagar.setColumnWidth(3, 300)
        self.tb_APagar.setColumnWidth(4, 120)
        self.tb_APagar.setColumnWidth(5, 90)
        self.tb_APagar.setColumnWidth(6, 90)
        self.tb_APagar.setColumnWidth(7, 20)

        # Add Categoria Combobox
        self.listaStatus()

        # Chamando busca Movimento
        self.buscaReceita()
        self.buscaDespesa()

        # Populando tabela a Receber
        self.tabelaAReceber()

        # Populando tabela a Pagar
        self.tabelaAPagar()

        # Botao Buscar Movimento
        self.bt_BuscaMovimento.clicked.connect(self.buscaReceita)
        self.bt_BuscaMovimento.clicked.connect(self.buscaDespesa)

        # Botao Buscar a receber
        self.bt_BuscaAReceber.clicked.connect(self.tabelaAReceber)

        # Total Receita
        if self.lb_despesaPaga.text() and self.lb_entradaRecebido.text():
            self.calculoMovimento()

    # Buscando Movimentação por periodo

    def buscaReceita(self):
        dataInicio = QtCore.QDate.toString(
            self.dt_InicioMovimento.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_FimMovimento.date(), "yyyy-MM-dd")

        # Movimento a Receber
        busca = CrudAReceber()
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        totalReceita = busca.movimentoTotalReceita()

        if totalReceita[0] > 0.01:
            self.lb_inicioMovimento.setText(busca.dataInicio)
            self.lb_fimMovimento.setText(busca.dataFim)
            self.lb_entradaRecebido.setText(str(totalReceita[1]))
            self.lb_entradaPendente.setText(str(totalReceita[0]))

        if totalReceita[0] and totalReceita[1]:
            valor = float(totalReceita[1]) / \
                float(totalReceita[0]) * 100
            self.pr_receita.setFormat("%.02f%%" % (valor))

            self.pr_receita.setMaximum(float(totalReceita[0]))
            self.pr_receita.setValue(float(totalReceita[1]))
        self.detalheReceita()

    def buscaDespesa(self):
        dataInicio = QtCore.QDate.toString(
            self.dt_InicioMovimento.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_FimMovimento.date(), "yyyy-MM-dd")

        # Movimento A Pagar
        busca = CrudAPagar()
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        totalDespesa = busca.movimentoTotalDespesa()

        if totalDespesa[0] > 0.01:
            self.lb_inicioDespesa.setText(busca.dataInicio)
            self.lb_fimDespesa.setText(busca.dataFim)
            self.lb_despesaPaga.setText(str(totalDespesa[1]))
            self.lb_despesaAPagar.setText(str(totalDespesa[0]))

        if totalDespesa[1] and totalDespesa[0]:
            valor = float(totalDespesa[1]) / \
                float(totalDespesa[0]) * 100
            self.pr_despesa.setFormat("%.02f%%" % (valor))
            self.pr_despesa.setMaximum(totalDespesa[0])
            self.pr_despesa.setValue(totalDespesa[1])

        self.detalheDespesa()

    def detalheReceita(self):
        busca = CrudAReceber()
        dataInicio = QtCore.QDate.toString(
            self.dt_InicioMovimento.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_FimMovimento.date(), "yyyy-MM-dd")
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.movimentoRecebido()

        while self.tb_receita.rowCount() > 0:
            self.tb_receita.removeRow(0)

        for i in range(len(busca.totalReceita)):
            self.tb_receita.insertRow(i)
            self.conteudoTabelaLeft(self.tb_receita, i, 0, busca.categoria[i])
            self.conteudoTabela(self.tb_receita, i, 1,
                                "R$  "+str(busca.totalReceita[i]))

    def detalheDespesa(self):
        busca = CrudAPagar()
        dataInicio = QtCore.QDate.toString(
            self.dt_InicioMovimento.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_FimMovimento.date(), "yyyy-MM-dd")
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.movimentoPago()

        while self.tb_despesa.rowCount() > 0:
            self.tb_despesa.removeRow(0)

        for i in range(len(busca.totalDespesa)):
            self.tb_despesa.insertRow(i)
            self.conteudoTabelaLeft(self.tb_despesa, i, 0, busca.categoria[i])
            self.conteudoTabela(self.tb_despesa, i, 1,
                                "R$  "+str(busca.totalDespesa[i]))

    def calculoMovimento(self):
        despesa = float(self.lb_despesaPaga.text())
        receita = float(self.lb_entradaRecebido.text())

        total = receita - despesa

        self.lb_totalMovimento.setText("R$ "+format(total, ".2f"))

        # # Gerando html
        # template_loader = FileSystemLoader(
        #     searchpath=self.resourcepath('Template/'))
        # # Jinja2 template environment
        # env = Environment(loader=template_loader)
        # template = env.get_template('movimento.html')

        # titulo = "Movimento de {} à {}".format(
        #     busca.dataInicio, busca.dataFim)

        # total = float(self.lb_entradaRecebido.text()) - \
        #     float(self.lb_despesaPaga.text())

        # base = {'estilo': self.resourcepath('Template/estilo.css'),
        #         'titulo': titulo,
        #         'total': total
        #         }
        # html = template.render(base)
        # with open(self.resourcepath('report.html'), 'w') as f:
        #     f.write(html)
        # self.documento = QWebEngineView(self.tab_MovCaixa)
        # self.documento.setGeometry(QtCore.QRect(20, 180, 960, 250))

        # self.documento.load(QtCore.QUrl("file:///" +
        #                                 self.resourcepath("report.html")))
        # self.documento.show()
    def listaStatus(self):
        busca = CrudAReceber()
        busca.listaStatus()
        self.cb_situacaoAReceber.clear()
        self.cb_situacaoAPagar.clear()
        for i in range(len(busca.status)):
            self.cb_situacaoAReceber.addItem(
                busca.status[i].upper(), str(busca.idStatus[i]))
            self.cb_situacaoAPagar.addItem(
                busca.status[i].upper(), str(busca.idStatus[i]))

        self.cb_situacaoAReceber.setCurrentIndex(
            self.cb_situacaoAReceber.findData(2))
        self.cb_situacaoAPagar.setCurrentIndex(
            self.cb_situacaoAReceber.findData(2))

    def tabelaAReceber(self):
        busca = CrudAReceber()
        dataInicio = QtCore.QDate.toString(
            self.dt_InicioAReceber.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_FimAReceber.date(), "yyyy-MM-dd")
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.idStatus = self.cb_situacaoAReceber.itemData(
            self.cb_situacaoAReceber.currentIndex(), QtCore.Qt.UserRole)
        busca.listaAReceber()
        while self.tb_AReceber.rowCount() > 0:
            self.tb_AReceber.removeRow(0)
        self.tb_AReceber.clearContents()

        for i in range(len(busca.cliente)):
            self.tb_AReceber.insertRow(i)
            self.conteudoTabela(self.tb_AReceber, i, 0, str(busca.idConta[i]))
            self.TabelaStatus(self.tb_AReceber, i, 1,
                              self.StatusEntrega(1,
                                                 busca.idStatus[i]))
            self.TabelaNomeTelefone(self.tb_AReceber, i, 2, busca.cliente[i],
                                    busca.telefoneCliente[i])
            self.TabelaNomeTelefone(
                self.tb_AReceber, i, 3, busca.descricao[i], "")

            self.TabelaEntrega(self.tb_AReceber, i, 4,
                               busca.dataVencimento[i],
                               self.StatusEntrega(busca.idStatus[i]),
                               busca.status[i].upper())
            self.conteudoTabela(self.tb_AReceber, i, 5,
                                "R$ "+str(busca.valor[i]))

            self.tx_tabelaReceber(self.tb_AReceber, i, 6, busca.idStatus[i], str(
                busca.valor[i]))
            self.botaoReceberParcela(
                self.tb_AReceber, i, 7, partial(self.ReceberParcela, i), "Receber",  busca.idStatus[i])

    # Recebendo pagamento DB
    def ReceberParcela(self, id):
        # print(self.tb_AReceber.item(id, 0).text())

        if self.tb_AReceber.cellWidget(id, 6).text():
            INSERI = CrudAReceber()
            INSERI.idConta = self.tb_AReceber.item(id, 0).text()
            INSERI.valorRecebido = self.tb_AReceber.cellWidget(
                id, 6).text().replace(",", ".")

            INSERI.dataRecebimento = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), "yyyy-MM-dd")
            # if float(self.tb_AReceber.cellWidget(id, 3).text().replace(",", ".")) < float(self.tb_AReceber.item(id, 2).text().replace(",", ".")):
            #     INSERI.status = 2
            # else:
            #     INSERI.status = 1

            INSERI.cadContaReceber()
            self.tabelaAReceber()
            self.buscaReceita()
            self.buscaDespesa()
            self.calculoMovimento()

    def tabelaAPagar(self):
        busca = CrudAPagar()
        dataInicio = QtCore.QDate.toString(
            self.dt_InicioAPagar.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_FimAPagar.date(), "yyyy-MM-dd")
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.status = self.cb_situacaoAPagar.itemData(
            self.cb_situacaoAPagar.currentIndex(), QtCore.Qt.UserRole)
        busca.listaAPagar()
        while self.tb_APagar.rowCount() > 0:
            self.tb_APagar.removeRow(0)

        for i in range(len(busca.fornecedor)):
            self.tb_APagar.insertRow(i)
            self.conteudoTabela(self.tb_APagar, i, 0, str(busca.idConta[i]))
            self.TabelaStatus(self.tb_APagar, i, 1,
                              self.StatusEntrega(1,
                                                 busca.status[i]))
            self.TabelaNomeTelefone(self.tb_APagar, i, 2, busca.fornecedor[i],
                                    busca.telefone[i])
            self.TabelaNomeTelefone(
                self.tb_APagar, i, 3, busca.descricao[i], "")

            self.TabelaEntrega(self.tb_APagar, i, 4,
                               busca.dataVencimento[i],
                               self.StatusEntrega(busca.status[i]),
                               busca.nomeStatus[i].upper())
            self.conteudoTabela(self.tb_APagar, i, 5,
                                "R$ "+str(busca.valor[i]))

            self.tx_tabelaReceber(self.tb_APagar, i, 6, busca.status[i], str(
                busca.valor[i]))
            self.botaoReceberParcela(
                self.tb_APagar, i, 7, partial(self.PagarParcela, i), "Pagar",  busca.status[i])

    # Pagando Compra
    def PagarParcela(self, id):
        # print(self.tb_parcelasVenda.item(id, 0).text())

        if self.tb_APagar.cellWidget(id, 6).text():
            INSERI = CrudAPagar()
            INSERI.idConta = self.tb_APagar.item(id, 0).text()
            INSERI.valorPago = self.tb_APagar.cellWidget(
                id, 6).text().replace(",", ".")

            INSERI.dataRecebimento = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), "yyyy-MM-dd")

            INSERI.cadContaPagar()
            self.tabelaAPagar()
            self.buscaReceita()
            self.buscaDespesa()
            self.calculoMovimento()
