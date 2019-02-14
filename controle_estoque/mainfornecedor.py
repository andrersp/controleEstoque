# -*- coding: utf-8 -*-
from PySide2 import QtCore
from PySide2.QtWebEngineWidgets import QWebEngineView
from functools import partial
from Views.mainFornecedor import Ui_ct_MainFornecedor
from Views.formFornecedor import Ui_ct_FormFornecedor
from Crud.CrudFornecedor import CrudFornecedor
from Crud.CrudEmpresa import CrudEmpresa
import re
from jinja2 import Environment, PackageLoader, FileSystemLoader


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
        busca = self.tx_BuscaFornecedor.text()
        lista.ListaFornecedorTabela(busca)

        # Limpando Tabela
        while self.tb_Fornecedor.rowCount() > 0:
            self.tb_Fornecedor.removeRow(0)

        i = 0
        if len(lista.NomeFantasia) >= 1:
            while i < len(lista.NomeFantasia):
                self.tb_Fornecedor.insertRow(i)
                self.TabelaStatus(self.tb_Fornecedor, i,
                                  0, self.StatusEntrega(1))
                self.TabelaID(self.tb_Fornecedor, i, 1, lista.idFornecedor[i])
                self.TabelaNomeTelefone(self.tb_Fornecedor, i, 2,
                                        lista.NomeFantasia[i],
                                        lista.RazaoSocial[i])
                self.TabelaNomeTelefone(self.tb_Fornecedor, i, 3,
                                        lista.telefone[i], "")
                self.TabelaNomeTelefone(self.tb_Fornecedor, i, 4,
                                        lista.email[i], "")
                self.TabelaNomeTelefone(self.tb_Fornecedor, i, 5,
                                        lista.site[i], "")
                # Sinal click tabela
                self.botaoTabela(self.tb_Fornecedor, i, 6,
                                 partial(self.SelectFornecedor,
                                         lista.idFornecedor[i]), "#005099")
                i += 1

    def SelectFornecedor(self, id):
        busca = CrudFornecedor()
        self.FormFornecedor()
        busca.SelectFornecedorId(id)
        self.tx_Id.setText(str(busca.idFornecedor))
        self.tx_NomeFantasia.setText(busca.NomeFantasia)
        self.tx_RazaoSocial.setText(busca.RazaoSocial)
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

        # Botao Salvar
        self.bt_Salvar.clicked.connect(self.VerificaInputFornecedor)

        # Botão Voltar
        self.bt_Voltar.clicked.connect(self.janelaFornecedor)

    # checando campo Id se é Edicao ou Novo Fornecedor
    def IdCheckFornecedor(self):
        if not self.tx_Id.text():
            busca = CrudFornecedor()
            self.tx_Id.setText(str(busca.LasIdFornecedor()))

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
        INSERI.idFornecedor = self.tx_Id.text()
        INSERI.NomeFantasia = self.tx_NomeFantasia.text().upper()
        INSERI.RazaoSocial = self.tx_RazaoSocial.text().upper()
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
        INSERI.CadFornecedor()
        self.janelaFornecedor()

    # Imprimindo
    def imprimir(self):
        self.documento = QWebEngineView()

        headertable = ["Cod", "Nome Fantasia", "Telefone", "Email", "Site"]
        buscaFornecedor = CrudFornecedor()
        buscaFornecedor.ListaFornecedorTabela(self.tx_BuscaFornecedor.text())
        html = self.renderTemplate(
            "report.html",
            estilo=self.resourcepath('Template/estilo.css'),
            titulo="LISTAGEM FORNECEDOR",
            headertable=headertable,
            codcliente=buscaFornecedor.idFornecedor,
            nomeFornecedor=buscaFornecedor.NomeFantasia,
            telefoneFornecedor=buscaFornecedor.telefone,
            siteFornecedor=buscaFornecedor.site,
            emailFornecedor=buscaFornecedor.email

        )

        self.documento.load(QtCore.QUrl("file:///" +
                                        self.resourcepath("report.html")))
        self.documento.loadFinished['bool'].connect(self.previaImpressao)
