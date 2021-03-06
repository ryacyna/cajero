import sqlite3
import time
import os

con = sqlite3.connect('Cajero.db')

cur = con.cursor()

#Creamos la tabla si no existe
#The function can return any of the types supported by SQLite: unicode, str, int, long, float, buffer and None.
cur.execute("CREATE TABLE IF NOT EXISTS personas (idpersona  INTEGER PRIMARY KEY, nombre text, apellido text, edad int, dni int, domicilio text, e_mail text)")
cur.execute("CREATE TABLE IF NOT EXISTS clientes (idcliente  INTEGER PRIMARY KEY, idpersona int, fec_alta text, fec_baja text, sucursal int )")
cur.execute("CREATE TABLE IF NOT EXISTS cuentas  (idcuenta  INTEGER PRIMARY KEY, idcliente int, saldo float )")
cur.execute("CREATE TABLE IF NOT EXISTS movimientos  (idoperacion  INTEGER PRIMARY KEY, idcliente int, idcuenta int, operacion text, horaingreso date, monto float, estado text )")

#Cerramos el archivo y la conexion a la bd
con.commit()
con.close()

#crea un nuevo registro en personas
def crearPersona(nom, ape, ed, dni, dom, co):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("INSERT INTO personas(nombre, apellido, edad, dni, domicilio, e_mail) VALUES (?,?,?,?,?,?)", (nom, ape, ed, dni, dom, co))
    con.commit()
    con.close()

#devuelve el idpersona de la tabla personas cuyo campo dni coincida con el q se le pasa
def obtenerIdPersona(dni):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("SELECT idpersona from personas where dni=?", (dni,))
    id_persona = cur.fetchone()[0]
    con.close()
    return id_persona

#devuelve una tupla con un registro completo dado un dni
def obtenerPersona(dni):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("SELECT * from personas where dni=?", (dni,))
    persona = cur.fetchone()
    con.close()
    return persona

#crea un nuevo registro en clientes
def crearCliente(idper, alta, suc):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("INSERT INTO clientes(idpersona, fec_alta, sucursal) VALUES (?,?,?)", (idper, alta, suc))
    con.commit()
    con.close()

# devuelve el idcliente dado un idpersona
def obtenerIdCliente(id_persona):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("SELECT idcliente from clientes where idpersona=?", (id_persona,))
    id_cliente = cur.fetchone()[0]
    con.close()
    return id_cliente

#devuelve una tupla con el contenido de todos los campos de un registro de clientes dado en idPersona
def obtenerCliente(persona):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("SELECT * from clientes where idpersona=?", (persona,))
    cliente = cur.fetchone()
    con.close()
    return cliente

#agrega la fecha de baja en el campo baja dado un idcliente
def bajaCliente(baja, cliente):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("UPDATE clientes set fec_baja=? where idcliente=?", (baja, cliente,))
    #debe insertar fecha de baja en el campo fec_baja del registro de este cliente
    con.commit()
    con.close()

#crea un nuevo registro en clientes
def crearCuenta(cliente):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("INSERT INTO cuentas(idcliente, saldo) VALUES (?,?)", (cliente, 00))
    con.commit()
    con.close()

#devuelve el contendido dado un campo (string) y un idcliente
def obtenerDato(campo, tabla, campo_ref, valor_ref):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("SELECT {} from {} where {}={}".format(campo, tabla, campo_ref, valor_ref))
    dato = cur.fetchone()[0]
    con.close()
    return dato

#devuelve una tupla con el contenido de todos los campos de un registro de cuentas dato un idcliente
def obtenerCuenta(cliente):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("SELECT * from cuentas where idcliente=?", (cliente,))
    cuenta = cur.fetchone()
    con.close()
    return cuenta

#devuelve el saldo dado un idcuenta
def obtenerSaldo(cuenta):
    return obtenerDato('saldo', 'cuentas', 'idcuenta', cuenta)

#imprime todos los registros de la tabla
def listarTabla(tabla):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    for registro in cur.execute("SELECT * from {}".format(tabla)):
        print (registro)
    con.close()
