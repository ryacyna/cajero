Este es un programa pensado para un banco, sirve para administrar personas, clientes, cuentas y las operaciones correspondientes a cada entidad mencionada.


cajeroCentral.py: 

Opciones para crear Clientes y Cuentas.


menu_para_cajero_automatico.py: 

Este archivo sirve para que el cliente ingrese al sistema luego de colocar su DNI, posteriormete se detallan las opciones:
Depositar dinero de la Cuenta
Extraer dinero de la Cuentas
Hacer una consulta sobre la cuenta
Salir del sistema

clases.py : 

Acá se definen las Clases utilizadas en los módulos.

Persona
Cliente
Cuenta
Cajero
Cola de cliente

basededatos.py:

Se definen las funciones que trabajan con sqlite:

crearPersona
obtenerIdPersona
imprimirPersonas
obtenerPersona
crearCliente
obtenerIdCliente
obtenerCliente
imprimir
bajaCliente
crearCuenta
obtenerDatoCuenta
obtenerCuenta
obtenerSaldo
actualizarSaldo

Cajero.db: 

Base de datos sqlite con datos de Personas, Clientes, Cuentas y Operaciones.
..
