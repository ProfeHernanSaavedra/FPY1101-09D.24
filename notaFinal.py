nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2: "))
nota3 = int(input("Ingrese nota 3: "))

promedio = nota1*(30/100) + nota2*0.3+nota3*0.4
print("Su promedio es: ",promedio)

examen = int(input("Ingrese nota examen"))
"""
    + suma
    - resta
    / division
    * multiplicaicon
    
    int enteros
    float real
    str caracteres
    valor = True o False Logicos o Boolean
"""

notaFinal = promedio*0.6 + examen*0.4

print("la nota final es: ", notaFinal)

#condiciones

if notaFinal >= 40:
    print("Ud aprobo")
else:
    print("Ud ha reprobado")

print("Cambio!!")