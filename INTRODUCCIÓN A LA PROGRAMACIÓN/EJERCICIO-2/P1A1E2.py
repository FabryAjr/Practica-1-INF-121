class Bus:
    def __init__(self, Capacidad):
        self.Capacidad = Capacidad
        self.Pasajeros = 0
        self.CostoPasaje = 1.50

    def SubirPasajeros(self, Cantidad):
        if self.Pasajeros + Cantidad <= self.Capacidad:
            self.Pasajeros += Cantidad
            print(f"Subieron {Cantidad} pasajeros. Total: {self.Pasajeros}")
        else:
            print("No hay suficientes asientos disponibles.")

    def CobrarPasaje(self):
        total = self.Pasajeros * self.CostoPasaje
        print(f"Total cobrado: Bs. {total:.2f}")
        return total

    def AsientosDisponibles(self):
        disponibles = self.Capacidad - self.Pasajeros
        print(f"Asientos disponibles: {disponibles}")
        return disponibles

    def MostrarInfo(self):
        print(f"Capacidad: {self.Capacidad}, Pasajeros: {self.Pasajeros}, Costo: Bs.{self.CostoPasaje:.2f}")

bus1 = Bus(60)
bus1.SubirPasajeros(12)
bus1.CobrarPasaje()
bus1.AsientosDisponibles()
bus1.MostrarInfo()
