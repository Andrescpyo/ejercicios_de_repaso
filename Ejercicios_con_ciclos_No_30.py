#30. Escribir un programa que sume los números comprendidos entre un rango suministrado por el usuario.

inicio = int(input("\nIntroduce el número de inicio: "))
fin = int(input("\nIntroduce el número de fin: "))

# Sumamos los números comprendidos entre el rango introducido por el usuario.
suma = 0
for i in range(inicio, fin + 1):
    suma += i

# Imprimimos el resultado en pantalla.
print("\nLa suma de los números comprendidos entre", inicio, "y", fin, "es", suma)