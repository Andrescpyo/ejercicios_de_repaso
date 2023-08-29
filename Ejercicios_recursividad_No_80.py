#80. Escribir un programa que mediante funciones recursivas calcule el termino “x” de la serie de fibonacci. 

def fibonacci_recursivo(x):

  if x == 0 or x == 1:
    return x
  else:
    return fibonacci_recursivo(x - 1) + fibonacci_recursivo(x - 2)


if __name__ == "__main__":
  x = int(input("\nIntroduce el término x de la serie de Fibonacci: "))

  print("\nEl término", x, "de la serie de Fibonacci es:", fibonacci_recursivo(x),"\n")