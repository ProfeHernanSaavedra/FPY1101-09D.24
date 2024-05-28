mi_diccionario = {
    "nombre" : "Juan",
    "edad" : 30,
    "ciudad" : "Viña"
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
