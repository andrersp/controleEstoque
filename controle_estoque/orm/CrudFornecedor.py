# -*- coding: utf-8 -*-

import peewee

from orm.Conexao import Conexao, Fornecedor


class CrudFornecedor(object):

    def __init__(self, id="", nomeFantasia="", razaoSocial="", cnpj="",
                 inscEstadual="", telefone="", email="", site="", obs="",
                 cep="", endereco="", numero="", bairro="", cidade="",
                 estado="", query=""):

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
        self.query = query

     # Recebendo última id inserido

    def lastIdFornecedor(self):
        try:

            # Query
            ultimo = Fornecedor.select().order_by(Fornecedor.id.desc()).get()

            self.id = ultimo.id + 1

            # Fechando Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist:

            self.id = 1

        return self.id

    # Cadastro de Fornecedor

    def inseriFornecedor(self):

        try:

            # Query
            row = Fornecedor.insert(
                id=self.id,
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
                estado=self.estado
            ).on_conflict(
                update={
                    Fornecedor.nome_fantasia: self.nomeFantasia,
                    Fornecedor.razao_social: self.razaoSocial,
                    Fornecedor.cnpj: self.cnpj,
                    Fornecedor.insc_estadual: self.inscEstadual,
                    Fornecedor.telefone: self.telefone,
                    Fornecedor.email: self.email,
                    Fornecedor.site: self.site,
                    Fornecedor.obs: self.obs,
                    Fornecedor.cep: self.cep,
                    Fornecedor.endereco: self.endereco,
                    Fornecedor.numero: self.numero,
                    Fornecedor.bairro: self.bairro,
                    Fornecedor.cidade: self.cidade,
                    Fornecedor.estado: self.estado
                }
            )

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass

    # Selecionar Fornecedor por Id

    def SelectFornecedorId(self):

        try:

            # Query
            busca = Fornecedor.get_by_id(self.id)

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

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

        pass

    # Buscando Fornecedor por Nome

    def listaFornecedor(self):

        try:

            # Query
            self.query = (Fornecedor.select().where(
                Fornecedor.nome_fantasia.contains(self.nomeFantasia)))

            # Convertendo variaveis em lista
            self.id = []
            self.nomeFantasia = []
            self.razaoSocial = []
            self.telefone = []
            self.email = []
            self.site = []

            # Salvando resultado da query e suas listas
            for row in self.query:
                self.id.append(row.id)
                self.nomeFantasia.append(row.nome_fantasia)
                self.razaoSocial.append(row.razao_social)
                self.telefone.append(row.telefone)
                self.email.append(row.email)
                self.site.append(row.site)

            # Fechando a conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

        pass

    # Lista AutoComplete Fornecedor

    def autoCompleteFornecedor(self):

        try:

            # Query
            self.query = (Fornecedor
                          .select(Fornecedor.nome_fantasia, Fornecedor.razao_social)
                          .where(Fornecedor.nome_fantasia
                                 .contains(self.nomeFantasia)))

            # Convertendo variaveis em lista
            self.nomeFantasia = []

            # salvando resultado em sua lista
            for row in self.query:
                self.nomeFantasia.append(row.nome_fantasia)

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

        pass
