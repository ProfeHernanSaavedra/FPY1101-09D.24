miLista = ["juan",21,288,True]

print(miLista)

for i in range(4):
    print(miLista[i])
print()
for elemento in miLista:
    print(elemento)

miLista.append("Maria")

print(miLista)

miLista.insert(2,34)

print(miLista)

miLista2 = [34,5,67,9]

miLista2.sort()

print(miLista2)
miLista2.reverse()
print(miLista2)
miLista.reverse()
print(miLista)

miLista3 = ["Juan","Maria","Anastasia","Amelia"]
miLista3.sort()
print(miLista3)
miLista3.remove("Juan")
print(miLista3)