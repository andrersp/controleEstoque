# -*- codding: utf-8 -*-

from Crud.CrudStatusEntrega import CrudStatusEntrega
from Crud.CrudStatusPagamento import CrudStatusPagamento


def cb_statusPagamento(box):
    busca = CrudStatusPagamento()
    busca.listaStatusPagamento()
    box.addItem('AMBOS', '')

    i = 0
    for row in busca.statusPagamento:
        box.addItem(row, str(busca.id[i]))
        i += 1


def cb_statusEntrega(box):
    busca = CrudStatusEntrega()
    busca.listaStatusEntrega()
    box.addItem('AMBOS', '')
    i = 0
    for row in busca.statusEntrega:
        box.addItem(row, str(busca.id[i]))
        i += 1
