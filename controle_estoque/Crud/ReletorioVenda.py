# -*- coding: utf-8 -*-


from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

from core import Conexao
from Models import Venda
from Models import Produto
from Models import RelacaoVenda
from Models import Usuarios


class RelatorioVenda(object):
    def __init__(self, idVenda="", dataVenda="", totalVenda="", numItens="",
                 idProduto="", produto="", qtde="",
                 idVendedor="", vendedor="", dataInicio="", dataFim=""):
        self.idVenda = idVenda
        self.dataVenda = dataVenda
        self.totalVenda = totalVenda
        self.numItens = numItens
        self.idProduto = idProduto
        self.produto = produto
        self.qtde = qtde
        self.idVendedor = idVendedor
        self.vendedor = vendedor
        self.dataInicio = dataInicio
        self.dataFim = dataFim

    # Agrupar por vendedor

    def RelatorioVendedor(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query

            query = (sessao.query(Venda.vendedor)
                     .filter(Venda.data_emissao.between(
                         self.dataInicio, self.dataFim))
                     .group_by(Venda.vendedor).subquery()
                     )

            query2 = (sessao.query(Venda.__table__,
                                   query.c.vendedor, Usuarios.nome)
                      .join(Usuarios, Venda.vendedor == Usuarios.id)
                      .group_by(Venda.id)
                      )

            self.idVenda = []
            self.dataVenda = []
            self.totalVenda = []
            self.numItens = []
            self.idProduto = []
            self.produto = []
            self.qtde = []
            self.idVendedor = []
            self.vendedor = []
            self.dataInicio = []
            self.dataFim = []

            for row in query2:
                # self.idVenda.append(row.id)
                # self.dataVenda.append(row.data_emissao)
                # self.totalVenda.append(row.valor_total)
                # self.numItens.append(row.quant)
                # self.vendedor.append(row.nome)

                print(row.nome, row.valor_total)

            # Fechando Sessao
            sessao.close()

        except IntegrityError as err:
            print(err)


busca = RelatorioVenda()
busca.dataInicio = '2019-01-01'
busca.dataFim = '2019-03-30'
busca.RelatorioVendedor()

# i = 0
# for row in busca.vendedor:
#     print(row)
#     for detalhe in row:
#         print(busca.totalVenda[i])

#     i += 1
