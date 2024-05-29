datos = """
    Este curso es potencialmente ......
    el profesor dijo en abril sobe sfa
"""
with open('datos.txt','w') as archivo:
    archivo.write(datos)
    
## lectura de archivo
#opción 1
with open('datos.txt','r') as archivo:
    contenido = archivo.read()
    
print(contenido)
print()
#opción 2
archivo = open('datos.txt','r')
contenido = archivo.read()
print(contenido)
archivo.close()

    