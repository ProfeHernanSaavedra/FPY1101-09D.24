# ciclo para ---> for
'''cont = 234
cont = cont + 1

for cont in range(3):
    print(cont)

#promedio de 3 notas
suma = 0
for i in range(3):
    nota = int(input(f"ingrese una nota {i+1}: "))
    suma = suma + nota
    #print(suma)

promedio = suma /3
print("Su promedio es: ",promedio)

#tabla multiplicar de 1 al 10 de un numero
num = int(input("Ingrese un numero a realiza tabla: "))
#for i in range(10):
#    print(num*(i+1))
for i in range(1,11):
    multi = num*i
    print(num,"x",i,"=",multi) 
    '''
#while --> mientras   

#mientras condicion 
cont = 0
suma = 0
while cont < 3:
    cont = cont + 1
    nota = int(input("Ingrese nota: "))
    suma = suma + nota
promedio = suma /3
print("el promedio es ", promedio)
    


