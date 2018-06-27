import sqlite3
import time
import os

con = sqlite3.connect('Cajero.odb')

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
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    cur.execute("INSERT INTO personas(nombre, apellido, edad, dni, domicilio, e_mail) VALUES (?,?,?,?,?,?)", (nom, ape, ed, dni, dom, co))
    con.commit()
    con.close()

#devuelve el idpersona de la tabla personas cuyo campo dni coincida con el q se le pasa
def obtenerIdPersona(dni):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    for i in cur.execute("SELECT idpersona from personas where dni=?", (dni,)):
        id_persona = i[0]
    con.close()
    return id_persona

#imprime todos los registros de la tabla personas
def imprimirPersonas():
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    for registro in cur.execute("SELECT * from personas"): #=?", (tabla,)):
        print (registro)
    con.close()

#devuelve una tupla con un registro completo dado un dni
def obtenerPersona(dni):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    cur.execute("SELECT * from personas where dni=?", (dni,))
    persona = cur.fetchone()
    con.close()
    return persona

#crea un nuevo registro en clientes
def crearCliente(idper, alta, suc):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    cur.execute("INSERT INTO clientes(idpersona, fec_alta, sucursal) VALUES (?,?,?)", (idper, alta, suc))
    con.commit()
    con.close()

# devuelve el idcliente dado un idpersona
def obtenerIdCliente(id_persona):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    for i in cur.execute("SELECT idcliente from clientes where idpersona=?", (id_persona,)):
        id_cliente = i[0]
    con.close()
    return id_cliente

#agrega la fecha de baja en el campo baja dado un idcliente
def bajaCliente(baja, cliente):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    cur.execute("UPDATE clientes set fec_baja=? where idcliente=?", (baja, cliente,))
    #debe insertar fecha de baja en el campo fec_baja del registro de este cliente
    con.commit()
    con.close()

#crea un nuevo registro en clientes
def crearCuenta(cliente):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    cur.execute("INSERT INTO cuentas(idcliente, saldo) VALUES (?,?)", (cliente, 00))
    con.commit()
    con.close()

#devuelve el contendido dado un campo y un idcliente
def obtenerDatoCuenta(campo, cliente):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    for i in cur.execute("SELECT campo=? from cuentas where idcliente=?", (campo, cliente)):
        dato = i[0]
    con.close()
    return dato

#devuelve una tupla con el contenido de todos los campos de un registro de cuentas dato un idcliente
def obtenerCuenta(cliente):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    cur.execute("SELECT * from cuentas where idcliente=?", (cliente,))
    cuenta = cur.fetchone()
    con.close()
    return cuenta

#devuelve el saldo dado un idcuenta
def obtenerSaldo(cuenta):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    for i in cur.execute("SELECT saldo from cuentas where idcuenta=?", (cuenta,)):
        saldo = i[0]
    con.close()
    return saldo

#actualiza el saldo dado un idcuenta
def actualizarSaldo(cuenta, monto):
    con = sqlite3.connect('Cajero.odb')
    cur = con.cursor()
    cur.execute("UPDATE cuentas set saldo=? where idcuenta=?", (monto, cuenta))
    con.commit()
    con.close()
