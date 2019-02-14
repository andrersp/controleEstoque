#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PySide2 import QtCore
from PySide2 import QtWebKitWidgets

import os
from jinja2 import Environment, PackageLoader, FileSystemLoader


class ProgramaImpressor(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(ProgramaImpressor, self).__init__(parent)
        rotuloNome = QtWidgets.QLabel("Nome: ")
        rotuloEndereco = QtWidgets.QLabel(u"Endereço: ")
        rotuloOutros = QtWidgets.QLabel("Diversos: ")
        self.impressor = QtPrintSupport.QPrinter()
        self.txtnome = QtWidgets.QLineEdit()
        self.txtendereco = QtWidgets.QLineEdit()
        self.txtdiversos = QtWidgets.QTextEdit()
        self.btnimprimir = QtWidgets.QPushButton("&Imprimir")
        layoutHorizontal = QtWidgets.QHBoxLayout()
        layoutHorizontal2 = QtWidgets.QHBoxLayout()
        layoutHorizontal3 = QtWidgets.QHBoxLayout()
        layoutVertical = QtWidgets.QVBoxLayout()
        layoutHorizontal.addWidget(rotuloNome)
        layoutHorizontal.addWidget(self.txtnome)
        layoutHorizontal2.addWidget(rotuloEndereco)
        layoutHorizontal2.addWidget(self.txtendereco)
        layoutHorizontal3.addWidget(rotuloOutros)
        layoutHorizontal3.addWidget(self.txtdiversos)
        layoutVertical.addLayout(layoutHorizontal)
        layoutVertical.addLayout(layoutHorizontal2)
        layoutVertical.addLayout(layoutHorizontal3)
        layoutVertical.addWidget(self.btnimprimir)
        self.setLayout(layoutVertical)

        self.dialogo = QtPrintSupport.QPrintPreviewDialog()
        self.html = u""
        self.documento = QWebEngineView()
        self.dialogo.paintRequested.connect(self.documento.print_)

        self.documento.loadFinished['bool'].connect(self.previaImpressao)
        self.btnimprimir.clicked.connect(self.imprimir)

    def previaImpressao(self, arg):
        self.dialogo.exec_()

    def imprimir(self):

        self.documento.load(QtCore.QUrl(
            "file:///Files/Sistema/Novo/report.html"))

    def MakePage(self):
        document = QWebEngineView()

        paragraphs = 'Tetando essa merda'

        busca = CrudEmpresa()
        busca.idEmpresa = 1
        busca.SelectEmpresaId()
        html = self.renderTemplate(
            "report.html",
            estilo=self.resourcepath('Template/estilo.css'),
            logo=busca.logo,
            nomeFantasia=busca.NomeFantasia,
            razaoSocial=busca.RazaoSocial,
            cnpj=busca.cnpj,
            endereco=busca.endereco,
            numero=busca.numero,
            bairro=busca.bairro,
            cep=busca.cep,
            cidade=busca.cidade,
            estado=busca.estado,
            telefone=busca.telefone,

            paragraphs=paragraphs
        )

        self.documento.setHtml(html)

        # document.print_(self.PrintTab)

    def renderTemplate(self, template_file, **kwargs):
        template_loader = FileSystemLoader(
            searchpath=self.resourcepath('Template/'))
        # Jinja2 template environment
        env = Environment(loader=template_loader)
        template = env.get_template(template_file)
        busca = CrudEmpresa()
        busca.idEmpresa = 1
        busca.SelectEmpresaId()
        base = {'logo': busca.logo,
                'nomeFantasia': busca.NomeFantasia,
                'razaoSocial': busca.RazaoSocial,
                'cnpj': busca.cnpj,
                'endereco': busca.endereco,
                'numero': busca.numero,
                'bairro': busca.bairro,
                'cep': busca.cep,
                'cidade': busca.cidade,
                'estado': busca.estado,
                'telefone': busca.telefone}
        html = template.render(base, **kwargs)
        with open(self.resourcepath('report.html'), 'w') as f:
            f.write(html)

        return html

        # self.documento.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaPrincipal = ProgramaImpressor()
    JanelaPrincipal.show()
    app.exec_()
