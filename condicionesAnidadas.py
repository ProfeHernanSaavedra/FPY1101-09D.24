##condiciones anidadas

añoActual = int(input("Ingrese año Actual: "))
añoNac = int(input("Ingrese año de nacimiento: "))

edad = añoActual - añoNac

print("Su edad es : ",edad," años app")

if edad >= 18 :
    print("UD es mayor de edad")
else:
    if edad > 0 and edad <= 4:
        print("Ud es un bebe")
    else:
        if edad >4 and edad <=12:
            print("es un niño")
        else:
            if edad >12 and edad <18:
                print("ud es una adolescente")
                
print("FIN") 
                
            