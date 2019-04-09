# -*- coding: utf-8 -*-

from datetime import date


from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from sqlalchemy import case
from sqlalchemy import func
from sqlalchemy import distinct


from Crud.core import Conexao
from Crud.Models import Venda
from Crud.Models import Cliente
from Crud.Models import StatusEntrega
from Crud.Models import StatusPagamento


class CrudVenda(object):

    def __init__(self, id="", idCliente="", nomeCliente="", celularCliente="",
                 dataEmissao="", prazoEntrega="",
                 dataEntrega="", categoria="", desconto="", frete="",
                 valorTotal="", valorRecebido="", valorPendente="",
                 idStatusEntrega="", statusEntrega="",
                 idStatusPagamento="", statusPagamento="", vendedor="",
                 dataFim="", query=""):
        self.id = id
        self.idCliente = idCliente
        self.nomeCliente = nomeCliente
        self.celularCliente = celularCliente
        self.dataEmissao = dataEmissao
        self.prazoEntrega = prazoEntrega
        self.dataEntrega = dataEntrega
        self.categoria = categoria
        self.desconto = desconto
        self.frete = frete
        self.valorTotal = valorTotal
        self.valorRecebido = valorRecebido
        self.valorPendente = valorPendente
        self.idStatusEntrega = idStatusEntrega
        self.statusEntrega = statusEntrega
        self.idStatusPagamento = idStatusPagamento
        self.statusPagamento = statusPagamento
        self.vendedor = vendedor
        self.dataFim = dataFim
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdVenda(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            ultimo = sessao.query(Venda.id).order_by(
                desc(Venda.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando a Conexao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Inseri Venda
    def inseriVenda(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = Venda(
                id=self.id,
                id_cliente=self.idCliente,
                data_emissao=self.dataEmissao,
                prazo_entrega=self.prazoEntrega,
                categoria=self.categoria,
                desconto=self.desconto,
                frete=self.frete,
                valor_total=self.valorTotal,
                vendedor=self.vendedor

            )

            # Add Query na Sessao
            sessao.add(row)

            # Executando a Query
            sessao.commit()

            # Fechado a conexao
            sessao.close()

        except IntegrityError:
            self.updateVenda()

    # update Venda
    def updateVenda(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando Id
            row = sessao.query(Venda).get(self.id)

            # Novos Valoes
            row.id_cliente = self.idCliente
            row.prazo_entrega = self.prazoEntrega
            row.desconto = self.desconto
            row.frete = self.frete
            row.valor_total = self.valorTotal

            # Executando a Query
            sessao.commit()

            # Fechado a conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Lista de compras realizadas pelo cliente

    def selectVendaCliente(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(Venda.data_emissao, Venda.data_entrega,
                                       Venda.valor_total)
                          .filter(Venda.id_cliente == self.idCliente,
                                  Venda.pagamento == 1))
            self.query.all()

            # Convertendo variaveis em lista
            self.dataEmissao = []
            self.dataEntrega = []
            self.valorTotal = []

            # Salvando resultado da query e suas listas
            for row in self.query:
                self.dataEmissao.append(row.data_emissao)
                self.dataEntrega.append(row.data_entrega)
                self.valorTotal.append(row.valor_total)

            # Fechandoa Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Selecionar Venda por ID

    def selectVendaId(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            busca = sessao.query(Venda).get(self.id)

            # Salvando resultado da Query
            self.id = busca.id
            self.idCliente = busca.id_cliente
            self.dataEmissao = busca.data_emissao
            self.prazoEntrega = busca.prazo_entrega
            self.dataEntrega = busca.data_entrega
            self.categoria = busca.categoria
            self.desconto = busca.desconto
            self.frete = busca.frete
            self.valorTotal = busca.valor_total
            self.valorRecebido = busca.valor_recebido
            self.valorPendente = busca.valor_pendente
            self.idStatusEntrega = busca.entrega
            self.idStatusPagamento = busca.pagamento

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Listar Venda por nome Cliente e data emissão

    def listaVenda(self, cliente):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(Venda.id,
                                       Venda.data_emissao,
                                       Venda.prazo_entrega,
                                       Venda.valor_total,
                                       Venda.entrega,
                                       Venda.pagamento,
                                       Cliente.nome,
                                       Cliente.celular,
                                       StatusEntrega.status_entrega,
                                       StatusPagamento.status_pagamento)
                          .join(Cliente)
                          .join(StatusEntrega)
                          .join(StatusPagamento)
                          .order_by(desc(Venda.id))
                          .filter(Cliente.nome.contains(cliente),
                                  Venda.data_emissao.between(self.dataEmissao,
                                                             self.dataFim),
                                  Venda.categoria == '1',
                                  Venda.pagamento.contains(
                                      self.statusPagamento),
                                  Venda.entrega.contains(self.statusEntrega))
                          )

            # Convertendo variaveis em lista
            self.id = []
            self.dataEmissao = []
            self.prazoEntrega = []
            self.valorTotal = []
            self.idStatusEntrega = []
            self.statusEntrega = []
            self.idStatusPagamento = []
            self.statusPagamento = []
            self.nomeCliente = []
            self.celularCliente = []

            # Salvando resultado da query e suas listas

            for row in self.query:
                self.id.append(row.id)
                self.dataEmissao.append(
                    date.strftime(row.data_emissao, "%d-%m-%Y"))
                self.prazoEntrega.append(
                    date.strftime(row.prazo_entrega, "%d-%m-%Y"))
                self.valorTotal.append(row.valor_total)
                self.idStatusEntrega.append(row.entrega)
                self.statusEntrega.append(row.status_entrega)
                self.idStatusPagamento.append(row.pagamento)
                self.statusPagamento.append(row.status_pagamento)
                self.nomeCliente.append(row.nome)
                self.celularCliente.append(row.celular)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        pass

    # Atualizando estatus entrega ao entregar produtos

    def Entregar(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando ID
            row = sessao.query(Venda).get(self.id)
            # Query
            row.data_entrega = self.dataEntrega
            row.entrega = 1

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Atualizando valor recebido e alterando status

    def Receber(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando por ID
            row = sessao.query(Venda).get(self.id)

            # Update status Pagamento
            status = case([
                (Venda.valor_recebido >= Venda.valor_total, '1')
            ], else_='2'
            )

            # Query
            row.valor_recebido = Venda.valor_recebido + self.valorRecebido
            row.pagamento = status

            # Executando a query
            sessao.commit()

            # Fechando a conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Relatório Vendas por periodo
    def relatValorDia(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(Venda.valor_recebido), 0).label('vendido'),
                func.COUNT(distinct(Venda.id_cliente)).label('cliente'))
                .filter(Venda.data_emissao.between(self.dataEmissao,
                                                   self.dataFim)))
            row.all()

            # salvando resultado
            for query in row:
                self.valorRecebido = str(query.vendido).replace('.', ',')
                self.idCliente = query.cliente

            # Fechando a COnexao
            sessao.close()

        except IntegrityError as err:
            print(err)
