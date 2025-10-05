class Videojuego:
    def __init__(self, nombre=None, plataforma=None, cantidad_jugadores=0):
        if nombre is None and plataforma is None:
          
            self.nombre = "Desconocido"
            self.plataforma = "Sin plataforma"
            self.cantidad_jugadores = 0
        elif plataforma is None:
       
            self.nombre = nombre
            self.plataforma = "Sin definir"
            self.cantidad_jugadores = 0
        else:
           
            self.nombre = nombre
            self.plataforma = plataforma
            self.cantidad_jugadores = cantidad_jugadores

    def mostrar_datos(self):
        print(f"Videojuego: {self.nombre} | Plataforma: {self.plataforma} | Jugadores: {self.cantidad_jugadores}")

    def agregarJugadores(self, cantidad=None):
        """Si no se pasa cantidad, agrega 1 jugador.
           Si se pasa cantidad, agrega esa cantidad."""
        if cantidad is None:
            self.cantidad_jugadores += 1
            print(f"Se agregó 1 jugador a {self.nombre}. Total ahora: {self.cantidad_jugadores}")
        else:
            self.cantidad_jugadores += cantidad
            print(f"Se agregaron {cantidad} jugadores a {self.nombre}. Total ahora: {self.cantidad_jugadores}")


juego1 = Videojuego("Minecraft", "PC", 5)
juego2 = Videojuego("FIFA 25")   
juego3 = Videojuego()            


print("=== Videojuegos creados ===")
juego1.mostrar_datos()
juego2.mostrar_datos()
juego3.mostrar_datos()

print("\n=== Agregar jugadores ===")
juego1.agregarJugadores()        
juego2.agregarJugadores(3)       
juego3.agregarJugadores()        

print("\n=== Datos finales ===")
juego1.mostrar_datos()
juego2.mostrar_datos()
juego3.mostrar_datos()
