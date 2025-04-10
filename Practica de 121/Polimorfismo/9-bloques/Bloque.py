class Bloque:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def accion(self):
        print(f"Acción genérica en bloque {self.tipo}")
    
    def colocar(self, orientacion="suelo"):
        print(f"Bloque {self.tipo} colocado en {orientacion}")
    
    def romper(self):
        print(f"Bloque {self.tipo} roto")

# a) Creación de clases específicas para cada tipo de bloque
class BloqueCofre(Bloque):
    def __init__(self, capacidad, resistencia, tipo="cofre"):
        super().__init__(tipo)
        self.capacidad = capacidad
        self.resistencia = resistencia
    
    # b) Sobrescribir método accion()
    def accion(self):
        print(f"Abriendo cofre con capacidad {self.capacidad} items")
    
    # c) Sobrecargar método colocar()
    def colocar(self, orientacion="suelo", junto_a=None):
        if junto_a:
            print(f"Cofre colocado en {orientacion} junto a {junto_a}")
        else:
            print(f"Cofre colocado en {orientacion}")
    
    # d) Sobrescribir método romper()
    def romper(self):
        print(f"¡Cuidado! Al romper el cofre pierdes los items dentro")
        super().romper()

class BloqueTnt(Bloque):
    def __init__(self, tipo="tnt", daño=10):
        super().__init__(tipo)
        self.daño = daño
    
    # b) Sobrescribir método accion()
    def accion(self):
        print(f"¡La TNT explotó causando {self.daño} puntos de daño!")
    
    # c) Sobrecargar método colocar()
    def colocar(self, orientacion="suelo", con_redstone=False):
        if con_redstone:
            print(f"TNT colocada en {orientacion} con mecanismo de redstone")
        else:
            print(f"TNT colocada en {orientacion}")
    
    # d) Sobrescribir método romper()
    def romper(self):
        print("¡BOOM! La TNT explotó al romperla")

class BloqueHorno(Bloque):
    def __init__(self, color, capacidad_comida, tipo="horno"):
        super().__init__(tipo)
        self.color = color
        self.capacidad_comida = capacidad_comida
    
    # b) Sobrescribir método accion()
    def accion(self):
        print(f"Cocinando comida en horno {self.color}")
    
    # c) Sobrecargar método colocar()
    def colocar(self, orientacion="suelo", combustible=None):
        if combustible:
            print(f"Horno {self.color} colocado en {orientacion} con {combustible}")
        else:
            print(f"Horno {self.color} colocado en {orientacion}")
    
    # d) Sobrescribir método romper()
    def romper(self):
        print(f"Rompiendo horno {self.color} - ¡Cuidado con los items cocinados!")
        super().romper()

# a) Instanciar 2 bloques de cada tipo
cofre1 = BloqueCofre(27, 10)
cofre2 = BloqueCofre(54, 15, "cofre grande")

tnt1 = BloqueTnt()
tnt2 = BloqueTnt("tnt super", 20)

horno1 = BloqueHorno("negro", 3)
horno2 = BloqueHorno("blanco", 5, "horno mejorado")

# b) Demostrar método accion() sobrescrito
print("\nAcciones de los bloques:")
cofre1.accion()
tnt1.accion()
horno1.accion()

# c) Demostrar método colocar() sobrecargado
print("\nColocando bloques:")
cofre2.colocar("pared", "otro cofre")
tnt2.colocar("techo", True)
horno2.colocar("suelo", "carbón")

# d) Demostrar método romper() sobrescrito
print("\nRompiendo bloques:")
cofre1.romper()
tnt1.romper()
horno1.romper()