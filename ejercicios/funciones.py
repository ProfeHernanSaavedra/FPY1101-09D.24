CARGOS = ['ceo','desarrollador','analista de datos']

def registrar_trabajador(trabajadores):
    nombre = input("Ingrese nombre del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador (CEO/Desarrollador/Analista de datos): ").lower()
    while cargo not in CARGOS:
        print("Cargo no existe, vuelva a ingresar un cargo válido")
        cargo = input("Ingrese el cargo del trabajador (CEO/Desarrollador/Analista de datos): ").lower()
    sueldoBruto = int(input("Ingrese sueldo bruto del trabajador: "))
    
    # calcular los descuentos
    descSalud = sueldoBruto * 0.07
    descAFP = sueldoBruto * 0.12
    liquidoPagar = sueldoBruto - descSalud- descAFP
    
    
    trabajadores.append({
        'Nombre' : nombre,
        'Cargo' : cargo,
        'SueldoBruto' : sueldoBruto,
        'DescSalud' : descSalud,
        'DescAFP' : descAFP,
        'LiquidoPagar' : liquidoPagar
    })
    
def listar_trabajadores(trabajadores):
    print("Lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)
        #print(trabajador['Nombre'])
    
def imprimir_planilla(trabajadores):
    cargoSeleccionado = input("Ingrese el cargo para imprimir la plantilla(o presiona Enter para impimir todos: )").lower()
    if cargoSeleccionado == "":
        trabajadores_a_imprimir = trabajadores
        nombreArchivo = 'plantilla_todos.txt'
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
            if trabajador['Cargo'] == cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombreArchivo = f'planilla_{cargoSeleccionado}.txt'
    else:
        print("Cargo inválido")
        return 
 
    with open(nombreArchivo,'w') as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre y Apellido :{trabajador['Nombre']}\n")
            archivo.write(f"Cargo :{trabajador['Cargo']}\n")
            archivo.write(f"Sueldo Bruto :{trabajador['SueldoBruto']}\n")
            archivo.write(f"Desc Salud :{trabajador['DescSalud']}\n")
            archivo.write(f"Desc AFP :{trabajador['DescAFP']}\n")
            archivo.write(f"Liquido a Pagar  :{trabajador['LiquidoPagar']}\n\n")
            
                          