import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') 
	print ("Selecciona una opción")
	print ("\t1 - Dar de Alta un cliente")
	print ("\t2 - Modificar datos de un cliente")
	print ("\t3 - Dar de baja un cliente")
	print ("\t9 - salir")
 
 
while True:
	# Muestra el menu
	menu()
 
	# solicita una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu==1:
		print ("Has pulsado la opción 1")
		idPersona = input("Inserta el DNI de la persona >> ")
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