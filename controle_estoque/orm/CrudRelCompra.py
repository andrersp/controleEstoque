# -*- coding: utf-8 -*-

import peewee

from orm.Conexao import Conexao, RelacaoCompra, Produto


class CrudRelCompra(object):
    def __init__(self, id="", idCompra="", idProduto="", qtde="",
                 valorUnitario="", valorTotal="", obs="", query=""):

        self.id = id
        self.idCompra = idCompra
        self.idProduto = idProduto
        self.qtde = qtde
        self.valorUnitario = valorUnitario
        self.valorTotal = valorTotal
        self.obs = obs
        self.query = query

    # Cadastrando item referente a compra

    def inseriItens(self):

        try:
            # Query
            row = RelacaoCompra.insert(
                id=self.id,
                id_compra=self.idCompra,
                id_produto=self.idProduto,
                qtde=self.qtde,
                valor_unitario=self.valorUnitario,
                valor_total=self.valorTotal,
                obs=self.obs
            )

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
            self.query = (RelacaoCompra.select(
                RelacaoCompra, Produto.id, Produto.produto)
                .join(Produto)
                .where(RelacaoCompra.id_compra == self.idCompra))

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

    # Deletando item

    def delItem(self):

        try:

            # Query
            self.query = (RelacaoCompra.delete()
                          .where(RelacaoCompra.id == self.id))

            # Executando a query
            self.query.execute()

            # Fechando Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass
