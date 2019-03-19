# -*- coding: utf-8 -*-

from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from sqlalchemy import case
from sqlalchemy import func


from sql.core import Conexao
from sql.Models import ContaAPagar
from sql.Models import Fornecedor
from sql.Models import StatusPagamento
from sql.Models import CatAPagar
from sql.Models import FormaPagamento


class CrudContaAPagar(object):

    def __init__(self, id="", idCompra="", idFornecedor="", descricao="",
                 obs="", categoria="", dataVencimento="", valor="",
                 formaPagamento="", dataPagamento="", valorPago="",
                 statusPagamento="", query="", dataFim="", valorAPagar="",
                 nomeFantasia="", telefone=""):

        self.id = id
        self.idCompra = idCompra
        self.idFornecedor = idFornecedor
        self.nomeFantasia = nomeFantasia
        self.telefone = telefone
        self.descricao = descricao
        self.obs = obs
        self.categoria = categoria
        self.dataVencimento = dataVencimento
        self.valor = valor
        self.formaPagamento = formaPagamento
        self.dataPagamento = dataPagamento
        self.valorPago = valorPago
        self.statusPagamento = statusPagamento
        self.query = query
        self.dataFim = dataFim
        self.valorAPagar = valorAPagar

    # Recebendo ultimo id

    def lastIdContaAPagar(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            ultimo = (sessao.query(ContaAPagar.id).order_by(
                desc(ContaAPagar.id)).limit(1).first())
            self.id = ultimo.id + 1

            # Fechando Sessao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Cadastrando Parcelas de Compra

    def inseriParcelaCompra(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = ContaAPagar(
                id=self.id,
                id_compra=self.idCompra,
                id_fornecedor=self.idFornecedor,
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

    # Lista de  parcelas de compra
    def listaParcelas(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(ContaAPagar.__table__,
                                       StatusPagamento.status_pagamento,
                                       FormaPagamento.forma_pagamento.label('fpaga'))
                          .join(StatusPagamento)
                          .join(FormaPagamento)
                          .filter(
                ContaAPagar.id_compra == self.idCompra))
            self.query.all()

            # Convertendo variaveis em lista
            self.id = []
            self.descricao = []
            self.dataVencimento = []
            self.valor = []
            self.idFormaPagamento = []
            self.formaPagamento = []
            self.valorPago = []
            self.idStatusPagamento = []
            self.statusPagamento = []

            # Salvando resultado da query e suas listas

            for row in self.query:
                self.id.append(row.id)
                self.descricao.append(row.descricao)
                self.dataVencimento.append(row.data_vencimento)
                self.valor.append(row.valor)
                self.idFormaPagamento.append(row.forma_pagamento)
                self.formaPagamento.append(row.fpaga)
                self.valorPago.append(row.valor_pago)
                self.idStatusPagamento.append(row.pagamento)
                self.statusPagamento.append(row.status_pagamento)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Cadastrando Conta a Pagar
    def inseriContaAPagar(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = ContaAPagar(
                id=self.id,
                id_fornecedor=self.idFornecedor,
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
            self.updateContaAPagar()

    # Update Conta a Pagar
    def updateContaAPagar(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando ID
            row = sessao.query(ContaAPagar).get(self.id)

            # Novos valores
            row.id_fornecedor = self.idFornecedor
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

    # Buscando conta a pagar por vencimento, fornecedor e status
    def listaContaAPagar(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(ContaAPagar.__table__,
                                       Fornecedor.nome_fantasia,
                                       Fornecedor.telefone,
                                       StatusPagamento.status_pagamento)
                          .join(Fornecedor)
                          .join(StatusPagamento)
                          .filter(ContaAPagar.data_vencimento.between(
                              self.dataVencimento, self.dataFim),
                ContaAPagar.pagamento == self.statusPagamento)
            )
            self.query.all()

            # Convertendo variaveis em lista
            self.id = []
            self.nomeFantasia = []
            self.telefone = []
            self.descricao = []
            self.dataVencimento = []
            self.valor = []
            self.valorPago = []
            self.idStatusPagamento = []
            self.statusPagamento = []

            # salvando resultado em suas listas
            for row in self.query:

                self.id.append(row.id)
                self.nomeFantasia.append(row.nome_fantasia)
                self.telefone.append(row.telefone)
                self.descricao.append(row.descricao)
                self.dataVencimento.append(
                    date.strftime(row.data_vencimento, "%d-%m-%Y"))
                self.valor.append(row.valor)
                self.valorPago.append(row.valor_pago)
                self.idStatusPagamento.append(row.pagamento)
                self.statusPagamento.append(row.status_pagamento)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Selecionando conta a Pagar por ID
    def selectContaID(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = sessao.query(ContaAPagar).get(self.id)

            # salvando resultado em variaveis
            self.id = row.id
            self.idFornecedor = row.id_fornecedor
            self.descricao = row.descricao
            self.obs = row.obs
            self.categoria = row.categoria
            self.dataVencimento = row.data_vencimento
            self.valor = row.valor
            self.idFormaPagamento = row.forma_pagamento
            self.dataPagamento = row.data_pagamento
            self.valorPago = row.valor_pago
            self.idStatusPagamento = row.pagamento

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Pagar Conta
    def pagarConta(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # selecionando ID

            row = sessao.query(ContaAPagar).get(self.id)

            # Update Status se valor pago igual ou maior que valor parcela
            status = case([
                (ContaAPagar.valor_pago >= ContaAPagar.valor, '1')
            ], else_='2'
            )

            # Novos Valores
            row.forma_pagamento = self.formaPagamento
            row.data_pagamento = self.dataPagamento
            row.valor_pago = ContaAPagar.valor_pago + self.valorPago
            row.pagamento = status

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        pass

    """  Obtendo Movimentação financeira """

    # Total a receber referente a data selecionada
    def movDespesa(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(ContaAPagar.valor_pago), 0
            ).label('valorPago'))

                .filter(ContaAPagar.data_pagamento.between(
                    self.dataPagamento, self.dataFim))
            )
            row.all()

            # Salvando resultado
            for row in row:
                self.valorPago = row.valorPago

            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(ContaAPagar.valor), 0
            ).label('valorAPagar'))

                .filter(ContaAPagar.data_vencimento.between(
                    self.dataPagamento, self.dataFim))
            )
            row.all()

            # Salvando resultado
            for row in row:
                self.valorAPagar = row.valorAPagar

            # Fechando a Conexao
            sessao.close

        except IntegrityError as err:
            print(err)

    # detalhes entrada por categoria de receita
    def detalheDespesa(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(func.SUM(ContaAPagar.valor_pago),
                                       CatAPagar.categoria_a_pagar,
                                       FormaPagamento.forma_pagamento)
                          .join(CatAPagar)
                          .join(FormaPagamento)
                          .filter(ContaAPagar.data_pagamento
                                  .between(self.dataPagamento,
                                           self.dataFim))
                          .group_by(ContaAPagar.forma_pagamento, ContaAPagar.categoria)
                          )

            # Convertendo variaveis em lista
            self.valorPago = []
            self.categoria = []
            self.formaPagamento = []

            # Salvando resultado em suas listas
            for row in self.query:
                self.categoria.append(row.categoria_a_pagar)
                self.valorPago.append(row[0])
                self.formaPagamento.append(row.forma_pagamento)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Total a Pagar Hoje
    def aPagarHoje(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(ContaAPagar.valor), 0).label('total'))
                .filter(ContaAPagar.data_vencimento == date.today(), ContaAPagar.pagamento == 2))

            # Salvando Resultado
            for row in row:
                self.valorAPagar = row.total

        except IntegrityError as err:
            print(err)

        return self.valorAPagar
