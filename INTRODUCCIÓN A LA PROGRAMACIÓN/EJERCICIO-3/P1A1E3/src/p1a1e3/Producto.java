package p1a1e3;

public class Producto {
    private String Nombre;
    private double Precio;
    private int Stock;

    public Producto(String Nombre, double Precio, int Stock) {
        this.Nombre = Nombre;
        this.Precio = Precio;
        this.Stock = Stock;
    }

    public void Vender(int Cantidad) {
        if (Cantidad <= Stock) {
            Stock -= Cantidad;
            System.out.println("Se vendieron " + Cantidad + " unidades de " + Nombre + ".");
        } else {
            System.out.println("No hay suficiente stock para realizar la venta.");
        }
    }

    public void Reabastecer(int Cantidad) {
        Stock += Cantidad;
        System.out.println("Se reabastecieron " + Cantidad + " unidades. Stock actual: " + Stock);
    }

    public void MostrarInfo() {
        System.out.println("Producto: " + Nombre + " | Precio: Bs." + Precio + " | Stock: " + Stock);
    }

    public static void main(String[] args) {
        Producto producto1 = new Producto("Refresco", 5.00, 20);
        producto1.MostrarInfo();
        producto1.Vender(5);
        producto1.MostrarInfo();
        producto1.Reabastecer(10);
        producto1.MostrarInfo();
    }
}