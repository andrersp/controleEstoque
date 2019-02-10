# -*- codind: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
from Views.APagar import Ui_ct_APagar
from Crud.CrudAPagar import CrudAPagar
from functools import partial


class MainAPagar(Ui_ct_APagar):
    def mainAPagar(self, frame):
        super(MainAPagar, self).setAPagar(frame)
        self.fr_Apagar.show()

        # Icone dos botoes
        self.IconeBotaoMenu(self.bt_Busca,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_Print,
                            self.resourcepath('Images/gtk-print.png'))
        self.IconeBotaoForm(self.bt_AddConta,
                            self.resourcepath('Images/addConta.svg'))

        # Setando Data Padrão
        self.dt_Inicio.setDate(self.primeiroDiaMes())
        self.dt_Fim.setDate(self.ultimoDiaMes())

        # Tamanho da Tabela
        self.tb_APagar.blockSignals(True)
        self.tb_APagar.setColumnHidden(0, True)
        self.tb_APagar.setColumnWidth(1, 10)
        self.tb_APagar.setColumnWidth(2, 270)
        self.tb_APagar.setColumnWidth(3, 260)
        self.tb_APagar.setColumnWidth(4, 120)
        self.tb_APagar.setColumnWidth(5, 107)
        self.tb_APagar.setColumnWidth(6, 107)
        self.tb_APagar.setColumnWidth(7, 40)

        # Chamando funcao popular checkBox
        self.listaStatus()

        # Chamando funcao Popular tabela a receber
        self.tabelaAPagar()

        # Funcao chamada botoes
        self.bt_Busca.clicked.connect(self.tabelaAPagar)

    # Populando tabela a Pagar

    def tabelaAPagar(self):
        busca = CrudAPagar()
        dataInicio = QtCore.QDate.toString(
            self.dt_Inicio.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_Fim.date(), "yyyy-MM-dd")
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.status = self.cb_Situacao.itemData(
            self.cb_Situacao.currentIndex(), QtCore.Qt.UserRole)
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

            INSERI.dataPagamento = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), "yyyy-MM-dd")

            INSERI.cadContaPagar()
            self.tabelaAPagar()
