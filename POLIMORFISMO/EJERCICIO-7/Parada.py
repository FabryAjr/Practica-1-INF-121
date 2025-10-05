class Parada:
    def __init__(self, nombreP="", admins=None, autos=None):

        self.nombreP = nombreP
        self.admins = admins if admins is not None else [""] * 10
        self.autos = autos if autos is not None else [["", ""] for _ in range(10)]
        self.nroAdmins = 0
        self.nroAutos = 0

    def mostrar(self):
        print(f"Nombre de la parada: {self.nombreP}")
        print("\nAdministradores:")
        for i in range(self.nroAdmins):
            print(f"  {i+1}. {self.admins[i]}")
        
        print("\nAutos:")
        for i in range(self.nroAutos):
            print(f"  {i+1}. Modelo: {self.autos[i][0]}, Conductor: {self.autos[i][1]}")

    def adicionar(self, x):
        if self.nroAdmins < 10:
            self.admins[self.nroAdmins] = x
            self.nroAdmins += 1
        else:
            print("No se pueden agregar más administradores (límite alcanzado).")

    def adicionar_auto(self, modelo, conductor):
        if self.nroAutos < 10:
            self.autos[self.nroAutos][0] = modelo
            self.autos[self.nroAutos][1] = conductor
            self.nroAutos += 1
        else:
            print("No se pueden agregar más autos (límite alcanzado).")

p1 = Parada()
p1.nombreP = "Parada Central"

p1.adicionar("Carlos")
p1.adicionar("Ana")

p1.adicionar_auto("Toyota", "Luis")
p1.adicionar_auto("Nissan", "María")

p1.mostrar()
