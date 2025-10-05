class Cliente:
    def __init__(self, Nombre, Pedido):
        self.Nombre = Nombre
        self.Pedido = Pedido

    def getNombre(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre

    def getPedido(self):
        return self.Pedido

    def setPedido(self, Pedido):
        self.Pedido = Pedido

    def mostrar(self):
        print(f"Cliente: {self.Nombre}, Pedido: {self.Pedido}")

    def __del__(self):
        print(f"Cliente {self.Nombre} eliminado.")


class Empleado:
    def __init__(self, Nombre, Rol):
        self.Nombre = Nombre
        self.Rol = Rol

    def getNombre(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre

    def getRol(self):
        return self.Rol

    def setRol(self, Rol):
        self.Rol = Rol

    def mostrar(self):
        print(f"Empleado: {self.Nombre}, Rol: {self.Rol}")

    def __del__(self):
        print(f"Empleado {self.Nombre} eliminado.")

cliente1 = Cliente("Andrea", "Cafe con leche y pastel")
empleado1 = Empleado("Carlos", "Barista")

cliente1.mostrar()
empleado1.mostrar()
