# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from sql.core import Conexao
from sql.Models import CatAReceber


class CrudCatAReceber(object):
    def __init__(self, id="", categoriaReceber="", query=""):
        self.id = id
        self.categoriaReceber = categoriaReceber
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdCatAReceber(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            ultimo = sessao.query(CatAReceber.id).order_by(
                desc(CatAReceber.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando a conexao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Cadastrando categoria a receber

    def inseriCatAReceber(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = CatAReceber(
                id=self.id,
                categoria_a_receber=self.categoriaReceber
            )

            # Add Query na sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateCatAReceber()

    # Update categoria a Pagar
    def updateCatAReceber(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando id
            row = sessao.query(CatAReceber).get(self.id)

            # Novos Valores
            row.categoria_a_receber = self.categoriaReceber

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Listando todas as categorias
    def listaCatAReceber(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(CatAReceber).all()

            # Convertendo variaveis em lista
            self.id = []
            self.categoriaReceber = []

            # Salvando resultado em suas lisats
            for row in self.query:
                self.id.append(row.id)
                self.categoriaReceber.append(row.categoria_a_receber)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
