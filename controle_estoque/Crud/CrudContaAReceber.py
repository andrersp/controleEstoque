# -*- coding: utf-8 -*-

from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from sqlalchemy import case
from sqlalchemy import func


from Crud.core import Conexao
from Crud.Models import ContaAReceber
from Crud.Models import Cliente
from Crud.Models import StatusPagamento
from Crud.Models import CatAReceber
from Crud.Models import FormaPagamento


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
            conecta = Conexao()
            sessao = conecta.Session()

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
            conecta = Conexao()
            sessao = conecta.Session()

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
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(ContaAReceber.__table__,
                                       StatusPagamento.status_pagamento,
                                       FormaPagamento.forma_pagamento.label('fpaga'))
                          .join(StatusPagamento)
                          .join(FormaPagamento)
                          .filter(
                ContaAReceber.id_venda == self.idVenda))
            self.query.all()

            # Convertendo variaveis em lista
            self.id = []
            self.descricao = []
            self.dataVencimento = []
            self.valor = []
            self.formaPagamento = []
            self.idFormaPagamento = []
            self.valorRecebido = []
            self.statusPagamento = []
            self.idStatusPagamento = []

            # Salvando resultado da query e suas listas

            for row in self.query:
                self.id.append(row.id)
                self.descricao.append(row.descricao)
                self.dataVencimento.append(row.data_vencimento)
                self.valor.append(row.valor)
                self.formaPagamento.append(row.fpaga)
                self.idFormaPagamento.append(row.forma_pagamento)
                self.valorRecebido.append(row.valor_recebido)
                self.idStatusPagamento.append(row.pagamento)
                self.statusPagamento.append(row.status_pagamento)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Cadastrando Conta a Receber
    def inseriContaAReceber(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

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
            conecta = Conexao()
            sessao = conecta.Session()

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
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(ContaAReceber.__table__,
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
                self.dataVencimento.append(
                    date.strftime(row.data_vencimento, "%d-%m-%Y"))
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
            conecta = Conexao()
            sessao = conecta.Session()

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
            conecta = Conexao()
            sessao = conecta.Session()

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
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(ContaAReceber.valor_recebido), 0
            ).label('valorRecebido'))

                .filter(ContaAReceber.data_recebimento.between(
                    self.dataRecebimento, self.dataFim))
            )
            row.all()

            # Salvando resultado
            for row in row:
                self.valorRecebido = row.valorRecebido

            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(ContaAReceber.valor), 0
            ).label('valorAReceber'))

                .filter(ContaAReceber.data_vencimento.between(
                    self.dataRecebimento, self.dataFim))
            )
            row.all()

            # Salvando resultado
            for row in row:
                self.valorAReceber = row.valorAReceber

            # Fechando a Conexao
            sessao.close

        except IntegrityError as err:
            print(err)

        pass

    # detalhes entrada por categoria de receita
    def detalheEntrada(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(func.SUM(ContaAReceber.valor_recebido).label('entrada'),
                                       CatAReceber.categoria_a_receber,
                                       FormaPagamento.forma_pagamento)
                          .join(CatAReceber)
                          .join(FormaPagamento)
                          .filter(ContaAReceber.data_recebimento
                                  .between(self.dataRecebimento,
                                           self.dataFim))
                          .group_by(ContaAReceber.forma_pagamento, ContaAReceber.categoria)
                          )

            # Convertendo variaveis em lista
            self.valorRecebido = []
            self.categoria = []
            self.formaPagamento = []

            # Salvando resultado em suas listas
            for row in self.query:
                self.categoria.append(row.categoria_a_receber)
                self.valorRecebido.append(row.entrada)
                self.formaPagamento.append(row.forma_pagamento)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Total a Receber Hoje
    def aReceberHoje(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(ContaAReceber.valor), 0).label('total'))
                .filter(ContaAReceber.data_vencimento == date.today(), ContaAReceber.pagamento == 2))

            # Salvando Resultado
            for row in row:
                self.valorAReceber = row.total

        except IntegrityError as err:
            print(err)

        return self.valorAReceber
