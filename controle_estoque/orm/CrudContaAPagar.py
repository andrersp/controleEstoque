# -*- coding: utf-8 -*-

import peewee

from Conexao import Conexao, ContaAPagar, Fornecedor, StatusPagamento


class CrudContaAPagar(object):

    def __init__(self, id="", idCompra="", idFornecedor="", descricao="",
                 obs="", categoria="", dataVencimento="", valor="",
                 formaPagamento="", dataPagamento="", valorPago="",
                 statusPagamento="", query="", dataFim=""):

        self.id = id
        self.idCompra = idCompra
        self.idFornecedor = idFornecedor
        self.descricao = descricao
        self.obs = obs
        self.categoria = categoria
        self.dataVencimento = dataVencimento
        self.valor = valor
        self.formaPagamento = formaPagamento
        self.dataPagamento = dataPagamento
        self.valorPago = valorPago
        self.statusPagamento = statusPagamento
        self.query = query
        self.dataFim = dataFim

    # Recebendo ultimo id

    def lastIdContaAPagar(self):

        try:

            # Query

            ultimo = (ContaAPagar.select()
                      .order_by(-ContaAPagar.id).get())
            self.id = ultimo.id + 1

        except:
            self.id = 1

        return self.id

    # Cadastrando Parcelas de Compra

    def inseriParcelaCompra(self):

        try:

            # Query
            row = ContaAPagar.insert(
                id=self.id,
                id_compra=self.idCompra,
                id_fornecedor=self.idFornecedor,
                descrica=self.descricao,
                categoria=1,
                data_vencimento=self.dataVencimento,
                valor=self.valor,
                forma_pagamento=self.formaPagamento
            )

            # Executando a Query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Lista de  parcelas de compra

    def listaParcelas(self):

        try:

            # Query
            self.query = (ContaAPagar.select().where(
                ContaAPagar.id_compra == self.idCompra))

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

    # Cadastrando Conta a Pagar

    def inseriContaAPagar(self):

        try:

            # Query
            row = ContaAPagar.insert(
                id=self.id,
                id_fornecedor=self.idFornecedor,
                descricao=self.descricao,
                obs=self.obs,
                categoria=self.categoria,
                data_vencimento=self.dataVencimento,
                valor=self.valor,
                forma_pagamento=self.formaPagamento
            ).on_conflict(
                update={
                    ContaAPagar.descricao: self.descricao,
                    ContaAPagar.obs: self.obs,
                    ContaAPagar.categoria: self.categoria,
                    ContaAPagar.data_vencimento: self.dataVencimento,
                    ContaAPagar.valor: self.valor,
                    ContaAPagar.forma_pagamento: self.formaPagamento
                }
            )

            # Executando a Query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Buscando conta a pagar por vencimento, fornecedor e status
    def listaContaAPagar(self, busca):

        try:

            # Query
            self.query = (ContaAPagar.select(ContaAPagar,
                                             Fornecedor.id,
                                             Fornecedor.nome_fantasia,
                                             StatusPagamento)
                          .join(Fornecedor,
                                on=(ContaAPagar.id_fornecedor == Fornecedor.id))
                          .join(StatusPagamento,
                                on=(ContaAPagar.status_pagamento == StatusPagamento.id))
                          .where(ContaAPagar.data_vencimento.between(
                              self.dataVencimento, self.dataFim),
                ContaAPagar.status_pagamento == self.statusPagamento)
            )

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
