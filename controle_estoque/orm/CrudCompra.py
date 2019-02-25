# -*- coding: utf-8 -*-

import peewee
from datetime import date

from Conexao import Conexao, Compra
from Conexao import Fornecedor, CatAPagar, StatusEntrega, StatusPagamento


class CrudCompra(object):

    def __init__(self, id="", idFornecedor="", dataEmissao="", prazoEntrega="",
                 dataEntrega="", categoria="", desconto="", frete="",
                 valorTotal="", valorPago="", valorPendente="",
                 statusEntrega="", statusPagamento="", dataFim="",
                 query=""):
        self.id = id
        self.idFornecedor = idFornecedor
        self.dataEmissao = dataEmissao
        self.prazoEntrega = prazoEntrega
        self.dataEntrega = dataEntrega
        self.categoria = categoria
        self.desconto = desconto
        self.frete = frete
        self.valorTotal = valorTotal
        self.valorPago = valorPago
        self.valorPendente = valorPendente
        self.statusEntrega = statusEntrega
        self.statusPagamento = statusPagamento
        self.dataFim = dataFim
        self.query = query

    # Recebendo ultimo Id inserido

    def lastIdCompra(self):

        try:

            # Query
            ultimo = Compra.select().order_by(-Compra.id).get()

            self.id = ultimo.id + 1

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except:
            self.id = 1

        return self.id

    # Inseri Compra

    def inseriCompra(self):

        try:

            # Query

            row = Compra.insert(
                id=self.id,
                id_fornecedor=self.idFornecedor,
                data_emissao=self.dataEmissao,
                prazo_entrega=self.prazoEntrega,
                categoria=self.categoria,
                desconto=self.desconto,
                frete=self.frete,
                valor_total=self.valorTotal,
            ).on_conflict(
                update={
                    Compra.id_fornecedor: self.idFornecedor,
                    Compra.prazo_entrega: self.prazoEntrega,
                    Compra.desconto: self.desconto,
                    Compra.frete: self.frete,
                    Compra.valor_total: self.valorTotal
                }
            )

            # Executando a Query
            row.execute()

        except peewee.InternalError as err:
            print(err)

    # # Selecionar compras por Cód Cliente

    # def selectCompraCliente(self):

    #     try:
    #         Compra.select().where(Compra.id)
    #     except peewee.DoesNotExist as err:
    #         print(err)

    # Selecionar compra por ID

    def selectCompraId(self):

        try:

            # Query

            busca = Compra.get_by_id(self.id)

            # Salvando resultado da Query
            self.id = busca.id
            self.idFornecedor = busca.id_fornecedor
            self.dataEmissao = busca.data_emissao
            self.prazoEntrega = busca.prazo_entrega
            self.dataEntrega = busca.data_entrega
            self.categoria = busca.categoria
            self.desconto = busca.desconto
            self.frete = busca.frete
            self.valorTotal = busca.valor_total
            self.valorPago = busca.valor_pago
            self.valorPendente = busca.valor_pendente
            self.statusEntrega = busca.status_entrega
            self.statusPagamento = busca.status_pagamento

        except peewee.DoesNotExist as err:
            print(err)

    # Selecionar compra por nome fornecedor e data emissão

    def listaCompra(self, fornecedor):

        try:

            # Query
            self.query = (Compra.select(Compra.id,
                                        Compra.id_fornecedor,
                                        Compra.data_emissao,
                                        Compra.prazo_entrega,
                                        Compra.valor_total,
                                        Compra.status_entrega,
                                        Compra.status_pagamento,
                                        Fornecedor.nome_fantasia,
                                        Fornecedor.telefone,
                                        CatAPagar.categoria_a_pagar,
                                        StatusEntrega.status_entrega,
                                        StatusPagamento.status_pagamento)
                          .join(Fornecedor)
                          .join(CatAPagar,
                                on=(Compra.categoria == CatAPagar.id))
                          .join(StatusEntrega, on=(
                              Compra.status_entrega == StatusEntrega.id))
                          .join(StatusPagamento, on=(
                              Compra.status_pagamento == StatusPagamento.id))
                          .where(Fornecedor.nome_fantasia.contains(fornecedor),
                                 Compra.data_emissao.between(self.dataEmissao,
                                                             self.dataFim),
                                 Compra.categoria == '1')
                          )

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
