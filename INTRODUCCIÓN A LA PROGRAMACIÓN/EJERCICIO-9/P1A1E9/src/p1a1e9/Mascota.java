package p1a1e9;

public class Mascota {
    private String Nombre;
    private String Tipo;
    private int Energia;

    public Mascota(String Nombre, String Tipo, int Energia) {
        this.Nombre = Nombre;
        this.Tipo = Tipo;
        this.Energia = Energia;
    }

    public void Alimentar() {
        Energia += 20;
        if (Energia > 100) {
            Energia = 100;
        }
        System.out.println(Nombre + " ha sido alimentado. Energía actual: " + Energia);
    }

    public void Jugar() {
        Energia -= 15;
        if (Energia < 0) {
            Energia = 0;
        }
        System.out.println(Nombre + " ha jugado. Energía actual: " + Energia);
    }

    public void MostrarInfo() {
        System.out.println("Mascota: " + Nombre + " | Tipo: " + Tipo + " | Energía: " + Energia);
    }

    public static void main(String[] args) {
        Mascota mascota1 = new Mascota("Firulais", "Perro", 60);
        Mascota mascota2 = new Mascota("Michi", "Gato", 80);

        mascota1.MostrarInfo();
        mascota1.Alimentar();
        mascota1.Jugar();

        mascota2.MostrarInfo();
        mascota2.Jugar();
        mascota2.Alimentar();
    }
}
