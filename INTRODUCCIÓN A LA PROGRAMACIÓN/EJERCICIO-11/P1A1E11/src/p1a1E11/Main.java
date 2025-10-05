package p1a1E11;

public class Main {
    public static void main(String[] args) {
        Cliente cliente1 = new Cliente("Andrea", "Cafe con leche y pastel");
        Empleado empleado1 = new Empleado("Carlos", "Barista");

        cliente1.mostrar();
        empleado1.mostrar();
    }
}
