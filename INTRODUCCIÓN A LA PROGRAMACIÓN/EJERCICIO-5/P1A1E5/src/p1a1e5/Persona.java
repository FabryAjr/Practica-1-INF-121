package p1a1e5;

public class Persona {
    private String Nombre;
    private String Paterno;
    private String Materno;
    private int Edad;
    private String Ci;

    public Persona(String Nombre, String Paterno, String Materno, int Edad, String Ci) {
        this.Nombre = Nombre;
        this.Paterno = Paterno;
        this.Materno = Materno;
        this.Edad = Edad;
        this.Ci = Ci;
    }

    public void MostrarDatos() {
        System.out.println("Nombre Completo: " + Nombre + " " + Paterno + " " + Materno);
        System.out.println("Edad: " + Edad + " años | CI: " + Ci);
    }

    public boolean MayorDeEdad() {
        if (Edad >= 18) {
            System.out.println(Nombre + " es mayor de edad.");
            return true;
        } else {
            System.out.println(Nombre + " es menor de edad.");
            return false;
        }
    }

    public void ModificarEdad(int Nuevo) {
        System.out.println("Edad anterior: " + Edad);
        Edad = Nuevo;
        System.out.println("Nueva edad: " + Edad);
    }

    public boolean TieneMismoPaterno(Persona Otra) {
        return this.Paterno.equalsIgnoreCase(Otra.Paterno);
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Kevin", "Arze", "Cachi", 21, "10017630");
        Persona persona2 = new Persona("Luis", "Arze", "Jonz", 37, "7654351");

        persona1.MostrarDatos();
        persona2.MostrarDatos();

        persona1.MayorDeEdad();
        persona2.MayorDeEdad();

        persona2.ModificarEdad(18);
        System.out.println("¿Tienen el mismo apellido paterno? " + persona1.TieneMismoPaterno(persona2));
    }
}
