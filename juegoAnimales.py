print("¿Cuál de los siguientes animales vive en el agua?\n")
print("\t 1. Perro")
print("\t 2. Cocodrilo")
print("\t 3. Conejo")
print("\t 4. Tiburón")

resp = int(input("Ingrese opción de respuesta: "))
puntaje = 0
if resp == 2:
    puntaje = puntaje + 0.5
    #print("Su puntaje es: ",puntaje)
else:
    if resp == 4 :
        puntaje = puntaje + 1
     #   print("Su puntaje es: ",puntaje)
    else:
        puntaje = 0
      #  print("Su puntaje es: ",puntaje)

print("Su puntaje es: ",puntaje)
