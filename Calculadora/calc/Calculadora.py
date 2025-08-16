"""
Created on Wed Aug 2, 2025
@author: Hugo Franco
"""

import math

class Calculadora:
    def __init__(self, operando1=0, operando2=None, operacion=None):
        self.operando1 = operando1
        self.operando2 = operando2
        self.operacion = operacion

    def __str__(self):
        if self.operacion is None:
            return f"Calculadora en espera... Valor actual: {self.operando1}"
        if self.operacion in ('raiz', '√'):
            return f"√({self.operando1})"
        return f"{self.operando1} {self.operacion} {self.operando2}"

    def ejecutar(self):
        if self.operacion is None:
            return "Error: No hay operación almacenada para ejecutar."

        try:
            if self.operacion == '+':
                res = self.operando1 + self.operando2
            elif self.operacion == '-':
                res = self.operando1 - self.operando2
            elif self.operacion == '*':
                res = self.operando1 * self.operando2
            elif self.operacion == '/':
                if self.operando2 == 0:
                    return "Error: No se puede dividir entre cero."
                res = self.operando1 / self.operando2
            elif self.operacion == '^':
                res = self.operando1 ** self.operando2
            elif self.operacion in ('raiz', '√'):
                if self.operando1 < 0:
                    return "Error: Raíz de número negativo."
                res = math.sqrt(self.operando1)
            else:
                return "Error: Operación no válida."
        except Exception as e:
            return f"Error inesperado: {str(e)}"

        self.operando1 = res
        self.operando2 = None
        self.operacion = None
        return res

    def suma(self, valor):
        self.operacion = '+'
        self.operando2 = valor
        try:
            self.operando1 = (self.operando1 if self.operando1 is not None else 0) + valor
        except TypeError:
            print("Error: Los operandos deben ser numéricos para la suma.")
            return None
        return self

    def resta(self, valor):
        self.operacion = '-'
        self.operando2 = valor
        try:
            self.operando1 = (self.operando1 if self.operando1 is not None else 0) - valor
        except TypeError:
            print("Error: Los operandos deben ser numéricos para la resta.")
            return None
        return self

    def multiplicacion(self, valor):
        self.operacion = '*'
        self.operando2 = valor
        try:
            self.operando1 = (self.operando1 if self.operando1 is not None else 0) * valor
        except TypeError:
            print("Error: Los operandos deben ser numéricos para la multiplicación.")
            return None
        return self

    def division(self, valor):
        self.operacion = '/'
        self.operando2 = valor
        try:
            if valor == 0:
                print("Error: No se puede dividir entre cero.")
                return None
            self.operando1 = (self.operando1 if self.operando1 is not None else 0) / valor
        except TypeError:
            print("Error: Los operandos deben ser numéricos para la división.")
            return None
        return self

    def potencia(self, exponente):
        self.operacion = '^'
        self.operando2 = exponente
        try:
            self.operando1 = (self.operando1 if self.operando1 is not None else 0) ** exponente
        except Exception as e:
            self.operando1 = None
            return f"Error: {str(e)}"
        return self

    def raiz_cuadrada(self, valor=None):
        self.operacion = 'raiz'
        if valor is not None:
            self.operando1 = valor
        if self.operando1 is None:
            return "Error: No hay operando para calcular la raíz."
        if self.operando1 < 0:
            self.operando1 = None
            return "Error: Raíz de número negativo."
        self.operando2 = None
        self.operando1 = math.sqrt(self.operando1)
        return self

class CalculadoraCientifica(Calculadora):
    def seno(self):
        if self.operando1 is None:
            return "Error: No hay operando para calcular el seno."
        self.operacion = 'sin'
        self.operando1 = math.sin(self.operando1)
        self.operando2 = None
        return self

    def coseno(self):
        if self.operando1 is None:
            return "Error: No hay operando para calcular el coseno."
        self.operacion = 'cos'
        self.operando1 = math.cos(self.operando1)
        self.operando2 = None
        return self

    def tangente(self):
        if self.operando1 is None:
            return "Error: No hay operando para calcular la tangente."
        self.operacion = 'tan'
        try:
            self.operando1 = math.tan(self.operando1)
        except Exception as e:
            return f"Error: {str(e)}"
        self.operando2 = None
        return self