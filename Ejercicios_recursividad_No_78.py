#78. Escribir un programa que usando recursividad calcule el producto de dos enteros usando sumas sucesivas.

def producto_recursivo(a, b):

  if b == 0:
    return 0
  else:
    return a + producto_recursivo(a, b - 1)


if __name__ == "__main__":
  a = int(input("\nIntroduce el primer entero: "))
  b = int(input("Introduce el segundo entero: "))

  print("\nEl producto de los dos enteros es:", producto_recursivo(a, b))