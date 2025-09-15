class Usuario:
    def __init__(self, id_usuario, nombre, correo, contraseña, telefono, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.telefono = telefono
        self.rol = rol

    def obtener_es_admin(self):    
        return True if self.rol == "admin" else False

def obtener_estado_usuario(usuario):
    print("-----------------")
    print(f"Nombre: {usuario.nombre}")
    print(f"mail: {usuario.correo}")
    print(f"Es admin o usuario: {'Admin' if usuario.obtener_es_admin() else 'Usuario'}")

usuario1 = Usuario(1, "Bruno", "brunorazzotti@gmail.com", "123", "36594595959", "admin")
usuario2 = Usuario(2, "Juan", "juanlopez@gmail.com", "123", "16168811", "usuario")
usuario3 = Usuario(3, "Clara", "clarita1977@gmail.com", "123", "785244556", "usuario")

usuarios = [usuario1,usuario2,usuario3]

def obtener_usuarios ():
    return usuarios

def setear_nuevo_usuario(usuario):
    usuarios.append(usuario)

usuario_logeado = False

def obtener_usuario_logeado():
    return usuario_logeado

def setear_usuario_logeado(usuario):
    global usuario_logeado
    usuario_logeado = usuario


  
    