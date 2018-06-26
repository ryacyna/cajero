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

def crearPersona(nom, ape, ed, dni, dom, co):
    cur.execute("INSERT INTO personas(nombre, apellido, edad, dni, domicilio, e_mail) VALUES (?,?,?,?,?,?)", (nom, ape, ed, dni, dom, co))

def obtenerIdPersona(dni):
    id_pers = cur.execute("SELECT id_persona from personas where dni=?", (dni))
    return id_pers

def crearCliente(idper, alta, suc):
    cur.execute("INSERT INTO clientes(idpersona, fec_alta, sucursal) VALUES (?,?,?)", (idper, alta, suc))

def obtenerIdCliente(id_persona):
    id_cli = cur.execute("SELECT idcliente from clientes where idpersona=?", (id_persona))
    return id_cli

def bajaCliente(baja, cliente):
    cur.execute("UPDATE clientes set fec_baja=? where idcliente=?", (baja, cliente)
    con.commit()
    #debe insertar fecha de baja en el campo fec_baja del registro de este cliente

def crearCuenta(cliente):
    cur.execute("INSERT INTO cuentas(idcliente, saldo) VALUES (?,?)", (cliente, 00,00))

def obtenerIdCuenta(cliente):
    id_cue = cur.execute("SELECT idcuenta from cuentas where idcliente=?", (cliente))
    return id_cue

def obtenerSaldo(cuenta):
    saldo = cur.execute("SELECT saldo from cuentas where idcuenta=?", (cuenta))
    return saldo

def actualizarSaldo(cuenta, monto):
    cur.execute("UPDATE cuentas set saldo = monto where idcuenta=?", (cuenta))

#Cerramos el archivo y la conexion a la bd
con.commit()
con.close()
