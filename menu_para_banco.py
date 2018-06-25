import os
from clientes import *
from cuentas import *
from Persona import *

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('clear') 
    print ("Selecciona una opción")
    print ("\t1 - Personas")
    print ("\t2 - Clientes")
    print ("\t3 - Cuentas")
    print ("\t4 - Movimientos")   
    print ("\t9 - salir")


while True:
    # Muestra el menu
    menu()

    # solicita una opción al usuario
    opcionMenu = int(input("inserta un numero valor >> "))

    if opcionMenu==1:
        alta_per()
    elif opcionMenu==2:
        alta_cli()
    elif opcionMenu==3:
        alta_cta()
    elif opcionMenu==4:
        alta_oper()
         
         
    elif opcionMenu==9:
        break
    else:
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
