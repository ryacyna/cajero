import time
import os
from baseDatos import *

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


class Cliente(Persona):
    """ tiene los datos de persona, añade fecha de alta, fecha de baja (si existe) y sucursal.
    Funcionalidad: darse de alta y de baja"""
    def __init__(self,**kw):
        super().__init__()
        self.fechaAlta = None
        self.fechaBaja = None
        self.sucursal = None
        self.id_cliente = None

    def altaCliente(self):

        self.fechaAlta = input(" Fecha de alta: ")
        self.sucursal  = input(" Sucursal: ")

        sn  = input('Confirma los datos (S ó N) ? \n').upper()
        if sn == 'S':
            crearCliente(self.id_persona, self.fechaAlta, self.sucursal)
            self.id_cliente = obtenerIdCliente(self.id_persona)


    def bajaCliente(self):

        self.fechaBaja = input(" Fecha de baja: ")


class Cuenta(Cliente):
    ''' Posee los atributos de cliente, añade número, saldo y la capacidad de agregar y extraer dinero.'''
    def __init__(self, nCuenta, **kw):
        super().__init__(fechaAlta=fechaAlta, fechaBaja=fechaBaja, sucursal=sucursal, id_cliente=id_cliente)
        self.nCuenta = nCuentaclases
        self.saldo = None
        self.movimientos = None

    def agregarDinero(self):
        pass

    def extraerDinero(self):
        pass

    def consultarSaldo(self):
        pass

    def consultarMovimientos(self):
        pass



class Cajero():
    """Aquí se ejecuta la extracción. Tiene atributos:
    1) cola de clientes, posee todos los clientes que quieren realizar alguna operación.
    2) va atendiendo a cada cliente y ejecutando lo que deseen hacer."""
    def __init__(self, **kw):
        super().__init__(**kw)
        self.colaCliente = []

    def atenderCliente(self):
        pass

class ColaClientes(self):
    def __init__(self):
        self.arg = arg'''
