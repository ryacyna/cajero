

def  alta_cli():
    while True:
        line = input("CLIENTES. A:Alta, M:Modificacion, S:Salir")
        if line == "S" or line == "s":
            break

      
        # es una modificacion
        dni = input("           DNI: ")
        nom = input(" Fecha de alta: ")
        ape = input(" Fecha de baja: ")
        ed  = input("      Sucursal: ")
                
        sn  = input('Confirma los datos (S ó N) ?')
        
                    
              
