package p1a1E11;

public class Empleado {
    private String Nombre;
    private String Rol;

    public Empleado(String Nombre, String Rol) {
        this.Nombre = Nombre;
        this.Rol = Rol;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public String getRol() {
        return Rol;
    }

    public void setRol(String Rol) {
        this.Rol = Rol;
    }

    public void mostrar() {
        System.out.println("Empleado: " + Nombre + ", Rol: " + Rol);
    }
}
