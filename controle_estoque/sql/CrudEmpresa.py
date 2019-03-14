# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from sql.core import Conexao
from sql.Models import Empresa


class CrudEmpresa(object):

    def __init__(self, id="", nomeFantasia="", razaoSocial="", cnpj="",
                 inscEstadual="", telefone="", email="", site="", obs="",
                 cep="", endereco="", numero="", bairro="", cidade="",
                 estado="",  titulo="", subtitulo="", logo="",
                 query=""):

        self.id = id
        self.nomeFantasia = nomeFantasia
        self.razaoSocial = razaoSocial
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
        self.query = query

    # Recebendo última id inserido

    def lastIdEmpresa(self):
        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            ultimo = sessao.query(Empresa).order_by(
                desc(Empresa.id)).limite(1).first()

            self.id = ultimo.id + 1

            # Fechando Conexao
            sessao.close()

            pass

        except:

            self.id = 1

            pass

        return self.id

    # Cadastro de Empresa
    def inseriEmpresa(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = Empresa(
                id=1,
                nome_fantasia=self.nomeFantasia,
                razao_social=self.razaoSocial,
                cnpj=self.cnpj,
                insc_estadual=self.inscEstadual,
                telefone=self.telefone,
                email=self.email,
                site=self.site,
                obs=self.obs,
                cep=self.cep,
                endereco=self.endereco,
                numero=self.numero,
                bairro=self.bairro,
                cidade=self.cidade,
                estado=self.estado,
                titulo=self.titulo,
                subtitulo=self.subtitulo,
                logo=self.logo
            )

            # Add Query sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:

            self.updateEmpresa()

    # Update de Empresa
    def updateEmpresa(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando ID
            row = sessao.query(Empresa).get(1)

            # Novos Valores

            row.nome_fantasia = self.nomeFantasia
            row.razao_social = self.razaoSocial
            row.cnpj = self.cnpj
            row.insc_estadual = self.inscEstadual
            row.telefone = self.telefone
            row.email = self.email
            row.site = self.site
            row.obs = self.obs
            row.cep = self.cep
            row.endereco = self.endereco
            row.numero = self.numero
            row.bairro = self.bairro
            row.cidade = self.cidade
            row.estado = self.estado
            row.titulo = self.titulo
            row.subtitulo = self.subtitulo
            row.logo = self.logo

            # Add Query sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

    # Selecionar Empresa por Id
    def SelectEmpresaId(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            busca = sessao.query(Empresa).get(1)

            # Salvando resultado da Query
            self.id = busca.id
            self.nomeFantasia = busca.nome_fantasia
            self.razaoSocial = busca.razao_social
            self.cnpj = busca.cnpj
            self.inscEstadual = busca.insc_estadual
            self.telefone = busca.telefone
            self.email = busca.email
            self.site = busca.site
            self.obs = busca.obs
            self.cep = busca.cep
            self.endereco = busca.endereco
            self.numero = busca.numero
            self.bairro = busca.bairro
            self.cidade = busca.cidade
            self.estado = busca.estado
            self.titulo = busca.titulo
            self.subtitulo = busca.subtitulo
            self.logo = busca.logo

            # Fechando a Conexao
            sessao.close()

            pass
        except:
            self.titulo = None
