'''
Un programa funcional que, dada una lista de números ingresada por el usuario, identifica y 
muestra los números pares e impares de manera clara y organizada.
Reglas de negocio:
1.	Solicitar al usuario que ingrese una lista de números enteros separados por espacios.
2.	Implementar una función llamada validar_lista_numeros que verifique que todos los elementos
    ingresados sean números enteros. Si se ingresa algún valor no válido, solicitar nuevamente 
    la lista.
3.	la función validar_lista_numeros debe utilizar un bucle y maneja excepciones para asegurar 
    que todos los elementos ingresados sean números enteros.
4.	Utilizar el operador de módulo % (MOD) para determinar si un número es par o 
    impar en la lista de números a ingresar. Considerar que un número es par cuando 
    el mod es igual a 0, en caso contrario, es impar
5.	Crear dos listas separadas: una para los números pares y otra para los impares.
6.	Mostrar al usuario las listas resultantes, indicando los números pares, e 
    indicando los números impares

'''
import funciones as fn            
            
#print(fn.validar_lista_numeros())
lista = fn.validar_lista_numeros()
#print(lista)
pares = []
impares = []

for num in lista:
    if num%2 == 0 :
        pares.append(num)
    else:
        impares.append(num)

print("Números pares son: ",pares)
print("Números impares son: ", impares)


