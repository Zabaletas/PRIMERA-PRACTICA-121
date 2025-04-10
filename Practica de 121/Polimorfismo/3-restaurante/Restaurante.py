#Un restaurante organiza a su personal mediante las siguientes clases:
# Clase "Empleado" base para reutilizar atributos comunes
class Empleado:
    def __init__(self, nombre, sueldoMes):
        self._nombre = nombre
        self._sueldoMes = sueldoMes
    # c) Método para mostrar si el sueldo mensual es igual a X
    def mostrarSiSueldoEs(self, x):
        if self._sueldoMes == x:
            print(f"Empleado: {self._nombre} - Sueldo: {self._sueldoMes}")
# Clase Cocinero
class Cocinero(Empleado):
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora):
        super().__init__(nombre, sueldoMes)
        self.__horasExtra = horasExtra
        self.__sueldoHora = sueldoHora
    # b) Método sobrecargado: sueldo total
    def sueldoTotal(self):
        total = self._sueldoMes + (self.__horasExtra * self.__sueldoHora)
        print(f"Cocinero: {self._nombre} - Sueldo Total: {total}")
        return total
# Clase Mesero
class Mesero(Empleado):
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora, propina):
        super().__init__(nombre, sueldoMes)
        self.__horasExtra = horasExtra
        self.__sueldoHora = sueldoHora
        self.__propina = propina
    # b) Método sobrecargado: sueldo total
    def sueldoTotal(self):
        total = self._sueldoMes + (self.__horasExtra * self.__sueldoHora) + self.__propina
        print(f"Mesero: {self._nombre} - Sueldo Total: {total}")
        return total
# Clase Administrativo
class Administrativo(Empleado):
    def __init__(self, nombre, sueldoMes, cargo):
        super().__init__(nombre, sueldoMes)
        self.__cargo = cargo
    # b) Método sobrecargado: sueldo total (sin horas extra)
    def sueldoTotal(self):
        print(f"Administrativo: {self._nombre} - Sueldo Total: {self._sueldoMes}")
        return self._sueldoMes
# a) Instanciar objetos
c1 = Cocinero("Carlos", 1800, 10, 20)
m1 = Mesero("Ana", 1500, 5, 15, 200)
m2 = Mesero("Luis", 1600, 8, 15, 150)
a1 = Administrativo("María", 2000, "Gerente")
a2 = Administrativo("Jorge", 1800, "Contador")
# Mostrar sueldos totales
print("=== SUELDOS TOTALES ===")
c1.sueldoTotal()
m1.sueldoTotal()
m2.sueldoTotal()
a1.sueldoTotal()
a2.sueldoTotal()
# c) Mostrar empleados cuyo sueldo mensual es igual a X
print("\n=== EMPLEADOS CON SUELDO MENSUAL IGUAL A 1800 ===")
x = 1800
for emp in [c1, m1, m2, a1, a2]:
    emp.mostrarSiSueldoEs(x)
