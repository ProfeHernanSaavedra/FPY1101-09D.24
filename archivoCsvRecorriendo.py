import csv
with open('nuevo_archivo_csv.csv','r',newline='') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        nombre = fila['Nombre']
        edad = int(fila['Edad'])
        comuna = fila['Comuna']
        estado_edad = "mayor de edad " if edad >=18 else "Menor Edad"
        print(f"{nombre} tiene {edad} años, es {estado_edad} y vive en {comuna}")