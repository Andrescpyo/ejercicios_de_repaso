#86. Escribir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto. 

import string

# Crear una lista con todos los caracteres ASCII.
caracteres_ascii = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

# Crear un archivo de texto y escribir la lista de caracteres ASCII en él.
with open("caracteres_ascii.txt", "w") as archivo:
    for caracter in caracteres_ascii:
        archivo.write(caracter)