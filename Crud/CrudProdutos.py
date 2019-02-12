# -*- coding: utf-8 -*-
from Crud.conexao import Conexao
import mysql.connector


class CrudProdutos(object):

    def __init__(self, idProduto="", descricaoProduto="", imagemProduto="",
                 categoria="", marca="", estoqueMinimo="", estoqueMaximo="",
                 qtdeProduto="", valorCompra="", valorUnitario="",
                 valorAtacado="", qtdeAtacado="", obsProduto="", lastId="",
                 idCategoria="", idMarca="", idRelacao='{}', data='{}'):
        self.idProduto = idProduto
        self.descricaoProduto = descricaoProduto
        self.imagemProduto = imagemProduto
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
        self.lastId = lastId
        self.idCategoria = idCategoria
        self.idMarca = idMarca
        self.idRelacao = idRelacao
        self.data = data

    def lastIdProduto(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" SELECT id FROM produto ORDER BY id DESC LIMIT 1 """)
            row = c.fetchone()
            if row:
                self.lastId = row[0] + 1

            else:
                self.lastId = 1
            c.close()

        except mysql.connector.Error as err:
            print(err)

        return self.lastId

    def lasIdcategoria(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(
                """ SELECT id FROM categoriaproduto ORDER BY id DESC LIMIT 1 """)
            row = c.fetchone()
            if row:
                self.idCategoria = row[0] + 1
            else:
                self.idCategoria = 1

            c.close()
        except mysql.connector.Error as err:
            print(err)
        return self.idCategoria

    def lastIdMarca(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute(
                """ SELECT id FROM marcaproduto ORDER BY id DESC LIMIT 1 """)
            row = c.fetchone()
            if row:
                self.idMarca = row[0] + 1
            else:
                self.idMarca = 1
            c.close()

        except mysql.connector.Error as err:
            print(err)
        return self.idMarca

    # Lista Categorias
    def listaCategoria(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        self.idCategoria = []
        self.categoria = []

        try:
            c.execute("SELECT * FROM categoriaproduto")
            row = c.fetchall()
            for linha in row:
                self.idCategoria.append(linha[0])
                self.categoria.append(linha[1])
            c.close()

        except mysql.connector.Error as err:
            print(err)

    # Adicionando Categoria
    def AddCategoria(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO categoriaproduto VALUES ('{}', '{}')
            ON DUPLICATE KEY UPDATE categoria='{}' """
                      .format(self.idCategoria, self.categoria, self.categoria))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # Lista Marcas por Categoria
    def listaMarca(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        self.idMarca = []
        self.marca = []

        try:
            c.execute("""SELECT id, marca FROM marcaproduto WHERE categoria = '{}' """
                      .format(self.idCategoria))
            row = c.fetchall()
            for linha in row:
                self.idMarca.append(linha[0])
                self.marca.append(linha[1])
            c.close()

        except mysql.connector.Error as err:
            print(err)

    # Adicionando Marca
    def Addmarca(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO marcaproduto (categoria, marca) VALUES 
                ('{}', '{}')"""
                      .format(self.idCategoria, self.marca))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    def cadProduto(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ INSERT INTO produto (id, descricao, imagem, categoria, 
                marca, estoque_minimo, estoque_maximo, valor_compra, 
                valor_unitario, valor_atacado, qtde_atacado, obs) 
                VALUES ('{}', '{}', '{}', '{}', '{}',
                '{}', '{}', '{}', '{}', '{}', '{}', '{}')
                ON DUPLICATE KEY UPDATE  descricao='{}', imagem='{}',
                categoria='{}', marca='{}', 
                estoque_minimo='{}', estoque_maximo='{}',
                valor_compra='{}', valor_unitario='{}', valor_atacado='{}',
                qtde_atacado='{}', obs='{}' """
                .format(self.idProduto, self.descricaoProduto,
                        self.imagemProduto, self.idCategoria,
                        self.idMarca, self.estoqueMinimo,
                        self.estoqueMaximo, self.valorCompra,
                        self.valorUnitario, self.valorAtacado,
                        self.qtdeAtacado, self.obsProduto,
                        self.descricaoProduto, self.imagemProduto,
                        self.idCategoria, self.idMarca,
                        self.estoqueMinimo, self.estoqueMaximo,
                        self.valorCompra, self.valorUnitario,
                        self.valorAtacado, self.qtdeAtacado, self.obsProduto))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # Entrada de produto no estoque
    def EntradaProduto(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" UPDATE produto SET qtde = qtde + '{}', 
            valor_compra = '{}'
            WHERE id='{}' """.format(self.qtdeProduto, self.valorCompra,
                                     self.idProduto))
            conecta.conecta.commit()
        except mysql.connector.Error as err:
            print("Erro saida Produto: {}").format(err)
        pass

    def SaidaProduto(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" UPDATE produto SET qtde = qtde - '{}'
            WHERE id='{}' """.format(self.qtdeProduto, self.idProduto))
            conecta.conecta.commit()
        except mysql.connector.Error as err:
            print("Erro saida Produto: {}").format(err)
        pass

    # Lista Produtos Tabela
    def ListaProdutoTabela(self, produto):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        self.idProduto = []
        self.descricaoProduto = []
        self.qtdeProduto = []
        self.valorUnitario = []
        self.valorAtacado = []
        self.estoqueMinimo = []
        self.marca = []
        self.qtdeAtacado = []

        try:
            c.execute(""" SELECT produto.id, produto.descricao, 
                produto.estoque_minimo, produto.qtde, produto.valor_unitario,
                produto.valor_atacado, produto.qtde_atacado, marcaproduto.* FROM produto 
                INNER JOIN marcaproduto ON produto.marca = marcaproduto.id
                WHERE descricao LIKE '%{}%' ORDER BY produto.id ASC"""
                      .format(produto))
            row = c.fetchall()
            if row:
                for linha in row:
                    self.idProduto.append(linha[0])
                    self.descricaoProduto.append(linha[1])
                    self.estoqueMinimo.append(linha[2])
                    self.qtdeProduto.append(linha[3])
                    self.valorUnitario.append(linha[4])
                    self.valorAtacado.append(linha[5])
                    self.qtdeAtacado.append(linha[6])
                    self.marca.append(linha[9])

            c.close()

        except mysql.connector.Error as err:
            print(err)

    # Seleciona produto ID
    def SelectProdutoId(self, id):
        self.idProduto = id
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT * FROM produto WHERE id = '{}' """
                .format(self.idProduto))
            row = c.fetchone()
            if row:
                self.idProduto = row[0]
                self.descricaoProduto = row[1]
                self.imagemProduto = row[2]
                self.idCategoria = row[3]
                self.idMarca = row[4]
                self.estoqueMinimo = str(row[5])
                self.estoqueMaximo = str(row[6])
                self.qtdeProduto = str(row[7])
                self.valorCompra = format(row[8], ".2f")
                self.valorUnitario = format(row[9], ".2f")
                self.valorAtacado = format(row[10], ".2f")
                self.qtdeAtacado = str(row[11])
                self.obsProduto = row[12]

        except mysql.connector.Error as err:
            print(err)


# create table produtos (
# id integer generated by default as identity primary key,
#   descricao varchar(80) DEFAULT NULL,
#   imagem BLOB SUB_TYPE 0 SEGMENT SIZE 80,
#   categoria integer NOT NULL,
#   marca integer NOT NULL,
#   estoque_minimo integer DEFAULT NULL,
#   estoque_maximo integer DEFAULT NULL,
#   qtde integer NOT NULL,
#   valor_compra decimal(9,2) NOT NULL,
#   valor_unitario decimal(9,2) NOT NULL,
#   valor_atacado decimal(9,2) NOT NULL,
#   qtde_atacado integer NOT NULL,
#   obs varchar(80) NOT NULL
# )
