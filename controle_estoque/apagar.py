# -*- codind: utf-8 -*-
from functools import partial


from PySide2 import QtCore


from Views.APagar import Ui_ct_APagar
from Crud.CrudAPagar import CrudAPagar
from Views.formAPagar import Ui_ct_FormPagar
from Crud.CrudCategoriaAPagar import CrudCatAPagar


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

            self.conteudoTabela(self.tb_APagar, i, 6,
                                "R$ "+str(busca.valorPendente[i]))
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

        # Pupulando combobox Repetir
        self.cboxRepedir(self.cb_repetir)

        # Botao Add Categoria
        self.bt_AddCategoriaProduto.clicked.connect(
            self.AddCategoriaFinanceiro)

        # Botao Cancela add Categoria
        self.bt_CancelAddCatergoria.clicked.connect(
            partial(self.CalcelAddFinanceiro, self.bt_CancelAddCatergoria,
                    self.bt_AddCategoriaProduto, self.tx_addCategoria,
                    self.cb_categoria))

        # Validador Campos Float
        self.ValidaInputFloat(self.tx_valor)
        self.ValidaInputFloat(self.tx_valorPago)

        # valida Campo Int
        self.ValidaInputInt(self.tx_Id)
        """ Fim Chamanda financeiro.py  """

        """ Chamanda de funções localizadas no arquivo FormaPagamento.py na pasta Funcoes """
        # Populando combobox Forma de Pagamento
        self.CboxFPagamento(self.cb_formaPagamento)
        """ Fim Chamanda FormaPagamento.py  """

        """ Chamanda de funções localizadas no arquivo categoriaAPagar.py na pasta Funcoes """
        # Populando combobox Forma de Pagamento
        self.cboxCatAPagar(self.cb_categoria)
        """ Fim Chamanda categoriaAPagar.py """

        """ Chamanda de funções localizadas no arquivo fornecedor.py na pasta Funcoes """
        # Campo Busca por nome e Autocompletar Fornecedor
        self.tx_NomeFantasia.textEdited.connect(self.autocompleFornecedor)
        self.tx_NomeFantasia.returnPressed.connect(
            partial(self.BuscaFornecedorNome, self.tx_descricao))

        # Return Press Busca Id Fornecedor
        self.tx_Id.returnPressed.connect(
            partial(self.BuscaFornecedorId, self.tx_descricao))

        """ Fim Chamadas """

        # Adicionando Nova Categoria
        self.tx_addCategoria.returnPressed.connect(self.CadCategoriraPagar)

        # Foco campos ID Cliente
        self.tx_Id.setFocus()

        # Botao Pagar
        self.bt_receber.clicked.connect(self.PagarParcela)

        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.validaCadPagar)

        # Botao Voltar
        self.bt_Voltar.clicked.connect(self.JanelaAPagar)

    # checando campo Id se é Edicao ou Nova Venda
    def idCheckAPagar(self):
        if not self.tx_Cod.text():
            busca = CrudAPagar()
            self.tx_Cod.setText(str(busca.lastIdAPagar()))
        pass

    # Buscando Conta a Pagar através de ID recebido da Tabela
    def BuscaContaAPagar(self, id):
        self.formAPagar()
        busca = CrudAPagar()
        busca.idConta = id
        busca.selectContaId()
        self.tx_Cod.setText(str(busca.idConta))
        self.tx_Id.setText(str(busca.idFornecedor))
        self.BuscaFornecedorId(self.tx_descricao)
        self.tx_descricao.setText(busca.descricao)
        self.cb_categoria.setCurrentIndex(
            self.cb_categoria.findData(busca.categoria))
        self.dt_Vencimento.setDate(busca.dataVencimento)
        self.tx_valor.setText(str(busca.valor))
        self.tx_Obs.setPlainText(busca.obs)
        if busca.dataPagamento:
            self.dt_dataPagamento.setDate(busca.dataPagamento)
        self.cb_formaPagamento.setCurrentIndex(
            self.cb_formaPagamento.findData(busca.formaPagamento))
        self.tx_valorPago.setText(str(busca.valorPendente))
        self.lb_ValorPendente.setText(str(busca.valorPendente))

        if busca.idStatus == 1:
            self.bt_receber.setDisabled(True)
            self.desabilitaLineEdit(self.fr_FormPagar)
        self.cb_repetir.setHidden(True)
        self.lb_Repetir.setHidden(True)
        self.lb_obsRepetir.setHidden(True)
        pass

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

    # Recebendo pagamento DB
    def PagarParcela(self, id):

        if not self.tx_valorPago.text():
            self.tx_valorPago.setFocus()
        elif not self.cb_formaPagamento.currentData():
            self.cb_formaPagamento.setFocus()
        else:
            INSERI = CrudAPagar()
            INSERI.idConta = self.tx_Cod.text()
            INSERI.formaPagamento = self.cb_formaPagamento.currentData()
            INSERI.valorPago = self.tx_valorPago.text().replace(",", ".")
            INSERI.dataPagamento = QtCore.QDate.toString(
                QtCore.QDate.currentDate(), "yyyy-MM-dd")
            INSERI.PagarConta()
            self.BuscaContaAPagar(self.tx_Cod.text())

        pass

    # Validando campos a pagar
    def validaCadPagar(self):
        if not self.tx_Id.text():
            self.tx_Id.setFocus()
        elif not self.tx_descricao.text():
            self.tx_descricao.setFocus()
        elif not self.tx_valor.text():
            self.tx_valor.setFocus()
        else:
            self.cadContaPagar()

    def cadContaPagar(self):
        repetir = int(self.cb_repetir.currentData())
        for i in range(repetir):
            id = int(self.tx_Cod.text()) + i
            INSERI = CrudAPagar()
            INSERI.idConta = id
            INSERI.idFornecedor = self.tx_Id.text()
            INSERI.descricao = self.tx_descricao.text()
            INSERI.categoria = self.cb_categoria.currentData()
            INSERI.dataVencimento = QtCore.QDate.toString(QtCore.QDate.addMonths(
                self.dt_Vencimento.date(), i), "yyyy-MM-dd")
            INSERI.valor = self.tx_valor.text()
            INSERI.obs = self.tx_Obs.toPlainText()
            INSERI.cadContaPagar()
        self.BuscaContaAPagar(self.tx_Cod.text())

    # Cadastro Categoria a Pagar
    def CadCategoriraPagar(self):
        INSERI = CrudCatAPagar()
        id = INSERI.lastIdCatAPagar()
        categoria = self.tx_addCategoria.text().upper()
        INSERI.idCatAPagar = id
        INSERI.descCatAPagar = categoria
        INSERI.cadCatAPagar()
        self.cb_categoria.addItem(categoria, str(id))
        self.cb_categoria.setCurrentIndex(self.cb_categoria.findData(str(id)))
        self.CalcelAddFinanceiro(self.bt_CancelAddCatergoria,
                                 self.bt_AddCategoriaProduto, self.tx_addCategoria,
                                 self.cb_categoria)
