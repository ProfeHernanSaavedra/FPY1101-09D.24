
def validar_lista_numeros():
    while True:
        try:
            numeros = input("Ingrese una lista de numeros enteros separados por un espacio: ").split()
            # split --> guardar en una lista lo ingresado separado por espacio
            # si ingreso 3 4 5 --> split --> ['3','4','5']
            for i in range(len(numeros)):
                numeros[i] = int(numeros[i])
                #numeros[0] = int(numeros[0])
                #    3       = int ('3')
            return numeros
        except ValueError:
            print("Por favor ingrese un numero entero ")
   