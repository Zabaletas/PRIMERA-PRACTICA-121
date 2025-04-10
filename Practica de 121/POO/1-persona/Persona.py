#Crea una clase Persona con nombre, edad y ciudad
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    # a) Método para mostrar saludo
    def saludar(self):
        return f"Hola, soy {self.nombre} de {self.ciudad}"
    
    # c) Método para verificar mayoría de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

# b) Crear tres personas y mostrar su saludo
persona1 = Persona("Juan", 25, "Madrid")
persona2 = Persona("María", 17, "Barcelona")
persona3 = Persona("Carlos", 30, "Valencia")

print(persona1.saludar()) 
print(persona2.saludar()) 
print(persona3.saludar())  

print(f"{persona1.nombre} es mayor de edad: {persona1.es_mayor_de_edad()}")  
print(f"{persona2.nombre} es mayor de edad: {persona2.es_mayor_de_edad()}")  
print(f"{persona3.nombre} es mayor de edad: {persona3.es_mayor_de_edad()}")  