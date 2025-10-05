class MP4:
    def __init__(self, marca, capacidadGb):
        self.marca = marca
        self.capacidadGb = capacidadGb  
        self.nroCanciones = 0
        self.nroVideos = 0
        self.canciones = []  
        self.videos = []

    def borrar_cancion(self, nombre=None, artista=None, peso=None):
        original = len(self.canciones)
        self.canciones = [
            c for c in self.canciones
            if (nombre and c["nombre"] != nombre)
            and (artista and c["artista"] != artista)
            and (peso and c["peso"] != peso)
        ]
        eliminadas = original - len(self.canciones)
        if eliminadas > 0:
            print(f"{eliminadas} canción(es) eliminada(s).")
        else:
            print("No se encontró ninguna canción que coincida.")

    def __add__(self, nueva_cancion):
        if not isinstance(nueva_cancion, dict):
            print("Error: La canción debe ser un diccionario {'nombre', 'artista', 'peso'}.")
            return self

        
        existe = any(c["nombre"] == nueva_cancion["nombre"] for c in self.canciones)
        if existe:
            print("La canción ya existe en el MP4.")
            return self

        if self.capacidad_disponible() >= nueva_cancion["peso"] / 1024 / 1024:
            self.canciones.append(nueva_cancion)
            self.nroCanciones += 1
            print(f"Canción '{nueva_cancion['nombre']}' agregada correctamente.")
        else:
            print("No hay suficiente espacio para agregar la canción.")
        return self


    def __sub__(self, nuevo_video):
        if not isinstance(nuevo_video, dict):
            print("Error: El video debe ser un diccionario {'nombre', 'artista', 'peso'}.")
            return self

        existe = any(v["nombre"] == nuevo_video["nombre"] for v in self.videos)
        if existe:
            print("El video ya existe en el MP4.")
            return self

        if self.capacidad_disponible() >= nuevo_video["peso"] / 1024:
            self.videos.append(nuevo_video)
            self.nroVideos += 1
            print(f"Video '{nuevo_video['nombre']}' agregado correctamente.")
        else:
            print("No hay suficiente espacio para agregar el video.")
        return self

    def capacidad_disponible(self):

        peso_canciones_GB = sum(c["peso"] for c in self.canciones) / (1024 * 1024)
        peso_videos_GB = sum(v["peso"] for v in self.videos) / 1024
        usado = peso_canciones_GB + peso_videos_GB
        return round(self.capacidadGb - usado, 3)

    def mostrar(self):
        print(f"\nMP4: {self.marca} - Capacidad Total: {self.capacidadGb} GB")
        print(f"Canciones ({self.nroCanciones}):")
        for c in self.canciones:
            print(f"   {c['nombre']} - {c['artista']} - {c['peso']} Kb")

        print(f"Videos ({self.nroVideos}):")
        for v in self.videos:
            print(f"   {v['nombre']} - {v['artista']} - {v['peso']} Mb")

        print(f"Capacidad disponible: {self.capacidad_disponible()} GB")

# Crear MP4
mp4 = MP4("Sony", 1.0)  # 1 GB de capacidad

# Agregar canciones iniciales
mp4.canciones = [
    {"nombre": "Back To Black", "artista": "Amy Winehouse", "peso": 100},
    {"nombre": "Lost On You", "artista": "LP", "peso": 150},
]
mp4.nroCanciones = 2

# Agregar videos iniciales
mp4.videos = [
    {"nombre": "Heathens", "artista": "twenty one pilots", "peso": 50},
    {"nombre": "Harmonica Andromeda", "artista": "KSHMR", "peso": 70},
    {"nombre": "Without Me", "artista": "Halsey", "peso": 30},
]
mp4.nroVideos = 3

mp4.mostrar()

# b) Agregar nueva canción
mp4 + {"nombre": "Believer", "artista": "Imagine Dragons", "peso": 200}

# c) Agregar nuevo video
mp4 - {"nombre": "Thunder", "artista": "Imagine Dragons", "peso": 40}

# a) Borrar una canción por nombre
mp4.borrar_cancion(nombre="Lost On You")

# d) Mostrar capacidad final
mp4.mostrar()
