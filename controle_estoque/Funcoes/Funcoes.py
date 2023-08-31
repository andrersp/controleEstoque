# -*- coding: utf-8 -*-
from functools import partial
import re


from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon

from brazilcep import get_address_from_cep, exceptions

class Funcao(object):

    def LimpaFrame(self, frame):
        for i in range(len(frame.children())):
            frame.children()[i].deleteLater()

    def DesativaBotao(self, frame, botao):
        for filho in frame.findChildren(QPushButton):
            filho.setEnabled(True)

        botao.setEnabled(False)

    def ativaBotoes(self, frame):
        for filho in frame.findChildren(QPushButton):
            filho.setEnabled(True)

    def IconeBotaoTopo(self, botao, imagem):

        icon = QIcon()
        icon.addPixmap(QPixmap(imagem),
                       QIcon.Normal, QIcon.Off)
        # icon.addPixmap(QPixmap((os.path.join(caminho, imagem)),
        #                              QIcon.Normal, QIcon.Off))
        botao.setIcon(icon)
        botao.setIconSize(QSize(50, 35))

    def IconeBotaoMenu(self, botao, imagem):

        icon = QIcon()
        icon.addPixmap(QPixmap(imagem),
                       QIcon.Normal, QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QSize(25, 25))

    def IconeHome(self, botao, imagem):

        icon = QIcon()
        icon.addPixmap(QPixmap(imagem),
                       QIcon.Normal, QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QSize(130, 120))

    def IconeBotaoForm(self, botao, imagem):
        icon = QIcon()
        icon.addPixmap(QPixmap(imagem),
                       QIcon.Normal, QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QSize(80, 35))

    # Mascara Telefone
    def TelefoneMask(self, telefone):
        if len(telefone) == 11:
            self.tx_Telefone.setInputMask("(00) 00000-0000")
        else:
            self.tx_Telefone.setInputMask("(00) 0000-0000")
        pass

    # Formatando numero de telefone as tabelas
    def formatoNumTelefone(self, telefone):
        if telefone:
            telefone = re.sub('[^0-9]+', '', telefone)
            if len(telefone) == 11:
                formato = re.sub('(\d{2})(\d{5})(\d{4})',
                                 r'(\1) \2-\3', telefone)

            elif len(telefone) == 10:
                formato = re.sub('(\d{2})(\d{4})(\d{4})',
                                 r'(\1) \2-\3', telefone)
            else:
                formato = ""
        else:
            formato = ""

        return formato

    # Cbox Numero Parcelas

    def cboxParcelas(self, cbox):
        cbox.clear()
        cbox.addItem("À Vista", str(1))
        for i in range(2, 13):
            cbox.addItem("{} Vezes".format(i), i)

    # buscar Cep
    def buscarCepCliente(self):
        cep = self.tx_Cep.text()

        try:
            busca = get_address_from_cep(cep)
            self.tx_Endereco.setText(busca['logradouro'])
            self.tx_Bairro.setText(busca['bairro'])
            self.tx_Cidade.setText(busca['cidade'])
            self.tx_Estado.setText(busca['uf'])
            self.tx_Numero.setFocus()
        except ConnectionError:
            self.tx_Endereco.setText('Sem conexão com serviço dos Correios')
        except exceptions.InvalidCEP as eic:
            self.tx_Endereco.setText('CEP inválido')
        except exceptions.CEPNotFound as ecnf:
            self.tx_Endereco.setText('CEP não encontrado')
        except:
            self.tx_Endereco.setText('Erro desconhecido')