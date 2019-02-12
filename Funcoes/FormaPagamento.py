# -*- coding: utf-8 -*-
from Crud.CrudFormaPagamento import CrudFormaPagamento


class FormaPagamento(object):

    # Populando combobox forma de pagamento
    def CboxFPagamento(self, combobox):
        busca = CrudFormaPagamento()
        busca.listaFPagamento()
        combobox.clear()

        for i in range(len(busca.descFPagamento)):
            combobox.addItem(busca.descFPagamento[i], str(
                str(busca.idFPagamento[i])))
