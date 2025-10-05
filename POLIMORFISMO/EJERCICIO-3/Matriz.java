package Ejercicio3;

public class Matriz {
    private float[][] matriz;

    public Matriz() {
        matriz = new float[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                matriz[i][j] = (i == j) ? 1.0f : 0.0f;
            }
        }
    }

    public Matriz(float[][] m) {
        matriz = new float[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                matriz[i][j] = m[i][j];
            }
        }
    }

    public Matriz sumar(Matriz m) {
        Matriz resultado = new Matriz();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado.matriz[i][j] = this.matriz[i][j] + m.matriz[i][j];
            }
        }
        return resultado;
    }

    public Matriz restar(Matriz m) {
        Matriz resultado = new Matriz();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado.matriz[i][j] = this.matriz[i][j] - m.matriz[i][j];
            }
        }
        return resultado;
    }
    public boolean igual(Matriz m) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (this.matriz[i][j] != m.matriz[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    public void mostrar() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        float[][] m2 = new float[10][10];
        m2[0][0] = 5;
        m2[1][1] = 2; 

        Matriz A = new Matriz();    
        Matriz B = new Matriz(m2);  

        System.out.println("Matriz A (Identidad):");
        A.mostrar();

        System.out.println("\nMatriz B:");
        B.mostrar();

        Matriz C = A.sumar(B);
        System.out.println("\nA + B:");
        C.mostrar();

        Matriz D = A.restar(B);
        System.out.println("\nA - B:");
        D.mostrar();

        System.out.println("\nA es igual a B? " + (A.igual(B) ? "Si" : "No"));
    }
}
