import funciones as fn

trabajadores = []

while True:
    print("Bienvenidos al super sistema!! ")
    print("1. Registrar trabajador")
    print("2. Listar trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir")
    
    opcion = int(input("Ingrese su opcion: "))
    
    if opcion == 1:
         fn.registrar_trabajador(trabajadores)
    elif opcion == 2:
        fn.listar_trabajadores(trabajadores)
    elif opcion == 3:
        fn.imprimir_planilla(trabajadores)
    elif opcion == 4:
        break
    else:
        print("Opción no válida, seleccione nuevamente")