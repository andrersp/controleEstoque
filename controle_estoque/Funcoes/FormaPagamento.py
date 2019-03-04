# -*- coding: utf-8 -*-
from Crud.CrudFormaPagamento import CrudFormaPagamento


class FormaPagamento(object):

    # Populando combobox forma de pagamento
    def CboxFPagamento(self, combobox):
        busca = CrudFormaPagamento()
        busca.listaFormaPagamento()
        combobox.clear()

        for lista in busca.query:
            combobox.addItem(lista.forma_pagamento, str(
                str(lista.id)))
