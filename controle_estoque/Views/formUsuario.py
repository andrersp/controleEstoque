# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formUsuario.ui',
# licensing of 'formUsuario.ui' applies.
#
# Created: Fri Mar 22 14:46:35 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ct_FormUsuario(object):
    def setFormUsuario(self, ct_FormUsuario):
        ct_FormUsuario.setObjectName("ct_FormUsuario")
        ct_FormUsuario.resize(1000, 500)
        ct_FormUsuario.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormUsuario = QtWidgets.QFrame(ct_FormUsuario)
        self.fr_FormUsuario.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormUsuario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_FormUsuario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormUsuario.setObjectName("fr_FormUsuario")
        self.lb_FormUsuario_21 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_21.setGeometry(QtCore.QRect(670, 60, 150, 20))
        self.lb_FormUsuario_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_21.setObjectName("lb_FormUsuario_21")
        self.tx_Celular = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Celular.setGeometry(QtCore.QRect(20, 205, 196, 25))
        self.tx_Celular.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Celular.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Celular.setPlaceholderText("")
        self.tx_Celular.setObjectName("tx_Celular")
        self.lb_FormUsuario_27 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_27.setGeometry(QtCore.QRect(580, 335, 50, 20))
        self.lb_FormUsuario_27.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_27.setObjectName("lb_FormUsuario_27")
        self.lb_FormUsuario_28 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_28.setGeometry(QtCore.QRect(20, 335, 50, 20))
        self.lb_FormUsuario_28.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_28.setObjectName("lb_FormUsuario_28")
        self.lb_FormUsuario_23 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_23.setGeometry(QtCore.QRect(670, 120, 150, 20))
        self.lb_FormUsuario_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_23.setObjectName("lb_FormUsuario_23")
        self.lb_FormUsuario_20 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_20.setGeometry(QtCore.QRect(20, 390, 120, 20))
        self.lb_FormUsuario_20.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_20.setObjectName("lb_FormUsuario_20")
        self.lb_FormUsuario_17 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_17.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.lb_FormUsuario_17.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_17.setObjectName("lb_FormUsuario_17")
        self.bt_BuscaCep = QtWidgets.QPushButton(self.fr_FormUsuario)
        self.bt_BuscaCep.setGeometry(QtCore.QRect(120, 360, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.bt_BuscaCep.setFont(font)
        self.bt_BuscaCep.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_BuscaCep.setText("")
        self.bt_BuscaCep.setObjectName("bt_BuscaCep")
        self.tx_rg = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_rg.setGeometry(QtCore.QRect(236, 145, 196, 25))
        self.tx_rg.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_rg.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_rg.setPlaceholderText("")
        self.tx_rg.setObjectName("tx_rg")
        self.lb_FormUsuario_26 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_26.setGeometry(QtCore.QRect(300, 390, 120, 20))
        self.lb_FormUsuario_26.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_26.setObjectName("lb_FormUsuario_26")
        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Telefone.setGeometry(QtCore.QRect(236, 205, 196, 25))
        self.tx_Telefone.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Telefone.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Telefone.setPlaceholderText("")
        self.tx_Telefone.setObjectName("tx_Telefone")
        self.lb_FormUsuario_30 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_30.setGeometry(QtCore.QRect(236, 180, 190, 20))
        self.lb_FormUsuario_30.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_30.setObjectName("lb_FormUsuario_30")
        self.lb_FormUsuario_16 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_16.setGeometry(QtCore.QRect(580, 390, 70, 20))
        self.lb_FormUsuario_16.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_16.setObjectName("lb_FormUsuario_16")
        self.lb_FormUsuario_6 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_6.setGeometry(QtCore.QRect(236, 120, 190, 20))
        self.lb_FormUsuario_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_6.setObjectName("lb_FormUsuario_6")
        self.tx_Bairro = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Bairro.setGeometry(QtCore.QRect(20, 415, 260, 25))
        self.tx_Bairro.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Bairro.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Bairro.setInputMask("")
        self.tx_Bairro.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Bairro.setPlaceholderText("")
        self.tx_Bairro.setObjectName("tx_Bairro")
        self.tx_Estado = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Estado.setGeometry(QtCore.QRect(580, 415, 70, 25))
        self.tx_Estado.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Estado.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Estado.setInputMask("")
        self.tx_Estado.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Estado.setPlaceholderText("")
        self.tx_Estado.setObjectName("tx_Estado")
        self.tx_cpf = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_cpf.setGeometry(QtCore.QRect(20, 145, 196, 25))
        self.tx_cpf.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cpf.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cpf.setPlaceholderText("")
        self.tx_cpf.setObjectName("tx_cpf")
        self.tx_Num = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Num.setGeometry(QtCore.QRect(580, 360, 70, 25))
        self.tx_Num.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Num.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Num.setInputMask("")
        self.tx_Num.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Num.setPlaceholderText("")
        self.tx_Num.setObjectName("tx_Num")
        self.lb_FormUsuario = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario.setGeometry(QtCore.QRect(100, 10, 880, 30))
        self.lb_FormUsuario.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormUsuario.setObjectName("lb_FormUsuario")
        self.lb_FormUsuario_25 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_25.setGeometry(QtCore.QRect(452, 180, 190, 20))
        self.lb_FormUsuario_25.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_25.setObjectName("lb_FormUsuario_25")
        self.tx_Cidade = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Cidade.setGeometry(QtCore.QRect(300, 415, 260, 25))
        self.tx_Cidade.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Cidade.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Cidade.setInputMask("")
        self.tx_Cidade.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Cidade.setPlaceholderText("")
        self.tx_Cidade.setObjectName("tx_Cidade")
        self.tx_senha = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_senha.setGeometry(QtCore.QRect(670, 145, 300, 25))
        self.tx_senha.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_senha.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_senha.setObjectName("tx_senha")
        self.frame = QtWidgets.QFrame(self.fr_FormUsuario)
        self.frame.setGeometry(QtCore.QRect(0, 460, 1000, 40))
        self.frame.setStyleSheet("border-bottom: 2px solid #CCC;\n"
"background: #F7F7F7")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_salvarUsuario = QtWidgets.QPushButton(self.frame)
        self.bt_salvarUsuario.setGeometry(QtCore.QRect(750, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_salvarUsuario.setFont(font)
        self.bt_salvarUsuario.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_salvarUsuario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_salvarUsuario.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_salvarUsuario.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_salvarUsuario.setIconSize(QtCore.QSize(75, 35))
        self.bt_salvarUsuario.setObjectName("bt_salvarUsuario")
        self.bt_Voltar = QtWidgets.QPushButton(self.frame)
        self.bt_Voltar.setGeometry(QtCore.QRect(880, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.bt_Voltar.setFont(font)
        self.bt_Voltar.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Voltar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Voltar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Voltar.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_Voltar.setIconSize(QtCore.QSize(75, 35))
        self.bt_Voltar.setObjectName("bt_Voltar")
        self.tx_cep = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_cep.setGeometry(QtCore.QRect(20, 360, 100, 25))
        self.tx_cep.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cep.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cep.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_cep.setObjectName("tx_cep")
        self.tx_usuario = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_usuario.setGeometry(QtCore.QRect(670, 85, 300, 25))
        self.tx_usuario.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_usuario.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_usuario.setObjectName("tx_usuario")
        self.lb_FormUsuario_29 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_29.setGeometry(QtCore.QRect(160, 335, 250, 20))
        self.lb_FormUsuario_29.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_29.setObjectName("lb_FormUsuario_29")
        self.lb_FormUsuario_9 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_9.setGeometry(QtCore.QRect(20, 180, 196, 20))
        self.lb_FormUsuario_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_9.setObjectName("lb_FormUsuario_9")
        self.tx_Endereco = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Endereco.setGeometry(QtCore.QRect(160, 360, 400, 25))
        self.tx_Endereco.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Endereco.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Endereco.setInputMask("")
        self.tx_Endereco.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Endereco.setPlaceholderText("")
        self.tx_Endereco.setObjectName("tx_Endereco")
        self.tx_Email = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Email.setGeometry(QtCore.QRect(452, 205, 196, 25))
        self.tx_Email.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Email.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Email.setPlaceholderText("")
        self.tx_Email.setObjectName("tx_Email")
        self.lb_FormUsuario_18 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_18.setGeometry(QtCore.QRect(20, 120, 190, 20))
        self.lb_FormUsuario_18.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_18.setObjectName("lb_FormUsuario_18")
        self.lb_FormUsuario_31 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_31.setGeometry(QtCore.QRect(20, 290, 630, 30))
        self.lb_FormUsuario_31.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_31.setObjectName("lb_FormUsuario_31")
        self.lb_FormUsuario_19 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_19.setGeometry(QtCore.QRect(20, 235, 150, 20))
        self.lb_FormUsuario_19.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_19.setObjectName("lb_FormUsuario_19")
        self.tx_nome = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_nome.setGeometry(QtCore.QRect(20, 85, 630, 25))
        self.tx_nome.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_nome.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_nome.setObjectName("tx_nome")
        self.tx_id = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_id.setEnabled(False)
        self.tx_id.setGeometry(QtCore.QRect(20, 10, 50, 30))
        self.tx_id.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border: 1px solid #A2A2A2;\n"
"color: #000;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.tx_id.setText("")
        self.tx_id.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_id.setObjectName("tx_id")
        self.tx_Obs = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Obs.setGeometry(QtCore.QRect(20, 260, 630, 25))
        self.tx_Obs.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Obs.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Obs.setObjectName("tx_Obs")
        self.tx_senha2 = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_senha2.setGeometry(QtCore.QRect(670, 205, 300, 25))
        self.tx_senha2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_senha2.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_senha2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_senha2.setObjectName("tx_senha2")
        self.lb_FormUsuario_24 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_24.setGeometry(QtCore.QRect(670, 180, 271, 20))
        self.lb_FormUsuario_24.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_24.setObjectName("lb_FormUsuario_24")
        self.lb_FormUsuario_32 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_32.setGeometry(QtCore.QRect(670, 240, 271, 20))
        self.lb_FormUsuario_32.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_32.setObjectName("lb_FormUsuario_32")
        self.cb_nivel = QtWidgets.QComboBox(self.fr_FormUsuario)
        self.cb_nivel.setGeometry(QtCore.QRect(670, 265, 300, 25))
        self.cb_nivel.setStyleSheet("QComboBox{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url("+self.resourcepath('Images/down.png')+");\n"
" }\n"
"")
        self.cb_nivel.setObjectName("cb_nivel")
        self.cb_ativo = QtWidgets.QComboBox(self.fr_FormUsuario)
        self.cb_ativo.setGeometry(QtCore.QRect(670, 325, 300, 27))
        self.cb_ativo.setStyleSheet("QComboBox{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url("+self.resourcepath('Images/down.png')+");\n"
" }\n"
"")
        self.cb_ativo.setObjectName("cb_ativo")
        self.lb_FormUsuario_33 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormUsuario_33.setGeometry(QtCore.QRect(670, 300, 271, 20))
        self.lb_FormUsuario_33.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormUsuario_33.setObjectName("lb_FormUsuario_33")

        self.tradFormUsuario(ct_FormUsuario)
        QtCore.QMetaObject.connectSlotsByName(ct_FormUsuario)
        ct_FormUsuario.setTabOrder(self.tx_id, self.tx_nome)
        ct_FormUsuario.setTabOrder(self.tx_nome, self.tx_cpf)
        ct_FormUsuario.setTabOrder(self.tx_cpf, self.tx_rg)
        ct_FormUsuario.setTabOrder(self.tx_rg, self.tx_Celular)
        ct_FormUsuario.setTabOrder(self.tx_Celular, self.tx_Telefone)
        ct_FormUsuario.setTabOrder(self.tx_Telefone, self.tx_Email)
        ct_FormUsuario.setTabOrder(self.tx_Email, self.tx_Obs)
        ct_FormUsuario.setTabOrder(self.tx_Obs, self.tx_cep)
        ct_FormUsuario.setTabOrder(self.tx_cep, self.bt_BuscaCep)
        ct_FormUsuario.setTabOrder(self.bt_BuscaCep, self.tx_Endereco)
        ct_FormUsuario.setTabOrder(self.tx_Endereco, self.tx_Num)
        ct_FormUsuario.setTabOrder(self.tx_Num, self.tx_Bairro)
        ct_FormUsuario.setTabOrder(self.tx_Bairro, self.tx_Cidade)
        ct_FormUsuario.setTabOrder(self.tx_Cidade, self.tx_Estado)
        ct_FormUsuario.setTabOrder(self.tx_Estado, self.tx_usuario)
        ct_FormUsuario.setTabOrder(self.tx_usuario, self.tx_senha)

    def tradFormUsuario(self, ct_FormUsuario):
        ct_FormUsuario.setWindowTitle(QtWidgets.QApplication.translate("ct_FormUsuario", "Frame", None, -1))
        self.lb_FormUsuario_21.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "USUÁRIO", None, -1))
        self.tx_Celular.setInputMask(QtWidgets.QApplication.translate("ct_FormUsuario", "(00) 00000-0000", None, -1))
        self.tx_Celular.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "() -", None, -1))
        self.lb_FormUsuario_27.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "Nº", None, -1))
        self.lb_FormUsuario_28.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "CEP", None, -1))
        self.lb_FormUsuario_23.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "SENHA", None, -1))
        self.lb_FormUsuario_20.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "BAIRRO", None, -1))
        self.lb_FormUsuario_17.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "NOME COMPLETO", None, -1))
        self.tx_rg.setInputMask(QtWidgets.QApplication.translate("ct_FormUsuario", "00.000.000-0", None, -1))
        self.lb_FormUsuario_26.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "CIDADE", None, -1))
        self.tx_Telefone.setInputMask(QtWidgets.QApplication.translate("ct_FormUsuario", "(00) 0000-0000", None, -1))
        self.lb_FormUsuario_30.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "TELEFONE", None, -1))
        self.lb_FormUsuario_16.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "ESTADO", None, -1))
        self.lb_FormUsuario_6.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "RG", None, -1))
        self.tx_cpf.setInputMask(QtWidgets.QApplication.translate("ct_FormUsuario", "000.000.000-00", None, -1))
        self.tx_cpf.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "..-", None, -1))
        self.lb_FormUsuario.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "CADASTRO DE USUÁRIO", None, -1))
        self.lb_FormUsuario_25.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "Email", None, -1))
        self.tx_senha.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormUsuario", "Senha", None, -1))
        self.bt_salvarUsuario.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "SALVAR", None, -1))
        self.bt_Voltar.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "VOLTAR", None, -1))
        self.tx_cep.setInputMask(QtWidgets.QApplication.translate("ct_FormUsuario", "99999-999", None, -1))
        self.tx_cep.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormUsuario", "123456789", None, -1))
        self.tx_usuario.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormUsuario", "Usuário", None, -1))
        self.lb_FormUsuario_29.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "ENDEREÇO", None, -1))
        self.lb_FormUsuario_9.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "CELULAR", None, -1))
        self.lb_FormUsuario_18.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "CPF", None, -1))
        self.lb_FormUsuario_31.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "ENDEREÇO", None, -1))
        self.lb_FormUsuario_19.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "OBSERVAÇÃO", None, -1))
        self.tx_nome.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormUsuario", "nome completo", None, -1))
        self.tx_Obs.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormUsuario", "Observação", None, -1))
        self.tx_senha2.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormUsuario", "Digite sua senha novamente", None, -1))
        self.lb_FormUsuario_24.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "DIGITE A SENHA NOVAMENTE", None, -1))
        self.lb_FormUsuario_32.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "NÍVEL DE ACESSO", None, -1))
        self.lb_FormUsuario_33.setText(QtWidgets.QApplication.translate("ct_FormUsuario", "STATUS", None, -1))

