# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_


from Crud.core import Conexao
from Crud.Models import Usuarios


class Login(object):

    def __init__(self, usuario="", senha="", idUser="", nomeUser="", nivel="",
                 validar=""):

        self.usuario = usuario
        self.senha = senha
        self.idUser = idUser
        self.nomeUser = nomeUser
        self.nivel = nivel

    def logar(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            row = sessao.query(Usuarios).filter(
                and_(Usuarios.usuario == self.usuario,
                     Usuarios.senha == self.senha, Usuarios.ativo == 1)).first()

            if row:
                self.validar = True
                self.idUser = row.id
                self.usuario = row.usuario
                self.senha = row.senha
                self.nomeUser = row.nome
                self.nivel = row.nivel

            else:
                self.validar = False

            # Fechando Sessao
            sessao.close()

        except IntegrityError as err:
            print(err)
            pass

        return self.validar
