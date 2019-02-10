# -*- coding: utf-8 -*-


class Teste(object):
    def setnome(self, nome, **kwargs):
        nomee = nome
        if 'funcao' in kwargs:
            print(kwargs['funcao'])

        return kwargs['cliente']

    def nada(self):
        print("Nada")


busca = Teste()
busca.setnome("andre Luis", sobrenome="teste",
              cliente="Azul e Rosa", funcao='teste')
