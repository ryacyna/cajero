

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
        pass

    def modificarDatos(self):
        pass


class Cliente(Persona):
    """ tiene los datos de persona, añade fecha de alta, fecha de baja (si existe) y sucursal.
    Funcionalidad: darse de alta y de baja"""
    def __init__(self, fechaAlta, fechaBaja, sucursal, id_cliente, **kw):
        super().__init__(nombre=nombre, apellido=apellido, edad=edad, dni=ndi, domicilio=domicilio, email=email, id_persona=id_persona)
        self.fechaAlta = fechaAlta
        self.fechaBaja = fechaBaja
        self.sucursal = sucursal
        self.id_cliente = id_cliente

    def Cuenta(Cliente):
        ''' Posee los atributos de cliente, añade número, saldo y la capacidad de agregar y extraer dinero.'''
        def __init__(self, nCuenta, saldo, **kw):
            super().__init__(fechaAlta=fechaAlta, fechaBaja=fechaBaja, sucursal=sucursal, id_cliente=id_cliente)
            self.nCuenta = nCuenta
            self.saldo = saldo

        def agregarDinero(self):
            pass

        def extraerDinero(self):
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
