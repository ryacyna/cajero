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


buffer = ""


while True:
    line = input("Altas: A, Modificaciones:M, S:Salir")
    if line == "S" or line == "s":
        break

    #preguntar si es A o M, para ver que hace
    dni = input("      DNI: ")

    _t=(dni,)
    cur.execute("select nombre, apellido, domicilio, e_mail from personas where dni=?", _t )
  
    resultado = cur.fetchone()
    #if resultado is None:
    # o   data=cursor.fetchall()
    # if len(data)==0:
        
    for i in resultado:
        print ("%s %s %s %s" % (i[0],i[1],i[2],i[3]))

    
    nom = input("   Nombre: ")
    ape = input(" Apellido: ")
    ed  = input("     Edad: ")
    dom = input("Domicilio: ")
    co  = input("   Correo: ")
    sn  = input('Confirma los datos (S ó N) ?')
    if sn=='S' or sn=='s':
        cur.execute("INSERT INTO personas(nombre, apellido, edad, dni, domicilio, e_mail) VALUES (?,?,?,?,?,?)", (nom, ape, ed, dni, dom, co) )
    
    
                


#cur.execute("SELECT * FROM personas")
#resultado = cur.fetchall()
#for i in resultado:
#    print ("%s %s %s %s" % (i[0],i[1],i[2],i[3]))
#for row in cur.execute('SELECT * FROM personas'):
#    print(row)    
#Llenamos la BD con los datos del CSV
#for row in reader:
#    cur.execute("INSERT INTO posiciones VALUES (?, ?, ?, ?)", (row[0], row[1], row[2], row[3]))
# ver  con.total_changes
#Muestro las filas guardadas en la tabla
#for row in cur.execute('SELECT * FROM posiciones'):
#    print(row)

 
#Cerramos el archivo y la conexion a la bd
con.commit()
con.close()
                      
