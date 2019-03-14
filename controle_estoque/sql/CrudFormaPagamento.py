# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from sql.core import Conexao
from sql.Models import FormaPagamento


class CrudFormaPagamento(object):
    def __init__(self, id="", formaPagamento="", query=""):
        self.id = id
        self.formaPagamento = formaPagamento
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdFormaPagamento(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            ultimo = sessao.query(FormaPagamento.id).order_by(
                desc(FormaPagamento.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando a conexao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Cadastrando Forma Pagemento
    def inseriFormaPagamento(self):

        try:

            # Abrindo Sessao
            sessao = Session()
            # Query
            row = FormaPagamento(
                id=self.id,
                forma_pagamento=self.formaPagamento
            )

            # Add query na sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateFormaPagamento()

    # Update Forma Pagemento
    def updateFormaPagamento(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Selecionando id
            row = sessao.query(FormaPagamento).get(self.id)

            # Query
            row.forma_pagamento = self.formaPagamento

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            print('err')

    # Listando todas as categorias
    def listaFormaPagamento(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            self.query = sessao.query(FormaPagamento).order_by(
                FormaPagamento.id).all()

            # Convertendo variaveis em lista
            self.id = []
            self.formaPagamento = []

            for row in self.query:
                self.id.append(row.id)
                self.formaPagamento.append(row.forma_pagamento)

                # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
