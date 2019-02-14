# -*- coding: utf-8 -*-
from Crud.CrudClientes import CrudClientes


class Clientes(object):
    # AutoComplete Cliente
    def autocompleCliente(self):
        cliente = self.tx_NomeFantasia.text()
        busca = CrudClientes()
        busca.ListaClientesTabela(cliente)
        lista = busca.nomeCliente
        if cliente:
            self.model.setStringList(lista)

    # Busca cliente por nome
    def BuscaClienteNome(self, campoFoco):
        cliente = self.tx_NomeFantasia.text()
        busca = CrudClientes()
        busca.ListaClientesTabela(cliente)
        self.tx_Id.setText(str(busca.idCliente[0]))
        self.BuscaClienteId(campoFoco)

    # Busca cliente por ID
    def BuscaClienteId(self, campoFoco):
        id = int(self.tx_Id.text())
        busca = CrudClientes()
        busca.SelectClienteID(id)
        if busca.nomeCliente:
            self.tx_NomeFantasia.setText(busca.nomeCliente)
            self.TelefoneMask(busca.celularCliente)
            self.tx_Telefone.setText(busca.celularCliente)
            campoFoco.setFocus()
        else:
            self.tx_NomeFantasia.setText(
                "Cliente não encontrado")
            self.tx_Id.clear()
            self.tx_Id.setFocus()

    # Mascara Telefone
    def TelefoneMask(self, telefone):
        if len(telefone) == 11:
            self.tx_Telefone.setInputMask("(00) 00000-0000")
        else:
            self.tx_Telefone.setInputMask("(00) 0000-0000")
        pass
