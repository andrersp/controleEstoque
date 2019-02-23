# -*- coding: utf-8 -*-

import peewee

from Conexao import Conexao, CatAReceber


class CrudCatAReceber(object):
    def __init__(self, id="", categoriaReceber="", query=""):
        self.id = id
        self.categoriaReceber = categoriaReceber
        self.query = query

        # Inserindo Dado padrão

        try:

            # Inserindo Dado caso não exista
            CatAReceber.get_or_create(categoria_a_receber='Venda')

        except:

            print(Conexao().erro)

    # Recebendo ultimo Id inserido

    def lastIdCatAReceber(self):

        try:

            # Query
            ultimo = (CatAReceber.select().order_by(
                CatAReceber.id.desc()).get())

            self.id = ultimo.id + 1

            # Fechando a conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist:
            self.id = 1

        return self.id

    # Cadastrando categoria a receber

    def inseriCatAReceber(self):

        try:

            # Query
            row = CatAReceber.insert(
                id=self.id,
                categoria_a_receber=self.categoriaReceber
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Listando todas as categorias
    def listaCatAReceber(self):

        try:

            # Query
            self.query = CatAReceber.select()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
