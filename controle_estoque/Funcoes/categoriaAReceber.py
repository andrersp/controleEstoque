# -*- coding: utf-8 -*-
from orm.CrudCatAReceber import CrudCatAReceber


class CategoriaAReceber(object):

    # Populando combobox forma de pagamento
    def cboxCatAReceber(self, combobox):
        busca = CrudCatAReceber()
        busca.listaCatAReceber()
        combobox.clear()

        for i in range(len(busca.categoriaReceber)):
            combobox.addItem(busca.categoriaReceber[i], str(
                str(busca.id[i])))
