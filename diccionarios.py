## diccionario

lista = []

# lista2 = ['hola','carlos',12]

# for variable in lista2:
#     print(variable)
    
# matriz = [
#     [1,2,3],
#     [4,5,6]
# ]

# for fila in matriz:
#     for col in fila:
#         print(col)

# print(matriz[0][2])

resp = "s"
while resp == "s":
    
    rut = input("Ingrese rut: ")
    nombre = input("Ingrese nombre: ")
    diccionario = {
        "rut"   : rut,
        "nombre": nombre
    }
    lista.append(diccionario)

    resp = input("Desea ingresar otro mas ? (s/n): ").lower()


for i in lista:
    print(i)



# lista3 = [diccionario]
# print("lista3: ",lista3)


# diccionario["nombre"] = "Juan"

# print(diccionario)
# print(diccionario["nombre"])


