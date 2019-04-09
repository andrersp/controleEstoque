# -*- coding: utf-8 -*-
from functools import partial


from Views.mainUsuario import Ui_ct_Usuario
from Views.formUsuario import Ui_ct_FormUsuario
from Funcoes.cb_nivel import cb_nivel
from Crud.CrudUsuarios import CrudUsuario


class Usuarios(Ui_ct_Usuario, Ui_ct_FormUsuario):

    # Janela Inicial usuarios / tabela de usuários
    def mainUsuario(self, frame):
        super(Usuarios, self).setMainUsuario(frame)
        self.fr_Usurio.show()

        # Icones dos Botoes
        self.IconeBotaoForm(self.bt_AddNovoUsuario,
                            self.resourcepath('Images/addUsuario.svg'))
        self.IconeBotaoMenu(self.bt_BuscaUsurio,
                            self.resourcepath('Images/search.png'))
        self.IconeBotaoMenu(self.bt_PrintRelatUsuario,
                            self.resourcepath('Images/gtk-print.png'))

        # Tamanho colunas tabela
        self.tb_Usuario.blockSignals(True)
        self.tb_Usuario.setColumnWidth(0, 40)
        self.tb_Usuario.setColumnWidth(1, 350)
        self.tb_Usuario.setColumnWidth(2, 190)
        self.tb_Usuario.setColumnWidth(3, 190)
        self.tb_Usuario.setColumnWidth(4, 120)
        self.tb_Usuario.setColumnWidth(5, 40)

        # Botao Novo usuario
        self.bt_AddNovoUsuario.clicked.connect(self.janelaFormUsuario)

        # chamando tabela usuario
        self.tabelaUsuarios()

    # Tabela Usuários
    def tabelaUsuarios(self):

        busca = CrudUsuario()
        busca.nome = self.tx_BuscarUsuario.text()
        busca.listaUsuarios()

        # limpando tabela
        while self.tb_Usuario.rowCount() > 0:
            self.tb_Usuario.removeRow(0)

        # populando tabela

        i = 0

        while i < len(busca.usuario):

            # inserindo linhas tabela
            self.tb_Usuario.insertRow(i)

            self.TabelaID(self.tb_Usuario, i, 0, busca.id[i])

            self.TabelaNomeTelefone(self.tb_Usuario, i, 1,
                                    busca.nome[i],
                                    busca.usuario[i])

            self.TabelaNomeTelefone(self.tb_Usuario, i, 2,
                                    self.formatoNumTelefone(
                                        busca.celular[i]),
                                    self.formatoNumTelefone(
                                        busca.telefone[i]))

            self.TabelaNomeTelefone(self.tb_Usuario, i, 3,
                                    busca.email[i], "")

            self.TabelaEntrega(self.tb_Usuario, i, 4,
                               busca.nivel[i],
                               self.StatusEntrega(
                                   busca.ativo[i]),
                               self.statusUsuario(busca.ativo[i]))

            # Sinal click tabela
            self.botaoTabela(self.tb_Usuario, i, 5, partial(
                self.selectUsuario, busca.id[i]), "#005099")

            i += 1

    # Selecionar usuario por id
    def selectUsuario(self, id):
        # Chamando Janela Form Usuário
        self.janelaFormUsuario()

        # Buscando no DB
        busca = CrudUsuario()
        busca.id = id
        busca.selectUserId()

        # Setando valores nos campos
        self.tx_id.setText(str(busca.id))
        self.tx_nome.setText(busca.nome)
        self.tx_cpf.setText(busca.cpf)
        self.tx_rg.setText(busca.rg)
        self.tx_Celular.setText(busca.celular)
        self.tx_Telefone.setText(busca.telefone)
        self.tx_Obs.setText(busca.obs)
        self.tx_cep.setText(busca.cep)
        self.tx_Endereco.setText(busca.endereco)
        self.tx_Num.setText(str(busca.num))
        self.tx_Bairro.setText(busca.bairro)
        self.tx_Cidade.setText(busca.cidade)
        self.tx_Estado.setText(busca.estado)
        self.tx_usuario.setText(busca.usuario)
        self.tx_senha.setText(busca.senha)
        self.tx_senha2.setText(busca.senha)
        self.cb_nivel.setCurrentIndex(self.cb_nivel.findData(busca.nivel))
        self.cb_ativo.setCurrentIndex(self.cb_ativo.findData(busca.ativo))

    def formUsuario(self, frame):
        super(Usuarios, self).setFormUsuario(frame)

        # populando combobox Nível de acess
        cb_nivel(self.cb_nivel)

        # populando Combobox Status
        self.cb_ativo.addItem('Ativo', str(1))
        self.cb_ativo.addItem('Inativo', str(2))

        # Exibindo Formulário
        self.fr_FormUsuario.show()

        # Checando se existe ID válido
        self.idCheckUser()

        # salvar
        self.bt_salvarUsuario.clicked.connect(self.validarUsuario)

        # Voltar
        self.bt_Voltar.clicked.connect(self.janelaUsuarios)

    # checando campo Id se é Edicao ou Novo Usuario

    def idCheckUser(self):
        if not self.tx_id.text():
            busca = CrudUsuario()
            self.tx_id.setText(str(busca.lastIdUser()))
        pass

    """
    Convertendo inteiro para texto status usuário
    1 = Ativo
    2 = Inativo
    """

    # validar Campos obrigátórios
    def validarUsuario(self):

        if not self.tx_nome.text():
            self.tx_nome.setFocus()
        elif not self.tx_usuario.text():
            self.tx_usuario.setFocus()
        elif not self.tx_senha.text():
            self.tx_senha.setFocus()
        elif not self.tx_senha2.text():
            self.tx_senha2.setFocus()
        elif self.tx_senha2.text() != self.tx_senha.text():
            self.tx_senha2.clear()
            self.tx_senha2.setPlaceholderText("As senhas não conferem")
            self.tx_senha2.setFocus()
        else:
            self.cadUsuario()

    # Cadastrando / Atualizando Usuario

    def cadUsuario(self):
        inseri = CrudUsuario()

        # Setando valores nas variaveis
        inseri.id = self.tx_id.text().upper()
        inseri.nome = self.tx_nome.text().upper()
        inseri.cpf = self.tx_cpf.text().upper()
        inseri.rg = self.tx_rg.text().upper()
        inseri.celular = self.tx_Celular.text().upper()
        inseri.telefone = self.tx_Telefone.text().upper()
        inseri.obs = self.tx_Obs.text().upper()
        inseri.cep = self.tx_cep.text().upper()
        inseri.endereco = self.tx_Endereco.text().upper()
        inseri.num = self.tx_Num.text().upper()
        inseri.bairro = self.tx_Bairro.text().upper()
        inseri.cidade = self.tx_Cidade.text().upper()
        inseri.estado = self.tx_Estado.text().upper()
        inseri.usuario = self.tx_usuario.text()
        inseri.senha = self.tx_senha.text()
        inseri.senha = self.tx_senha2.text()
        inseri.nivel = self.cb_nivel.currentData()
        inseri.ativo = self.cb_ativo.currentData()

        # Inserindo no DB
        inseri.inseriUser()

        # ALterando Nome de usuário caso o editor seja o mesmo logado
        if int(self.idUser) == int(inseri.id):
            self.lb_userName.setText(inseri.nome)

        # Se nivel for administrador redireciona pra tabela de usuários
        if int(self.userNivel) == 4:
            self.janelaUsuarios()
        else:
            # Redirecionando pra home
            self.index[self.userNivel]()

    def statusUsuario(self, arg):

        if arg == 1:
            status = "ATIVO"
        elif arg == 2:
            status = "INATIVO"

        return status
