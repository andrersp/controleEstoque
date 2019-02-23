# -*- coding: utf-8 -*-

import peewee
from datetime import date

from Conexao import Conexao, Venda
from Conexao import Cliente, CatAReceber, StatusEntrega, StatusPagamento


class CrudVenda(object):

    def __init__(self, id="", idCliente="", dataEmissao="", prazoEntrega="",
                 dataEntrega="", categoria="", desconto="", frete="",
                 valorTotal="", valorRecebido="", valorPendente="",
                 statusEntrega="", statusPagamento="", dataFim="",
                 query=""):
        self.id = id
        self.idCliente = idCliente
        self.dataEmissao = dataEmissao
        self.prazoEntrega = prazoEntrega
        self.dataEntrega = dataEntrega
        self.categoria = categoria
        self.desconto = desconto
        self.frete = frete
        self.valorTotal = valorTotal
        self.valorRecebido = valorRecebido
        self.valorPendente = valorPendente
        self.statusEntrega = statusEntrega
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

    # Selecionar Venda por ID

    def selectVendaId(self):

        try:

            # Query

            busca = Venda.get_by_id(self.id)

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
            self.statusEntrega = busca.status_entrega
            self.statusPagamento = busca.status_pagamento

        except peewee.DoesNotExist as err:
            print(err)

    # Selecionar Venda por nome Cliente e data emissão

    def listaVenda(self, cliente):

        try:

            # Query
            self.query = (Venda.select(Venda.id,
                                       Venda.id_cliente,
                                       Venda.data_emissao,
                                       Venda.prazo_entrega,
                                       Venda.valor_total,
                                       Venda.status_entrega,
                                       Venda.status_pagamento,
                                       Cliente.nome,
                                       Cliente.celular,
                                       CatAReceber.categoria_a_receber,
                                       StatusEntrega.status_entrega,
                                       StatusPagamento.status_pagamento)
                          .join(Cliente)
                          .join(CatAReceber, on=(Venda.categoria == CatAReceber.id))
                          .join(StatusEntrega, on=(
                              Venda.status_entrega == StatusEntrega.id))
                          .join(StatusPagamento, on=(
                              Venda.status_pagamento == StatusPagamento.id))
                          .where(Cliente.nome.contains(cliente),
                                 Venda.data_emissao.between(self.dataEmissao,
                                                            self.dataFim),
                                 Venda.categoria == '1')
                          )

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
