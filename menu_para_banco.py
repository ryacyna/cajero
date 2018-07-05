import os


def menu():

    #Función que limpia la pantalla y muestra nuevamente el menu

    os.system('clear')
    opcionMenu = int(input("Selecciona una opción\n\t1 - Personas\n\t2 - Clientes\n\t3 - Cuentas\n\t4 - Movimientos\n\t9 - Salir\n\t"))
    return opcionMenu


''''while True:
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
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")'''
