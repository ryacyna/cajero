

import os
import time
from baseDatos import *
from clases import *

#creo un objeto cajero
cajero = Cajero()

while True:
	#cada vez crea objeto colaClientes al que ira agregando datos
	proximo = ColaClientes()
	#pide por pantalla el dni del cliente y lo guarda en el atributo dni de colaCliente
	proximo.dni = int(input('BIENVENIDO. \n\nINGRESE DNI\n'))
	#busca el idpersona para el dni ingresado
	idpers = obtenerIdPersona(proximo.dni)
	proximo.id_cliente = obtenerIdCliente(idpers)
	proximo.id_cuenta = obtenerDatoCuenta('idcuenta', proximo.id_cliente)
	#crea un objeto cuenta
	cuenta = Cuenta()
	#y lo guarda en el atributo cliente de proximo
	proximo.cliente = cuenta.cargarDatos(proximo.dni)


	# Muestra el menu y almacena la operacion requerida por el cliente en el atributo operaciones
	proximo.operacion = cajero.menuAutomatico()

	if proximo.operacion<1 or proximo.operacion>4:
		print ("Ingrese un numero del 1 al 4")

	if proximo.operacion==1:
		print ("Has pulsado la opción 1 - DEPOSITOS")
		proximo.monto = int(input("Inserta el monto que va a depositar >> $"))

		if proximo.monto <= 0:
			proximo.monto = int(input("Por favor, ingrese un monto mayor a $0>> "))
		else:
			print ("Muchas gracias, en 24hs se efectuará el depósito")

		cajero.atenderCliente()

		if input('Desea realizar otra operacion? S:si N:no\n >> ').upper() == 'S':
			proximo.

	elif proximo.operacion==2:
		print ("Has pulsado la opción 2")
		montoExtraccion = int(input("Inserta el monto de dinero que desea extraer>> "))
		#if montoExtraccion>saldoCliente:
		while montoExtraccion <= 0:
			montoExtraccion = int(input("Por favor, ingrese un monto mayor a $0>> "))
		else:
			print ("Retire su dinero por favor, muchas gracias")

	elif proximo.operacion==3:
		print ("Has pulsado la opción 3")
		idPersona = input("Aquí puede ver la información de su cuenta >> ")
		##Acá se haría una consulta a la base de datos para mostrar los datos del cliente, los movimientos de la cuenta y su saldo

	elif proximo.operacion==4:
		break

	else:
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

	#cajero.atenderCliente()
