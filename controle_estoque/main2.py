# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PySide2.QtWebEngineWidgets import QWebEngineView

from Crud.CrudFornecedor import CrudFornecedor
from Crud.CrudEmpresa import CrudEmpresa
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

        self.btnimprimir.clicked.connect(self.imprimir)

    def previaImpressao(self):
        self.printer = QtPrintSupport.QPrinter()
        self.printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        self.printer.setOutputFileName('/home/andre/print.pdf')
        painter = QtGui.QPainter()
        painter.begin(self.printer)
        self.documento.drawContents(painter, QtCore.QRectF(1,1,0,10))
        painter.end()
        
        
    def handerpaint(self, print):
        self.documento.render(QtGui.QPainter(print))


    def resourcepath(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(
            os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def imprimir(self):
        self.documento = QtGui.QTextDocument()

        headertable = ["Cod", "Nome Fantasia", "Telefone", "Email", "Site"]
        buscaFornecedor = CrudFornecedor()
        buscaFornecedor.ListaFornecedorTabela('')
        html = self.renderTemplate(
            "report.html",
            estilo=self.resourcepath('Template/estilo.css'),
            titulo="pedidos",
            headertable=headertable,
            codcliente=buscaFornecedor.idFornecedor,
            nomeFornecedor=buscaFornecedor.RazaoSocial,
            telefoneFornecedor=buscaFornecedor.telefone,
            siteFornecedor=buscaFornecedor.site,
            emailFornecedor=buscaFornecedor.email

        )
        self.documento.setHtml(html)
        self.previaImpressao()
        # self.documento.load(QtCore.QUrl("file:///" +
        #                                 self.resourcepath("report.html")))
        # self.documento.loadFinished['bool'].connect(self.previaImpressao)

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

    #     # self.documento.show()
    # def handle_paint_request(self, printer):
    #     painter = QtGui.QPainter(printer)
    #     painter.setViewport(self.documento.rect())
    #     painter.setWindow(self.documento.rect())
    #     self.documento.render(painter)
    #     painter.end()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaPrincipal = ProgramaImpressor()
    JanelaPrincipal.show()
    app.exec_()
