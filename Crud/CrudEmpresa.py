# -*- coding: utf-8 -*-
from Crud.conexao import Conexao
import mysql.connector


class CrudEmpresa(object):

    def __init__(self, idEmpresa="", NomeFantasia="", RazaoSocial="", cnpj="",
                 inscEstadual="", telefone="", email="", site="", obs="", cep="",
                 endereco="", numero="", bairro="", cidade="", estado="",
                 titulo="", subtitulo="", logo=""):
        self.idEmpresa = idEmpresa
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
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.logo = logo
    # Buscanado ultimo ID

    def LasIdEmpresa(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(" SELECT id FROM empresa ORDER BY id DESC LIMIT 1")
            row = c.fetchone()
            if row:
                self.idEmpresa = row[0]
            else:
                self.idEmpresa = 1
            c.close()
        except mysql.connector.Error as err:
            print(err)

        return self.idEmpresa

    # Cadastro Empresa
    def CadEmpresa(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO empresa VALUES ('{}', '{}', '{}', '{}', 
                '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', 
                '{}', '{}', '{}', '{}')  ON DUPLICATE KEY UPDATE nomeFantasia ='{}', 
                razaoSocial="{}", cnpj='{}', inscEstadual='{}', telefone='{}',
                email='{}', site='{}', obs='{}', cep='{}', endereco='{}',
                numero='{}', bairro='{}', cidade='{}', estado='{}',
                titulo='{}', subtitulo='{}', logo='{}'
                 """.format(self.idEmpresa,
                            self.NomeFantasia, self.RazaoSocial, self.cnpj,
                            self.inscEstadual, self.telefone, self.email,
                            self.site, self.obs, self.cep, self.endereco,
                            self.numero, self.bairro, self.cidade, self.estado,
                            self.titulo, self.subtitulo, self.logo,
                            self.NomeFantasia, self.RazaoSocial, self.cnpj,
                            self.inscEstadual, self.telefone, self.email,
                            self.site, self.obs, self.cep, self.endereco,
                            self.numero, self.bairro, self.cidade, self.estado,
                            self.titulo, self.subtitulo, self.logo))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    def SelectEmpresaId(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """SELECT * FROM empresa WHERE id='{}'"""
                .format(self.idEmpresa))
            row = c.fetchone()
            if row:
                self.idEmpresa = row[0]
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
                self.titulo = row[15]
                self.subtitulo = row[16]
                self.logo = row[17]

            c.close()

        except mysql.connector.Error as err:
            print(err)


# busca = CrudEmpresa()
# busca.SelectEmpresaId(1)
# # busca.NomeFantasia = "Azul e RazaoSocial"
# # busca.RazaoSocial = "Azul"
# # busca.ListaEmpresaTabela('')
# print busca.NomeFantasia
