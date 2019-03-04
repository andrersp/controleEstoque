# -*- coding: utf-8 -*-

import peewee

from Crud.Conexao import Conexao
from Crud.Conexao import CatAPagar


class CrudCatAPagar(object):
    def __init__(self, id="", categoriaPagar="", query=""):
        self.id = id
        self.categoriaPagar = categoriaPagar
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdCatAPagar(self):

        try:

            # Query
            ultimo = (CatAPagar.select().order_by(
                CatAPagar.id.desc()).get())

            self.id = ultimo.id + 1

            # Fechando a conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist:
            self.id = 1

        return self.id

    # Cadastrando categoria a receber

    def inseriCatAPagar(self):

        try:

            # Query
            row = CatAPagar.insert(
                id=self.id,
                categoria_a_pagar=self.categoriaPagar
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Listando todas as categorias a pagar
    def listaCatAPagar(self):

        try:

            # Query
            self.query = CatAPagar.select()

            # Convertendo variaveis em lista
            self.id = []
            self.categoriaPagar = []

            # Salvando resultado em suas lisats
            for row in self.query:
                self.id.append(row.id)
                self.categoriaPagar.append(row.categoria_a_pagar)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
