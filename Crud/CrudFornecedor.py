# -*- coding: utf-8 -*-
from Crud.conexao import Conexao
import mysql.connector


class CrudFornecedor(object):

    def __init__(self, idFornecedor="", NomeFantasia="", RazaoSocial="", cnpj="",
                 inscEstadual="", telefone="", email="", site="", obs="", cep="",
                 endereco="", numero="", bairro="", cidade="", estado=""):
        self.idFornecedor = idFornecedor
        self.NomeFantasia = NomeFantasia
        self.RazaoSocial = RazaoSocial
        self.cnpj = cnpj
        self.inscEstadual = inscEstadual
        self.telefone = telefone
        self.email = email
        self.site = site
        self.obs = obs
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
    # Buscanado ultimo ID

    def LasIdFornecedor(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(" SELECT id FROM fornecedor ORDER BY id DESC LIMIT 1")
            row = c.fetchone()
            if row:
                self.idFornecedor = row[0] + 1
            else:
                self.idFornecedor = 1
            c.close()
        except mysql.connector.Error as err:
            print(err)

        return self.idFornecedor

    # Cadastro Fornecedor
    def CadFornecedor(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO fornecedor VALUES ('{}', '{}', '{}', '{}', 
            	'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', 
            	'{}')  ON DUPLICATE KEY UPDATE nomeFantasia ='{}', 
            	razaoSocial="{}", cnpj='{}', inscEstadual='{}', telefone='{}',
            	email='{}', site='{}', obs='{}', cep='{}', endereco='{}',
            	numero='{}', bairro='{}', cidade='{}', estado='{}'
            	 """.format(self.idFornecedor,
                         self.NomeFantasia, self.RazaoSocial, self.cnpj,
                         self.inscEstadual, self.telefone, self.email,
                         self.site, self.obs, self.cep, self.endereco,
                         self.numero, self.bairro, self.cidade, self.estado,
                         self.NomeFantasia, self.RazaoSocial, self.cnpj,
                         self.inscEstadual, self.telefone, self.email,
                         self.site, self.obs, self.cep, self.endereco,
                         self.numero, self.bairro, self.cidade, self.estado))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    # LIstando Clientes para tabela e busca
    def ListaFornecedorTabela(self, fornecedor):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        self.idFornecedor = []
        self.NomeFantasia = []
        self.RazaoSocial = []
        self.telefone = []
        self.email = []
        self.site = []

        try:
            c.execute(""" SELECT id, nomeFantasia, razaoSocial, telefone, email,
        	site FROM fornecedor WHERE nomeFantasia LIKE '%{}%' """
                      .format(fornecedor))
            row = c.fetchall()
            if row:
                for linha in row:
                    self.idFornecedor.append(linha[0])
                    self.NomeFantasia.append(linha[1])
                    self.RazaoSocial.append(linha[2])
                    self.telefone.append(linha[3])
                    self.email.append(linha[4])
                    self.site.append(linha[5])
            c.close()
        except mysql.connector.Error as err:
            print(err)

    def SelectFornecedorId(self, id):
        conecta = Conexao()
        self.idFornecedor = id
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """SELECT * FROM fornecedor WHERE id='{}'"""
                .format(self.idFornecedor))
            row = c.fetchone()
            if row:
                self.idFornecedor = row[0]
                self.NomeFantasia = row[1]
                self.RazaoSocial = row[2]
                self.cnpj = row[3]
                self.inscEstadual = row[4]
                self.telefone = row[5]
                self.email = row[6]
                self.site = row[7]
                self.obs = row[8]
                self.cep = row[9]
                self.endereco = row[10]
                self.numero = row[11]
                self.bairro = row[12]
                self.cidade = row[13]
                self.estado = row[14]
            c.close()

        except mysql.connector.Error as err:
            print(err)


# busca = CrudFornecedor()
# busca.SelectFornecedorId(1)
# # busca.NomeFantasia = "Azul e RazaoSocial"
# # busca.RazaoSocial = "Azul"
# # busca.ListaFornecedorTabela('')
# print busca.NomeFantasia
