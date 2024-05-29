import csv

with open('nuevo_archivo_csv.csv','w',newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    escritor_csv.writerow(['Nombre','Edad','Comuna'])
    escritor_csv.writerows([
        ['Jose',21,'Valpo'],
        ['Maria',14,'Quilpue'],
        ['Pedro',30,'Limache'],
        ['Fran',24,'Vina']
    ])

#leer datos de csv
with open('nuevo_archivo_csv.csv','r',newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)
    
    