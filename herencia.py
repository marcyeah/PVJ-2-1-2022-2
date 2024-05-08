#Ejemplo 1
'''
class transporte:
    def __init__(self, velocidad, capacidad):
        self.velocidad = velocidad
        self.capacidad = capacidad
    def __str__(self):
        return "tiene una velocidad de {} km/h, capacidad de {}".format(self.velocidad, self.capacidad)
class auto(transporte):
    def __init__(self, velocidad, capacidad, color, matricula, destino):
        super().__init__(velocidad, capacidad)
        self.color = color
        self.matricula = matricula
        self.destino = destino
    def __str__(self):
        return super().__str__() + ", el color es {}, la matrícula es {}, su destino es {}.".format(self.color, self.matricula, self.destino)
def tipo(vehiculo):
    print("El", type(vehiculo).__name__, vehiculo)
def main():
    vehiculo = auto(200, 30, "Azul", "BD467F", "Los Angeles")
    tipo(vehiculo)
main()
'''

#Ejemplo 2
'''
class Animal:
    def __init__(self, color, peso):
        self.color = color
        self.peso = peso
class Ave(Animal):
    def __init__(self, color, peso, tipo):
class Perro(Animal):
    def __init__(self, color, peso, raza):
'''