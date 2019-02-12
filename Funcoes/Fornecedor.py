# -*- coding: utf-8 -*-
from PySide2 import QtGui, QtCore, QtWidgets
from Crud.CrudFornecedor import CrudFornecedor


class Fornecedor(object):
    # AutoComplete Fornecedor
    def autocompleFornecedor(self):
        fornecedor = self.tx_NomeFantasia.text()
        busca = CrudFornecedor()
        busca.ListaFornecedorTabela(fornecedor)
        lista = busca.NomeFantasia
        if fornecedor:
            self.model.setStringList(lista)

    # Busca Fornecedor por nome
    def BuscaFornecedorNome(self, campoFoco):
        cliente = self.tx_NomeFantasia.text()
        busca = CrudFornecedor()
        busca.ListaFornecedorTabela(cliente)
        self.tx_Id.setText(str(busca.idFornecedor[0]))
        self.BuscaFornecedorId(campoFoco)

    # Busca Fornecedor por ID
    def BuscaFornecedorId(self, campoFoco):
        id = int(self.tx_Id.text())
        busca = CrudFornecedor()
        busca.SelectFornecedorId(id)
        if busca.NomeFantasia:
            self.tx_NomeFantasia.setText(busca.NomeFantasia)
            self.tx_Telefone.setText(busca.telefone)
            campoFoco.setFocus()
        else:
            self.tx_NomeFantasia.setText(
                "Cliente não encontrado")
            self.tx_Id.clear()
            self.tx_Id.setFocus()
