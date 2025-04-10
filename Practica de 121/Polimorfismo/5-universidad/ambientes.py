#Se hace referencia a algunos de los diferentes ambientes de la Universidad mediante las siguientes clases:
# Clase Oficina
class Oficina:
    def __init__(self, sillas, escritorios, estanterias):
        self.__nroSillas = sillas
        self.__nroEscritorios = escritorios
        self.__nroEstanterias = estanterias

    # b) mostrar()
    def mostrar(self):
        print(f"Oficina -> Sillas: {self.__nroSillas}, Escritorios: {self.__nroEscritorios}, Estanterías: {self.__nroEstanterias}")

    # c) cantidadMuebles()
    def cantidadMuebles(self):
        return self.__nroSillas + self.__nroEscritorios + self.__nroEstanterias

# Clase Aula
class Aula:
    def __init__(self, nombre, capacidad, pupitres):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__nroPupitres = pupitres

    def mostrar(self):
        print(f"Aula '{self.__nombre}' -> Capacidad: {self.__capacidad}, Pupitres: {self.__nroPupitres}")

    def cantidadMuebles(self):
        return self.__nroPupitres

# Clase Laboratorio
class Laboratorio:
    def __init__(self, nombre, capacidad, mesas, sillas):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__nroMesas = mesas
        self.__nroSillas = sillas

    def mostrar(self):
        print(f"Laboratorio '{self.__nombre}' -> Capacidad: {self.__capacidad}, Mesas: {self.__nroMesas}, Sillas: {self.__nroSillas}")

    def cantidadMuebles(self):
        return self.__nroMesas + self.__nroSillas

# a) Crear objetos
o1 = Oficina(4, 2, 1)
o2 = Oficina(6, 3, 2)
a1 = Aula("A-101", 30, 30)
a2 = Aula("A-102", 25, 25)
l1 = Laboratorio("Lab Física", 20, 10, 20)

# Mostrar datos
print("=== MOSTRAR DATOS ===")
o1.mostrar()
o2.mostrar()
a1.mostrar()
a2.mostrar()
l1.mostrar()

# Mostrar cantidad de muebles
print("\n=== CANTIDAD DE MUEBLES ===")
print(f"Oficina 1: {o1.cantidadMuebles()} muebles")
print(f"Oficina 2: {o2.cantidadMuebles()} muebles")
print(f"Aula 1: {a1.cantidadMuebles()} muebles")
print(f"Aula 2: {a2.cantidadMuebles()} muebles")
print(f"Laboratorio: {l1.cantidadMuebles()} muebles")
