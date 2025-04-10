#Sea la clase Videojuego:
class Videojuego:
    # b) Sobrecargar el constructor simuladamente (uso de valores por defecto)
    def __init__(self, nombre="Desconocido", plataforma="Ninguna", cantidadJugadores=0):
        self.__nombre = nombre
        self.__plataforma = plataforma
        self.__cantidadJugadores = cantidadJugadores

    # c) Implementar un método mostrar()
    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Plataforma:", self.__plataforma)
        print("Cantidad de jugadores:", self.__cantidadJugadores)
        print("--------------------------")

    # d) Sobrecargar el método agregarJugadores (simulado por parámetros opcionales)
    def agregarJugadores(self, cantidad=1):
        self.__cantidadJugadores += cantidad

# a) Instanciar al menos 2 videojuegos
v1 = Videojuego()
v2 = Videojuego("FIFA 24", "PS5")
v3 = Videojuego("Minecraft", "PC", 2)

v1.mostrar()
v2.mostrar()
v3.mostrar()

v1.agregarJugadores()       # +1
v2.agregarJugadores(3)      # +3
v3.agregarJugadores(2)      # +2

print("Después de agregar jugadores:")
v1.mostrar()
v2.mostrar()
v3.mostrar()

