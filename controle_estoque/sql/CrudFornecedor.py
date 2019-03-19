# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import ProgrammingError
from sqlalchemy import desc


from sql.core import Conexao
from sql.Models import Fornecedor


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

            # Abrindo a Sessao
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            ultimo = sessao.query(Fornecedor).order_by(
                desc(Fornecedor.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando Conexao
            sessao.close()

        except:

            self.id = 1

        return self.id

    # Cadastro de Fornecedor

    def inseriFornecedor(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = Fornecedor(
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
            )

            # Add Query na sessao
            sessao.add(row)

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except IntegrityError:
            self.updateFornecedor()

        pass

    # Atualiza cadastro de Fornecedor

    def updateFornecedor(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando id
            query = sessao.query(Fornecedor).get(self.id)

            # Novos Valores
            query.nome_fantasia = self.nomeFantasia
            query.razao_social = self.razaoSocial
            query.cnpj = self.cnpj
            query.insc_estadual = self.inscEstadual
            query.telefone = self.telefone
            query.email = self.email
            query.site = self.site
            query.obs = self.obs
            query.cep = self.cep
            query.endereco = self.endereco
            query.numero = self.numero
            query.bairro = self.bairro
            query.cidade = self.cidade
            query.estado = self.estado

            # Executando a query
            sessao.commit()

            # Fechando a Conexao
            sessao.close()

        except ProgrammingError as err:
            print(err)

        pass

    # Selecionar Fornecedor por Id

    def SelectFornecedorId(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            busca = sessao.query(Fornecedor).get(self.id)

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
            sessao.close()

        except:
            pass

        pass

    # Buscando Fornecedor por Nome

    def listaFornecedor(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(Fornecedor).filter(
                Fornecedor.nome_fantasia.contains(self.nomeFantasia))
            self.query.all()

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
            sessao.close()

        except ProgrammingError as err:
            print(err)

        pass

    # Lista AutoComplete Fornecedor

    def autoCompleteFornecedor(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(Fornecedor).filter(
                Fornecedor.nome_fantasia.contains(self.nomeFantasia))
            self.query.all()

            # Convertendo variaveis em lista
            self.nomeFantasia = []

            # salvando resultado em sua lista
            for row in self.query:
                self.nomeFantasia.append(row.nome_fantasia)

            # Fechando a Conexao
            sessao.close()

        except ProgrammingError as err:
            print(err)

        pass

    # Busca Fornecedor por nome
    def buscaNomeFornecedor(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(Fornecedor).filter(
                Fornecedor.nome_fantasia == self.nomeFantasia).first()

            # Salvando resultado
            self.id = self.query.id
            self.nomeFantasia = self.query.nome_fantasia
            self.telefone = self.query.telefone

            # Fechando a Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
