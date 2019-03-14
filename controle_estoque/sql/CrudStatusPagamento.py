# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from sql.core import Conexao
from sql.Models import StatusPagamento


class CrudStatusPagamento(object):
    def __init__(self, id="", statusPagamento="", query=""):
        self.id = id
        self.statusPagamento = statusPagamento
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdStatusPagamento(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            ultimo = sessao.query(StatusPagamento.id).order_by(
                desc(StatusPagamento.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando a conexao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Cadastrando Status Pagamento
    def inseriStatusPagamento(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = StatusPagamento(
                id=self.id,
                status_pagamento=self.statusPagamento
            )

            # Add Query na sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateStatusPagamento()

    # Update Status Pagamento
    def updateStatusPagamento(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando
            row = sessao.query(StatusPagamento).get(self.id)

            # Query

            row.status_pagamento = self.statusPagamento

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Listando todas as categorias
    def listaStatusPagamento(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(StatusPagamento).all()

            # Convertendo variaveis em lista

            self.id = []
            self.statusPagamento = []

            # salvando resultado em suas listas

            for row in self.query:
                self.id.append(row.id)
                self.statusPagamento.append(row.status_pagamento)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
