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

def crearRegistro(nom, ape, ed, dni, dom, co):
    cur.execute("INSERT INTO personas(nombre, apellido, edad, dni, domicilio, e_mail) VALUES (?,?,?,?,?,?)", (nom, ape, ed, dni, dom, co))
