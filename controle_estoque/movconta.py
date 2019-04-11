# -*- codind: utf-8 -*-
from PyQt5.QtCore import QDate, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import re


from Views.movConta import Ui_ct_movimento
from Crud.CrudContaAReceber import CrudContaAReceber
from Crud.CrudContaAPagar import CrudContaAPagar


class MainMovimentoConta(Ui_ct_movimento):

    def mainmovconta(self, frame):
        super(MainMovimentoConta, self).setMovConta(frame)
        self.fr_movimento.show()

        # Icone dos botoes
        self.IconeBotaoMenu(self.bt_BuscaMovimento,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_PrintMovimento,
                            self.resourcepath('Images/gtk-print.png'))

        # Setando Data Padrão
        self.dt_inicio.setDate(self.primeiroDiaMes())
        self.dt_fim.setDate(self.ultimoDiaMes())

        # Tamanho da tabela de detalhes
        self.tb_receita.setColumnWidth(0, 360)
        self.tb_receita.setColumnWidth(1, 100)
        self.tb_despesa.setColumnWidth(0, 360)
        self.tb_despesa.setColumnWidth(1, 100)

        # Funcao chamada botoes
        # Buscar
        self.bt_BuscaMovimento.clicked.connect(self.Entrada)
        self.bt_BuscaMovimento.clicked.connect(self.Despesa)

        # Imprimir
        self.bt_PrintMovimento.clicked.connect(self.imprimirMovimento)

        # Chamando primeira consulta
        self.Entrada()
        self.Despesa()

    def Entrada(self):
        dataInicio = QDate.toString(
            self.dt_inicio.date(), "yyyy-MM-dd")
        dataFim = QDate.toString(
            self.dt_fim.date(), "yyyy-MM-dd")

        busca = CrudContaAReceber()
        busca.dataRecebimento = dataInicio
        busca.dataFim = dataFim
        busca.movEntrada()

        # Setando a data referente a busca
        self.lb_inicioMovimento.setText(QDate.toString(
            self.dt_inicio.date(), "dd-MM-yyyy"))
        self.lb_fimMovimento.setText(QDate.toString(
            self.dt_fim.date(), "dd-MM-yyyy"))
        self.lb_inicioDespesa.setText(QDate.toString(
            self.dt_inicio.date(), "dd-MM-yyyy"))
        self.lb_fimDespesa.setText(QDate.toString(
            self.dt_fim.date(), "dd-MM-yyyy"))

        self.lb_entradaPendente.setText(str(busca.valorAReceber))
        self.lb_entradaRecebido.setText(str(busca.valorRecebido))

        if busca.valorAReceber > 0.01:
            # Grafico
            if busca.valorRecebido:
                valor = busca.valorRecebido / busca.valorAReceber * 100
                # formato
                self.pr_receita.setFormat("%.02f%%" % (valor))
                # Max e valor
                self.pr_receita.setMaximum(busca.valorAReceber)
                self.pr_receita.setValue(busca.valorRecebido)
        self.detalheEntrada()
        pass

    def detalheEntrada(self):
        dataInicio = QDate.toString(
            self.dt_inicio.date(), "yyyy-MM-dd")
        dataFim = QDate.toString(
            self.dt_fim.date(), "yyyy-MM-dd")

        busca = CrudContaAReceber()
        busca.dataRecebimento = dataInicio
        busca.dataFim = dataFim
        busca.detalheEntrada()

        while self.tb_receita.rowCount() > 0:
            self.tb_receita.removeRow(0)

        i = 0
        while i < len(busca.categoria):
            self.tb_receita.insertRow(i)
            self.conteudoTabelaLeft(
                self.tb_receita, i, 0, busca.categoria[i] + " - "+busca.formaPagamento[i])
            self.conteudoTabela(self.tb_receita, i, 1,
                                "R$ " + str(busca.valorRecebido[i]))
            i += 1

        pass

    def Despesa(self):
        dataInicio = QDate.toString(
            self.dt_inicio.date(), "yyyy-MM-dd")
        dataFim = QDate.toString(
            self.dt_fim.date(), "yyyy-MM-dd")

        busca = CrudContaAPagar()
        busca.dataPagamento = dataInicio
        busca.dataFim = dataFim
        busca.movDespesa()
        self.lb_despesaAPagar.setText(str(busca.valorAPagar))
        self.lb_despesaPaga.setText(str(busca.valorPago))

        if busca.valorAPagar > 0.01:

            # Grafico
            if busca.valorPago:
                valor = busca.valorPago / busca.valorAPagar * 100
                # formato
                self.pr_despesa.setFormat("%.02f%%" % (valor))
                # Max e valor
                self.pr_despesa.setMaximum(busca.valorAPagar)
                self.pr_despesa.setValue(busca.valorPago)
        self.detalheDespesa()
        pass

    def detalheDespesa(self):
        dataInicio = QDate.toString(
            self.dt_inicio.date(), "yyyy-MM-dd")
        dataFim = QDate.toString(
            self.dt_fim.date(), "yyyy-MM-dd")

        busca = CrudContaAPagar()
        busca.dataPagamento = dataInicio
        busca.dataFim = dataFim
        busca.detalheDespesa()

        while self.tb_despesa.rowCount() > 0:
            self.tb_despesa.removeRow(0)

        i = 0
        while i < len(busca.categoria):
            self.tb_despesa.insertRow(i)
            self.conteudoTabelaLeft(
                self.tb_despesa, i, 0, busca.categoria[i] + " - "+busca.formaPagamento[i])
            self.conteudoTabela(self.tb_despesa, i, 1,
                                "R$ " + str(busca.valorPago[i]))

            i += 1
        self.calculoMovimento()
        pass

    def calculoMovimento(self):

        if self.lb_despesaPaga.text() and self.lb_entradaRecebido.text():
            despesa = float(self.lb_despesaPaga.text())
            receita = float(self.lb_entradaRecebido.text())
        elif self.lb_despesaPaga.text() and not self.lb_entradaRecebido.text():
            despesa = float(self.lb_despesaPaga.text())
            receita = 0.00
        elif not self.lb_despesaPaga.text() and self.lb_entradaRecebido.text():
            receita = float(self.lb_entradaRecebido.text())
            despesa = 0.00

        total = receita - despesa
        if total < 0:
            self.lb_totalMovimento.setStyleSheet("QLabel{\n"
                                                 "font-size: 26px;\n"
                                                 "font-family: \"Arial\";\n"
                                                 "font-weight: bold;\n"
                                                 "color:  red;\n"
                                                 "border: none;\n"
                                                 "background: none;\n"
                                                 "}")
        else:
            self.lb_totalMovimento.setStyleSheet("QLabel{\n"
                                                 "font-size: 26px;\n"
                                                 "font-family: \"Arial\";\n"
                                                 "font-weight: bold;\n"
                                                 "color:  #072D06;\n"
                                                 "border: none;\n"
                                                 "background: none;\n"
                                                 "}")
        self.lb_totalMovimento.setText("R$ "+format(total, ".2f"))

    # Imprimindo

    def imprimirMovimento(self):
        self.documento = QWebEngineView()

        headertable = ["Receitas", "  Despesas"]

        data_inicio = QDate.toString(self.dt_inicio.date(), "dd-MM-yyyy")
        data_fim = QDate.toString(self.dt_fim.date(), "dd-MM-yyyy")

        desc_receita = []
        total_desc = []
        desc_despesa = []
        total_descDespesa = []
        print(self.usuario)

        if self.tb_receita.rowCount() >= 1:
            for i in range(self.tb_receita.rowCount()):
                desc_receita.append(self.tb_receita.item(i, 0).text())
                total_desc.append(self.tb_receita.item(i, 1).text())

        if self.tb_despesa.rowCount() >= 1:
            for i in range(self.tb_despesa.rowCount()):
                desc_despesa.append(self.tb_despesa.item(i, 0).text())
                total_descDespesa.append(self.tb_despesa.item(i, 1).text())

        if self.lb_despesaPaga.text():
            totaldespesa = self.lb_despesaPaga.text()
        else:
            totaldespesa = 0.00

        if self.lb_entradaRecebido.text():
            totalreceita = self.lb_entradaRecebido.text()
        else:
            totalreceita = 0.00

        totalFinal = self.lb_totalMovimento.text()
        totalFinal2 = re.sub(r'([^\d]+) ', '', totalFinal)

        self.renderTemplate(
            "movimento.html",
            estilo=self.resourcepath('Template/estilo.css'),
            titulo="Fluxo de Caixa periodo {} à {}".format(
                data_inicio, data_fim),
            headertable=headertable,
            desc_receita=desc_receita,
            total_desc=total_desc,
            desc_despesa=desc_despesa,
            total_descDespesa=total_descDespesa,
            totaldespesa=totaldespesa,
            totalreceita=totalreceita,
            totalFinal=totalFinal,
            totalFinal2=float(totalFinal2)
        )

        self.documento.load(QUrl.fromLocalFile(
                                 self.resourcepath("report.html")))
        self.documento.loadFinished['bool'].connect(self.previaImpressao)
