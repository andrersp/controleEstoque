# -*- codind: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
from Views.aReceber import Ui_ct_AReceber
from Crud.CrudAReceber import CrudAReceber
from functools import partial
from Views.formAReceber import Ui_ct_FormReceber


class MainAReceber(Ui_ct_AReceber, Ui_ct_FormReceber):
    def mainAReceber(self, frame):
        super(MainAReceber, self).setAReceber(frame)
        self.fr_AReceber.show()

        """ Chamanda de funções localizadas no arquivo financeiro.py na pasta Funcoes """
        # Icone dos botoes
        self.setIconFinanceiro()

        # Setando Data Padrão
        self.setDataFinanceiro()

        # Tamanho da Tabela
        self.tamanhoTabelaFinanceiro(self.fr_AReceber)
        """ Fim das chamandas """

        # Chamando funcao popular checkBox
        self.listaStatus()

        # Chamando funcao Popular tabela a receber
        self.tabelaAReceber()

        # Funcao chamada botoes
        self.bt_Busca.clicked.connect(self.tabelaAReceber)

        # Abrindo form cadastrar
        self.bt_AddConta.clicked.connect(self.formAReceber)

    # Populando check Box
    def listaStatus(self):
        busca = CrudAReceber()
        busca.listaStatus()
        self.cb_Situacao.clear()
        for i in range(len(busca.status)):
            self.cb_Situacao.addItem(
                busca.status[i].upper(), str(busca.idStatus[i]))

        self.cb_Situacao.setCurrentIndex(
            self.cb_Situacao.findData(2))

    # Populando tabela de contas a receber
    def tabelaAReceber(self):
        busca = CrudAReceber()
        dataInicio = QtCore.QDate.toString(
            self.dt_Inicio.date(), "yyyy-MM-dd")
        dataFim = QtCore.QDate.toString(
            self.dt_Fim.date(), "yyyy-MM-dd")
        busca.dataInicio = dataInicio
        busca.dataFim = dataFim
        busca.idStatus = self.cb_Situacao.itemData(
            self.cb_Situacao.currentIndex(), QtCore.Qt.UserRole)
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

            self.tx_tabelaReceber(self.tb_AReceber, i, 6, busca.idStatus[i],
                                  str(busca.valor[i]))
            self.botaoReceberParcela(
                self.tb_AReceber, i, 7, partial(
                    self.BuscaContaAReceber, busca.idConta[i]),
                "Receber",  busca.idStatus[i])

    # Cadastro e Edição conta a receber

    def formAReceber(self):
        self.LimpaFrame(self.fr_AReceber)
        super(MainAReceber, self).setFormAReceber(self.fr_AReceber)
        self.fr_FormReceber.show()

        # Checado ID
        self.idCheckAReceber()

        """ Chamanda de funções localizadas no arquivo financeiro.py na pasta Funcoes """
        # Autocomplete
        self.setAutocompleteFinanceiro()

        # Data Vencimento e Pagamento com data Atual
        self.setDataVencPgto()
        """ Fim Chamanda financeiro.py  """

        """ Chamanda de funções localizadas no arquivo FormaPagamento.py na pasta Funcoes """
        # Autocomplete
        self.CboxFPagamento(self.cb_formaPagamento)
        """ Fim Chamanda FormaPagamento.py  """

        """ Chamanda de funções localizadas no arquivo categoriaAReceber.py na pasta Funcoes """
        # Populando combobox Forma de Pagamento
        self.cboxCatAReceber(self.cb_categoria)
        """ Fim Chamanda categoriaAPagar.py  """

        """ Chamanda de funções localizadas no arquivo clientes.py na pasta Funcoes """
        # Campo Busca por nome e Autocompletar Cliente
        self.tx_NomeFantasia.textEdited.connect(self.autocompleCliente)
        self.tx_NomeFantasia.returnPressed.connect(
            partial(self.BuscaClienteNome, self.tx_descricao))

        # Return Press Busca Id Cliente
        self.tx_Id.returnPressed.connect(
            partial(self.BuscaClienteId, self.tx_descricao))

        """ Fim Chamadas """

        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.cadConta)

        # Botao Voltar
        self.bt_Voltar.clicked.connect(self.JanelaAReceber)
        pass

    # checando campo Id se é Edicao ou Nova Venda
    def idCheckAReceber(self):
        if not self.tx_Cod.text():
            busca = CrudAReceber()
            self.tx_Cod.setText(str(busca.lastIdAReceber()))
        pass

    def BuscaContaAReceber(self, id):
        self.formAReceber()
        self.tx_Cod.setText(str(id))
        pass

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
            INSERI.cadContaReceber()
            self.tabelaAReceber()
        pass

    def cadConta(self):
        print(self.cb_formaPagamento.currentData())
