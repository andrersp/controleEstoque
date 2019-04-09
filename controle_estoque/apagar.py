# -*- codind: utf-8 -*-
from functools import partial
from datetime import date


from PyQt5.QtCore import QDate, Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


from Views.APagar import Ui_ct_APagar
from Views.formAPagar import Ui_ct_FormPagar

from Crud.CrudContaAPagar import CrudContaAPagar
from Crud.CrudCatAPagar import CrudCatAPagar
from Funcoes.extenso import retorno


class MainAPagar(Ui_ct_APagar, Ui_ct_FormPagar):
    def mainAPagar(self, frame):
        super(MainAPagar, self).setAPagar(frame)
        self.fr_Apagar.show()

        """ 
        Chamanda de funções localizadas no arquivo 
        financeiro.py na pasta Funcoes 
        """

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

        # Imprimir
        self.bt_Print.clicked.connect(self.imprimirAPagar)

        # Abrindo form cadastrar
        self.bt_AddConta.clicked.connect(self.formAPagar)

    # Populando tabela a Pagar
    def tabelaAPagar(self):
        busca = CrudContaAPagar()
        dataInicio = QDate.toString(
            self.dt_Inicio.date(), "yyyy-MM-dd")
        dataFim = QDate.toString(
            self.dt_Fim.date(), "yyyy-MM-dd")
        busca.dataVencimento = dataInicio
        busca.dataFim = dataFim
        busca.statusPagamento = self.cb_Situacao.currentData()
        busca.listaContaAPagar()

        while self.tb_APagar.rowCount() > 0:
            self.tb_APagar.removeRow(0)

        self.totalRecebido = 0.00
        self.totalPendente = 0.00

        for i in range(len(busca.nomeFantasia)):
            self.tb_APagar.insertRow(i)

            self.conteudoTabela(self.tb_APagar, i, 0, str(busca.id[i]))

            self.TabelaStatus(self.tb_APagar, i, 1,
                              self.StatusEntrega(1,
                                                 busca.idStatusPagamento[i]))

            self.TabelaNomeTelefone(self.tb_APagar, i, 2, busca.nomeFantasia[i],
                                    busca.telefone[i])

            self.TabelaNomeTelefone(
                self.tb_APagar, i, 3, busca.descricao[i], "")

            self.TabelaEntrega(self.tb_APagar, i, 4,
                               busca.dataVencimento[i],
                               self.StatusEntrega(busca.idStatusPagamento[i]),
                               busca.statusPagamento[i].upper())

            self.conteudoTabela(self.tb_APagar, i, 5,
                                "R$ "+str(busca.valor[i]))

            self.conteudoTabela(self.tb_APagar, i, 6,
                                "R$ "+str(busca.valor[i] - busca.valorPago[i]))

            self.botaoReceberParcela(
                self.tb_APagar, i, 7, partial(self.BuscaContaAPagar, busca.id[i]), "Pagar",  '2')
            # Total Pendente
            self.totalPendente = self.totalPendente + \
                float((busca.valor[i] - busca.valorPago[i]))
            # Total Recebido
            self.totalRecebido = self.totalRecebido + \
                float(busca.valorPago[i])

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

        # Imprimir Recibo
        self.bt_PrintRecibo.clicked.connect(self.imprimirReciboPag)

        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.validaCadPagar)

        # Botao Voltar
        self.bt_Voltar.clicked.connect(self.JanelaAPagar)

    # checando campo Id se é Edicao ou Nova Venda
    def idCheckAPagar(self):
        if not self.tx_Cod.text():
            busca = CrudContaAPagar()
            self.tx_Cod.setText(str(busca.lastIdContaAPagar()))
        pass

    # Buscando Conta a Pagar através de ID recebido da Tabela
    def BuscaContaAPagar(self, id):
        self.formAPagar()
        busca = CrudContaAPagar()
        busca.id = id
        busca.selectContaID()
        self.tx_Cod.setText(str(busca.id))
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
            self.cb_formaPagamento.findData(busca.idFormaPagamento))
        self.tx_valorPago.setText(str(busca.valor - busca.valorPago))
        self.lb_ValorPendente.setText(str(busca.valor - busca.valorPago))

        if busca.idStatusPagamento == 1:
            self.desabilitaLineEdit(self.fr_FormPagar)
            self.bt_PrintRecibo.setVisible(True)
        elif busca.idStatusPagamento == 2:
            self.bt_receber.setEnabled(True)

        self.cb_repetir.setHidden(True)
        self.lb_Repetir.setHidden(True)
        self.lb_obsRepetir.setHidden(True)
        pass

    # realizando pagamento DB
    def PagarParcela(self, id):

        if not self.tx_valorPago.text():
            self.tx_valorPago.setFocus()
        elif not self.cb_formaPagamento.currentData():
            self.cb_formaPagamento.setFocus()
        else:
            INSERI = CrudContaAPagar()
            INSERI.id = self.tx_Cod.text()
            INSERI.formaPagamento = self.cb_formaPagamento.currentData()
            INSERI.valorPago = self.tx_valorPago.text().replace(",", ".")
            INSERI.dataPagamento = QDate.toString(
                QDate.currentDate(), "yyyy-MM-dd")
            INSERI.pagarConta()
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
            INSERI = CrudContaAPagar()
            INSERI.id = id
            INSERI.idFornecedor = self.tx_Id.text()
            INSERI.descricao = self.tx_descricao.text()
            INSERI.categoria = self.cb_categoria.currentData()
            INSERI.dataVencimento = QDate.toString(QDate.addMonths(
                self.dt_Vencimento.date(), i), "yyyy-MM-dd")
            INSERI.valor = self.tx_valor.text()
            INSERI.formaPagamento = self.cb_formaPagamento.currentData()
            INSERI.obs = self.tx_Obs.toPlainText()
            INSERI.inseriContaAPagar()

        self.BuscaContaAPagar(self.tx_Cod.text())

    # Cadastro Categoria a Pagar
    def CadCategoriraPagar(self):
        INSERI = CrudCatAPagar()
        id = INSERI.lastIdCatAPagar()
        categoria = self.tx_addCategoria.text().upper()
        INSERI.id = id
        INSERI.categoriaPagar = categoria
        INSERI.inseriCatAPagar()
        self.cb_categoria.addItem(categoria, str(id))
        self.cb_categoria.setCurrentIndex(self.cb_categoria.findData(str(id)))
        self.CalcelAddFinanceiro(self.bt_CancelAddCatergoria,
                                 self.bt_AddCategoriaProduto, self.tx_addCategoria,
                                 self.cb_categoria)

    # Imprimindo
    def imprimirAPagar(self):
        self.documento = QWebEngineView()

        headertable = ["Fornecedor", "Descrição ",
                       "Vencimento", "Valor", "V. Pendente"]

        data_inicio = QDate.toString(self.dt_Inicio.date(), "dd-MM-yyyy")
        data_fim = QDate.toString(self.dt_Fim.date(), "dd-MM-yyyy")

        if self.cb_Situacao.currentData() == '1':
            situacao = "Pago"

        elif self.cb_Situacao.currentData() == '2':
            situacao = "Pendente"

        cliente = []
        descricao = []
        vencimento = []
        valor = []
        pendente = []
        for i in range(self.tb_APagar.rowCount()):
            cliente.append(self.tb_APagar.cellWidget(i, 2).text())
            descricao.append(self.tb_APagar.cellWidget(i, 3).text())
            vencimento.append(self.tb_APagar.cellWidget(i, 4).text())
            valor.append(self.tb_APagar.item(i, 5).text())
            pendente.append(self.tb_APagar.item(i, 6).text())

        self.renderTemplate(
            "apagar.html",
            estilo=self.resourcepath('Template/estilo.css'),
            titulo="Relatório de conta a pagar {} de {} à {}".format(
                situacao, data_inicio, data_fim),
            headertable=headertable,
            nome=cliente,
            desc=descricao,
            venc=vencimento,
            valor=valor,
            pendente=pendente,
            totalPen=format(self.totalPendente, '.2f'),
            totalRec=format(self.totalRecebido, '.2f')

        )

        self.documento.load(QUrl("file:///" +
                                 self.resourcepath("report.html")))
        self.documento.loadFinished['bool'].connect(self.previaImpressao)

# Imprimindo

    def imprimirReciboPag(self):

        self.documento = QWebEngineView()

        self.renderTemplate(
            "recibopagamento.html",
            estilo=self.resourcepath('Template/estilo.css'),
            cod=self.tx_Cod.text(),

            descricao=self.tx_descricao.text(),
            valor=self.tx_valor.text().replace('.', ','),
            valor_ext=retorno(self.tx_valor.text()),
            data=date.today().strftime("%d-%m-%Y")

        )

        self.documento.load(QUrl("file:///" +
                                 self.resourcepath("report.html")))
        self.documento.loadFinished['bool'].connect(self.previaImpressao)
