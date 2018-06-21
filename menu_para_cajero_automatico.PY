import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona la opción deseada")
	print ("\t1 - Depósito")
	print ("\t2 - Extracción")
	print ("\t3 - Consulta")
	print ("\t9 - salir")
 
 
while True:
	# Muestra el menu
	menu()
 
	# solicita una opción al usuario
	opcionMenu = input("Inserta el numero de la opcion deseada >> ")
 
	if opcionMenu==1:
		print ("Has pulsado la opción 1")
		montodepositado = input("Inserta el monto que va a depositar >> ")
                if montodepositado > 0:
                    print ("Muchas gracias, en 24hs se efectuará el depósito")
        elif opcionMenu==2:
            print ("Has pulsado la opción 2")
		idPersona = input("Inserta el ID del cliente que desea modificar >> ")
        elif opcionMenu==3:
            print ("Has pulsado la opción 3")
            idPersona = input("Inserta el ID del cliente a dar de baja >> ")
        elif opcionMenu==9:
            break
        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")