# -*- coding: utf-8 -*-

import peewee


from Crud.Conexao import Conexao, MarcaProduto


class CrudMarcaProduto(object):
    def __init__(self, id="", marca_produto="", query=""):
        self.id = id
        self.marca_produto = marca_produto
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdMarcaProduto(self):
        try:

            ultimo = MarcaProduto.select().order_by(
                MarcaProduto.id.desc()).get()
            self.id = ultimo.id + 1

            # Fechando Conexao
            Conexao().dbhandler.close()

        except:

            self.id = 1

        return self.id

    # Cadastrando Marca produto

    def inseriMarcaProduto(self):

        try:
            # Query
            row = MarcaProduto.insert(
                id=self.id,
                marca_produto=self.marca_produto
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass

    # Listando todas as Marcas

    def listaMarcaProdutos(self):

        try:
            # Query
            self.query = MarcaProduto.select()

            # Fechando Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

        pass
