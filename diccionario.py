lista = []

mi_diccionario = {
    "nombre" : "Juan",
    "edad" : 30,
    "ciudad" : "Viña"
}

mi_diccionario2 = {
    "nombre" : "Maria",
    "edad" : 21,
    "ciudad" : "Valpo"
}

print(mi_diccionario)
print(mi_diccionario["nombre"])

mi_diccionario["profesion"] = "ingeniero"

print(mi_diccionario)

mi_diccionario["edad"] = 21

print(mi_diccionario)

del mi_diccionario["ciudad"]
print(mi_diccionario)

for clave,valor in mi_diccionario.items():
    print(clave,"=",valor)
    
if "nombre" in mi_diccionario:
    print("nombre esta en el diccionario")
else:
    print("no existe")
    
if "Juan" == mi_diccionario["nombre"]:
    print("Existe Juan")

lista.append(mi_diccionario)
lista.append(mi_diccionario2)

print(lista)

for fila in lista:
    print(fila)