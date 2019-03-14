# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from sqlalchemy import case
from sqlalchemy import func


from sql.core import Conexao
from sql.Models import ContaAReceber
from sql.Models import Cliente
from sql.Models import StatusPagamento
from sql.Models import CatAReceber


class CrudContaAReceber(object):

    def __init__(self, id="", idVenda="", idCliente="", descricao="",
                 obs="", categoria="", dataVencimento="",
                 valor="", idFormaPagamento="",  formaPagamento="",
                 dataRecebimento="", valorRecebido="", idStatusPagamento="",
                 statusPagamento="", query="", dataFim="", valorAReceber="",
                 nomeCliente="", telefoneCliente=""):

        self.id = id
        self.idVenda = idVenda
        self.idCliente = idCliente
        self.descricao = descricao
        self.obs = obs
        self.categoria = categoria
        self.dataVencimento = dataVencimento
        self.valor = valor
        self.idFormaPagamento = idFormaPagamento
        self.formaPagamento = formaPagamento
        self.dataRecebimento = dataRecebimento
        self.valorRecebido = valorRecebido
        self.idStatusPagamento = idStatusPagamento
        self.statusPagamento = statusPagamento
        self.query = query
        self.dataFim = dataFim
        self.valorAReceber = valorAReceber
        self.nomeCliente = nomeCliente
        self.telefoneCliente = telefoneCliente

    # Recebendo ultimo id

    def lastIdContaAReceber(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            ultimo = (sessao.query(ContaAReceber)
                      .order_by(desc(ContaAReceber.id)).limit(1).first())
            self.id = ultimo.id + 1

        except:

            self.id = 1

        return self.id

    # Cadastrando Parcelas de Venda

    def inseriParcelaVenda(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            row = ContaAReceber(
                id=self.id,
                id_venda=self.idVenda,
                id_cliente=self.idCliente,
                descricao=self.descricao,
                categoria=1,
                data_vencimento=self.dataVencimento,
                valor=self.valor,
                forma_pagamento=self.formaPagamento
            )

            # Add Query Sessao
            sessao.add(row)

            # Executando a Query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Lista de  parcelas de Venda
    def listaParcelas(self):

        try:

            # Abrindo sessao
            sessao = Session()

            # Query
            self.query = (sessao.query(ContaAReceber).filter(
                ContaAReceber.id_venda == self.idVenda))
            self.query.all()

            # Convertendo variaveis em lista
            self.id = []
            self.descricao = []
            self.dataVencimento = []
            self.valor = []
            self.idFormaPagamento = []
            self.valorRecebido = []
            self.idStatusPagamento = []

            # Salvando resultado da query e suas listas

            for row in self.query:
                self.id.append(row.id)
                self.descricao.append(row.descricao)
                self.dataVencimento.append(row.data_vencimento)
                self.valor.append(row.valor)
                self.idFormaPagamento.append(row.forma_pagamento)
                self.valorRecebido.append(row.valor_recebido)
                self.idStatusPagamento.append(row.pagamento)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Cadastrando Conta a Receber
    def inseriContaAReceber(self):

        try:

            # Abrindo sessao
            sessao = Session()

            # Query
            row = ContaAReceber(
                id=self.id,
                id_cliente=self.idCliente,
                descricao=self.descricao,
                obs=self.obs,
                categoria=self.categoria,
                data_vencimento=self.dataVencimento,
                valor=self.valor,
                forma_pagamento=self.formaPagamento
            )

            # Add query a sessao
            sessao.add(row)

            # Executando a Query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateContaAReceber()

    # Update Conta a Receber
    def updateContaAReceber(self):

        try:

            # Abrindo sessao
            sessao = Session()

            # Selecionando id
            row = sessao.query(ContaAReceber).get(self.id)

            # Novos Valores
            row.id_cliente = self.idCliente
            row.descricao = self.descricao
            row.obs = self.obs
            row.categoria = self.categoria
            row.data_vencimento = self.dataVencimento
            row.valor = self.valor
            row.forma_pagamento = self.formaPagamento

            # Executando a Query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Buscando conta a pagar por vencimento, Cliente e status
    def listaContaAReceber(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            self.query = (sessao.query(ContaAReceber.__table__,
                                       Cliente.id,
                                       Cliente.nome,
                                       Cliente.celular,
                                       StatusPagamento.status_pagamento)
                          .join(Cliente)
                          .join(StatusPagamento)
                          .filter(ContaAReceber.data_vencimento.between(
                              self.dataVencimento, self.dataFim),
                ContaAReceber.pagamento == self.statusPagamento)
            )

            # Convertendo variaveis em lista
            self.id = []
            self.nomeCliente = []
            self.telefoneCliente = []
            self.descricao = []
            self.dataVencimento = []
            self.valor = []
            self.valorRecebido = []
            self.idStatusPagamento = []
            self.statusPagamento = []

            # salvando resultado em suas listas
            for row in self.query:

                self.id.append(row.id)
                self.nomeCliente.append(row.nome)
                self.telefoneCliente.append(row.celular)
                self.descricao.append(row.descricao)
                self.dataVencimento.append(row.data_vencimento)
                self.valor.append(row.valor)
                self.valorRecebido.append(row.valor_recebido)
                self.idStatusPagamento.append(row.pagamento)
                self.statusPagamento.append(row.status_pagamento)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        pass

    # Selecionando conta a receber por ID
    def selectContaID(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            row = sessao.query(ContaAReceber).get(self.id)

            # salvando resultado em variaveis
            self.id = row.id
            self.idCliente = row.id_cliente
            self.descricao = row.descricao
            self.obs = row.obs
            self.categoria = row.categoria
            self.dataVencimento = row.data_vencimento
            self.valor = row.valor
            self.idFormaPagamento = row.forma_pagamento
            self.dataRecebimento = row.data_recebimento
            self.valorRecebido = row.valor_recebido
            self.idStatusPagamento = row.pagamento

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Receber Conta
    def receberConta(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Selecionando ID
            row = sessao.query(ContaAReceber).get(self.id)

            # Update Status se valor recebido igual ou maior que valor parcela
            status = case([
                (ContaAReceber.valor_recebido >= row.valor, '1')
            ], else_='2'
            )

            # Query
            row.forma_pagamento = self.formaPagamento
            row.data_recebimento = self.dataRecebimento
            row.valor_recebido = ContaAReceber.valor_recebido + self.valorRecebido
            row.pagamento = status

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    """  Obtendo Movimentação financeira """

    # Total a receber referente a data selecionada
    def movEntrada(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(ContaAReceber.valor), 0
            ),
                func.COALESCE(
                func.SUM(ContaAReceber.valor_recebido), 0
            ))

                .filter(ContaAReceber.data_vencimento.between(
                    self.dataVencimento, self.dataFim))
            )
            row.all()

            # Salvando resultado
            for lista in row:
                self.valorAReceber = lista[0]
                self.valorRecebido = lista[1]

            # Fechando a Conexao
            sessao.close

        except IntegrityError as err:
            print(err)

        pass

    # detalhes entrada por categoria de receita
    def detalheEntrada(self):

        try:

            # Abrindo Sessao
            sessao = Session()

            # Query
            self.query = (sessao.query(func.SUM(ContaAReceber.valor_recebido),
                                       CatAReceber.categoria_a_receber)
                          .join(CatAReceber)
                          .filter(ContaAReceber.data_recebimento
                                  .between(self.dataRecebimento,
                                           self.dataFim))
                          .group_by(ContaAReceber.categoria)
                          )

            # Convertendo variaveis em lista
            self.valorRecebido = []
            self.categoria = []

            # Salvando resultado em suas listas
            for row in self.query:
                self.categoria.append(row.categoria_a_receber)
                self.valorRecebido.append(row[0])

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
