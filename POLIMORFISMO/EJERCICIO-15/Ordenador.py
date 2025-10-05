class Ordenador:
    def __init__(self, codigo_serial, numero, ram, procesador, estado):
        self.codigo_serial = codigo_serial
        self.numero = numero
        self.ram = ram  
        self.procesador = procesador
        self.estado = estado  

    def __str__(self):
        return f"Ordenador {self.numero} | Serial: {self.codigo_serial} | RAM: {self.ram}GB | Procesador: {self.procesador} | Estado: {self.estado}"


class Laboratorio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ordenadores = []

    def agregar_ordenador(self, ordenador):
        if len(self.ordenadores) < self.capacidad:
            self.ordenadores.append(ordenador)
        else:
            print(f"No se puede agregar más ordenadores a {self.nombre}, capacidad llena.")

    def informacion(self, estado=None, min_ram=None):
       
        print(f"\n--- Información de {self.nombre} ---")
        for o in self.ordenadores:
            if estado and o.estado != estado:
                continue
            if min_ram and o.ram <= min_ram:
                continue
            print(o)

    def mostrar_todos(self):
        print(f"\n--- Todos los ordenadores de {self.nombre} ---")
        for o in self.ordenadores:
            print(o)


def trasladar_ordenadores(origen, destino, codigos):
    print(f"\n--- Traslado de {origen.nombre} a {destino.nombre} ---")
    print("Antes del traslado:")
    origen.mostrar_todos()
    destino.mostrar_todos()

    trasladados = []
    for codigo in codigos:
        for o in origen.ordenadores:
            if o.codigo_serial == codigo:
                trasladados.append(o)
                origen.ordenadores.remove(o)
                break

    for o in trasladados:
        destino.agregar_ordenador(o)

    print("\nDespués del traslado:")
    origen.mostrar_todos()
    destino.mostrar_todos()

lab1 = Laboratorio("Lasin 1", 4)
lab2 = Laboratorio("Lasin 2", 4)

o1 = Ordenador("S001", 1, 8, "i5", "activo")
o2 = Ordenador("S002", 2, 16, "i7", "activo")
o3 = Ordenador("S003", 3, 4, "i3", "inactivo")
o4 = Ordenador("S004", 4, 12, "i7", "activo")
o5 = Ordenador("S005", 5, 8, "i5", "inactivo")
o6 = Ordenador("S006", 6, 16, "i9", "activo")

lab1.agregar_ordenador(o1)
lab1.agregar_ordenador(o2)
lab1.agregar_ordenador(o3)

lab2.agregar_ordenador(o4)
lab2.agregar_ordenador(o5)
lab2.agregar_ordenador(o6)

lab1.informacion(estado="activo")
lab2.informacion(estado="inactivo")

lab1.informacion(min_ram=8)
lab2.informacion(min_ram=8)

trasladar_ordenadores(lab1, lab2, ["S001", "S002"])
