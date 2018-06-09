
import sqlite3
con = sqlite3.connect('Cajero.db')

cur = con.cursor()
 
#Creamos la tabla si no existe
cur.execute('''CREATE TABLE IF NOT EXISTS personas (idpersona int, nombre text, apellido text, edad int, dni int, domicilio text)''')
cur.execute('''CREATE TABLE IF NOT EXISTS clientes (idcliente int, idpersona int, fec_alta text, fec_baja text, sucursal int )''')
cur.execute('''CREATE TABLE IF NOT EXISTS cuentas  (idcuenta int, idcliente int, saldo float )''')




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
                      
