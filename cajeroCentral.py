from clases import *
from menu_para_banco import menu
import os


while True:
    # Muestra el menu y solicita una opción al usuario
    opcionMenu = menu()

    if opcionMenu==1:
        opcionPers = int(input("Selecciona una opción\n\t1 - Alta Nueva Persona\n\t2 - modificar Datos personales\n\t"))
        if opcionPers == 1:
            persona = Persona()
            persona.nuevaPersona()

        elif opcionPers == 2:
            input('Sistema en construccion. \nPulse una tecla')

        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

    elif opcionMenu==2:
        opcion = int(input("Selecciona una opción\n\t1 - Alta Nuevo Cliente\n\t2 - Modificar Datos \n\t"))
        if opcion == 1 :
            cliente = Cliente()
            cliente.altaCliente()
        elif opcion == 2:
            input('Sistema en construccion. \nPulse una tecla')

        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


    elif opcionMenu==3:
        opcion = int(input("Selecciona una opción\n\t1 - Alta Nueva Cuenta\n\t2 - Modificar Datos \n\t"))
        if opcion == 1 :
            cuenta = Cuenta()
            cuenta.altaCuenta()
            

    elif opcionMenu==4:
        alta_oper()


    elif opcionMenu==9:
        break
    else:
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
