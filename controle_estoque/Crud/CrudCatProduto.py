# -*- coding: utf-8 -*-

import peewee


from Crud.Conexao import Conexao, CategoriaProduto


class CrudCatProduto(object):
    def __init__(self, id="", categoria_produto="", query=""):
        self.id = id
        self.categoria_produto = categoria_produto
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdCatProduto(self):

        try:

            # Query
            ultimo = CategoriaProduto.select().order_by(
                CategoriaProduto.id.desc()).get()
            self.id = ultimo.id + 1

            # Fechando Conexao
            Conexao().dbhandler.close()

        except:

            self.id = 1

        return self.id

    # Cadastrando categoria produto

    def inseriCatProduto(self):

        try:
            # Query
            row = CategoriaProduto.insert(
                id=self.id,
                categoria_produto=self.categoria_produto
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Listando todas as categorias

    def listaCatProduto(self):

        try:
            # Query
            self.query = CategoriaProduto.select()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

            pass
