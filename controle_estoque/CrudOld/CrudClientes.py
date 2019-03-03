# -*- coding: utf-8 -*-
import mysql.connector
from datetime import date

from Crud.conexao import Conexao


class CrudClientes(object):

    def __init__(self, idCliente="", nomeCliente="", apelidoCliente="",
                 cpfCliente="", rgCliente="", nascimentoCliente="",
                 celularCliente="", telefoneCliente="", emailCliente="",
                 obsCliente="", cepCliente="", enderecoCliente="",
                 numCliente="", bairroCliente="", cidadeCliente="",
                 estadoCliente="", dataEmissao="", dataEntrega="", Total="",
                 idPedido=""):
        self.idCliente = idCliente
        self.nomeCliente = nomeCliente
        self.apelidoCliente = apelidoCliente
        self.cpfCliente = cpfCliente
        self.rgCliente = rgCliente
        self.nascimentoCliente = nascimentoCliente
        self.celularCliente = celularCliente
        self.telefoneCliente = telefoneCliente
        self.emailCliente = emailCliente
        self.obsCliente = obsCliente
        self.cepCliente = cepCliente
        self.enderecoCliente = enderecoCliente
        self.numCliente = numCliente
        self.bairroCliente = bairroCliente
        self.cidadeCliente = cidadeCliente
        self.estadoCliente = estadoCliente
        self.dataEntrega = dataEntrega
        self.dataEmissao = dataEmissao
        self.Total = Total
        self.idPedido = idPedido

    def lastIDCliente(self):

        conecta = Conexao()
        c = conecta.conecta.cursor()
        try:
            c.execute("SELECT id FROM clientes ORDER BY id DESC LIMIT 1")
            row = c.fetchone()
            if row:
                self.idCliente = row[0] + 1
            else:
                self.idCliente = 1
            c.close()
        except mysql.connector.Error as err:
            print(err)
        return self.idCliente

    # Cadastro Clientes
    def CadCliente(self):
        conecta = Conexao()
        c = conecta.conecta.cursor()

        try:
            c.execute(""" INSERT INTO clientes VALUES ('{}', '{}', '{}', '{}',
        		'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
        		'{}', '{}') ON DUPLICATE KEY UPDATE nome='{}', apelido='{}',
        		cpf='{}', rg='{}', nascimento='{}', celular='{}',
        		telefone='{}', email='{}', obs='{}', cep='{}', endereco='{}',
        		num='{}', bairro='{}', cidade='{}', estado='{}' """
                      .format(self.idCliente, self.nomeCliente,
                              self.apelidoCliente, self.cpfCliente,
                              self.rgCliente, self.nascimentoCliente,
                              self.celularCliente, self.telefoneCliente,
                              self.emailCliente, self.obsCliente,
                              self.cepCliente, self.enderecoCliente,
                              self.numCliente, self.bairroCliente,
                              self.cidadeCliente, self.estadoCliente,
                              self.nomeCliente,
                              self.apelidoCliente, self.cpfCliente,
                              self.rgCliente, self.nascimentoCliente,
                              self.celularCliente, self.telefoneCliente,
                              self.emailCliente, self.obsCliente,
                              self.cepCliente, self.enderecoCliente,
                              self.numCliente, self.bairroCliente,
                              self.cidadeCliente, self.estadoCliente))
            conecta.conecta.commit()
            c.close()
        except mysql.connector.Error as err:
            print(err)

    def ListaClientesTabela(self, cliente):
        conecta = Conexao()
        c = conecta.conecta.cursor()
        self.idCliente = []
        self.nomeCliente = []
        self.apelidoCliente = []
        self.celularCliente = []
        self.telefoneCliente = []
        self.emailCliente = []

        try:
            c.execute(
                """ SELECT id, nome, apelido, celular, telefone, email
                FROM clientes WHERE nome LIKE '%{}%' """
                .format(cliente))
            row = c.fetchall()
            if row:
                for linha in row:
                    self.idCliente.append(linha[0])
                    self.nomeCliente.append(linha[1])
                    self.apelidoCliente.append(linha[2])
                    self.celularCliente.append(linha[3])
                    self.telefoneCliente.append(linha[4])
                    self.emailCliente.append(linha[5])
            c.close()
        except mysql.connector.Error as err:
            print(err)

    def SelectClienteID(self, id):
        conecta = Conexao()
        self.idCliente = id
        c = conecta.conecta.cursor()

        try:
            c.execute(
                """ SELECT * FROM clientes WHERE id='{}' """.format(self.idCliente))
            row = c.fetchone()
            if row:
                self.idCliente = row[0]
                self.nomeCliente = row[1]
                self.apelidoCliente = row[2]
                self.cpfCliente = row[3]
                self.rgCliente = row[4]
                self.nascimentoCliente = row[5]
                self.celularCliente = row[6]
                self.telefoneCliente = row[7]
                self.emailCliente = row[8]
                self.obsCliente = row[9]
                self.cepCliente = row[10]
                self.enderecoCliente = row[11]
                self.numCliente = row[12]
                self.bairroCliente = row[13]
                self.cidadeCliente = row[14]
                self.estadoCliente = row[15]

            c.execute(""" SELECT  id, dataEmissao, dataEntrega, valorTotal
                from pedidos WHERE clienteID='{}' AND statusEntrega=1 
                 """.format(self.idCliente))
            self.idPedido = []
            self.dataEmissao = []
            self.dataEntrega = []
            self.Total = []

            row = c.fetchall()
            for linha in row:
                self.idPedido.append(linha[0])
                self.dataEmissao.append(date.strftime(linha[1], "%d/%m/%Y"))
                self.dataEntrega.append(date.strftime(linha[2], "%d/%m/%Y"))
                self.Total.append(linha[3])
            c.close()

        except mysql.connector.Error as err:
            print(err)


# busca = CrudClientes()

# busca.SelectClienteID(1)
# print busca.Total
