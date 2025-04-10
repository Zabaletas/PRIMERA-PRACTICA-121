//Realiza la abstracción de una Computadora
public class Computadora {
    // Componentes principales
    private String procesador;
    private int ramGB;
    private int almacenamientoGB;
    private String tarjetaGrafica;
    private boolean encendida;

    public Computadora(String procesador, int ramGB, int almacenamientoGB, String tarjetaGrafica) {
        this.procesador = procesador;
        this.ramGB = ramGB;
        this.almacenamientoGB = almacenamientoGB;
        this.tarjetaGrafica = tarjetaGrafica;
        this.encendida = false; // Por defecto apagada
    }

    // a) Mostrar componentes
    public void mostrarComponentes() {
        System.out.println("\nComponentes de la computadora:");
        System.out.println("Procesador: " + procesador);
        System.out.println("RAM: " + ramGB + "GB");
        System.out.println("Almacenamiento: " + almacenamientoGB + "GB");
        System.out.println("Tarjeta gráfica: " + tarjetaGrafica);
    }

    // b) Mostrar estado
    public void mostrarEstado() {
        System.out.println("\nEstado de la computadora:");
        System.out.println("Encendida: " + (encendida ? "Sí" : "No"));
    }

    public void encender() {
        if (!encendida) {
            encendida = true;
            System.out.println("\nLa computadora se está encendiendo...");
            System.out.println("BIOS iniciando...");
            System.out.println("Sistema operativo cargando...");
            System.out.println("¡Computadora lista!");
        } else {
            System.out.println("\nLa computadora ya está encendida");
        }
    }

    public void apagar() {
        if (encendida) {
            encendida = false;
            System.out.println("\nLa computadora se está apagando...");
            System.out.println("Guardando configuración...");
            System.out.println("¡Computadora apagada!");
        } else {
            System.out.println("\nLa computadora ya está apagada");
        }
    }

    // c) Ejemplo de uso
    public static void main(String[] args) {
        Computadora miPC = new Computadora("Intel Core i7", 16, 512, "NVIDIA RTX 3060");

        miPC.mostrarComponentes();

        miPC.mostrarEstado();

        miPC.encender();
        miPC.mostrarEstado();

        miPC.apagar();
        miPC.mostrarEstado();
    }
}