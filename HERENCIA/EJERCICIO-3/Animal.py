class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def desplazarse(self):
        print(f"{self.nombre} se está desplazando de manera general.")

class Leon(Animal):
    def desplazarse(self):
        print(f"{self.nombre} camina majestuosamente por la sabana.")

class Pinguino(Animal):
    def desplazarse(self):
        print(f"{self.nombre} nada ágilmente en el agua.")

class Canguro(Animal):
    def desplazarse(self):
        print(f"{self.nombre} salta dando grandes brincos.")

animales = [
    Leon("Simba", 5),
    Pinguino("Pingu", 3),
    Canguro("Kanga", 7),
    Leon("Mufasa", 8),
    Pinguino("Skipper", 4)
]

for animal in animales:
    animal.desplazarse()
