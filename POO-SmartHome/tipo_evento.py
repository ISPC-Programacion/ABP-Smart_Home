class Automatizacion:
    def __init__(self, nombre):
        self.nombre = nombre 

    def ejecutar(self):
        print(f"Ejecutando la automatización {self.nombre}")  

    def __str__(self):
        return f"Evento: {self.nombre}"
              

class AutomatizacionModoAhorro(Automatizacion):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.estado = False 

    def obtener_estado(self):
        return "ACTIVADO" if self.estado else "DESACTIVADO"

    def cambiar_estado(self):
        self.estado = not self.estado
        print(f"{self.nombre} ahora está {self.obtener_estado()}")

    def ejecutar(self):
        print(f"Ejecutando {self.nombre} (estado: {self.obtener_estado()})")       

modo_ahorro = AutomatizacionModoAhorro("Modo Ahorro Energía")
print(modo_ahorro.obtener_estado())
modo_ahorro.cambiar_estado()
modo_ahorro.ejecutar()         


if __name__ == "__main__":
    evento_prueba = Automatizacion("Alarma activada")
    print(f"Se creó un tipo de evento: {evento_prueba}")