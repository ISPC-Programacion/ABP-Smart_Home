from datetime import datetime

class Evento:
    def __init__(self,id_evento, id_dispositivo, id_tipo_evento, fecha=None):
        self.id_evento = id_evento
        self.id_dispositivo = id_dispositivo
        self.id_tipo_evento = id_tipo_evento
        self.fecha = fecha if fecha else datetime.now()   
     

    def mostrar_evento(self):
        print(f"Evento: {self.id_evento}")
        print(f"Dispositivo ID: {self.id_dispositivo}")
        print(f"Tipo Evento ID: {self.id_tipo_evento}") 
        print(f"Fecha: {self.fecha} ")  
         

evento1 = Evento(1, 25, 4)
evento2 = Evento(2, 6, 2, fecha=datetime(2000, 3, 6, 10, 10))

evento1.mostrar_evento()
evento2.mostrar_evento()