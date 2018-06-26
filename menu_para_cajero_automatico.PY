import os

def menu():
	print ("Seleccione la opción deseada")
	print ("\t1 - Depósito")
	print ("\t2 - Extracción")
	print ("\t3 - Consulta")
	print ("\t4 - Salir")
	

while True:
	# Muestra el menu
	menu()
	
	opcionMenu = int(input("Inserta el numero de la opcion dentroseada >> "))
	
	while opcionMenu<1 or opcionMenu>4:
		print ("Ingrese un numero del 1 al 4")
		opcionMenu = int(input("Inserta el numero de la opcion deseada >> "))
	
	if opcionMenu==1:
		print ("Has pulsado la opción 1")
		montoDepositado = int(input("Inserta el monto que va a depositar >> "))
		while montoDepositado <= 0:
			montoDepositado = int(input("Por favor, ingrese un monto mayor a $0>> "))
		else:
			print ("Muchas gracias, en 24hs se efectuará el depósito")
			
	elif opcionMenu==2:
		print ("Has pulsado la opción 2")
		montoExtraccion = int(input("Inserta el monto de dinero que desea extraer>> "))
		#if montoExtraccion>saldoCliente:
		while montoExtraccion <= 0: 
			montoExtraccion = int(input("Por favor, ingrese un monto mayor a $0>> "))
		else:
			print ("Retire su dinero por favor, muchas gracias")
	
	elif opcionMenu==3:
		print ("Has pulsado la opción 3")
		idPersona = input("Aquí puede ver la información de su cuenta >> ")
		##Acá se haría una consulta a la base de datos para mostrar los datos del cliente, los movimientos de la cuenta y su saldo
		
	elif opcionMenu==4:
		break
	
	else:
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")