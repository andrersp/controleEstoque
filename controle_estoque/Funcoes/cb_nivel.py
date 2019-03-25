# -*- coding: utf-8 -*-

from Crud.CrudNivel import CrudNivel


# Populando Combobox Nivel
def cb_nivel(campo):

    busca = CrudNivel()
    busca.listaNivel()

    i = 0

    for row in busca.nivel:
        campo.addItem(row, str(busca.id[i]))
        i += 1
