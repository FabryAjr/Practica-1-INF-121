class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio  
        self.ram = ram          
        self.nroApp = nroApp

    def mostrar(self):
        print(f"Número: {self.nroTel}, Dueño: {self.dueño}, Espacio: {self.espacio}GB, RAM: {self.ram}GB, Nro de Apps: {self.nroApp}")

    def __iadd__(self, valor):
        self.nroApp += valor
        return self

    def __isub__(self, valor):
        self.espacio -= valor
        return self

if __name__ == "__main__":
    c = Celular("789456123", "Deysly", 64, 8, 20)

    print("Antes de los operadores:")
    c.mostrar()
    c += 10
    c -= 5

    print("\nDespués de los operadores:")
    c.mostrar()
