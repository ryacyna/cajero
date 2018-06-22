import sqlite3
import time 
import os


while True:
    line = input("Cargar datos de CLIENTES. Pulse 'S' para salir")
    if line == "S" or line == "s":
        break

  
    # es una modificacion
    nom = input(" : ")
    ape = input(" : ")
    ed  = input(" : ")
    dom = input(" : ")
            
    sn  = input('Confirma los datos (S ó N) ?')
    
                

con.commit()
con.close()
                      
