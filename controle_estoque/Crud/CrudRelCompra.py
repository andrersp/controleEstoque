# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError


from Crud.core import Conexao
from Crud.Models import RelacaoCompra, Produto


class CrudRelCompra(object):
    def __init__(self, id="", idCompra="", idProduto="", produto="",
                 qtde="",
                 valorUnitario="", valorTotal="", obs="", query=""):

        self.id = id
        self.idCompra = idCompra
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

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = RelacaoCompra(
                id=self.id,
                id_compra=self.idCompra,
                id_produto=self.idProduto,
                qtde=self.qtde,
                valor_unitario=self.valorUnitario,
                valor_total=self.valorTotal,
                obs=self.obs
            )

            # Add Query Sessa
            sessao.add(row)

            # Executando a Query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateItens()

    # update item referente a compra
    def updateItens(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando ID

            row = sessao.query(RelacaoCompra).get(self.id)

            # Novos Valores

            row.id_compra = self.idCompra
            row.id_produto = self.idProduto
            row.qtde = self.qtde
            row.valor_unitario = self.valorUnitario
            row.valor_total = self.valorTotal
            row.obs = self.obs

            # Executando a Query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Lista Itens por id de Compra
    def listaItens(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(
                RelacaoCompra.id, RelacaoCompra.id_compra,
                RelacaoCompra.id_produto, RelacaoCompra.qtde,
                RelacaoCompra.valor_unitario, RelacaoCompra.valor_total,
                RelacaoCompra.obs,
                Produto.produto)
                .join(Produto)
                .filter(RelacaoCompra.id_compra == self.idCompra))
            self.query.all()

            # Convertendo variaveis em lista
            self.id = []
            self.idCompra = []
            self.idProduto = []
            self.produto = []
            self.qtde = []
            self.valorUnitario = []
            self.valorTotal = []
            self.obs = []

            # Salvando resultado da query e suas listas
            for row in self.query:
                self.id.append(row.id)
                self.idCompra.append(row.id_compra)
                self.idProduto.append(row.id_produto)
                self.produto.append(row.produto)
                self.qtde.append(row.qtde)
                self.valorUnitario.append(row.valor_unitario)
                self.valorTotal.append(row.valor_total)
                self.obs.append(row.obs)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Deletando item

    def delItem(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # selecionando ID
            self.query = sessao.query(RelacaoCompra).get(self.id)

            if self.query:
                # Add query na Sessao
                sessao.delete(self.query)

                # Executando a query
                sessao.commit()

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        pass
