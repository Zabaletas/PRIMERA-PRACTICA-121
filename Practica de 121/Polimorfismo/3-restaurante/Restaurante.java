//Un restaurante organiza a su personal mediante las siguientes clases:
//Clase "Empleado" base para reutilizar atributos comunes
class Empleado {
    protected String nombre;
    protected float sueldoMes;

    public Empleado(String nombre, float sueldoMes) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
    }

    // c) Método para mostrar si el sueldo mensual es igual a X
    public void mostrarSiSueldoEs(float x) {
        if (sueldoMes == x) {
            System.out.println("Empleado: " + nombre + " - Sueldo: " + sueldoMes);
        }
    }

    public float sueldoTotal() {
        return sueldoMes;
    }
}

// Cocinero
class Cocinero extends Empleado {
    private int horasExtra;
    private float sueldoHora;

    public Cocinero(String nombre, float sueldoMes, int horasExtra, float sueldoHora) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
    }

    // b) Sueldo total con horas extra
    @Override
    public float sueldoTotal() {
        float total = sueldoMes + horasExtra * sueldoHora;
        System.out.println("Cocinero: " + nombre + " - Sueldo Total: " + total);
        return total;
    }
}

// Mesero
class Mesero extends Empleado {
    private int horasExtra;
    private float sueldoHora;
    private float propina;

    public Mesero(String nombre, float sueldoMes, int horasExtra, float sueldoHora, float propina) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
        this.propina = propina;
    }

    // b) Sueldo total con horas extra y propina
    @Override
    public float sueldoTotal() {
        float total = sueldoMes + horasExtra * sueldoHora + propina;
        System.out.println("Mesero: " + nombre + " - Sueldo Total: " + total);
        return total;
    }
}

// Administrativo
class Administrativo extends Empleado {
    private String cargo;

    public Administrativo(String nombre, float sueldoMes, String cargo) {
        super(nombre, sueldoMes);
        this.cargo = cargo;
    }

    // b) Sueldo total (sin extras)
    @Override
    public float sueldoTotal() {
        System.out.println("Administrativo: " + nombre + " - Sueldo Total: " + sueldoMes);
        return sueldoMes;
    }
}

// a) Clase principal (ejecución)
class Restaurante {
    public static void main(String[] args) {
        Cocinero c1 = new Cocinero("Carlos", 1800, 10, 20);
        Mesero m1 = new Mesero("Ana", 1500, 5, 15, 200);
        Mesero m2 = new Mesero("Luis", 1600, 8, 15, 150);
        Administrativo a1 = new Administrativo("María", 2000, "Gerente");
        Administrativo a2 = new Administrativo("Jorge", 1800, "Contador");

        System.out.println("=== SUELDOS TOTALES ===");
        c1.sueldoTotal();
        m1.sueldoTotal();
        m2.sueldoTotal();
        a1.sueldoTotal();
        a2.sueldoTotal();

        // c) Mostrar empleados con sueldo mensual igual a 1800
        System.out.println("\n=== EMPLEADOS CON SUELDO MENSUAL IGUAL A 1800 ===");
        float x = 1800;
        Empleado[] lista = { c1, m1, m2, a1, a2 };
        for (Empleado e : lista) {
            e.mostrarSiSueldoEs(x);
        }
    }
}
