# -*- coding: utf-8 -*-

import peewee

from orm.Conexao import Conexao, Empresa


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

            # Query
            ultimo = Empresa.select().order_by(Empresa.id.desc()).get()

            self.id = ultimo.id + 1

            # Fechando Conexao
            Conexao().dbhandler.close()

            pass

        except peewee.DoesNotExist:

            self.id = 1

            pass

        return self.id

    # Cadastro de Empresa

    def inseriEmpresa(self):

        try:

            # Query
            row = Empresa.insert(
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
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Selecionar Empresa por Id

    def SelectEmpresaId(self):

        try:

            # Query
            busca = Empresa.get_by_id(1)

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
            Conexao().dbhandler.close()

            pass
        except peewee.DoesNotExist:
            self.titulo = None
