# -*- codind: utf-8 -*-
from PySide2 import QtCore
from Views.APagar import Ui_ct_APagar
from Crud.CrudAPagar import CrudAPagar
from functools import partial
from Views.formAPagar import Ui_ct_FormPagar


class MainAPagar(Ui_ct_APagar, Ui_ct_FormPagar):
    def mainAPagar(self, frame):
        super(MainAPagar, self).setAPagar(frame)
        self.fr_Apagar.show()

        """ Chamanda de funções localizadas no arquivo financeiro.py na pasta Funcoes """
        # Icone dos botoes
        self.setIconFinanceiro()

        # Setando Datas
        self.setDataFinanceiro()

        # Tamanho da Tabela
        self.tamanhoTabelaFinanceiro(self.fr_Apagar)
        """ Fim Chamanda financeiro.py  """

        # Chamando funcao popular checkBox
        self.listaStatus()

        # Chamando funcao Popular tabela a receber
        self.tabelaAPagar()

        # Funcao chamada botoes
        self.bt_Busca.clicked.connect(self.tabelaAPagar)

        # Abrindo form cadastrar
        self.bt_AddConta.clicked.connect(self.formAPagar)

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
                self.tb_APagar, i, 7, partial(self.BuscaContaAPagar, busca.idConta[i]), "Pagar",  '2')

    # Cadastro e Edição conta a pagar
    def formAPagar(self):
        self.LimpaFrame(self.fr_Apagar)
        super(MainAPagar, self).setFormAPagar(self.fr_Apagar)
        self.fr_FormPagar.show()

        # Checado ID
        self.idCheckAPagar()

        """ Chamanda de funções localizadas no arquivo financeiro.py na pasta Funcoes """
        # Autocomplete
        self.setAutocompleteFinanceiro()

        # Data Vencimento e Pagamento com data Atual
        self.setDataVencPgto()

        # Setando Icones Salvar, Voltar e Imprimir
        self.setIconFormFinanceiro()
        """ Fim Chamanda financeiro.py  """

        """ Chamanda de funções localizadas no arquivo FormaPagamento.py na pasta Funcoes """
        # Populando combobox Forma de Pagamento
        self.CboxFPagamento(self.cb_formaPagamento)
        """ Fim Chamanda FormaPagamento.py  """

        """ Chamanda de funções localizadas no arquivo categoriaAPagar.py na pasta Funcoes """
        # Populando combobox Forma de Pagamento
        self.cboxCatAPagar(self.cb_categoria)
        """ Fim Chamanda categoriaAPagar.py  """

        """ Chamanda de funções localizadas no arquivo fornecedor.py na pasta Funcoes """
        # Campo Busca por nome e Autocompletar Fornecedor
        self.tx_NomeFantasia.textEdited.connect(self.autocompleFornecedor)
        self.tx_NomeFantasia.returnPressed.connect(
            partial(self.BuscaFornecedorNome, self.tx_descricao))

        # Return Press Busca Id Fornecedor
        self.tx_Id.returnPressed.connect(
            partial(self.BuscaFornecedorId, self.tx_descricao))

        """ Fim Chamadas """

        self.bt_Voltar.clicked.connect(self.JanelaAPagar)

    # checando campo Id se é Edicao ou Nova Venda
    def idCheckAPagar(self):
        if not self.tx_Cod.text():
            busca = CrudAPagar()
            self.tx_Cod.setText(str(busca.lastIdAPagar()))
        pass

    # Editar / Cadastrar conta a Pagar
    def BuscaContaAPagar(self, id):
        self.formAPagar()
        self.tx_Cod.setText(str(id))

    # Pagando Compra
    def PagarParcela(self, id):
        # print(self.tb_parcelasVenda.item(id, 0).text())

        if self.tb_APagar.cellWidget(id, 6).text():
            INSERI = CrudAPagar()
            INSERI.idConta = id
            INSERI.valorPago = self.tb_APagar.cellWidget(
                id, 6).text().replace(",", ".")

            INSERI.dataPagamento = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), "yyyy-MM-dd")

            INSERI.cadContaPagar()
            self.tabelaAPagar()
