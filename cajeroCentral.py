from clases import *
from menu_para_banco import menu
import os
from baseDatos import imprimiRegistro

while True:
    # Muestra el menu y solicita una opción al usuario
    opcionMenu = menu()

    if opcionMenu==1:
        opcionPers = int(input("Selecciona una opción\n\t1 - Alta Nueva Persona\n\t2 - modificar Datos personales\n\t"))
        if opcionPers == 1:
            persona = Persona()
            persona.nuevaPersona()
            imprimiRegistro()
        elif opcionPers == 2:
            pass
        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



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
