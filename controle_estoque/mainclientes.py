# -*- coding: utf-8 -*-
import re
from functools import partial


from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView


from Views.mainClientes import Ui_ct_MainClientes
from Views.formClientes import Ui_ct_FormClientes
from orm.CrudCliente import CrudCliente
from orm.CrudVenda import CrudVenda


class MainClientes(Ui_ct_MainClientes, Ui_ct_FormClientes):

    def mainclientes(self, frame):
        super(MainClientes, self).setMainClientes(frame)
        self.frameMainClientes.show()

        # Icones Botoes
        self.IconeBotaoMenu(self.bt_BuscaClientes,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_PrintRelatCliente,
                            self.resourcepath('Images/gtk-print.png'))
        self.IconeBotaoForm(self.bt_AddNovoClientes,
                            self.resourcepath('Images/addCliente.svg'))

        # Botao Adicionar Cliente / FormClientes
        self.bt_AddNovoClientes.clicked.connect(self.FormClientes)

        # Tamanho colunas tabela
        self.tb_Clientes.blockSignals(True)
        self.tb_Clientes.setColumnHidden(0, True)
        self.tb_Clientes.setColumnWidth(1, 40)
        self.tb_Clientes.setColumnWidth(2, 350)
        self.tb_Clientes.setColumnWidth(3, 235)
        self.tb_Clientes.setColumnWidth(4, 265)
        self.tb_Clientes.setColumnWidth(5, 40)

        # Populando Tabela
        self.TabelaClientes()

        # Busca CLiente por nome
        self.tx_BuscaClientes.textEdited.connect(self.TabelaClientes)

        # Botao imprimir
        self.bt_PrintRelatCliente.clicked.connect(self.imprimirCliente)

    # Dados Tabela

    def TabelaClientes(self):
        lista = CrudCliente()
        lista.nome = self.tx_BuscaClientes.text()
        lista.listaCliente()
        i = 0

        while self.tb_Clientes.rowCount() > 0:
            self.tb_Clientes.removeRow(0)

        if len(lista.nome) >= 1:
            while i < len(lista.nome):
                self.tb_Clientes.insertRow(i)
                self.TabelaStatus(self.tb_Clientes, i, 0,
                                  self.StatusEntrega(1))
                self.TabelaID(self.tb_Clientes, i, 1, lista.id[i])
                self.TabelaNomeTelefone(self.tb_Clientes, i, 2,
                                        lista.nome[i],
                                        lista.sobrenome[i])
                self.TabelaNomeTelefone(self.tb_Clientes, i, 3,
                                        self.formatoNumTelefone(
                                            lista.celular[i]),
                                        self.formatoNumTelefone(
                                            lista.telefone[i]))
                self.TabelaNomeTelefone(self.tb_Clientes, i, 4,
                                        lista.email[i], "")
                # Sinal click tabela
                self.botaoTabela(self.tb_Clientes, i, 5, partial(
                    self.SelectCliente, lista.id[i]), "#005099")
                i += 1
            pass

    # Seleciona Cliente por ID
    def SelectCliente(self, valor):
        id = valor
        self.FormClientes()
        self.tx_Id.setText(str(id))
        busca = CrudCliente()
        busca.id = self.tx_Id.text()
        busca.selectClienteId()
        self.tx_NomeFantasia.setText(busca.nome)
        self.tx_RazaoSocial.setText(busca.sobrenome)
        self.tx_cnpj.setText(busca.cpf)
        self.tx_InscEstadual.setText(busca.rg)
        self.tx_Celular.setText(busca.celular)
        self.tx_Telefone.setText(busca.telefone)
        self.tx_Email.setText(busca.email)
        self.tx_Obs.setText(busca.obs)
        self.tx_Cep.setText(busca.cep)
        self.tx_Endereco.setText(busca.endereco)
        self.tx_Numero.setText(busca.numero)
        self.tx_Bairro.setText(busca.bairro)
        self.tx_Cidade.setText(busca.cidade)
        self.tx_Estado.setText(busca.estado)

        # Limpando tabela Histórico de Compras
        for row in range(self.tb_Historico.rowCount()):
            self.tb_Historico.removeRow(row)

        # Histórico de Compras cliente
        total = '0.00'
        lista = CrudVenda()
        lista.idCliente = valor
        lista.selectVendaCliente()
        i = 0

        while i < len(lista.dataEmissao):
            # print row
            self.tb_Historico.insertRow(i)
            self.conteudoTabela(
                self.tb_Historico, i, 0, str(lista.dataEmissao[i]))
            self.conteudoTabela(
                self.tb_Historico, i, 1, str(lista.dataEntrega[i]))
            self.conteudoTabela(
                self.tb_Historico, i, 2, str(lista.valorTotal[i]))

            total = float(lista.valorTotal[i]) + float(total)

            i += 1

        self.lb_TotalHistorico.setText(format(float(total), ".2f"))
        i += 1
        pass

    # Frame Formulário Produtos
    def FormClientes(self):
        # self.DesativaBotaoProdutos()
        self.LimpaFrame(self.ct_containerClientes)
        super(MainClientes, self).setFormClientes(self.ct_containerClientes)
        self.fr_FormClientes.show()

        # ICone Botoes
        self.IconeBotaoMenu(self.bt_Salvar,
                            self.resourcepath('Images/salvar.png'))
        self.IconeBotaoMenu(self.bt_Voltar,
                            self.resourcepath('Images/cancelar.png'))
        self.IconeBotaoMenu(self.bt_BuscaCep,
                            self.resourcepath('Images/find.png'))

        # Checando se existe ID válido
        self.IdCheckCliente()

        # Tamanho tabela Histórico
        self.tb_Historico.setColumnWidth(0, 100)
        self.tb_Historico.setColumnWidth(1, 100)
        self.tb_Historico.setColumnWidth(2, 100)
        self.tb_Historico.setColumnHidden(3, True)

        # Botão Voltar
        self.bt_Voltar.clicked.connect(self.janelaClientes)
        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.VerificaInputClientes)

        # Buscar Cep
        self.bt_BuscaCep.clicked.connect(self.buscarCepCliente)
        self.tx_Cep.returnPressed.connect(self.buscarCepCliente)

        pass

    # checando campo Id se é Edicao ou Novo Cliente
    def IdCheckCliente(self):
        if not self.tx_Id.text():
            busca = CrudCliente()
            self.tx_Id.setText(str(busca.lastIdCliente()))
        pass

    # Valida Inputs
    def VerificaInputClientes(self):
        if not self.tx_NomeFantasia.text():
            self.tx_NomeFantasia.setFocus()
        elif not self.tx_Celular.text():
            self.tx_Celular.setFocus()
        else:
            self.CadCliente()

    def CadCliente(self):
        INSERI = CrudCliente()
        INSERI.id = self.tx_Id.text()
        INSERI.nome = self.tx_NomeFantasia.text().upper()
        INSERI.sobrenome = self.tx_RazaoSocial.text().upper()
        INSERI.cpf = re.sub(
            '[^[0-9]', '', self.tx_cnpj.text())
        INSERI.rg = re.sub(
            '[^[0-9]', '', self.tx_InscEstadual.text())

        INSERI.celular = re.sub(
            '[^[0-9]', '', self.tx_Celular.text())
        INSERI.telefone = re.sub(
            '[^[0-9]', '', self.tx_Telefone.text())
        INSERI.email = self.tx_Email.text()
        INSERI.obs = self.tx_Obs.text().upper()
        INSERI.cep = re.sub(
            '[^[0-9]', '', self.tx_Cep.text())
        INSERI.endereco = self.tx_Endereco.text().upper()
        INSERI.numero = self.tx_Numero.text()
        INSERI.bairro = self.tx_Bairro.text().upper()
        INSERI.cidade = self.tx_Cidade.text().upper()
        INSERI.estado = self.tx_Estado.text().upper()
        INSERI.inseriCliente()

        self.janelaClientes()

        pass

        # Imprimindo

    def imprimirCliente(self):
        self.documento = QWebEngineView()

        headertable = ["Cod", "Nome ", "Telefone", "Email"]
        busca = CrudCliente()
        busca.nome = self.tx_BuscaClientes.text()
        busca.listaCliente()
        self.renderTemplate(
            "clientes.html",
            estilo=self.resourcepath('Template/estilo.css'),
            titulo="LISTAGEM CLIENTES",
            headertable=headertable,
            codcliente=busca.id,
            nome=busca.nome,
            telefoneFornecedor=busca.celular,
            emailFornecedor=busca.email
        )

        self.documento.load(QUrl("file:///" +
                                 self.resourcepath("report.html")))
        self.documento.loadFinished['bool'].connect(self.previaImpressao)
