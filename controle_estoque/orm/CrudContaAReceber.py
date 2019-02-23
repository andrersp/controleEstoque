# -*- coding: utf-8 -*-

import peewee

from Conexao import Conexao, ContaAReceber, Cliente, StatusPagamento


class CrudContaAReceber(object):

    def __init__(self, id="", idVenda="", idCliente="", descricao="",
                 obs="", categoria="", dataVencimento="", valor="",
                 formaPagamento="", dataRecebimento="", valorRecebido="",
                 statusPagamento="", query="", dataFim=""):

        self.id = id
        self.idVenda = idVenda
        self.idCliente = idCliente
        self.descricao = descricao
        self.obs = obs
        self.categoria = categoria
        self.dataVencimento = dataVencimento
        self.valor = valor
        self.formaPagamento = formaPagamento
        self.dataRecebimento = dataRecebimento
        self.valorRecebido = valorRecebido
        self.statusPagamento = statusPagamento
        self.query = query
        self.dataFim = dataFim

    # Recebendo ultimo id

    def lastIdContaAReceber(self):

        try:

            # Query

            ultimo = (ContaAReceber.select()
                      .order_by(-ContaAReceber.id).get())
            self.id = ultimo.id + 1

        except:
            self.id = 1

        return self.id

    # Cadastrando Parcelas de Venda

    def inseriParcelaVenda(self):

        try:

            # Query
            row = ContaAReceber.insert(
                id=self.id,
                id_venda=self.idVenda,
                id_cliente=self.idCliente,
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

    # Lista de  parcelas de Venda

    def listaParcelas(self):

        try:

            # Query
            self.query = (ContaAReceber.select().where(
                ContaAReceber.id_venda == self.idVenda))

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

    # Cadastrando Conta a Pagar

    def inseriContaAReceber(self):

        try:

            # Query
            row = ContaAReceber.insert(
                id=self.id,
                id_cliente=self.idCliente,
                descricao=self.descricao,
                obs=self.obs,
                categoria=self.categoria,
                data_vencimento=self.dataVencimento,
                valor=self.valor,
                forma_pagamento=self.formaPagamento
            ).on_conflict(
                update={
                    ContaAReceber.descricao: self.descricao,
                    ContaAReceber.obs: self.obs,
                    ContaAReceber.categoria: self.categoria,
                    ContaAReceber.data_vencimento: self.dataVencimento,
                    ContaAReceber.valor: self.valor,
                    ContaAReceber.forma_pagamento: self.formaPagamento
                }
            )

            # Executando a Query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Buscando conta a pagar por vencimento, Cliente e status
    def listaContaAReceber(self, busca):

        try:

            # Query
            self.query = (ContaAReceber.select(ContaAReceber,
                                               Cliente.id,
                                               Cliente.nome,
                                               StatusPagamento)
                          .join(Cliente,
                                on=(ContaAReceber.id_cliente == Cliente.id))
                          .join(StatusPagamento,
                                on=(ContaAReceber.status_pagamento == StatusPagamento.id))
                          .where(ContaAReceber.data_vencimento.between(
                              self.dataVencimento, self.dataFim),
                ContaAReceber.status_pagamento == self.statusPagamento)
            )

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
