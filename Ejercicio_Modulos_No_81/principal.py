from operaciones import Operaciones

numero1= int(input("Digita el primer número: "))
numero2= int(input("Digita el segundo número: "))

u = Operaciones()
u.num1= numero1
u.num2= numero2

print(f"\n La suma de los números es: {u.suma()}")
print(f"La resta de los números es: {u.resta()}")
print(f"La multiplicación de los números es: {u.multiplicacion()}")
print(f"La división de los números es: {u.division()}")


