# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from sql.core import Conexao
from sql.Models import CategoriaProduto


class CrudCatProduto(object):
    def __init__(self, id="", categoria_produto="", query=""):
        self.id = id
        self.categoria_produto = categoria_produto
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdCatProduto(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            ultimo = sessao.query(CategoriaProduto).order_by(
                desc(CategoriaProduto.id)).limit(1).first()
            self.id = ultimo.id + 1

            # Fechando Conexao
            sessao.close()

        except:

            self.id = 1

        return self.id

    # Cadastrando categoria produto

    def inseriCatProduto(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            row = CategoriaProduto(
                id=self.id,
                categoria_produto=self.categoria_produto
            )

            # Salvando query na sessao
            sessao.add(row)

            # Executando query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateCatProduto()

    # Cadastrando categoria produto

    def updateCatProduto(self):

        try:
            # Abrindo a Sessao
            sessao = Session()

            # Selecionando id
            row = sessao.query(CategoriaProduto).get(self.id)

            # Novos valores
            row.categoria_produto = self.categoria_produto

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Listando todas as categorias

    def listaCatProduto(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            self.query = sessao.query(CategoriaProduto).all()

            # Convertendo variaveis em lista
            self.id = []
            self.categoria_produto = []

            # salvando resultado em sua lista

            for row in self.query:
                self.id.append(row.id)
                self.categoria_produto.append(row.categoria_produto)

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

            pass
