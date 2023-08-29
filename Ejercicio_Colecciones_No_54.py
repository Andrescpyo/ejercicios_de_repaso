"""Escribir un programa que genera la matriz transpuesta de una matriz de 3 filas y 4 columnas."""

M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

filas = len(M)
columnas = len(M[0])

M_TRANS = [[0 for _ in range(filas)] for _ in range(columnas)]

for i in range(filas):
    for j in range(columnas):
        M_TRANS[j][i] = M[i][j]

for fila in M_TRANS:
    print(fila)