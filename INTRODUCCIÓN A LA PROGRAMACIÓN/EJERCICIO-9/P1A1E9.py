class Camara:
    def __init__(self, IdCamara, Resolucion, Estado, Ubicacion):
        self.IdCamara = IdCamara
        self.Resolucion = Resolucion
        self.Estado = Estado
        self.Ubicacion = Ubicacion

    def Encender(self):
        self.Estado = "Encendida"
        print(f"Cámara {self.IdCamara} encendida.")

    def Apagar(self):
        self.Estado = "Apagada"
        print(f"Cámara {self.IdCamara} apagada.")

    def MostrarInfo(self):
        print(f"Cámara {self.IdCamara} ({self.Resolucion}) - Estado: {self.Estado} - Ubicación: {self.Ubicacion}")


class OficialEncubierto:
    def __init__(self, Nombre, Rango, AreaVigilancia, IdentidadFalsa):
        self.Nombre = Nombre
        self.Rango = Rango
        self.AreaVigilancia = AreaVigilancia
        self.IdentidadFalsa = IdentidadFalsa

    def Patrullar(self):
        print(f"{self.Nombre} patrulla el área: {self.AreaVigilancia} bajo la identidad de {self.IdentidadFalsa}.")

    def Reportar(self):
        print(f"{self.Nombre} informa: situación controlada en {self.AreaVigilancia}.")

    def MostrarInfo(self):
        print(f"Oficial: {self.Nombre} | Rango: {self.Rango} | Identidad Falsa: {self.IdentidadFalsa}")


class SistemaRadio:
    def __init__(self, Frecuencia, Canal, Encendido, Mensaje):
        self.Frecuencia = Frecuencia
        self.Canal = Canal
        self.Encendido = Encendido
        self.Mensaje = Mensaje

    def Transmitir(self):
        if self.Encendido:
            print(f"Transmitiendo en {self.Canal} ({self.Frecuencia} MHz): {self.Mensaje}")
        else:
            print("Radio apagada. No se puede transmitir.")

    def Apagar(self):
        self.Encendido = False
        print("Radio apagada.")

    def MostrarInfo(self):
        estado = "Encendida" if self.Encendido else "Apagada"
        print(f"Radio {estado} - Canal: {self.Canal} - Frecuencia: {self.Frecuencia} MHz")


class CocineroPolicial:
    def __init__(self, Nombre, Edad, Experiencia, Especialidad):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Experiencia = Experiencia
        self.Especialidad = Especialidad

    def PrepararComida(self):
        print(f"{self.Nombre} prepara salchipapas ({self.Especialidad}).")

    def Arrestar(self):
        print(f"{self.Nombre} arresta a un sospechoso mientras cocinaba.")

    def MostrarInfo(self):
        print(f"Cocinero Policial: {self.Nombre}, {self.Edad} años, {self.Experiencia} años de servicio.")


class PuestoSalchipapas:
    def __init__(self, Nombre, Ubicacion, Camaras, Oficiales, Radio, Cocinero):
        self.Nombre = Nombre
        self.Ubicacion = Ubicacion
        self.Camaras = Camaras
        self.Oficiales = Oficiales
        self.Radio = Radio
        self.Cocinero = Cocinero

    def ActivarSistema(self):
        print(f"Activando sistema del puesto {self.Nombre} en {self.Ubicacion}...")
        for cam in self.Camaras:
            cam.Encender()
        for o in self.Oficiales:
            o.Patrullar()
        self.Radio.Transmitir()
        self.Cocinero.PrepararComida()

    def MostrarInfo(self):
        print(f"\n=== Puesto: {self.Nombre} ({self.Ubicacion}) ===")
        for cam in self.Camaras:
            cam.MostrarInfo()
        for o in self.Oficiales:
            o.MostrarInfo()
        self.Radio.MostrarInfo()
        self.Cocinero.MostrarInfo()


cam1 = Camara(1, "1080p", "Apagada", "Entrada")
cam2 = Camara(2, "720p", "Apagada", "Cocina")

of1 = OficialEncubierto("Sargento López", "Sargento", "Ceja Norte", "Vendedor de papas")
of2 = OficialEncubierto("Agente Rojas", "Agente", "Ceja Sur", "Repartidor de bebidas")

radio = SistemaRadio(99.9, "Canal Alfa", True, "Operativo en marcha")
cocinero = CocineroPolicial("Carlos Pérez", 35, 10, "Salchipapas especiales")

puesto = PuestoSalchipapas("El Antidelincuencia", "Ceja de El Alto", [cam1, cam2], [of1, of2], radio, cocinero)
puesto.MostrarInfo()
puesto.ActivarSistema()
