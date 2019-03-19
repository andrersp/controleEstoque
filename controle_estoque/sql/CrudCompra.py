# -*- coding: utf-8 -*-

from datetime import date


from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from sqlalchemy import case


from sql.core import Conexao
from sql.Models import Compra, Fornecedor, StatusEntrega, StatusPagamento, CatAPagar


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

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            ultimo = sessao.query(Compra.id).order_by(
                desc(Compra.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando a Conexao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Inseri Compra

    def inseriCompra(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = Compra(
                id=self.id,
                id_fornecedor=self.idFornecedor,
                data_emissao=self.dataEmissao,
                prazo_entrega=self.prazoEntrega,
                categoria=self.categoria,
                desconto=self.desconto,
                frete=self.frete,
                valor_total=self.valorTotal,
            )

            # Add query na sessao
            sessao.add(row)

            # Executando a Query
            sessao.commit()

            # Fechando Sessao
            sessao.close()

        except IntegrityError:
            self.updateCompra()

    # Update Compra
    def updateCompra(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando ID
            row = sessao.query(Compra).get(self.id)

            # novos valores
            row.id_fornecedor = self.idFornecedor
            row.data_emissao = self.dataEmissao
            row.prazo_entrega = self.prazoEntrega
            row.categoria = self.categoria
            row.desconto = self.desconto
            row.frete = self.frete
            row.valor_total = self.valorTotal

            # Executando a Query
            sessao.commit()

            # Fechando Sessao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Selecionar compras por Cód Fornecedor

    def selectCompraFornecedor(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(Compra.data_emissao,
                                       Compra.data_entrega,
                                       Compra.valor_total)
                          .filter(Compra.id_fornecedor == self.idFornecedor,
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
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Selecionar compra por ID

    def selectCompraId(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            busca = sessao.query(Compra).get(self.id)

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
            self.idStatusEntrega = busca.entrega
            self.idStatusPagamento = busca.pagamento

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Selecionar compra por nome fornecedor e data emissão

    def listaCompra(self, fornecedor):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = (sessao.query(Compra.id,
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
                          .join(Fornecedor)
                          .join(CatAPagar)
                          .join(StatusEntrega)
                          .join(StatusPagamento)
                          .order_by(desc(Compra.id))
                          .filter(Compra.categoria == '1',
                                  Compra.pagamento.contains(
                                      self.statusPagamento),
                                  Compra.entrega.contains(self.statusEntrega),
                                  Fornecedor.nome_fantasia.contains(
                                      fornecedor),
                                  Compra.data_emissao.between(self.dataEmissao,
                                                              self.dataFim),
                                  Compra.prazo_entrega.between(self.dataEmissao,
                                                               self.dataFim))
                          )
            self.query.all()

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
                self.dataEmissao.append(
                    date.strftime(row.data_emissao, "%d-%m-%Y"))
                self.prazoEntrega.append(
                    date.strftime(row.prazo_entrega, "%d-%m-%Y"))
                self.valorTotal.append(row.valor_total)
                self.idStatusEntrega.append(row.entrega)
                self.statusEntrega.append(row.status_entrega)
                self.idStatusPagamento.append(row.pagamento)
                self.statusPagamento.append(row.status_pagamento)
                self.fornecedor.append(row.nome_fantasia)
                self.telefone.append(row.telefone)

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Atualizando estatus entrega ao receber produtos
    def receberProduto(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = sessao.query(Compra).get(self.id)

            row.data_entrega = self.dataEntrega
            row.entrega = 1

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Atualizando valor recebido e alterando status

    def Pagar(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando Id
            row = sessao.query(Compra).get(self.id)

            # Update status Pagamento
            status = case([
                (Compra.valor_pago >= Compra.valor_total, '1')
            ], else_='2'
            )

            row.valor_pago = Compra.valor_pago + self.valorPago
            row.pagamento = status

            # Executando a Query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Lista de Pedidos a receber hoje
    def pedidosAReceber(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = sessao.query(Compra.prazo_entrega).filter(
                Compra.prazo_entrega == date.today()).count()

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        return row
