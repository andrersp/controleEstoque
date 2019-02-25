# -*- coding: utf-8 -*-

import peewee


from orm.Conexao import Conexao, Produto, MarcaProduto, CategoriaProduto


class CrudProduto(object):

    def __init__(self, id="", produto="", imagem="",
                 categoria="", marca="", estoqueMinimo="", estoqueMaximo="",
                 qtdeProduto="", valorCompra="", valorUnitario="",
                 valorAtacado="", qtdeAtacado="", obsProduto="", query=""):

        self.id = id
        self.produto = produto
        self.imagem = imagem
        self.categoria = categoria
        self.marca = marca
        self.estoqueMinimo = estoqueMinimo
        self.estoqueMaximo = estoqueMaximo
        self.qtdeProduto = qtdeProduto
        self.valorCompra = valorCompra
        self.valorUnitario = valorUnitario
        self.valorAtacado = valorAtacado
        self.qtdeAtacado = qtdeAtacado
        self.obsProduto = obsProduto
        self.query = query

    # Recendo ultimo ID inserido

    def lastIdProduto(self):

        try:

            ultimo = Produto.select().order_by(Produto.id.desc()).get()
            self.id = ultimo.id + 1

            # Fechando Conexao
            Conexao().dbhandler.close()

        except:

            self.id = 1

        return self.id

     # Cadastro de Produto

    def inseriProduto(self):

        try:

            # Query
            row = Produto.insert(
                id=self.id,
                produto=self.produto,
                imagem=self.imagem,
                categoria=self.categoria,
                marca=self.marca,
                estoque_minimo=self.estoqueMinimo,
                estoque_maximo=self.estoqueMaximo,
                valor_compra=self.valorCompra,
                valor_unitario=self.valorUnitario,
                valor_atacado=self.valorAtacado,
                qtde_atacado=self.qtdeAtacado,
                obs=self.obsProduto

            ).on_conflict_replace()

            # Executando a Query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.IntegrityError as err:
            print(err)

        pass

    # Busca por ID

    def selectProdutoId(self):

        try:

            # Query
            busca = Produto.get_by_id(self.id)

            # Salvando resultado da Query
            self.id = busca.id
            self.produto = busca.produto
            self.imagem = busca.imagem
            self.categoria = busca.categoria
            self.marca = busca.marca
            self.estoqueMinimo = busca.estoque_minimo
            self.estoqueMaximo = busca.estoque_maximo
            self.qtdeProduto = busca.qtde
            self.valorCompra = busca.valor_compra
            self.valorUnitario = busca.valor_unitario
            self.valorAtacado = busca.valor_atacado
            self.qtdeAtacado = busca.qtde_atacado
            self.obsProduto = busca.obs

            # Fechando a Conexao
            Conexao().dbhandler.close()

            pass

        except peewee.DoesNotExist as err:

            print(err)

            pass

    # Busca Produto por Nome

    def listaProduto(self):

        try:

            # Query
            self.query = (Produto.select(Produto.id, Produto.produto,
                                         Produto.estoque_minimo, Produto.qtde,
                                         Produto.valor_unitario,
                                         Produto.valor_atacado,
                                         Produto.qtde_atacado,
                                         MarcaProduto.marca_produto
                                         )
                          .join(MarcaProduto)
                          .where(
                Produto.produto.contains('{}'.format(self.produto))))

           # Fechando a Conexao
            Conexao().dbhandler.close()

            pass

        except peewee.DoesNotExist as err:

            print(err)

            pass

    # Busca Nome AutoCompete
    def autoCompleteProduto(self):

        try:

            # Query
            self.query = (Produto.select(Produto.id, Produto.produto)
                          .where(Produto.produto.contains(self.produto)))

            # Fechando Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
