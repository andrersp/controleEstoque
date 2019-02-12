# -*- coding: utf-8 -*-

import fdb

# con = fdb.connect(dsn='/var/lib/firebird/3.0/system/sistema.fdb',
#                   user='SYSDBA', password='rsp')
# cur = con.cursor()

# # cur.execute(
# #     """ INSERT INTO clientes values('1','andre Luis', 'rsp', '125', '22467',
# #     '1986-12-30', '99706916', '2722', 'rspassis', '', '', '', '','', '', '')""")
# cur.execute("""  SELECT * FROM produtos """)

# row = cur.fetchall()
# print(row)


class Conexao(object):
    """docstring for ClassName"""

    def __init__(self, DbHost="", DbName="", DbUser="", DbPassword="", conecta="", erro=""):
        # self.DbHost = DbHost
        # self.DbName = DbName
        # self.DbUser = DbUser
        # self.DbPassword = DbPassword
        # self.conecta = conecta
        # self.erro = erro
        # # self.path = os.path.dirname(os.path.abspath(__file__))
        # self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        # config = configparser.ConfigParser()
        # config.sections()

        # if config.read(os.path.join(self.path, 'config.ini')):
        #     self.DbHost = config['DEFAULT']['DbHost']
        #     self.DbName = config['DEFAULT']['DbName']
        #     self.DbUser = config['DEFAULT']['DbUser']
        #     self.DbPassword = config['DEFAULT']['DbPassword']

        try:
            self.conecta = fdb.connect(dsn='/var/lib/firebird/3.0/system/sistema.fdb',
                                       user='SYSDBA', password='rsp')
            c = self.conecta.cursor()
            c.close()
        except fdb.Error as err:
            print(err)


# busca = Conexao()
# c = busca.conecta.cursor()
# c.execute(""" SELECT * FROM produtos WHERE descricao LIKE '%{}%'""".format('ca'))
# row = c.fetchall()
# for lista in row:
#     print(lista[1])
