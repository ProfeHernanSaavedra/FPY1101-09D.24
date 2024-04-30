while True:
    try:
        cantidadPasajes = int(input("Ingrese cantidad de pasajes: "))
        break
    except ValueError:
        print("Ingrese un numero válido")

total = 0    # inicializacion de total en el acumulador    
for i in range(cantidadPasajes):
    while True:
        try:
            precioPasaje = int(input(f"Ingrese precio pasaje: {i+1}: "))
            break
        except:
            print("Debe ingresar un valor numerico para los pasajes")
    total = total + precioPasaje # acumulador 
            
            
print("El monto total de los pasajes es: ",total)            

            
    