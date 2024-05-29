import json

datos ={
    "nombre":"Juan",
    "edad" : 25,
    "comuna":"Valpo",
    "estudios":["liceo 1-A","DUOC-UC","Diplomado DUOC-UC"]
}

#crear archivo
with open('archivo.json','w') as archivo:
    json.dump(datos,archivo)
    
#abrir archivo
with open('archivo.json','r') as archivo:
    datos_leidos = json.load(archivo)
    
print(datos_leidos)