class Persona:
    def __init__(self, nombre, apellido, ci):
        self._nombre = nombre
        self._apellido = apellido
        self._ci = ci

    def mostrar_datos(self):
        print(f"Nombre: {self._nombre} {self._apellido}")
        print(f"CI: {self._ci}")


class Cliente(Persona):
    def __init__(self, nombre, apellido, ci, nro_compra, id_cliente):
        super().__init__(nombre, apellido, ci)
        self._nro_compra = nro_compra
        self._id_cliente = id_cliente

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Número de compra: {self._nro_compra}")
        print(f"ID Cliente: {self._id_cliente}")

class Jefe(Persona):
    def __init__(self, nombre, apellido, ci, sucursal, tipo):
        super().__init__(nombre, apellido, ci)
        self._sucursal = sucursal
        self._tipo = tipo

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Sucursal: {self._sucursal}")
        print(f"Tipo: {self._tipo}")


cliente = Cliente("Laura", "Gómez", "1234567", "C456", "CL001")
print("Datos del Cliente:")
cliente.mostrar_datos()

jefe = Jefe("Carlos", "Pérez", "7654321", "Sucursal Norte", "General")
print("Datos del Jefe:")
jefe.mostrar_datos()
