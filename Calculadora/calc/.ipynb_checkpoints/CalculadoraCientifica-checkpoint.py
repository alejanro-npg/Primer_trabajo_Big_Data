from Calculadora import Calculadora

class CalculadoraCientifica(Calculadora):
    
    def seno(self):
        self.operando1 = math.sin(self.operando1)
        return self
    
    def coseno(self):
        self.operando1 = math.cos(self.operando1)
        return self
    
    def tangente(self):
        self.operando1 = math.tan(self.operando1)
        return self
