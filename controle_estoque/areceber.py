# -*- codind: utf-8 -*-
from functools import partial
from datetime import date


from PyQt5.QtCore import QDate, Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


from Views.aReceber import Ui_ct_AReceber
from Views.formAReceber import Ui_ct_FormReceber


from Crud.CrudContaAReceber import CrudContaAReceber
from Crud.CrudCatAReceber import CrudCatAReceber
from Crud.CrudStatusPagamento import CrudStatusPagamento

from Funcoes.extenso import retorno


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
        # Buscar
        self.bt_Busca.clicked.connect(self.tabelaAReceber)

        # Imprimir
        self.bt_Print.clicked.connect(self.imprimirAReceber)

        # Abrindo form cadastrar
        self.bt_AddConta.clicked.connect(self.formAReceber)

    # Populando check Box
    def listaStatus(self):
        busca = CrudStatusPagamento()
        busca.listaStatusPagamento()
        self.cb_Situacao.clear()

        i = 0
        for lista in busca.statusPagamento:
            self.cb_Situacao.addItem(
                busca.statusPagamento[i].upper(), str(busca.id[i]))
            i += 1

        self.cb_Situacao.setCurrentIndex(
            self.cb_Situacao.findData(2))

    # Populando tabela de contas a receber
    def tabelaAReceber(self):
        busca = CrudContaAReceber()
        dataInicio = QDate.toString(
            self.dt_Inicio.date(), "yyyy-MM-dd")
        dataFim = QDate.toString(
            self.dt_Fim.date(), "yyyy-MM-dd")
        busca.dataVencimento = dataInicio
        busca.dataFim = dataFim
        busca.statusPagamento = self.cb_Situacao.currentData()
        busca.listaContaAReceber()
        while self.tb_AReceber.rowCount() > 0:
            self.tb_AReceber.removeRow(0)

        self.totalRecebido = 0.00
        self.totalPendente = 0.00

        i = 0
        for lista in busca.nomeCliente:
            self.tb_AReceber.insertRow(i)
            self.conteudoTabela(self.tb_AReceber, i, 0, str(busca.id[i]))
            self.TabelaStatus(self.tb_AReceber, i, 1,
                              self.StatusEntrega(1,
                                                 busca.idStatusPagamento[i]))
            self.TabelaNomeTelefone(self.tb_AReceber, i, 2, busca.nomeCliente[i],
                                    busca.telefoneCliente[i])
            self.TabelaNomeTelefone(
                self.tb_AReceber, i, 3, busca.descricao[i], "")

            self.TabelaEntrega(self.tb_AReceber, i, 4,
                               busca.dataVencimento[i],
                               self.StatusEntrega(busca.idStatusPagamento[i]),
                               busca.statusPagamento[i].upper())
            self.conteudoTabela(self.tb_AReceber, i, 5,
                                "R$ "+str(busca.valor[i]))

            self.conteudoTabela(self.tb_AReceber, i, 6,
                                "R$ "+str(busca.valor[i] - busca.valorRecebido[i]))
            self.botaoReceberParcela(
                self.tb_AReceber, i, 7, partial(
                    self.BuscaContaAReceber, busca.id[i]),
                "Receber",  2)

            # Total Pendente
            self.totalPendente = self.totalPendente + \
                float((busca.valor[i] - busca.valorRecebido[i]))
            # Total Recebido
            self.totalRecebido = self.totalRecebido + \
                float(busca.valorRecebido[i])

            i += 1

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
        # Adicionando Nova Categoria
        self.tx_addCategoria.returnPressed.connect(self.CadCategoriraReceber)

        # Foco campos ID Cliente
        self.tx_Id.setFocus()

        # Botao Receber
        self.bt_receber.clicked.connect(self.ReceberParcela)

        # Imprimir Recibo
        self.bt_PrintRecibo.clicked.connect(self.imprimirReciboRec)

        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.validaCadReceber)

        # Botao Voltar
        self.bt_Voltar.clicked.connect(self.JanelaAReceber)
        pass

    # checando campo Id se é Edicao ou Nova Venda
    def idCheckAReceber(self):
        if not self.tx_Cod.text():
            busca = CrudContaAReceber()
            self.tx_Cod.setText(str(busca.lastIdContaAReceber()))
        pass

    # Buscando Conta a Receber através de ID recebido da Tabela
    def BuscaContaAReceber(self, id):
        self.formAReceber()
        busca = CrudContaAReceber()
        busca.id = id
        busca.selectContaID()
        self.tx_Cod.setText(str(busca.id))
        self.tx_Id.setText(str(busca.idCliente))
        self.BuscaClienteId(self.tx_descricao)
        self.tx_descricao.setText(busca.descricao)
        self.cb_categoria.setCurrentIndex(
            self.cb_categoria.findData(busca.categoria))
        self.dt_Vencimento.setDate(busca.dataVencimento)
        self.tx_valor.setText(str(busca.valor))
        self.tx_Obs.setPlainText(busca.obs)
        if busca.dataRecebimento:
            self.dt_dataPagamento.setDate(busca.dataRecebimento)
        self.cb_formaPagamento.setCurrentIndex(
            self.cb_formaPagamento.findData(busca.idFormaPagamento))
        self.tx_valorPago.setText(str(busca.valor - busca.valorRecebido))
        self.lb_ValorPendente.setText(str(busca.valor - busca.valorRecebido))

        if busca.idStatusPagamento == 1:
            self.bt_receber.setDisabled(True)
            self.bt_PrintRecibo.setVisible(True)
            self.desabilitaLineEdit(self.fr_FormReceber)

        elif busca.idStatusPagamento == 2:
            self.bt_receber.setEnabled(True)

        self.cb_repetir.setHidden(True)
        self.lb_Repetir.setHidden(True)
        self.lb_obsRepetir.setHidden(True)
        pass

    # Recebendo pagamento DB
    def ReceberParcela(self, id):

        if not self.tx_valorPago.text():
            self.tx_valorPago.setFocus()
        elif not self.cb_formaPagamento.currentData():
            self.cb_formaPagamento.setFocus()
        else:
            INSERI = CrudContaAReceber()
            INSERI.id = self.tx_Cod.text()
            INSERI.valorRecebido = self.tx_valorPago.text().replace(",", ".")
            INSERI.formaPagamento = self.cb_formaPagamento.currentData()
            INSERI.dataRecebimento = QDate.toString(
                QDate.currentDate(), "yyyy-MM-dd")
            INSERI.receberConta()
            self.BuscaContaAReceber(self.tx_Cod.text())
        pass

    def validaCadReceber(self):
        if not self.tx_Id.text():
            self.tx_Id.setFocus()
        elif not self.tx_descricao.text():
            self.tx_descricao.setFocus()
        elif not self.tx_valor.text():
            self.tx_valor.setFocus()
        else:
            self.cadContaReceber()

    # Cadastro contaa Receber
    def cadContaReceber(self):
        repetir = int(self.cb_repetir.currentData())
        for i in range(repetir):
            id = int(self.tx_Cod.text()) + i
            INSERI = CrudContaAReceber()
            INSERI.id = id
            INSERI.idCliente = self.tx_Id.text()
            INSERI.descricao = self.tx_descricao.text()
            INSERI.categoria = self.cb_categoria.currentData()
            INSERI.formaPagamento = self.cb_formaPagamento.currentData()
            INSERI.dataVencimento = QDate.toString(QDate.addMonths(
                self.dt_Vencimento.date(), i), "yyyy-MM-dd")
            INSERI.valor = self.tx_valor.text()
            INSERI.obs = self.tx_Obs.toPlainText()
            INSERI.inseriContaAReceber()
        self.BuscaContaAReceber(self.tx_Cod.text())

    # Cadastro Categoria a Receber
    def CadCategoriraReceber(self):
        INSERI = CrudCatAReceber()
        id = INSERI.lastIdCatAReceber()
        categoria = self.tx_addCategoria.text().upper()
        INSERI.id = id
        INSERI.categoriaReceber = categoria
        INSERI.inseriCatAReceber()
        self.cb_categoria.addItem(categoria, str(id))
        self.cb_categoria.setCurrentIndex(self.cb_categoria.findData(str(id)))
        self.CalcelAddFinanceiro(self.bt_CancelAddCatergoria,
                                 self.bt_AddCategoriaProduto, self.tx_addCategoria,
                                 self.cb_categoria)

    # Imprimindo
    def imprimirAReceber(self):
        self.documento = QWebEngineView()

        headertable = ["Cliente", "Descrição ",
                       "Vencimento", "Valor", "V. Pendente"]

        data_inicio = QDate.toString(self.dt_Inicio.date(), "dd-MM-yyyy")
        data_fim = QDate.toString(self.dt_Fim.date(), "dd-MM-yyyy")

        if self.cb_Situacao.currentData() == '1':
            situacao = "Recebida"

        elif self.cb_Situacao.currentData() == '2':
            situacao = "Pendente"

        cliente = []
        descricao = []
        vencimento = []
        valor = []
        pendente = []
        for i in range(self.tb_AReceber.rowCount()):
            cliente.append(self.tb_AReceber.cellWidget(i, 2).text())
            descricao.append(self.tb_AReceber.cellWidget(i, 3).text())
            vencimento.append(self.tb_AReceber.cellWidget(i, 4).text())
            valor.append(self.tb_AReceber.item(i, 5).text())
            pendente.append(self.tb_AReceber.item(i, 6).text())

        self.renderTemplate(
            "areceber.html",
            estilo=self.resourcepath('Template/estilo.css'),
            titulo="Relatório de conta a receber {} de {} à {}".format(
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

    def imprimirReciboRec(self):

        self.documento = QWebEngineView()

        self.renderTemplate(
            "recibo.html",
            estilo=self.resourcepath('Template/estilo.css'),
            cod=self.tx_Cod.text(),
            nome=self.tx_NomeFantasia.text(),
            descricao=self.tx_descricao.text(),
            valor=self.tx_valor.text().replace('.', ','),
            valor_ext=retorno(self.tx_valor.text()),
            data=date.today().strftime("%d-%m-%Y")

        )

        self.documento.load(QUrl("file:///" +
                                 self.resourcepath("report.html")))
        self.documento.loadFinished['bool'].connect(self.previaImpressao)
