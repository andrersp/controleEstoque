# -*- coding: utf-8 -*-

import peewee

from orm.Conexao import Conexao
from orm.Conexao import ContaAReceber
from orm.Conexao import Cliente
from orm.Conexao import StatusPagamento
from orm.Conexao import CatAReceber


class CrudContaAReceber(object):

    def __init__(self, id="", idVenda="", idCliente="", descricao="",
                 obs="", categoria="", dataVencimento="",
                 valor="", idFormaPagamento="",  formaPagamento="",
                 dataRecebimento="", valorRecebido="", idStatusPagamento="",
                 statusPagamento="", query="", dataFim="", valorAReceber="",
                 nomeCliente="", telefoneCliente=""):

        self.id = id
        self.idVenda = idVenda
        self.idCliente = idCliente
        self.descricao = descricao
        self.obs = obs
        self.categoria = categoria
        self.dataVencimento = dataVencimento
        self.valor = valor
        self.idFormaPagamento = idFormaPagamento
        self.formaPagamento = formaPagamento
        self.dataRecebimento = dataRecebimento
        self.valorRecebido = valorRecebido
        self.idStatusPagamento = idStatusPagamento
        self.statusPagamento = statusPagamento
        self.query = query
        self.dataFim = dataFim
        self.valorAReceber = valorAReceber
        self.nomeCliente = nomeCliente
        self.telefoneCliente = telefoneCliente

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

    # Lista de  parcelas de Venda

    def listaParcelas(self):

        try:

            # Query
            self.query = (ContaAReceber.select().where(
                ContaAReceber.id_venda == self.idVenda))

            # Convertendo variaveis em lista
            self.id = []
            self.descricao = []
            self.dataVencimento = []
            self.valor = []
            self.idFormaPagamento = []
            self.formaPagamento = []
            self.valorRecebido = []
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
                self.valorRecebido.append(row.valor_recebido)
                self.idStatusPagamento.append(row.status_pagamento.id)
                self.statusPagamento.append(
                    row.status_pagamento.status_pagamento)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

    # Cadastrando Conta a Receber

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
    def listaContaAReceber(self):

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

            # Convertendo variaveis em lista
            self.id = []
            self.idCliente = []
            self.nomeCliente = []
            self.telefoneCliente = []
            self.descricao = []
            self.obs = []
            self.categoria = []
            self.dataVencimento = []
            self.valor = []
            self.idFormaPagamento = []
            self.formaPagamento = []
            self.dataRecebimento = []
            self.valorRecebido = []
            self.idStatusPagamento = []
            self.statusPagamento = []

            # salvando resultado em suas listas
            for row in self.query:
                self.id.append(row.id)
                self.idCliente.append(row.id_cliente.id)
                self.nomeCliente.append(row.id_cliente.nome)
                self.telefoneCliente.append(row.id_cliente.celular)
                self.descricao.append(row.descricao)
                self.dataVencimento.append(row.data_vencimento)
                self.valor.append(row.valor)
                self.idFormaPagamento.append(row.forma_pagamento.id)
                self.formaPagamento.append(row.forma_pagamento.forma_pagamento)
                self.valorRecebido.append(row.valor_recebido)
                self.idStatusPagamento.append(row.status_pagamento.id)
                self.statusPagamento.append(
                    row.status_pagamento.status_pagamento)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

        pass

    # Selecionando conta a receber por ID
    def selectContaID(self):

        try:
            row = ContaAReceber.get_by_id(self.id)

            # salvando resultado em variaveis
            self.id = row.id
            self.idCliente = row.id_cliente
            self.descricao = row.descricao
            self.obs = row.obs
            self.categoria = row.categoria.id
            self.dataVencimento = row.data_vencimento
            self.valor = row.valor
            self.idFormaPagamento = row.forma_pagamento.id
            self.dataRecebimento = row.data_recebimento
            self.valorRecebido = row.valor_recebido
            self.idStatusPagamento = row.status_pagamento.id

        except peewee.DoesNotExist as err:
            print(err)

    # Receber Conta
    def receberConta(self):

        try:

            # Update Status se valor recebido igual ou maior que valor parcela
            status = peewee.Case(None, (
                (ContaAReceber.valor_recebido >= ContaAReceber.valor, '1'),
            ), '2')

            # Query
            row = (ContaAReceber.update(
                forma_pagamento=self.formaPagamento,
                data_recebimento=self.dataRecebimento,
                valor_recebido=ContaAReceber.valor_recebido + self.valorRecebido,
                status_pagamento=status)
                .where(ContaAReceber.id == self.id)
            )

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    """  Obtendo Movimentação financeira """

    # Total a receber referente a data selecionada
    def movEntrada(self):

        try:

            # Query
            row = (ContaAReceber.select(peewee.fn.SUM(ContaAReceber.valor)
                                        .alias('valorAReceber'),
                                        peewee.fn.SUM(
                                            ContaAReceber.valor_recebido)
                                        .alias('valorRecebido'))
                   .where(ContaAReceber.data_vencimento.between(
                       self.dataVencimento, self.dataFim))
                   )

            # Salvando resultado
            for lista in row:
                self.valorAReceber = lista.valorAReceber
                self.valorRecebido = lista.valorRecebido

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass

    # detalhes entrada por categoria de receita
    def detalheEntrada(self):

        try:

            # Query
            self.query = (ContaAReceber.select(peewee.fn.SUM(ContaAReceber.valor_recebido)
                                               .alias('valor'),
                                               CatAReceber.categoria_a_receber)
                          .join(CatAReceber)
                          .where(ContaAReceber.data_recebimento
                                 .between(self.dataRecebimento,
                                          self.dataFim))
                          .group_by(ContaAReceber.categoria)
                          )

            # Convertendo variaveis em lista
            self.valorRecebido = []
            self.categoria = []

            # Salvando resultado em suas listas
            for row in self.query:
                self.categoria.append(row.categoria.categoria_a_receber)
                self.valorRecebido.append(row.valor)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass


Inseri = CrudContaAReceber()
# Inseri.id = 7
# Inseri.formaPagamento = 1
Inseri.dataRecebimento = '2019-02-27'
Inseri.dataFim = '2019-03-31'
Inseri.detalheEntrada()
