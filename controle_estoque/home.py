# -*- coding: utf-8 -*-

from datetime import date


from PyQt5.QtCore import Qt


from Views.home import Ui_ct_Home

from Crud.CrudVenda import CrudVenda
from Crud.CrudProduto import CrudProduto
from Crud.CrudCompra import CrudCompra
from Crud.CrudContaAReceber import CrudContaAReceber
from Crud.CrudContaAPagar import CrudContaAPagar


class MainHome(Ui_ct_Home):

    def main_home(self, frame):
        super(MainHome, self).setHome(frame)
        self.HomeFrame.show()

        # Data Inicio
        self.hoje = date.today()

        # Icone botoes menu
        self.IconeHome(self.bt_addItem, self.resourcepath(
            'Images/additem.svg'))

        self.IconeHome(self.bt_addCompra, self.resourcepath(
            'Images/novaCompra.svg'))

        self.IconeHome(self.bt_addVenda, self.resourcepath(
            'Images/novaVenda.svg'))

        self.IconeHome(self.bt_addCliente,
                       self.resourcepath('Images/novoCliente.svg'))

        self.IconeHome(self.bt_areceberHoje,
                       self.resourcepath('Images/areceberhoje.svg'))

        self.IconeHome(self.bt_apagarHoje,
                       self.resourcepath('Images/apagarhoje.svg'))

        # Ocultando Campos provisoriamente
        self.lb_produtosAtivos_13.setHidden(True)
        self.label_16.setHidden(True)
        self.label_13.setHidden(True)

        # Botao Add Item
        self.bt_addItem.clicked.connect(self.additem)

        # Botao Nova Compra
        self.bt_addCompra.clicked.connect(self.novaCompra)

        # Janela pedidos a receber hoje
        self.bt_pedidosHoje.clicked.connect(self.pedidosAReceber)

        # Botao Produtos
        self.bt_produtosAtivos.clicked.connect(self.janelaProdutos)

        # Botao Novo CLiente
        self.bt_addCliente.clicked.connect(self.novoCliente)

        # Botao Nova Venda
        self.bt_addVenda.clicked.connect(self.novaVenda)

        # Lista Vendido Hoje
        self.bt_vendidoHoje.clicked.connect(self.vendidoHoje)

        # Lista Vendido Mes
        self.bt_vendidoMes.clicked.connect(self.vendidoMes)

        # Janela Clientes
        self.bt_clientesAtendidos.clicked.connect(self.janelaClientes)

        # Janela a Receber Hoje
        self.bt_areceberHoje.clicked.connect(self.aReceberHoje)

        # janela a Pagar Hoje
        self.bt_apagarHoje.clicked.connect(self.aPagarHoje)

        # Setando Mes Atual
        self.lb_mesAtual.setText("Vendido em "+self.lb_mesAtualHome())

        # Frame Estoque e pedido a receber hoje
        self.estoque()

        # Frame total Vendido
        self.valorVendidoHoje()
        self.valorvendidoMes()

        # Frame Financeiro
        self.financeiroHoje()

    """ Funcoes Frame Estoque """

    #  janela Novo Item
    def additem(self):
        self.janelaProdutos()
        self.FormProdutos()

    # Janela Nova Compra
    def novaCompra(self):
        self.janelaCompras()
        self.FormCompras()

    # Janela Pedido a receber hoje
    def pedidosAReceber(self):
        self.janelaCompras()
        self.cb_entrega.setCurrentIndex(self.cb_entrega.findData(2))

        self.dt_InicioCompra.setDate(self.hoje)
        self.dt_FimCompra.setDate(self.hoje)
        self.DataTabCompras()

    # Janela Novo Cliente

    def novoCliente(self):
        self.janelaClientes()
        self.FormClientes()

    # janela Nova Venda
    def novaVenda(self):
        self.janelaVendas()
        self.FormVendas()

    # Janela Cliente

    # Janela Lista Vendas Hoje
    def vendidoHoje(self):
        self.janelaVendas()
        self.cb_pagamento.setCurrentIndex(self.cb_pagamento.findData(1))
        self.dt_InicioVenda.setDate(self.hoje)
        self.dt_FimVenda.setDate(self.hoje)
        self.DataTabVendas()

    # Janela Lista Vendas Hoje
    def vendidoMes(self):
        self.janelaVendas()
        self.cb_pagamento.setCurrentIndex(self.cb_pagamento.findData(1))
        self.dt_InicioVenda.setDate(self.primeiroDiaMes())
        self.dt_FimVenda.setDate(self.ultimoDiaMes())
        self.DataTabVendas()

    # janela Conta a Receber Hoje
    def aReceberHoje(self):
        self.janelaFinanceiro()
        self.JanelaAReceber()
        self.dt_Inicio.setDate(self.hoje)
        self.dt_Fim.setDate(self.hoje)
        self.tabelaAReceber()

    # janela Conta a Pagar Hoje
    def aPagarHoje(self):
        self.janelaFinanceiro()
        self.JanelaAPagar()
        self.dt_Inicio.setDate(self.hoje)
        self.dt_Fim.setDate(self.hoje)
        self.tabelaAPagar()

    # Alimentando Frame Estoque
    def estoque(self):

        # Produtos estoque baixo
        busca = CrudProduto()
        self.bt_estoqueBaixo.setText(str(busca.listaEstoqueBaixo()))

        # Produtos Cadastrados
        self.bt_produtosAtivos.setText(str(busca.totalProdutoCadastrado()))

        # Pedidos a Receber
        busca = CrudCompra()

        self.bt_pedidosHoje.setText(str(busca.pedidosAReceber()))

        pass
    """ Fim frame Estoque """

    """ Frame Vendas """

    # Valor vendido hoje
    def valorVendidoHoje(self):
        busca = CrudVenda()
        busca.dataEmissao = self.hoje
        busca.dataFim = self.hoje
        busca.relatValorDia()
        self.bt_vendidoHoje.setText(str(busca.valorRecebido))
        self.bt_clientesAtendidos.setText(str(busca.idCliente))

    # Valor Vendido no mês
    def valorvendidoMes(self):
        busca = CrudVenda()
        busca.dataEmissao = self.primeiroDiaMes()
        busca.dataFim = self.ultimoDiaMes()
        busca.relatValorDia()
        self.bt_vendidoMes.setText(str(busca.valorRecebido))

        # Abrindo Jenela Venda Mes
        pass

    """ Frame Financeiro """

    def financeiroHoje(self):

        # A Receber
        busca = CrudContaAReceber()
        self.qtdeHome(self.lb_areceberHoje, busca.aReceberHoje())

        # A PAgar
        busca = CrudContaAPagar()
        self.qtdeHome(self.lb_apagarHoje, busca.aPagarHoje())

    # texto quantidade e status produtos tabela Produto
    def qtdeHome(self, campo, qtde):
        html = """<span style="font-family:'Arial'; font-size:35px;
                font-weight: bold;color:#ffff00; ">{}</span>""".format(qtde)

        campo.setText(html)
