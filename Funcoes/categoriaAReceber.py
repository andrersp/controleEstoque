# -*- coding: utf-8 -*-
from Crud.CrudCategoriaAReceber import CrudCatAReceber


class CategoriaAReceber(object):

    # Populando combobox forma de pagamento
    def cboxCatAReceber(self, combobox):
        busca = CrudCatAReceber()
        busca.listaCatAReceber()
        combobox.clear()

        for i in range(len(busca.descCatAReceber)):
            combobox.addItem(busca.descCatAReceber[i], str(
                str(busca.idCatAReceber[i])))
