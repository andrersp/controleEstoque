# -*- codind: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
from Views.movConta import Ui_ct_movimento
from Crud.CrudMovCaixa import CrudMovCaixa


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
        self.bt_BuscaMovimento.clicked.connect(self.Entrada)
        self.bt_BuscaMovimento.clicked.connect(self.Despesa)

        # Chamando primeira consulta
        self.Entrada()
        self.Despesa()

    def Entrada(self):
        dataInicio = QtCore.QDate.toString(
            self.dt_inicio.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_fim.date(), "yyyy-MM-dd")

        busca = CrudMovCaixa()
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.movEntrada()

        # Setando a data referente a busca
        self.lb_inicioMovimento.setText(QtCore.QDate.toString(
            self.dt_inicio.date(), "dd-MM-yyyy"))
        self.lb_fimMovimento.setText(QtCore.QDate.toString(
            self.dt_fim.date(), "dd-MM-yyyy"))
        self.lb_inicioDespesa.setText(QtCore.QDate.toString(
            self.dt_inicio.date(), "dd-MM-yyyy"))
        self.lb_fimDespesa.setText(QtCore.QDate.toString(
            self.dt_fim.date(), "dd-MM-yyyy"))

        if busca.totaAReceber > 0.01:
            self.lb_entradaPendente.setText(str(busca.totaAReceber))
            self.lb_entradaRecebido.setText(str(busca.totalRecebido))

            # Grafico
            if busca.totalRecebido:
                valor = busca.totalRecebido / busca.totaAReceber * 100
                # formato
                self.pr_receita.setFormat("%.02f%%" % (valor))
                # Max e valor
                self.pr_receita.setMaximum(busca.totaAReceber)
                self.pr_receita.setValue(busca.totalRecebido)
            self.detalheEntrada()
        pass

    def detalheEntrada(self):
        dataInicio = QtCore.QDate.toString(
            self.dt_inicio.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_fim.date(), "yyyy-MM-dd")

        busca = CrudMovCaixa()
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.detalheReceita()

        while self.tb_receita.rowCount() > 0:
            self.tb_receita.removeRow(0)

        i = 0
        while i < len(busca.categoria):
            self.tb_receita.insertRow(i)
            self.conteudoTabelaLeft(
                self.tb_receita, i, 0, busca.categoria[i])
            self.conteudoTabela(self.tb_receita, i, 1,
                                "R$ " + str(busca.totalRecebido[i]))
            i += 1

        pass

    def Despesa(self):
        dataInicio = QtCore.QDate.toString(
            self.dt_inicio.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_fim.date(), "yyyy-MM-dd")

        busca = CrudMovCaixa()
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.movDespesa()

        if busca.totaAPagar > 0.01:
            self.lb_despesaAPagar.setText(str(busca.totaAPagar))
            self.lb_despesaPaga.setText(str(busca.totalPago))

            # Grafico
            if busca.totalPago:
                valor = busca.totalPago / busca.totaAPagar * 100
                # formato
                self.pr_despesa.setFormat("%.02f%%" % (valor))
                # Max e valor
                self.pr_despesa.setMaximum(busca.totaAPagar)
                self.pr_receita.setValue(busca.totalPago)
            self.detalheDespesa()
        pass

    def detalheDespesa(self):
        dataInicio = QtCore.QDate.toString(
            self.dt_inicio.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_fim.date(), "yyyy-MM-dd")

        busca = CrudMovCaixa()
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.detalheDespesa()

        while self.tb_despesa.rowCount() > 0:
            self.tb_despesa.removeRow(0)

        i = 0
        while i < len(busca.categoria):
            self.tb_despesa.insertRow(i)
            self.conteudoTabelaLeft(
                self.tb_despesa, i, 0, busca.categoria[i])
            self.conteudoTabela(self.tb_despesa, i, 1,
                                "R$ " + str(busca.totalPago[i]))
            i += 1
        self.calculoMovimento()
        pass

    def calculoMovimento(self):
        despesa = float(self.lb_despesaPaga.text())
        receita = float(self.lb_entradaRecebido.text())

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
