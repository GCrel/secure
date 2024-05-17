

#Modificar Segun se nesecite
BBDD_CONNECTION = "oracle+cx_oracle://seguridad:StrongPassword123#@bd2gcrel_high/?encoding=UTF-8&nencoding=UTF-8"

import cx_Oracle

d="C:\Program Files\Oracle\instantclient_19_22"
print(d)
cx_Oracle.init_oracle_client(lib_dir=d)
