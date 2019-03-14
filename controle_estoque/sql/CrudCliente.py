# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc


from sql.core import Conexao
from sql.Models import Cliente


class CrudCliente(object):

    def __init__(self, id="", nome="", sobrenome="", cpf="", rg="",
                 celular="", telefone="", email="", obs="", cep="",
                 endereco="", numero="", bairro="", cidade="", estado="",
                 dataEmissao="", dataEntrega="", Total="",
                 idPedido="", query=""):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.rg = rg
        self.celular = celular
        self.telefone = telefone
        self.email = email
        self.obs = obs
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.query = query

    # Recebendo última id inserido

    def lastIdCliente(self):
        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            ultimo = sessao.query(Cliente).order_by(
                desc(Cliente.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando Conexao
            sessao.close()

            pass

        except:

            self.id = 1

        return self.id

    #  Cadastro Cliente
    def inseriCliente(self):

        try:

            # Abrindo a sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = Cliente(
                id=self.id,
                nome=self.nome,
                sobrenome=self.sobrenome,
                cpf=self.cpf,
                rg=self.rg,
                celular=self.celular,
                telefone=self.telefone,
                email=self.email,
                obs=self.obs,
                cep=self.cep,
                endereco=self.endereco,
                numero=self.numero,
                bairro=self.bairro,
                cidade=self.cidade,
                estado=self.estado
            )

            # Execurando a Query
            sessao.add(row)
            sessao.commit()

            # Fechando a Sesao
            sessao.close()

            pass

        except IntegrityError:

            self.updateCliente()

            pass

    #  Update Cliente
    def updateCliente(self):

        try:

            # Abrindo a sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando id
            query = sessao.query(Cliente).get(self.id)

            # Novos valores
            query.nome = self.nome
            query.sobrenome = self.sobrenome
            query.cpf = self.cpf
            query.rg = self.rg
            query.celular = self.celular
            query.telefone = self.telefone
            query.email = self.email
            query.obs = self.obs
            query.cep = self.cep
            query.endereco = self.endereco
            query.numero = self.numero
            query.bairro = self.bairro
            query.cidade = self.cidade
            query.estado = self.estado

            # Execurando a Query
            sessao.commit()

            # Fechando a Sesao
            sessao.close()

            pass

        except IntegrityError as err:

            print(err)

            pass

    # Buscando cliente por ID
    def selectClienteId(self):
        try:
            conecta = Conexao()
            conecta.sessao = Session()

            # Query
            busca = sessao.query(Cliente).get(self.id)

            # Salvando resultado da Query
            self.id = busca.id
            self.nome = busca.nome
            self.sobrenome = busca.sobrenome
            self.cpf = busca.cpf
            self.rg = busca.rg
            self.celular = busca.celular
            self.telefone = busca.telefone
            self.email = busca.email
            self.obs = busca.obs
            self.cep = busca.cep
            self.endereco = busca.endereco
            self.numero = busca.numero
            self.bairro = busca.bairro
            self.cidade = busca.cidade
            self.estado = busca.estado

            # Fechando Conexao
            sessao.close()

            pass

        except:

            pass

        pass

    # Buscando Cliente por nome
    def listaCliente(self):

        try:
            conecta = Conexao()

            sessao = conecta.Session()

            # Query
            query = sessao.query(Cliente).filter(
                Cliente.nome.like('%{}%'.format(self.nome)))
            query.all()

            # # Convertendo variaveis em lista
            self.id = []
            self.nome = []
            self.sobrenome = []
            self.celular = []
            self.telefone = []
            self.email = []

            # # Salvando resultado da query e suas listas
            for row in query:
                self.id.append(row.id)
                self.nome.append(row.nome)
                self.sobrenome.append(row.sobrenome)
                self.celular.append(row.celular)
                self.telefone.append(row.telefone)
                self.email.append(row.email)

            # fechando a conexao
            sessao.close()

            pass

        except IntegrityError as err:

            print(err)

            pass

    # Lista AutoComplete Cliente

    def autoCompleteCliente(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(Cliente).filter(
                Cliente.nome.like('%{}%'.format(self.nome)))
            self.query.all()

            # Convertendo variavel em lista
            self.nome = []

            # salvando resultado em lista
            for row in self.query:
                self.nome.append(row.nome)

            # Fechando Conexao
            sessao.close()

            pass

        except IntegrityError as err:

            print(err)

            pass

    # Busca CLiente por nome
    def buscaClienteNome(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(Cliente).filter(
                Cliente.nome == self.nome).first()

            # Salvando Resultado
            self.id = self.query.id
            self.nome = self.query.nome
            self.celular = self.query.celular

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
