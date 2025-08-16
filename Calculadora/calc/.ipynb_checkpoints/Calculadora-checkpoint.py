"""
Created on Wed Aug 2, 2025
@author: Hugo Franco
"""
class Calculadora:
    tipo = 'cientifica'
    
    def __init__(self, operando1=0, operando2=0, operacion=None):
        self.operando1 = operando1
        self.operando2 = operando2
        self.operacion = operacion

    def __str__(self):
        if self.operacion is None:
            return "Esperando calculadora"
        return f"{self.operando1} {self.operacion} {self.operando2}"
    
    def suma(self, operando1=None, operando2=None):
        self.operacion = "+"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None:
            self.operando2 = operando1
        self.operando1 = self.operando1 + self.operando2
        return self
    
    def resta(self, operando1=None, operando2=None):
        self.operacion = "-"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None:
            self.operando2 = operando1
        self.operando1 = self.operando1 - self.operando2
        return self
    
    def multiplicacion(self, operando1=None, operando2=None):
        self.operacion = "*"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None:
            self.operando2 = operando1
        self.operando1 = self.operando1 * self.operando2
        return self
    
    def division(self, operando1=None, operando2=None):
        self.operacion = "/"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None:
            self.operando2 = operando1
        try:
            self.operando1 = self.operando1 / self.operando2
        except Exception as err:
            print('Gestión de excepciones:', err)
            self.operando1 = "valor no definido"
        return self
