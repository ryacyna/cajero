import time
import os
from baseDatos import *
from collections import deque

class Persona():
    """ Posee todos sus datos personales (nombre, apellido, edad, dni, domicilio, etc).
    Y posee una funcionalidad que permite cargar por consola estos datos"""

    def __init__(self):
        super().__init__()
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.dni = None
        self.domicilio = None
        self.email = None
        self.id_persona = None

    def cargarDatos(self):
        print('Alta Nueva Persona')

        self.dni = input("      DNI: ")
        self.nombre = input("   Nombre: ")
        self.apellido = input(" Apellido: ")
        self.edad  = input("     Edad: ")
        self.domicilio = input("Domicilio: ")
        self.email  = input("   Correo: ")

        sn  = input('Confirma los datos (S ó N) ? \n').upper()
        if sn == 'S':
            crearPersona(self.nombre, self.apellido, self.edad, self.dni, self.domicilio, self.email)
            self.id_persona = obtenerIdPersona(self.dni)

    def modificarDatos(self):
        pass

    def cargarPersona(self, dni):
        datos = obtenerPersona(dni)
        self.dni = dni
        self.nombre = datos[1]
        self.apellido = datos[2]
        self.edad  = datos[3]
        self.domicilio = [5]
        self.email  = datos[6]
        self.id_persona = datos[0]

class Cliente(Persona):
    """ tiene los datos de persona, añade fecha de alta, fecha de baja (si existe) y sucursal.
    Funcionalidad: darse de alta y de baja"""
    def __init__(self):
        super().__init__()
        self.fechaAlta = None
        self.fechaBaja = None
        self.sucursal = None
        self.id_cliente = None

    def altaCliente(self):

        self.fechaAlta = time.asctime()
        self.sucursal  = input(" Sucursal: ")

        sn  = input('Confirma los datos (S ócon N) ? \n').upper()
        if sn == 'S':
            crearCliente(self.id_persona, self.fechaAlta, self.sucursal)
            self.id_cliente = obtenerDatoCuenta(idcliente, self.id_persona)


    def bajaCliente(self):
        self.fechaBaja = time.asctime()
        bajaCliente(self.fechaBaja, self.id_cliente)

    def cargarCliente(self):



class Cuenta(Cliente):
    ''' Posee los atributos de cliente, añade número, saldo y la capacidad de agregar y extraer dinero.'''
    def __init__(self):
        super().__init__()
        self.nCuenta = None
        self.saldo = None

    def altaCuenta(self):
        crearCuenta(self.id_cliente)
        self.nCuenta = obtenerIdCuenta(self.id_cliente)
        self.saldo = obtenerSaldo(self.nCuenta)

    def cargarCuenta(self, ):
        datos = obtenerCuenta(self.id_cliente)
        self.nCuenta = datos[0]
        self.saldo = datos[2]

    def agregarDinero(self, monto):
        self.saldo = obtenerSaldo(self.nCuenta) + monto
        actualizarSaldo(self.nCuenta, self.saldo)

    def extraerDinero(self, monto):
        self.saldo = obtenerSaldo(self.nCuenta)
        if self.saldo >= monto:
            self.saldo -= monto
            actualizarSaldo(self.nCuenta, self.saldo)
            return 'Saldo {}'.format(self.saldo)
        else:
            return 'Saldo insuficiente. Saldo actual {}'.format(self.saldo)

    def consultarSaldo(self):
        self.saldo = obtenerSaldo(self.nCuenta)
        return 'Saldo actual {}'.format(self.saldo)

    def consultarMovimientos(self):
        pass



class Cajero():
    """Aquí se ejecuta la extracción. Tiene atributos:
    1) cola de clientes, posee todos los clientes que quieren realizar alguna operación.
    2) va atendiendo a cada cliente y ejecutando lo que deseen hacer."""
    def __init__(self):
        self.colaClientes = deque([])

    def atenderCliente(self):
        siguiente = self.colaClientes.popleft()
        operaciones = {'Deposito': 1, 'Extracción': 2, 'Consulta': 3}
        if siguiente.operacion in operaciones:


class ColaClientes():
    def __init__(self):
        self.dni = None
        self.idcliente = None
        self.idcuenta = None
        self.cliente = None #contendra un objeto cuenta
        self.operacion = None
        self.monto = None
        self.horaIngreso = time.asctime()
        self.estado = 'En proceso'
