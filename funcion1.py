def saludo():
    print("Hola a todos") # funcion sin argumentos y sin retorno
    
    
def saludo2(nombre):
    print("Hola ",nombre) # funcion con argumentos y sin retorno
    
def saludo3(nombre):
    return nombre + " que tal"  # funcion con argumentos y con retorno

def sumar(num1,num2)  :
    suma = num1 + num2
    return suma

    
# llamando funciones
saludo()
print("---------------------")
nombre = input("Ingrese nombre: ")
saludo2(nombre)

print(saludo3(nombre))

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
print(sumar(num1,num2))
