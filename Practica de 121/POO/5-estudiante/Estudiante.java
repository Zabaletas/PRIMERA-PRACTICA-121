//Crea una clase Estudiante con nombre, nota_1, nota_2
public class Estudiante {
    private String nombre;
    private double nota1;
    private double nota2;

    public Estudiante(String nombre, double nota1, double nota2) {
        this.nombre = nombre;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }

    // a Método para calcular el promedio
    public double calcularPromedio() {
        return (nota1 + nota2) / 2;
    }

    // b Método para verificar si aprobó
    public boolean aprobo() {
        return calcularPromedio() >= 6;
    }

    // c Crear tres estudiantes y mostrar resultados
    public static void main(String[] args) {
        Estudiante estudiante1 = new Estudiante("Juan", 7.5, 8.0);
        Estudiante estudiante2 = new Estudiante("María", 5.0, 6.5);
        Estudiante estudiante3 = new Estudiante("Carlos", 4.0, 3.5);

        System.out.println(estudiante1.nombre + " - Promedio: " + estudiante1.calcularPromedio() +
                " - Aprobó: " + estudiante1.aprobo());
        System.out.println(estudiante2.nombre + " - Promedio: " + estudiante2.calcularPromedio() +
                " - Aprobó: " + estudiante2.aprobo());
        System.out.println(estudiante3.nombre + " - Promedio: " + estudiante3.calcularPromedio() +
                " - Aprobó: " + estudiante3.aprobo());
    }
}