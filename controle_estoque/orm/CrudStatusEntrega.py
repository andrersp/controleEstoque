# -*- coding: utf-8 -*-

import peewee

from Conexao import Conexao, StatusEntrega


class CrudStatusEntrega(object):
    def __init__(self, id="", statusEntrega="", query=""):
        self.id = id
        self.statusEntrega = statusEntrega
        self.query = query

        # Inserindo Dado padrão

        try:
            # Inserindo Dado caso não exista
            StatusEntrega.get_or_create(status_entrega='Concluída')
            StatusEntrega.get_or_create(status_entrega='Pendente')

        except:

            print(Conexao().erro)

    # Recebendo ultimo Id inserido

    def lastIdStatusEntrega(self):

        try:

            # Query
            ultimo = (StatusEntrega.select().order_by(
                StatusEntrega.id.desc()).get())

            self.id = ultimo.id + 1

            # Fechando a conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist:
            self.id = 1

        return self.id

    # Cadastrando categoria a receber

    def inseriStatusEntrega(self):

        try:

            # Query
            row = StatusEntrega.insert(
                id=self.id,
                status_entrega=self.statusEntrega
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Listando todas as categorias
    def listaStatusEntrega(self):

        try:

            # Query
            self.query = StatusEntrega.select()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
