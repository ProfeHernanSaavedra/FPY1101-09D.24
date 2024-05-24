matriz_sencilla = [
    [1,2,3],
    [4,"juan",6]
]

print(matriz_sencilla)

for elemento in matriz_sencilla:
    print(elemento)

print(matriz_sencilla[1][1])

for fila in matriz_sencilla:
    for elemento in fila:
        print(elemento,end=" ")
print()        
for fila in range(2):
    for columna in range(3):
        print(matriz_sencilla[fila][columna])