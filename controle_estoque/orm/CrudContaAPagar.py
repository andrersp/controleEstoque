# -*- coding: utf-8 -*-

import peewee

from orm.Conexao import Conexao
from orm.Conexao import ContaAPagar
from orm.Conexao import Fornecedor
from orm.Conexao import StatusPagamento
from orm.Conexao import CatAPagar


class CrudContaAPagar(object):

    def __init__(self, id="", idCompra="", idFornecedor="", descricao="",
                 obs="", categoria="", dataVencimento="", valor="",
                 formaPagamento="", dataPagamento="", valorPago="",
                 statusPagamento="", query="", dataFim="", valorAPagar="",
                 nomeFantasia="", telefone=""):

        self.id = id
        self.idCompra = idCompra
        self.idFornecedor = idFornecedor
        self.nomeFantasia = nomeFantasia
        self.telefone = telefone
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
        self.valorAPagar = valorAPagar

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
                descricao=self.descricao,
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

            # Convertendo variaveis em lista
            self.id = []
            self.descricao = []
            self.dataVencimento = []
            self.valor = []
            self.idFormaPagamento = []
            self.formaPagamento = []
            self.valorPago = []
            self.idStatusPagamento = []
            self.statusPagamento = []

            # Salvando resultado da query e suas listas

            for row in self.query:
                self.id.append(row.id)
                self.descricao.append(row.descricao)
                self.dataVencimento.append(row.data_vencimento)
                self.valor.append(row.valor)
                self.idFormaPagamento.append(row.forma_pagamento.id)
                self.formaPagamento.append(row.forma_pagamento.forma_pagamento)
                self.valorPago.append(row.valor_pago)
                self.idStatusPagamento.append(row.status_pagamento.id)
                self.statusPagamento.append(
                    row.status_pagamento.status_pagamento)

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
    def listaContaAPagar(self):

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

            # Convertendo variaveis em lista
            self.id = []
            self.idFornecedor = []
            self.nomeFantasia = []
            self.telefone = []
            self.descricao = []
            self.obs = []
            self.categoria = []
            self.dataVencimento = []
            self.valor = []
            self.idFormaPagamento = []
            self.formaPagamento = []
            self.dataPagamento = []
            self.valorPago = []
            self.idStatusPagamento = []
            self.statusPagamento = []

            # salvando resultado em suas listas
            for row in self.query:
                self.id.append(row.id)
                self.idFornecedor.append(row.id_fornecedor.id)
                self.nomeFantasia.append(row.id_fornecedor.nome_fantasia)
                self.telefone.append(row.id_fornecedor.telefone)
                self.descricao.append(row.descricao)
                self.dataVencimento.append(row.data_vencimento)
                self.valor.append(row.valor)
                self.idFormaPagamento.append(row.forma_pagamento.id)
                self.formaPagamento.append(row.forma_pagamento.forma_pagamento)
                self.valorPago.append(row.valor_pago)
                self.idStatusPagamento.append(row.status_pagamento.id)
                self.statusPagamento.append(
                    row.status_pagamento.status_pagamento)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

    # Selecionando conta a Pagar por ID
    def selectContaID(self):

        try:
            row = ContaAPagar.get_by_id(self.id)

            # salvando resultado em variaveis
            self.id = row.id
            self.idFornecedor = row.id_fornecedor
            self.descricao = row.descricao
            self.obs = row.obs
            self.categoria = row.categoria.id
            self.dataVencimento = row.data_vencimento
            self.valor = row.valor
            self.idFormaPagamento = row.forma_pagamento.id
            self.dataPagamento = row.data_pagamento
            self.valorPago = row.valor_pago
            self.idStatusPagamento = row.status_pagamento.id

        except peewee.DoesNotExist as err:
            print(err)

    # Pagar Conta
    def pagarConta(self):

        try:

            # Update Status se valor pago igual ou maior que valor parcela
            status = peewee.Case(None, (
                (ContaAPagar.valor_pago >= ContaAPagar.valor, '1'),
            ), '2')

            # Query
            row = (ContaAPagar.update(
                forma_pagamento=self.formaPagamento,
                data_pagamento=self.dataPagamento,
                valor_pago=ContaAPagar.valor_pago + self.valorPago,
                status_pagamento=status)
                .where(ContaAPagar.id == self.id)
            )

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass

    """  Obtendo Movimentação financeira """

    # Total a receber referente a data selecionada
    def movDespesa(self):

        try:

            # Query
            row = (ContaAPagar.select(peewee.fn.SUM(ContaAPagar.valor)
                                      .alias('valorAPagar'),
                                      peewee.fn.SUM(
                ContaAPagar.valor_pago)
                .alias('valorPago'))
                .where(ContaAPagar.data_vencimento.between(
                       self.dataVencimento, self.dataFim))
            )

            # Salvando resultado
            for lista in row:
                self.valorAPagar = lista.valorAPagar
                self.valorPago = lista.valorPago

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # detalhes entrada por categoria de receita
    def detalheDespesa(self):

        try:

            # Query
            self.query = (ContaAPagar.select(peewee.fn.SUM(ContaAPagar.valor_pago)
                                             .alias('valor'),
                                             CatAPagar.categoria_a_pagar)
                          .join(CatAPagar)
                          .where(ContaAPagar.data_pagamento
                                 .between(self.dataPagamento,
                                          self.dataFim))
                          .group_by(ContaAPagar.categoria)
                          )

            # Convertendo variaveis em lista
            self.valorPago = []
            self.categoria = []

            # Salvando resultado em suas listas
            for row in self.query:
                self.categoria.append(row.categoria.categoria_a_pagar)
                self.valorPago.append(row.valor)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)
