# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from sql.core import Conexao
from sql.Models import StatusEntrega


class CrudStatusEntrega(object):
    def __init__(self, id="", statusEntrega="", query=""):
        self.id = id
        self.statusEntrega = statusEntrega
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdStatusEntrega(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            ultimo = sessao.query(StatusEntrega.id).order_by(
                desc(StatusEntrega.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando a conexao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Cadastrando categoria a receber
    def inseriStatusEntrega(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            row = StatusEntrega(
                id=self.id,
                status_entrega=self.statusEntrega
            )

            # Add query na Sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            self.updateStatusEntrega()

    # Update categoria a receber
    def updateStatusEntrega(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Selecionando id

            row = sessao.query(StatusEntrega).get(self.id)

            # Novos Dados
            row.status_entrega = self.statusEntrega

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Listando todas as categorias
    def listaStatusEntrega(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            self.query = sessao.query(StatusEntrega).all()

            # Convertendo Variaveis em lista
            self.id = []
            self.statusEntrega = []

            # Salvando dados em suas variaveis

            for row in self.query:
                self.id.append(row.id)
                self.statusEntrega.append(row.status_entrega)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
