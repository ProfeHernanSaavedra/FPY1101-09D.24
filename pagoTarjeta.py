deuda = 100000
saldo = 100000

while True:
    print("            MENU         ")
    print("*************************")
    print("1.Pago Tarjeta de Crédito")
    print("2.Simulación de Compras")
    print("3.Salir")
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        try:
            #print("haga opcion 1")
            print("Su saldo es: $",saldo)
            print("Su deuda es: $",deuda)
            montoPago = int(input("Ingrese el monto a pagar: "))
            if montoPago < 0 :
                print("El monto debe ser mayor que cero")
            else:
                if montoPago > saldo:
                    print("Saldo insuficiente para pagar")
                else:
                    deuda = deuda - montoPago
                    print("Ud pago: $",montoPago)
        except:
            print("Ingrese un valor válido")            
                
    else:
        if opcion == 2:
            #print("haga opcion 2")
            cantidadCompra = int(input("Ingrese cantidad de compras: "))
            for i in range(cantidadCompra):
                print("Compra: ", (i+1))
                try:
                    montoCompra = int(input("Ingrese el monto de la compra: "))
                    if montoCompra <= 0 :
                        print("Debe ingresar un valor mayor a cero")
                    else:
                        if saldo >= montoCompra:
                            deuda = deuda + montoCompra
                            saldo = saldo - montoCompra
                            print("Ud comopro un monto de $",montoCompra)
                        else:
                            print("Saldo insuficiente")
                except:
                    print("Ingrese un valor numérico válido")
        else:
            if opcion == 3:
                print("Saliendo...")
                break
            else:
                print("Opción no válida")
    
    
    