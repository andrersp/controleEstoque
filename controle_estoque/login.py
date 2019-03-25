# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QPushButton


# View
from Views.login import Ui_ct_login

# Crud
from Crud.CrudLogin import Login


class MainLogin(Ui_ct_login):
    def mainlogin(self, frame):
        super(MainLogin, self).setLogin(frame)
        self.frame_login.show()

        # Foco Campos Usuário
        self.tx_user.setFocus()

        global grupo
        grupo = {0: {self.bt_Vendas, self.bt_Clientes},
                 1: {self.bt_Fornecedor,
                     self.bt_MainProdutos, self.bt_Compras},
                 2: {self.bt_Financeiro}, 3: {self.bt_Conf}}

        self.index = {1: self.janelaVendas, 2: self.janelaCompras,
                      3: self.janelaHome, 4: self.janelaHome}

        self.tx_user.returnPressed.connect(self.tx_senha.setFocus)
        self.tx_senha.returnPressed.connect(self.login)
        self.bt_login.clicked.connect(self.login)

    def login(self):

        login = Login()
        login.usuario = self.tx_user.text()
        login.senha = self.tx_senha.text()

        if login.logar():
            self.usuario = login.usuario
            self.senha = login.senha
            self.idUser = login.idUser
            self.userNivel = login.nivel

            # Setando nome de usuário logado
            self.lb_userName.setText(login.nomeUser)

            # habilitando botoes de acordo com nível
            for row in range(login.nivel):
                for filho in grupo[row]:
                    filho.setVisible(True)

            # Habilitando Botao meus dados e logout
            self.bt_alterSenha.setEnabled(True)
            self.bt_logout.setEnabled(True)

            # Se nivel for menor que 3 desabilita a home
            if self.userNivel < 3:
                self.bt_Home.setDisabled(True)
            else:
                self.bt_Home.setEnabled(True)

            # Redirecionando pra home
            self.index[login.nivel]()

        else:
            self.lb_alert.setText("Ops. Algo deu errado. Tente novamente")
