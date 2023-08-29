# 61. Escribir un programa que lea una frase introducida desde el teclado y la escriba al revés.

frase = input("\nIntroduce una frase: ")

# Invertimos la frase.
frase_invertida = frase[::-1]

# Imprimimos la frase invertida en pantalla.
print(frase_invertida)