# -*- coding: utf-8 -*-

import peewee

from Crud.Conexao import Conexao
from Crud.Conexao import StatusPagamento


class CrudStatusPagamento(object):
    def __init__(self, id="", statusPagamento="", query=""):
        self.id = id
        self.statusPagamento = statusPagamento
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdStatusPagamento(self):

        try:

            # Query
            ultimo = (StatusPagamento.select().order_by(
                StatusPagamento.id.desc()).get())

            self.id = ultimo.id + 1

            # Fechando a conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist:
            self.id = 1

        return self.id

    # Cadastrando categoria a receber

    def inseriStatusPagamento(self):

        try:

            # Query
            row = StatusPagamento.insert(
                id=self.id,
                status_pagamento=self.statusPagamento
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Listando todas as categorias
    def listaStatusPagamento(self):

        try:

            # Query
            self.query = StatusPagamento.select()

            # Convertendo variaveis em lista

            self.id = []
            self.statusPagamento = []

            # salvando resultado em suas listas

            for row in self.query:
                self.id.append(row.id)
                self.statusPagamento.append(row.status_pagamento)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
