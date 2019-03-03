# -*- coding: utf-8 -*-

import peewee
from datetime import date

from orm.Conexao import Conexao
from orm.Conexao import Venda
from orm.Conexao import Cliente
from orm.Conexao import StatusEntrega
from orm.Conexao import StatusPagamento


class CrudVenda(object):

    def __init__(self, id="", idCliente="", nomeCliente="", celularCliente="",
                 dataEmissao="", prazoEntrega="",
                 dataEntrega="", categoria="", desconto="", frete="",
                 valorTotal="", valorRecebido="", valorPendente="",
                 idStatusEntrega="", statusEntrega="",
                 idStatusPagamento="", statusPagamento="",
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
        self.dataFim = dataFim
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdVenda(self):

        try:

            # Query
            ultimo = Venda.select().order_by(-Venda.id).get()

            self.id = ultimo.id + 1

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except:
            self.id = 1

        return self.id

    # Inseri Venda

    def inseriVenda(self):

        try:

            # Query

            row = Venda.insert(
                id=self.id,
                id_cliente=self.idCliente,
                data_emissao=self.dataEmissao,
                prazo_entrega=self.prazoEntrega,
                categoria=self.categoria,
                desconto=self.desconto,
                frete=self.frete,
                valor_total=self.valorTotal,
            ).on_conflict(
                update={
                    Venda.id_cliente: self.idCliente,
                    Venda.prazo_entrega: self.prazoEntrega,
                    Venda.desconto: self.desconto,
                    Venda.frete: self.frete,
                    Venda.valor_total: self.valorTotal
                }
            )

            # Executando a Query
            row.execute()

        except peewee.InternalError as err:
            print(err)

    # Lista de compras realizadas pelo cliente

    def selectVendaCliente(self):

        try:

            # Query
            self.query = (Venda.select(Venda.data_emissao, Venda.data_entrega,
                                       Venda.valor_total)
                          .where(Venda.id_cliente == self.idCliente,
                                 Venda.pagamento == 1))

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
            Conexao().dbhandler.close()
        except peewee.InternalError as err:
            print(err)

    # Selecionar Venda por ID

    def selectVendaId(self):

        try:

            # Query

            busca = Venda.get(Venda.id == self.id)

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
            self.idStatusEntrega = busca.entrega.id
            self.statusEntrega = busca.entrega.status_entrega
            self.idStatusPagamento = busca.pagamento.id
            self.statusPagamento = busca.pagamento.status_pagamento

        except peewee.DoesNotExist as err:
            print(err)

    # Selecionar Venda por nome Cliente e data emissão

    def listaVenda(self, cliente):

        try:

            # Query
            self.query = (Venda.select(Venda.id,
                                       Venda.data_emissao,
                                       Venda.prazo_entrega,
                                       Venda.valor_total,
                                       Venda.entrega,
                                       Venda.pagamento,
                                       Cliente.nome,
                                       Cliente.celular,
                                       StatusEntrega.status_entrega,
                                       StatusPagamento.status_pagamento)
                          .join(Cliente, on=(Venda.id_cliente == Cliente.id),
                                attr='cliente')
                          .join(StatusEntrega, on=(
                              Venda.entrega == StatusEntrega.id),
                              attr='entrega')
                          .join(StatusPagamento, on=(
                              Venda.pagamento == StatusPagamento.id),
                              attr='pagamento')
                          .order_by(-Venda.id)
                          .where(Cliente.nome.contains(cliente),
                                 Venda.data_emissao.between(self.dataEmissao,
                                                            self.dataFim),
                                 Venda.categoria == '1')
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
                self.dataEmissao.append(row.data_emissao)
                self.prazoEntrega.append(row.prazo_entrega)
                self.valorTotal.append(row.valor_total)
                self.idStatusEntrega.append(row.entrega.id)
                self.statusEntrega.append(row.entrega.status_entrega)
                self.idStatusPagamento.append(row.pagamento.id)
                self.statusPagamento.append(row.pagamento.status_pagamento)
                self.nomeCliente.append(row.cliente.nome)
                self.celularCliente.append(row.cliente.celular)

                # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass

    # Atualizando estatus entrega ao entregar produtos

    def Entregar(self):

        try:

            # Query
            row = (Venda.update(data_entrega=self.dataEntrega,
                                entrega=1)
                   .where(Venda.id == self.id))

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Atualizando valor recebido e alterando status

    def Receber(self):

        try:

            # Query
            status = peewee.Case(None, (
                (Venda.valor_recebido >= Venda.valor_total, '1'),
            ), '2')

            row = (Venda.update(
                valor_recebido=Venda.valor_recebido + self.valorRecebido,
                pagamento=status)
                .where(Venda.id == self.id))

            # Executando a query
            row.execute()

            # Fechando a conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)


busca = CrudVenda()
busca.dataEmissao = '2019-02-01'
busca.dataFim = '2019-02-28'


for i in range(len(busca.nomeCliente)):
    print(i)
    print(busca.nomeCliente[i])
