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
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("INSERT INTO personas(nombre, apellido, edad, dni, domicilio, e_mail) VALUES (?,?,?,?,?,?)", (nom, ape, ed, dni, dom, co))
    con.commit()
    con.close()

def obtenerIdPersona(dni):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    id_pers = cur.execute("SELECT idpersona from personas where dni=?", (dni,))
    con.close()
    return id_pers

def imprimiRegistro():
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("SELECT * from personas")
    for registro in cur:
        for campo in registro:
            print (campo, '\n')
    con.close()


def crearCliente(idper, alta, suc):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("INSERT INTO clientes(idpersona, fec_alta, sucursal) VALUES (?,?,?)", (idper, alta, suc))
    con.commit()
    con.close()


def obtenerIdCliente(id_persona):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    id_cli = cur.execute("SELECT idcliente from clientes where idpersona=?", (id_persona,))
    con.close()
    return id_cli

def bajaCliente(baja, cliente):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("UPDATE clientes set fec_baja=? where idcliente=?", (baja, cliente,))
    #debe insertar fecha de baja en el campo fec_baja del registro de este cliente
    con.commit()
    con.close()

def crearCuenta(cliente):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("INSERT INTO cuentas(idcliente, saldo) VALUES (?,?)", (cliente, 00,00))
    con.commit()
    con.close()

def obtenerIdCuenta(cliente):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    id_cue = cur.execute("SELECT idcuenta from cuentas where idcliente=?", (cliente,))
    con.close()
    return id_cue

def obtenerSaldo(cuenta):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    saldo = cur.execute("SELECT saldo from cuentas where idcuenta=?", (cuenta,))
    con.close()
    return saldo

def actualizarSaldo(cuenta, monto):
    con = sqlite3.connect('Cajero.db')
    cur = con.cursor()
    cur.execute("UPDATE cuentas set saldo = monto where idcuenta=?", (cuenta,))
    con.commit()
    con.close()

#Cerramos el archivo y la conexion a la bd

imprimiRegistro()
con.commit()
con.close()
