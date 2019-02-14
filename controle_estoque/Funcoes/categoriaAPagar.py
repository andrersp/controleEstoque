# -*- coding: utf-8 -*-
from Crud.CrudCategoriaAPagar import CrudCatAPagar


class CategoriaAPagar(object):

    # Populando combobox forma de pagamento
    def cboxCatAPagar(self, combobox):
        busca = CrudCatAPagar()
        busca.listaCatAPagar()
        combobox.clear()

        for i in range(len(busca.descCatAPagar)):
            combobox.addItem(busca.descCatAPagar[i], str(
                str(busca.idCatAPagar[i])))
