# -*- coding: utf-8 -*-
from sql.CrudFornecedor import CrudFornecedor


class Fornecedor(object):
    # AutoComplete Fornecedor
    def autocompleFornecedor(self):
        busca = CrudFornecedor()
        busca.nomeFantasia = self.tx_NomeFantasia.text()
        busca.autoCompleteFornecedor()
        lista = busca.nomeFantasia
        if busca.nomeFantasia:
            self.model.setStringList(lista)

    # Busca Fornecedor por nome
    def BuscaFornecedorNome(self, campoFoco):
        busca = CrudFornecedor()
        busca.nomeFantasia = self.tx_NomeFantasia.text()
        busca.listaFornecedor()
        self.tx_Id.setText(str(busca.id[0]))
        self.BuscaFornecedorId(campoFoco)

    # Busca Fornecedor por ID
    def BuscaFornecedorId(self, campoFoco):
        busca = CrudFornecedor()
        busca.id = int(self.tx_Id.text())
        busca.SelectFornecedorId()
        if busca.nomeFantasia:
            self.tx_NomeFantasia.setText(busca.nomeFantasia)
            self.TelefoneMask(busca.telefone)
            self.tx_Telefone.setText(busca.telefone)
            campoFoco.setFocus()
        else:
            self.tx_NomeFantasia.setText(
                "Cliente não encontrado")
            self.tx_Id.clear()
            self.tx_Id.setFocus()
