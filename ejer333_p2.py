import csv
import json

segmentacion_empresa = {
    "Pequeño Contribuyente" : [],
    "Mediano Contribuyente" : [],
    "Gran Contribuyente" : []
}

with open("listadoRutEmpresa.csv","r") as archivo:
    escritor = csv.DictReader(archivo)
    for fila in escritor:
        ventas = int(fila["ventas"])
        if ventas <= 100000000 :
            clasificacion = "Pequeño Contribuyente"
        elif ventas >=100000001 and ventas <= 200000000 :
            clasificacion = "Mediano Contribuyente"
        else:
            clasificacion = "Gran Contribuyente"
        
        empresa = {
            "rut" : fila["rut"],
            "nombre" : fila["nombre"],
            "ventas" : ventas
        }
        
        segmentacion_empresa[clasificacion].append(empresa)
        
    #print(segmentacion_empresa)
with open("segmentacionEmpresa.json","w") as archivo:
    json.dump(segmentacion_empresa,archivo,indent=2) 
    
