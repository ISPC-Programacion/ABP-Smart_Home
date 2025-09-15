from dispositivo import Dispositivo, DispositivoGrabacion, DispositivoTemperatura

class TipoDispositivo:
    def __init__(self, id_tipo_dispositivo, nombre):
        self.id_tipo_dispositivo = id_tipo_dispositivo
        self.nombre = nombre

    def mostrar_info(self):
        return f"ID: {self.id_tipo_dispositivo}, Nombre: {self.nombre}"
    
dispositivo1 = Dispositivo("Luces cochera")
dispositivo2 = Dispositivo("Luces entrada")
dispositivo3 = DispositivoGrabacion("Camaras dormitorio")
dispositivo4 = DispositivoTemperatura("Heladera quincho")
	
devices = [dispositivo1, dispositivo2, dispositivo3, dispositivo4]

def get_devices():	
	return devices


if __name__ == "__main__":
    for d in get_devices():
        print(d.id_dispositivo)