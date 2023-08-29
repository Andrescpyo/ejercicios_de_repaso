"""Escribir un programa que divida todos los elementos de una matriz M (3,4) por el elemento
situado en la posición 2,2 ."""

M = [[ 4, 20, 60, 7],
 [73, 52,  6, 75],
 [57, 12, 14, 37,],]

print("Matriz original: \n")
for i in M:
    print(i)

divisor = M[1][1]

for i in range(3):
    for j in range(4):
        M[i][j] /= divisor

print("\n Matriz resultante: \n")
for fila in M:
    print([f"{elemento:.3f}" for elemento in fila])