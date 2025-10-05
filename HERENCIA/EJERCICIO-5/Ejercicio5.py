class Vehiculo:
    def __init__(self, conductor, placa, id_vehiculo):
        self._conductor = conductor
        self._placa = placa
        self._id = id_vehiculo

    def mostrar_datos(self):
        print(f"Placa: {self._placa}, Conductor: {self._conductor}")

    def cambiar_conductor(self, nuevo_conductor):
        self._conductor = nuevo_conductor
class Bus(Vehiculo):
    def __init__(self, conductor, placa, id_vehiculo, capacidad, sindicato):
        super().__init__(conductor, placa, id_vehiculo)
        self.capacidad = capacidad
        self.sindicato = sindicato
class Auto(Vehiculo):
    def __init__(self, conductor, placa, id_vehiculo, caballos_fuerza, descapotable):
        super().__init__(conductor, placa, id_vehiculo)
        self.caballos_fuerza = caballos_fuerza
        self.descapotable = descapotable
class Moto(Vehiculo):
    def __init__(self, conductor, placa, id_vehiculo, cilindrada, casco):
        super().__init__(conductor, placa, id_vehiculo)
        self.cilindrada = cilindrada
        self.casco = casco

bus = Bus("Mario Pérez", "BUS123", 1, 50, "Sindicato Central")
auto = Auto("Lucía Gómez", "CAR456", 2, 120, True)
moto = Moto("Ana Torres", "MOTO789", 3, 250, True)
print("Datos del Bus:")
bus.mostrar_datos()

print("\nDatos del Auto:")
auto.mostrar_datos()

print("\nDatos de la Moto:")
moto.mostrar_datos()

auto.cambiar_conductor("Carlos Ruiz")

print("\nNuevo conductor del Auto:")
auto.mostrar_datos()
