package p1a1e2;

public class Bus {
    private int Capacidad;
    private int Pasajeros;
    private double CostoPasaje;

    public Bus(int Capacidad) {
        this.Capacidad = Capacidad;
        this.Pasajeros = 0;
        this.CostoPasaje = 1.50;
    }

    public void SubirPasajeros(int Cantidad) {
        if (Pasajeros + Cantidad <= Capacidad) {
            Pasajeros += Cantidad;
            System.out.println("Subieron " + Cantidad + " pasajeros. Total: " + Pasajeros);
        } else {
            System.out.println("No hay suficientes asientos disponibles.");
        }
    }

    public double CobrarPasaje() {
        double total = Pasajeros * CostoPasaje;
        System.out.println("Total cobrado: Bs. " + total);
        return total;
    }

    public int AsientosDisponibles() {
        int disponibles = Capacidad - Pasajeros;
        System.out.println("Asientos disponibles: " + disponibles);
        return disponibles;
    }

    public void MostrarInfo() {
        System.out.println("Capacidad: " + Capacidad + ", Pasajeros: " + Pasajeros + ", Costo: Bs." + CostoPasaje);
    }

    public static void main(String[] args) {
        Bus bus1 = new Bus(60);
        bus1.SubirPasajeros(45);
        bus1.CobrarPasaje();
        bus1.AsientosDisponibles();
        bus1.MostrarInfo();
    }
}
