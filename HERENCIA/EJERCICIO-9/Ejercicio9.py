class Politico:
    def __init__(self, profesion, añosExp):
        self.profesion = profesion
        self.añosExp = añosExp

class Partido:
    def __init__(self, nombreP, rol):
        self.nombreP = nombreP
        self.rol = rol

class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, añosExp, nombreP, rol):
        Politico.__init__(self, profesion, añosExp)
        Partido.__init__(self, nombreP, rol)
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        print(f"Presidente: {self.nombre} {self.apellido}")
        print(f"Profesión: {self.profesion}, Años de experiencia: {self.añosExp}")
        print(f"Partido: {self.nombreP}, Rol en el partido: {self.rol}\n")

pres1 = Presidente("Juan", "Perez", "Abogado", 20, "Partido A", "Líder")

prof = "Economista"
exp = 15
partido = "Partido B"
rol_partido = "Fundador"
pres2 = Presidente("Maria", "Lopez", prof, exp, partido, rol_partido)

presidentes = [
    pres1,
    pres2,
    Presidente("Carlos", "Gomez", "Ingeniero", 25, "Partido C", "Secretario")
]

nombre_buscar = "Maria"

print(f"Buscando presidente con nombre {nombre_buscar}...\n")
for p in presidentes:
    if p.nombre == nombre_buscar:
        print(f"Presidente encontrado: {p.nombre} {p.apellido}")
        print(f"Partido: {p.nombreP}, Profesión: {p.profesion}")
