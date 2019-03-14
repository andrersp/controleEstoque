# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from sql.core import Conexao
from sql.Models import MarcaProduto


class CrudMarcaProduto(object):
    def __init__(self, id="", marca_produto="", query=""):
        self.id = id
        self.marca_produto = marca_produto
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdMarcaProduto(self):
        try:

            # Abrindo a Sessao
            sessao = Session()

            # Query
            ultimo = (sessao.query(MarcaProduto).order_by(
                desc(MarcaProduto.id)).limit(1).first())

            self.id = ultimo.id + 1

            # Fechando Conexao
            sessao.close()

        except:

            self.id = 1

        return self.id

    # Cadastrando Marca produto

    def inseriMarcaProduto(self):

        try:
            # Abrindo a Sessao
            sessao = Session()

            # Query
            row = MarcaProduto(
                id=self.id,
                marca_produto=self.marca_produto
            )

            # Add Query na sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            self.updateMarcaProduto()

        pass

    # Cadastrando Marca produto

    def updateMarcaProduto(self):

        try:
            # Abrindo a Sessao
            sessao = Session()

            # Selecionando id
            row = sessao.query(MarcaProduto).get(self.id)

            # Novos valores
            row.marca_produto = self.marca_produto

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        pass

    # Listando todas as Marcas

    def listaMarcaProdutos(self):

        try:

            # Abrindo a Sessao
            sessao = Session()

            # Query
            self.query = sessao.query(MarcaProduto).all()

            # Convertendo variaveis em lista
            self.id = []
            self.marca_produto = []

            # salvando resultado em sua lista

            for row in self.query:
                self.id.append(row.id)
                self.marca_produto.append(row.marca_produto)

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        pass
