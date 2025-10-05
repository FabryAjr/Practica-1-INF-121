class Pasajero:
    def __init__(self, nombre="", costo=0, genero=""):
        self.nombre = nombre
        self.costo = costo
        self.genero = genero  

    def leer(self):
        self.nombre = input("Nombre del pasajero: ")
        self.costo = float(input("Costo del pasaje: "))
        self.genero = input("Género (M/F): ").upper()

    def mostrar(self):
        print(f"{self.nombre} - Costo: {self.costo} - Género: {self.genero}")


class Crucero:
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.pasajeros = []

    def leer(self):
        n = int(input(f"¿Cuántos pasajeros tiene el crucero {self.nombre}? "))
        for i in range(n):
            print(f"\nPasajero {i+1}:")
            p = Pasajero()
            p.leer()
            self.pasajeros.append(p)

    def mostrar(self):
        print(f"\nCrucero: {self.nombre}")
        for p in self.pasajeros:
            p.mostrar()

    def __eq__(self, otro):
        total = sum(p.costo for p in self.pasajeros)
        print(f"Total del crucero {self.nombre}: {total}")
        return total

    def __add__(self, otro):
        if len(self.pasajeros) == len(otro.pasajeros):
            print(f"Ambos cruceros ({self.nombre} y {otro.nombre}) tienen la misma cantidad de pasajeros.")
        else:
            print(f"Los cruceros tienen diferente cantidad de pasajeros.")
        return None

    def __sub__(self, otro=None):
        hombres = sum(1 for p in self.pasajeros if p.genero == "M")
        mujeres = sum(1 for p in self.pasajeros if p.genero == "F")
        print(f"En el crucero {self.nombre} hay {hombres} hombres y {mujeres} mujeres.")
        return hombres, mujeres


c1 = Crucero("Caribe Azul")
c2 = Crucero("Sol del Pacífico")

c1.pasajeros = [
    Pasajero("Juan Vargas", 502, "M"),
    Pasajero("Martina Vasques", 603, "F"),
    Pasajero("Wilmer Montero", 401, "M")
]

c2.pasajeros = [
    Pasajero("Luis Romero", 500, "M"),
    Pasajero("Lucía Pérez", 1000, "F"),
    Pasajero("Ana Torres", 925, "F")
]

c1.mostrar()
c2.mostrar()

c1 == c2  

c1 + c2

c1 - None
c2 - None
