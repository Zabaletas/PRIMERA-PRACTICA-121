//Se hace referencia a algunos animales mediante las siguientes clases:
class Perro {
    private String nombre;
    private int edad;
    private String raza;

    public Perro(String nombre, int edad, String raza) {
        this.nombre = nombre;
        this.edad = edad;
        this.raza = raza;
    }

    // b) hacerSonido()
    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Guau guau!");
    }

    // c) moverse()
    public void moverse() {
        System.out.println(nombre + " corre.");
    }
}

class Gato {
    private String nombre;
    private String color;

    public Gato(String nombre, String color) {
        this.nombre = nombre;
        this.color = color;
    }

    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Miau!");
    }

    public void moverse() {
        System.out.println(nombre + " salta.");
    }
}

class Pajaro {
    private String nombre;
    private String tipo;

    public Pajaro(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
    }

    public void hacerSonido() {
        System.out.println(nombre + " dice: ¡Pío pío!");
    }

    public void moverse() {
        System.out.println(nombre + " vuela.");
    }
}

class Animales {
    public static void main(String[] args) {
        // a) Instanciar 1 Perro, 1 Gato y 1 Pájaro
        Perro p1 = new Perro("Fido", 3, "Labrador");
        Gato g1 = new Gato("Michi", "Blanco");
        Pajaro pj1 = new Pajaro("Piolín", "Canario");

        System.out.println("=== SONIDOS ===");
        p1.hacerSonido();
        g1.hacerSonido();
        pj1.hacerSonido();

        System.out.println("\n=== MOVIMIENTO ===");
        p1.moverse();
        g1.moverse();
        pj1.moverse();
    }
}
