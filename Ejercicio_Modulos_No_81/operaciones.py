"""Crear un módulo de funciones aritméticas que realicen las operaciones de suma, resta,
multiplicación, división, escribir un programa que importe este
módulo y use estas funciones para operar con números capturados desde el teclado."""

class Operaciones():
    def __init__(self):
        self.num1=0
        self.num2=0
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 == 0:
            return "No se puede dividir por 0"
        else:
            return self.num1 / self.num2