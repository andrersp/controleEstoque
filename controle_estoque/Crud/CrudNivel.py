# -*- coding: utf-8 -*-

from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError

from Crud.core import Conexao
from Crud.Models import Nivel


class CrudNivel(object):

    def __init__(self, id="", nivel=""):
        self.id = id
        self.nivel = nivel

    def listaNivel(self):

        try:

            # Abrindo a sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            query = sessao.query(Nivel).all()

            # Convertendo variaveis em lista
            self.id = []
            self.nivel = []

            # Salvando resultado

            for row in query:
                self.id.append(row.id)
                self.nivel.append(row.nivel)

        except IntegrityError as err:
            print(err)
