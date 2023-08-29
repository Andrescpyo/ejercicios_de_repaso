#28. Escribir un programa que visualice en pantalla los números pares entre 1 y 25

# Creamos una lista con los números pares entre 1 y 25.
pares = [i for i in range(1, 26) if i % 2 == 0]

# Imprimimos la lista en pantalla.
print("\nLos números pares entre 1 y 25 son: \n",pares,"\n")