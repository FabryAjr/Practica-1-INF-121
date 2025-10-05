package Ejercicio2;

public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    // 🔹 Constructor 1: vacío
    public Videojuego() {
        this.nombre = "Desconocido";
        this.plataforma = "Sin plataforma";
        this.cantidadJugadores = 0;
    }

    // 🔹 Constructor 2: con nombre
    public Videojuego(String nombre) {
        this.nombre = nombre;
        this.plataforma = "Sin definir";
        this.cantidadJugadores = 0;
    }

    // 🔹 Constructor 3: con todos los parámetros
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    // 🔹 Método para mostrar los datos
    public void mostrarDatos() {
        System.out.println("Videojuego: " + nombre +
                " | Plataforma: " + plataforma +
                " | Jugadores: " + cantidadJugadores);
    }

    // 🔹 Sobrecarga del método agregarJugadores()
    // 1. Agregar un solo jugador
    public void agregarJugadores() {
        cantidadJugadores++;
        System.out.println("Se agregó 1 jugador a " + nombre +
                ". Total ahora: " + cantidadJugadores);
    }

    // 2. Agregar una cantidad específica
    public void agregarJugadores(int cantidad) {
        cantidadJugadores += cantidad;
        System.out.println("Se agregaron " + cantidad + " jugadores a " + nombre +
                ". Total ahora: " + cantidadJugadores);
    }

    // Getters y Setters (opcional)
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getPlataforma() {
        return plataforma;
    }

    public void setPlataforma(String plataforma) {
        this.plataforma = plataforma;
    }

    public int getCantidadJugadores() {
        return cantidadJugadores;
    }

    public void setCantidadJugadores(int cantidadJugadores) {
        this.cantidadJugadores = cantidadJugadores;
    }

    public static void main(String[] args) {
        // a) Instanciar al menos 2 videojuegos (usando sobrecarga del constructor)
        Videojuego v1 = new Videojuego("Minecraft", "PC", 5);
        Videojuego v2 = new Videojuego("FIFA 25");
        Videojuego v3 = new Videojuego();

        System.out.println("=== Videojuegos creados ===");
        v1.mostrarDatos();
        v2.mostrarDatos();
        v3.mostrarDatos();

        // c) Usar los métodos sobrecargados agregarJugadores()
        System.out.println("\n=== Agregando jugadores ===");
        v1.agregarJugadores();      // agrega 1 jugador
        v2.agregarJugadores(3);     // agrega 3 jugadores
        v3.agregarJugadores();      // agrega 1 jugador

        // Mostrar datos finales
        System.out.println("\n=== Datos finales ===");
        v1.mostrarDatos();
        v2.mostrarDatos();
        v3.mostrarDatos();
    }
}

