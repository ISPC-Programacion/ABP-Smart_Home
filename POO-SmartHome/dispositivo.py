class Dispositivo:
    def __init__(self, id_dispositivo, esencial=False, configuracion=None, estado=False, tipo_dispositivo=None, usuario=None):
        self.id_dispositivo = id_dispositivo
        self.esencial = esencial
        self.configuracion = configuracion
        self.estado = estado
        self.tipo_dispositivo = tipo_dispositivo
        self.usuario = usuario

    def obtener_estado(self):
        return "Prendido" if self.estado else "Apagado"

    def es_esencial(self):
        return "Sí" if self.esencial else "No"

class DispositivoGrabacion(Dispositivo):
    def __init__(self, nombre, estado=False, esencial=False, grabando=False):
        super().__init__(id_dispositivo=nombre, estado=estado, esencial=esencial)
        self.grabando = grabando

    def obtener_estado_grabacion(self):
        return "Grabando" if self.grabando else "No grabando"

class DispositivoTemperatura(Dispositivo):
    def __init__(self, nombre, estado=False, esencial=False, temperatura=0):
        super().__init__(id_dispositivo=nombre, estado=estado, esencial=esencial)
        self.temperatura = temperatura

    def mostrar_temperatura(self):
        return f"{self.temperatura}°C"
