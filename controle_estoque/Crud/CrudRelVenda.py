# -*- coding: utf-8 -*-

import peewee

from Crud.Conexao import Conexao, RelacaoVenda, Produto


class CrudRelVenda(object):
    def __init__(self, id="", idVenda="", idProduto="", produto="", qtde="",
                 valorUnitario="", valorTotal="", obs="", query=""):

        self.id = id
        self.idVenda = idVenda
        self.idProduto = idProduto
        self.produto = produto
        self.qtde = qtde
        self.valorUnitario = valorUnitario
        self.valorTotal = valorTotal
        self.obs = obs
        self.query = query

    # Cadastrando item referente a compra

    def inseriItens(self):

        try:
            # Query
            row = RelacaoVenda.insert(
                id=self.id,
                id_venda=self.idVenda,
                id_produto=self.idProduto,
                qtde=self.qtde,
                valor_unitario=self.valorUnitario,
                valor_total=self.valorTotal,
                obs=self.obs
            ).on_conflict_replace()

            # Executando a Query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Lista Itens por id de Compra

    def listaItens(self):

        try:

            # Query
            self.query = (RelacaoVenda.select(
                RelacaoVenda, Produto.id, Produto.produto)
                .join(Produto)
                .where(RelacaoVenda.id_venda == self.idVenda))

            # Convertendo variaveis em lista
            self.id = []
            self.idVenda = []
            self.idProduto = []
            self.produto = []
            self.qtde = []
            self.valorUnitario = []
            self.valorTotal = []
            self.obs = []

            # Salvando resultado da query e suas listas
            for row in self.query:
                self.id.append(row.id)
                self.idVenda.append(row.id_venda)
                self.idProduto.append(row.id_produto.id)
                self.produto.append(row.id_produto.produto)
                self.qtde.append(row.qtde)
                self.valorUnitario.append(row.valor_unitario)
                self.valorTotal.append(row.valor_total)
                self.obs.append(row.obs)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

    # Deletando item

    def delItem(self):

        try:

            # Query
            self.query = (RelacaoVenda.delete()
                          .where(RelacaoVenda.id == self.id))

            # Executando a query
            self.query.execute()

            # Fechando Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass
