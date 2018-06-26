
def alta_cta():
    while True:
        line = input("CUENTAS. A:Alta, M:Modificacion, S:Salir")
        if line == "S" or line == "s":
            break

      
        # es una modificacion
        nom = input(" Id Cliente: ")
        print('Su nro de cuenta es .....')                
        sn  = input('Confirma los datos (S ó N) ?')
        
                    
def alta_oper():
    while True:
        line = input("OPERACIONES. 1:Deposito, 2:Extraccion, 3:Consulta saldo, S:Salir")
        if line == "S" or line == "s":
            break

        if int(line)==1:
            print('*** Deposito ***')
        if int(line)==2:
            print('*** Extraccion ***')
        if int(line)==3:
            print('*** Saldo ***')
            
        cli = input(" Id Cliente: ")
        cta = input("  Id Cuenta: ")
        mto = input("    Importe: ")
        
              
        sn  = input('Confirma los datos (S ó N) ?')
