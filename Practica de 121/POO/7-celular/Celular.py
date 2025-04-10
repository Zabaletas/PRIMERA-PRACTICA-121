#Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
class Celular:
    def __init__(self):
        self.espacio_disponible = 1024  # MB
        self.max_aplicaciones = 20
        self.aplicaciones = []
        self.bateria = 100  # Porcentaje
    
    # a) Método para instalar aplicación
    def instalar_aplicacion(self, nombre, tamaño):
        if len(self.aplicaciones) >= self.max_aplicaciones:
            print("No hay espacio para más aplicaciones (límite de 20 alcanzado)")
            return False
        if self.espacio_disponible < tamaño:
            print(f"No hay suficiente espacio para instalar {nombre} (necesita {tamaño}MB)")
            return False
        
        self.aplicaciones.append({"nombre": nombre, "tamaño": tamaño})
        self.espacio_disponible -= tamaño
        print(f"Aplicación {nombre} instalada correctamente")
        return True
    
    # b) Método para usar aplicación con consumo de batería
    def usar_aplicacion(self, nombre, minutos):
        if self.bateria <= 0:
            print("Celular apagado. No se puede usar aplicaciones.")
            return
        
        app = next((a for a in self.aplicaciones if a["nombre"] == nombre), None)
        if not app:
            print(f"Aplicación {nombre} no encontrada")
            return
        
        ciclos = minutos / 10
        if app["tamaño"] > 250:
            consumo = 5 * ciclos
        elif app["tamaño"] > 100:
            consumo = 2 * ciclos
        else:
            consumo = 1 * ciclos
        
        if self.bateria - consumo <= 0:
            self.bateria = 0
            print(f"Usando {nombre} por {minutos} minutos... Celular apagado!")
        else:
            self.bateria -= consumo
            print(f"Usando {nombre} por {minutos} minutos. Batería consumida: {consumo}%")
    
    # c) Método para mostrar batería
    def estado_bateria(self):
        print(f"Batería restante: {self.bateria}%")
        if self.bateria <= 0:
            print("Celular apagado")

mi_celular = Celular()

mi_celular.instalar_aplicacion("WhatsApp", 80)
mi_celular.instalar_aplicacion("Facebook", 280)
mi_celular.instalar_aplicacion("Juego Pesado", 350)

mi_celular.usar_aplicacion("WhatsApp", 30)
mi_celular.estado_bateria()

mi_celular.usar_aplicacion("Facebook", 20)
mi_celular.estado_bateria()

# d) Simular apagado por batería
mi_celular.usar_aplicacion("Juego Pesado", 60)
mi_celular.estado_bateria()
mi_celular.usar_aplicacion("WhatsApp", 10) 