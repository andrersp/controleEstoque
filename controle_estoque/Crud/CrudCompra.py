# -*- coding: utf-8 -*-

import peewee


from Crud.Conexao import Conexao
from Crud.Conexao import Compra
from Crud.Conexao import Fornecedor
from Crud.Conexao import CatAPagar
from Crud.Conexao import StatusEntrega
from Crud.Conexao import StatusPagamento


class CrudCompra(object):

    def __init__(self, id="", idFornecedor="", dataEmissao="", prazoEntrega="",
                 dataEntrega="", categoria="", desconto="", frete="",
                 valorTotal="", valorPago="", valorPendente="",
                 idStatusEntrega="", idStatusPagamento="", fornecedor="",
                 telefone="",
                 statusEntrega="", statusPagamento="", dataFim="",
                 query=""):
        self.id = id
        self.idFornecedor = idFornecedor
        self.fornecedor = fornecedor
        self.telefone = telefone
        self.dataEmissao = dataEmissao
        self.prazoEntrega = prazoEntrega
        self.dataEntrega = dataEntrega
        self.categoria = categoria
        self.desconto = desconto
        self.frete = frete
        self.valorTotal = valorTotal
        self.valorPago = valorPago
        self.valorPendente = valorPendente
        self.idStatusEntrega = idStatusEntrega
        self.statusEntrega = statusEntrega
        self.idStatusPagamento = idStatusPagamento
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

    # Selecionar compras por Cód Fornecedor

    def selectCompraFornecedor(self):

        try:

            # Query
            self.query = (Compra.select(Compra.data_emissao,
                                        Compra.data_entrega,
                                        Compra.valor_total)
                          .where(Compra.id_fornecedor == self.idFornecedor,
                                 Compra.pagamento == 1))

            # Convertendo variaveis em lista
            self.dataEmissao = []
            self.dataEntrega = []
            self.valorTotal = []

            # Salvando resultado da query e suas listas
            for row in self.query:
                self.dataEmissao.append(row.data_emissao)
                self.dataEntrega.append(row.data_entrega)
                self.valorTotal.append(row.valor_total)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

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
            self.idFornecedor = busca.entrega.id
            self.idStatusEntrega = busca.entrega.id
            self.statusEntrega = busca.entrega.status_entrega
            self.idStatusPagamento = busca.pagamento.id
            self.statusPagamento = busca.pagamento.status_pagamento

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
                                        Compra.entrega,
                                        Compra.pagamento,
                                        Fornecedor.nome_fantasia,
                                        Fornecedor.telefone,
                                        CatAPagar.categoria_a_pagar,
                                        StatusEntrega.status_entrega,
                                        StatusPagamento.status_pagamento)
                          .join(Fornecedor,
                                on=(Compra.id_fornecedor == Fornecedor.id),
                                attr="fornecedor")
                          .join(CatAPagar,
                                on=(Compra.categoria == CatAPagar.id))
                          .join(StatusEntrega, on=(
                              Compra.entrega == StatusEntrega.id))
                          .join(StatusPagamento, on=(
                              Compra.pagamento == StatusPagamento.id))
                          .order_by(-Compra.id)
                          .where(Fornecedor.nome_fantasia.contains(fornecedor),
                                 Compra.data_emissao.between(self.dataEmissao,
                                                             self.dataFim),
                                 Compra.categoria == '1')
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
            self.fornecedor = []
            self.telefone = []

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
                self.fornecedor.append(row.fornecedor.nome_fantasia)
                self.telefone.append(row.fornecedor.telefone)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

    # Atualizando estatus entrega ao receber produtos
    def receberProduto(self):

        try:

            # Query
            row = (Compra.update(data_entrega=self.dataEntrega,
                                 entrega=1)
                   .where(Compra.id == self.id))

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Atualizando valor recebido e alterando status

    # Atualizando valor recebido e alterando status

    def Pagar(self):

        try:

            # Query
            status = peewee.Case(None, (
                (Compra.valor_pago >= Compra.valor_total, '1'),
            ), '2')

            row = (Compra.update(
                valor_pago=Compra.valor_pago + self.valorPago,
                pagamento=status)
                .where(Compra.id == self.id))

            # Executando a query
            row.execute()

            # Fechando a conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)
