class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self._nombre = nombre
        self._paterno = paterno
        self._materno = materno
        self._edad = edad

    def mostrar(self):
        print(f"Nombre: {self._nombre} {self._paterno} {self._materno}, Edad: {self._edad}")

    def getEdad(self):
        return self._edad


class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.ru = ru
        self.matricula = matricula

    def mostrar(self):
        super().mostrar()
        print(f"RU: {self.ru}, Matrícula: {self.matricula}")

    def modificarEdad(self, nueva_edad):
        self._edad = nueva_edad

class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, regProfesional):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.regProfesional = regProfesional

    def mostrar(self):
        super().mostrar()
        print(f"Sueldo: {self.sueldo}, Registro Profesional: {self.regProfesional}")


def promedio(estudiantes):
    total = sum(e.getEdad() for e in estudiantes)
    return total / len(estudiantes)


est1 = Estudiante("Juan", "Pérez", "López", 20, "RU123", "MAT001")
est2 = Estudiante("María", "Gómez", "Ruiz", 22, "RU124", "MAT002")
doc1 = Docente("Carlos", "Mendoza", "Flores", 40, 3500, "REG1234")

print("=== Datos de Estudiantes ===")
est1.mostrar()
est2.mostrar()

print("\n=== Datos del Docente ===")
doc1.mostrar()

print(f"\nPromedio de edad de los estudiantes: {promedio([est1, est2]):.2f}")

print("\nModificando edad de Juan a 25 años...")
est1.modificarEdad(25)
est1.mostrar()

for e in [est1, est2]:
    if e.getEdad() == doc1.getEdad():
        print(f"\n{e._nombre} tiene la misma edad que el docente.")
        break
else:
    print("\nNingún estudiante tiene la misma edad que el docente.")
