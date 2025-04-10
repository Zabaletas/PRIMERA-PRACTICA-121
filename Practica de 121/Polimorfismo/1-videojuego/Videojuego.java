//Sea la clase Videojuego:
class Videojuego {
    // Atributos privados
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    // b) Sobrecargar el constructor 2 veces
    public Videojuego() {
        this.nombre = "Desconocido";
        this.plataforma = "Ninguna";
        this.cantidadJugadores = 0;
    }

    public Videojuego(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = 0;
    }

    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }
    // c) Implementar un método mostrar()
    public void mostrar() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Cantidad de jugadores: " + cantidadJugadores);
        System.out.println("--------------------------");
    }
    // d) Sobrecargar el método agregarJugadores()
    public void agregarJugadores() {
        this.cantidadJugadores += 1;
    }
    public void agregarJugadores(int cantidad) {
        this.cantidadJugadores += cantidad;
    }
    public static void main(String[] args) {
        // a) Instanciar al menos 2 videojuegos
        Videojuego v1 = new Videojuego();
        Videojuego v2 = new Videojuego("FIFA 24", "PS5");
        Videojuego v3 = new Videojuego("Minecraft", "PC", 2);

        v1.mostrar();
        v2.mostrar();
        v3.mostrar();

        v1.agregarJugadores(); // +1
        v2.agregarJugadores(3); // +3
        v3.agregarJugadores(2); // +2

        System.out.println("Después de agregar jugadores:");
        v1.mostrar();
        v2.mostrar();
        v3.mostrar();
    }
}