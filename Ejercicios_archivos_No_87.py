#87. Escribir un programa que lea y muestre en pantalla el archivo generado en el ejercicio anterior.

with open("caracteres_ascii.txt", "r") as archivo:
    caracteres_ascii = archivo.read()

# Mostrar la lista de caracteres ASCII en pantalla.
print("\n",caracteres_ascii,"\n")
