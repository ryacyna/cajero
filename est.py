import sqlite3
import time 
import os

con = sqlite3.connect('est.sqlite')

cur = con.cursor()
 
cur.execute("select * from estados" )
resultado = cur.fetchone()


for i in resultado:
    print ("%s %s %s %s" % (i[0],i[1],i[2],i[3]))


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
                      
