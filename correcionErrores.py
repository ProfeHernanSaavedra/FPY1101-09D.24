'''
try:
    bloque código
except:
    codigo que sirve para indicar el error
else:
    funciona bien
finally:
    se ejecuta siempre sin importar si se cae o no.
'''
while True:
    try:
        num = int(input("Ingrese un número: "))
        #break
    except ValueError as ErrorIngresoNumero:
        print("Ud ingreso mal! debe ser número")
    else:
        print("Aca esta todo bien")
        break
    finally:
        print("que tengas un buen dia")
        

