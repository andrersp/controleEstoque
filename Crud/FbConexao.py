# -*- coding: utf-8 -*-

import fdb

con = fdb.connect(dsn='/Files/Python/Software/Crud/sistema.fdb',
                  user='SYSDBA', password='rsp')
cur = con.cursor()

# cur.execute(
#     """ INSERT INTO clientes values('1','andre Luis', 'rsp', '125', '22467',
#     '1986-12-30', '99706916', '2722', 'rspassis', '', '', '', '','', '', '')""")
cur.execute("""  SELECT * FROM clientes """)

row = cur.fetchall()
print(row)
