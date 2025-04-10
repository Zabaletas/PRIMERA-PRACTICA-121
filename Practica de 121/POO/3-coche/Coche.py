#Crea una clase Coche con marca, modelo y velocidad
class Coche:
    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
    
    # a) Método para acelerar (aumenta velocidad en 10)
    def acelerar(self):
        self.velocidad += 10
    
    # b) Método para frenar (disminuye velocidad en 5)
    def frenar(self):
        self.velocidad = max(0, self.velocidad - 5)
    
    def mostrar_velocidad(self):
        return f"{self.marca} {self.modelo}: Velocidad actual {self.velocidad} km/h"

# c) Crear dos coches y operar con ellos
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang", 30)

coche1.acelerar()
coche1.acelerar()
coche1.frenar()

coche2.acelerar()
coche2.frenar()
coche2.frenar()

print(coche1.mostrar_velocidad())
print(coche2.mostrar_velocidad())