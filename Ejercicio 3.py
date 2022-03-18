# Crear clases de figuras y calcular areas y perimetros, Fernando Esparza Tinoco, 17/03/2022, 17/03/2022

from abc import abstractmethod
import math
class Figura:

    def __init__(self, tipo= ""):
        self.tipo = tipo

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

    def __str__(self):
        return '{}'.format(self.tipo)

class Triangulo(Figura):
    def __init__(self, tipo, longitudL1, lonfitudL2, longitudL3):
        self.tipo = tipo
        self.longitudL1 = longitudL1
        self.longitudL2 = lonfitudL2
        self.longitudL3 = longitudL3

    def calcularPerimetro(self):
        return self.longitudL1 + self.longitudL2 + self.longitudL3

    def calcularArea(self):
        self.semi = (self.calcularPerimetro()/2)
        self.area = math.sqrt(self.semi*(self.semi-self.longitudL1)*(self.semi-self.longitudL2)*(self.semi-self.longitudL3))
        return self.area
    def __str__(self):
        return 'Tipo: {}, Lado1: {}, Lado2: {},Lado3: {}, Perimetro: {}, Área: {}'.format(self.tipo, self.longitudL1, self.longitudL2, self.longitudL3, self.calcularPerimetro(),self.calcularArea())

class Circulo(Figura):
    def __init__(self, tipo, radio):
        self.tipo = tipo
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio ** 2

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return 'Tipo: {}, Radio: {}, Perimetro: {}, Área: {}'.format(self.tipo,self.radio,self.calcularPerimetro(),self.calcularArea())

class Rectangulo(Figura):
    def __init__(self, tipo, ancho, largo):
        self.tipo = tipo
        self.ancho = ancho
        self.largo = largo

    def calcularArea(self):
        return self.largo * self.ancho

    def calcularPerimetro(self):
        return 2 * (self.largo + self.ancho)

    def __str__(self):
        return 'Tipo: {}, Ancho: {}, Largo: {}, Perimetro: {}, Área: {}'.format(self.tipo, self.ancho, self.largo, self.calcularPerimetro(),self.calcularArea())

triangulo = Triangulo("Triangulo",10,10,10)
circulo = Circulo("Circulo",20)
rectangulo = Rectangulo("Rectángulo",20,15)

print(triangulo)
print(circulo)
print(rectangulo)