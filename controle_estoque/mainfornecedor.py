# -*- coding: utf-8 -*-
from functools import partial
import re


from PySide2 import QtCore
from PySide2.QtWebEngineWidgets import QWebEngineView
from jinja2 import Environment, FileSystemLoader


from Views.mainFornecedor import Ui_ct_MainFornecedor
from Views.formFornecedor import Ui_ct_FormFornecedor
from Crud.CrudFornecedor import CrudFornecedor
from Crud.CrudCompra import CrudCompra


class MainFornecedor(Ui_ct_MainFornecedor, Ui_ct_FormFornecedor):

    def mainfornecedor(self, frame):
        super(MainFornecedor, self).setMainFornecedor(frame)
        self.frameMainFornecedor.show()

        # Icone Botoes
        self.IconeBotaoForm(self.bt_AddNovoFornecedor,
                            self.resourcepath('Images/addFornecedor.svg'))
        self.IconeBotaoMenu(self.bt_BuscaFornecedor,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_PrintRelatForn,
                            self.resourcepath('Images/gtk-print.png'))

        # Botao Adicionar Cliente / FormFornecedor
        self.bt_AddNovoFornecedor.clicked.connect(self.FormFornecedor)

        self.tb_Fornecedor.setColumnHidden(0, True)
        self.tb_Fornecedor.setColumnWidth(1, 40)
        self.tb_Fornecedor.setColumnWidth(2, 270)
        self.tb_Fornecedor.setColumnWidth(3, 130)
        self.tb_Fornecedor.setColumnWidth(4, 225)
        self.tb_Fornecedor.setColumnWidth(5, 225)
        self.tb_Fornecedor.setColumnWidth(6, 60)

        # Populando Tabela Fornecedor
        self.TabelaFornecedor()

        # buscando por nome
        self.tx_BuscaFornecedor.textEdited.connect(self.TabelaFornecedor)

        # Imprimindo Tabela
        self.bt_PrintRelatForn.clicked.connect(self.imprimir)

    def TabelaFornecedor(self):
        lista = CrudFornecedor()
        lista.nomeFantasia = self.tx_BuscaFornecedor.text()
        lista.listaFornecedor()

        # Limpando Tabela
        while self.tb_Fornecedor.rowCount() > 0:
            self.tb_Fornecedor.removeRow(0)

        i = 0
        if len(lista.nomeFantasia) >= 1:
            while i < len(lista.nomeFantasia):
                self.tb_Fornecedor.insertRow(i)
                self.TabelaStatus(self.tb_Fornecedor, i,
                                  0, self.StatusEntrega(1))
                self.TabelaID(self.tb_Fornecedor, i, 1,
                              lista.id[i])
                self.TabelaNomeTelefone(self.tb_Fornecedor, i, 2,
                                        lista.nomeFantasia[i],
                                        lista.razaoSocial[i])
                self.TabelaNomeTelefone(self.tb_Fornecedor, i, 3,
                                        self.formatoNumTelefone(
                                            lista.telefone[i]), "")
                self.TabelaNomeTelefone(self.tb_Fornecedor, i, 4,
                                        lista.email[i], "")
                self.TabelaNomeTelefone(self.tb_Fornecedor, i, 5,
                                        lista.site[i], "")
                # Sinal click tabela
                self.botaoTabela(self.tb_Fornecedor, i, 6,
                                 partial(self.SelectFornecedor,
                                         lista.id[i]), "#005099")
                i += 1
        pass

    # Seleciona Cliente por ID
    def SelectFornecedor(self, id):
        busca = CrudFornecedor()
        self.FormFornecedor()
        busca.id = id
        busca.SelectFornecedorId()
        self.tx_Id.setText(str(busca.id))
        self.tx_NomeFantasia.setText(busca.nomeFantasia)
        self.tx_RazaoSocial.setText(busca.razaoSocial)
        self.tx_cnpj.setText(str(busca.cnpj))
        self.tx_InscEstadual.setText(str(busca.inscEstadual))
        self.tx_Telefone.setText(str(busca.telefone))
        self.tx_Site.setText(busca.site)
        self.tx_Email.setText(busca.email)
        self.tx_Obs.setText(busca.obs)
        self.tx_Cep.setText(busca.cep)
        self.tx_Endereco.setText(busca.endereco)
        self.tx_Numero.setText(str(busca.numero))
        self.tx_Bairro.setText(busca.bairro)
        self.tx_Cidade.setText(busca.cidade)
        self.tx_Estado.setText(busca.estado)

        # Limpando tabela Histórico de Compras
        for row in range(self.tb_Historico.rowCount()):
            self.tb_Historico.removeRow(row)

        # Histórico de Compras cliente
        total = '0.00'
        lista = CrudCompra()
        lista.idFornecedor = id
        lista.selectCompraFornecedor()
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
        pass

        # Frame Formulário Produtos
    def FormFornecedor(self):
        # self.DesativaBotaoProdutos()
        self.LimpaFrame(self.ct_containerFornecedor)
        super(MainFornecedor, self).setFormFornecedor(
            self.ct_containerFornecedor)
        self.fr_FormFornecedor.show()

        # Icone Botoes
        self.IconeBotaoMenu(self.bt_Salvar,
                            self.resourcepath('Images/salvar.png'))
        self.IconeBotaoMenu(self.bt_Voltar,
                            self.resourcepath('Images/cancelar.png'))
        self.IconeBotaoMenu(self.bt_BuscaCep,
                            self.resourcepath('Images/find.png'))

        # Checando se existe ID válido
        self.IdCheckFornecedor()

        # Tamanho tabela Histórico
        self.tb_Historico.setColumnWidth(0, 100)
        self.tb_Historico.setColumnWidth(1, 100)
        self.tb_Historico.setColumnWidth(2, 100)

        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.VerificaInputFornecedor)

        # Botão Voltar
        self.bt_Voltar.clicked.connect(self.janelaFornecedor)

        # Buscar Cep
        self.bt_BuscaCep.clicked.connect(self.buscarCepCliente)
        self.tx_Cep.returnPressed.connect(self.buscarCepCliente)

    # checando campo Id se é Edicao ou Novo Fornecedor
    def IdCheckFornecedor(self):
        if not self.tx_Id.text():
            busca = CrudFornecedor()
            self.tx_Id.setText(str(busca.lastIdFornecedor()))

    # Verificando Campos antes do INPUT
    def VerificaInputFornecedor(self):
        if not self.tx_NomeFantasia.text():
            self.tx_NomeFantasia.setFocus()
        elif not self.tx_Telefone.text():
            self.tx_Telefone.setFocus()
        else:
            self.CadFornecedor()

    # Cadastrando fornecedor
    def CadFornecedor(self):
        INSERI = CrudFornecedor()
        INSERI.id = self.tx_Id.text()
        INSERI.nomeFantasia = self.tx_NomeFantasia.text().upper()
        INSERI.razaoSocial = self.tx_RazaoSocial.text().upper()
        INSERI.cnpj = self.tx_cnpj.text()
        INSERI.inscEstadual = self.tx_InscEstadual.text()
        INSERI.telefone = re.sub(
            '[^[0-9]', '', self.tx_Telefone.text())
        INSERI.email = self.tx_Email.text()
        INSERI.site = self.tx_Site.text()
        INSERI.obs = self.tx_Obs.text().upper()
        INSERI.cep = re.sub(
            '[^[0-9]', '', self.tx_Cep.text())
        INSERI.endereco = self.tx_Endereco.text().upper()
        INSERI.numero = self.tx_Numero.text()
        INSERI.bairro = self.tx_Bairro.text().upper()
        INSERI.cidade = self.tx_Cidade.text().upper()
        INSERI.estado = self.tx_Estado.text()
        INSERI.inseriFornecedor()
        self.janelaFornecedor()

    # Imprimindo
    def imprimir(self):
        self.documento = QWebEngineView()

        headertable = ["Cod", "Nome Fantasia", "Telefone", "Email", "Site"]

        codcliente = []
        nomeFornecedor = []
        telefoneFornecedor = []
        siteFornecedor = []
        emailFornecedor = []

        i = 0
        for i in range(self.tb_Fornecedor.rowCount()):
            codcliente.append(self.tb_Fornecedor.cellWidget(i, 1).text())
            nomeFornecedor.append(self.tb_Fornecedor.cellWidget(i, 2).text())
            telefoneFornecedor.append(
                self.tb_Fornecedor.cellWidget(i, 3).text())
            siteFornecedor.append(self.tb_Fornecedor.cellWidget(i, 4).text())
            emailFornecedor.append(self.tb_Fornecedor.cellWidget(i, 5).text())
            i += 1

        html = self.renderTemplate(
            "report.html",
            estilo=self.resourcepath('Template/estilo.css'),
            titulo="LISTAGEM FORNECEDOR",
            headertable=headertable,
            codcliente=codcliente,
            nomeFornecedor=nomeFornecedor,
            telefoneFornecedor=telefoneFornecedor,
            siteFornecedor=siteFornecedor,
            emailFornecedor=emailFornecedor
        )

        self.documento.load(QtCore.QUrl("file:///" +
                                        self.resourcepath("report.html")))
        self.documento.loadFinished['bool'].connect(self.previaImpressao)
