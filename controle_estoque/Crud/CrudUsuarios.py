# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from Crud.core import Conexao
from Crud.Models import Usuarios
from Crud.Models import Nivel


class CrudUsuario(object):

    def __init__(self, id="", nome="", cpf="", rg="", celular="", telefone="",
                 email="", obs="", cep="", endereco="", num="", bairro="",
                 cidade="", estado="", usuario="", senha="", nivel="",
                 ativo=""):

        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.celular = celular
        self.telefone = telefone
        self.email = email
        self.obs = obs
        self.cep = cep
        self.endereco = endereco
        self.num = num
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.usuario = usuario
        self.senha = senha
        self.nivel = nivel
        self.ativo = ativo

    def lastIdUser(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # query
            row = sessao.query(Usuarios).order_by(
                desc(Usuarios.id)).limit(1).first()

            # salvando resultado
            self.id = row.id + 1

            # Fechando Sessao
            sessao.close()

        except:
            self.id = 1

        return self.id

    # Cadastro Usuário
    def inseriUser(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = Usuarios(
                id=self.id,
                nome=self.nome,
                cpf=self.cpf,
                rg=self.rg,
                celular=self.celular,
                telefone=self.telefone,
                email=self.email,
                obs=self.obs,
                cep=self.cep,
                endereco=self.endereco,
                numero=self.num,
                bairro=self.bairro,
                cidade=self.cidade,
                estado=self.estado,
                usuario=self.usuario,
                senha=self.senha,
                nivel=self.nivel,
                ativo=self.ativo
            )

            # Add query na sessa
            sessao.add(row)

            # Executando Query
            sessao.commit()

            # fechando sessao
            sessao.close()

        except:
            self.updateUser()

    # Update Usuário
    def updateUser(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando a ID

            row = sessao.query(Usuarios).get(self.id)

            # Novos valores
            row.nome = self.nome
            row.cpf = self.cpf
            row.rg = self.rg
            row.celular = self.celular
            row.telefone = self.telefone
            row.email = self.email
            row.obs = self.obs
            row.cep = self.cep
            row.endereco = self.endereco
            row.numero = self.num
            row.bairro = self.bairro
            row.cidade = self.cidade
            row.estado = self.estado
            row.usuario = self.usuario
            row.senha = self.senha
            row.nivel = self.nivel
            row.ativo = self.ativo

            # Executando Query
            sessao.commit()

            # fechando sessao
            sessao.close()

        except:
            print("err")

    # Selecionar Usuário por id
    def selectUserId(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando a ID

            row = sessao.query(Usuarios).get(self.id)

            # Salvando Valores
            self.id = row.id
            self.nome = row.nome
            self.cpf = row.cpf
            self.rg = row.rg
            self.celular = row.celular
            self.telefone = row.telefone
            self.email = row.email
            self.obs = row.obs
            self.cep = row.cep
            self.endereco = row.endereco
            self.num = row.numero
            self.bairro = row.bairro
            self.cidade = row.cidade
            self.estado = row.estado
            self.usuario = row.usuario
            self.senha = row.senha
            self.nivel = row.nivel
            self.ativo = row.ativo

            # fechando sessao
            sessao.close()

        except:
            print("err")

    # Listando Usuário
    def listaUsuarios(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            query = (sessao.query(Usuarios.__table__,
                                  Nivel.nivel.label('acesso'))
                     .join(Nivel)
                     .filter(Usuarios.usuario.contains(self.nome))
                     .order_by(Usuarios.id)
                     )
            query.all()

            # Convertendo variavel em lista
            self.id = []
            self.nome = []
            self.celular = []
            self.telefone = []
            self.email = []
            self.usuario = []
            self.nivel = []
            self.ativo = []

            # Salvando Valores em suas listas
            for row in query:
                self.id.append(row.id)
                self.nome.append(row.nome)
                self.celular.append(row.celular)
                self.telefone.append(row.telefone)
                self.email.append(row.email)
                self.usuario.append(row.usuario)
                self.nivel.append(row.acesso)
                self.ativo.append(row.ativo)

            # Fechando a sessao
            sessao.close()

        except IntegrityError as err:
            print(err)
