//Crea una clase Persona con nombre, edad y ciudad
public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    // a) Método para mostrar saludo
    public String saludar() {
        return "Hola, soy " + this.nombre + " de " + this.ciudad;
    }

    // c) Método para verificar mayoría de edad
    public boolean esMayorDeEdad() {
        return this.edad >= 18;
    }

    // b) Main para crear tres personas y mostrar su saludo
    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan", 25, "Madrid");
        Persona persona2 = new Persona("María", 17, "Barcelona");
        Persona persona3 = new Persona("Carlos", 30, "Valencia");

        System.out.println(persona1.saludar());
        System.out.println(persona2.saludar());
        System.out.println(persona3.saludar());

        System.out.println(persona1.nombre + " es mayor de edad: " + persona1.esMayorDeEdad());
        System.out.println(persona2.nombre + " es mayor de edad: " + persona2.esMayorDeEdad());
        System.out.println(persona3.nombre + " es mayor de edad: " + persona3.esMayorDeEdad());
    }
}