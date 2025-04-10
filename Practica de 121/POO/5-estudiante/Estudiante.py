#Crea una clase Estudiante con nombre, nota_1, nota_2
class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
    # a) Método para calcular el promedio
    def calcular_promedio(self):
        return (self.nota1 + self.nota2) / 2
    # b) Método para verificar si aprobó
    def aprobo(self):
        return self.calcular_promedio() >= 6
    def mostrar_resultado(self):
        return f"{self.nombre} - Promedio: {self.calcular_promedio():.1f} - Aprobó: {self.aprobo()}"
# c) Crear tres estudiantes y mostrar resultados
if __name__ == "__main__":
    estudiante1 = Estudiante("Juan", 7.5, 8.0)
    estudiante2 = Estudiante("María", 5.0, 6.5)
    estudiante3 = Estudiante("Carlos", 4.0, 3.5)

    print(estudiante1.mostrar_resultado())
    print(estudiante2.mostrar_resultado())
    print(estudiante3.mostrar_resultado())