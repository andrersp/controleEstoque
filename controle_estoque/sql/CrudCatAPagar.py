# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from sql.core import Conexao
from sql.Models import CatAPagar


class CrudCatAPagar(object):
    def __init__(self, id="", categoriaPagar="", query=""):
        self.id = id
        self.categoriaPagar = categoriaPagar
        self.query = query

    # Recebendo ultimo Id inserido
    def lastIdCatAPagar(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            ultimo = sessao.query(CatAPagar.id).order_by(
                desc(CatAPagar.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando a conexao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Cadastrando categoria a Pagar
    def inseriCatAPagar(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = CatAPagar(
                id=self.id,
                categoria_a_pagar=self.categoriaPagar
            )

            # Add Query na sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateCatAPagar()

    # Update categoria a Pagar
    def updateCatAPagar(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando id
            row = sessao.query(CatAPagar).get(self.id)

            # Novos Valores
            row.categoria_a_pagar = self.categoriaPagar

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Listando todas as categorias a pagar
    def listaCatAPagar(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(CatAPagar).all()

            # Convertendo variaveis em lista
            self.id = []
            self.categoriaPagar = []

            # Salvando resultado em suas lisats
            for row in self.query:
                self.id.append(row.id)
                self.categoriaPagar.append(row.categoria_a_pagar)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
