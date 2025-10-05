package p1a1E11;

public class Cliente {
    private String Nombre;
    private String Pedido;

    public Cliente(String Nombre, String Pedido) {
        this.Nombre = Nombre;
        this.Pedido = Pedido;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public String getPedido() {
        return Pedido;
    }

    public void setPedido(String Pedido) {
        this.Pedido = Pedido;
    }

    public void mostrar() {
        System.out.println("Cliente: " + Nombre + ", Pedido: " + Pedido);
    }
}
