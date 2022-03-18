# Crear clase con x e y, aplicar formula, Fernando Esparza Tinoco, 17/03/2022, 17/03/2022

import math
class Punto:
    def __init__(self, x, y, x2, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

    def set_x(self):
        return self.x

    def set_y(self):
        return self.y

    def distanciaToZero(self):
        distancia = math.sqrt((self.get_x2()-self.get_x()) **2 + (self.get_y2()-self.get_y()) **2)
        return 'Distancia de self({},{}) a ({},{}): {}'.format(self.get_x(), self.get_y(),self.get_x2(),self.get_y2() ,distancia)

    def distance(self, x3, y3):
        self.x3 = x3
        self.y3 = y3
        distancia2 = math.sqrt((self.x3-self.get_x())**2+(self.y3-self.get_y())**2)
        return 'Distancia de self({},{}) a other({},{}): {}'.format(self.get_x(), self.get_y(),self.x3,self.y3, distancia2)

    def squaredDistanceToZero(self):
        distancia3 = (self.get_x2() - self.get_x())**2+(self.get_y2()-self.get_y())**2
        return 'Distancia de self({},{}) a ({},{}): {}'.format(self.get_x(), self.get_y(),self.get_x2(),self.get_y2(), distancia3)

    def __str__(self):
        return 'x y:({},{}), x2 y2:({},{})'.format(self.get_x(),self.get_y(),self.get_x2(),self.get_y2())

punto = Punto(3,5, 0, 0)
print(punto.distanciaToZero())
print(punto.distance(5,7))
print(punto.squaredDistanceToZero())