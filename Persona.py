

def alta_per():
    while True:
        line = input("Altas: A, Modificaciones:M, S:Salir")
        if line == "S" or line == "s":
            break

        dni = input("      DNI: ")
        nom = input("   Nombre: ")
        ape = input(" Apellido: ")
        ed  = input("     Edad: ")
        dom = input("Domicilio: ")
        co  = input("   Correo: ")
            
        sn  = input('Confirma los datos (S ó N) ?')
      
        
           
