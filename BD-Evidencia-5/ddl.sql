CREATE TABLE Usuario (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  correo VARCHAR(50) UNIQUE NOT NULL,
  contraseña VARCHAR(50) NOT NULL,
  telefono VARCHAR(20)
);

CREATE TABLE TipoDispositivo (
  id_tipo_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Dispositivo (
  id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
  esencial BOOLEAN,
  configuracion VARCHAR(100),
  estado VARCHAR(20),
  id_tipo_dispositivo INT,
  id_usuario INT,
  FOREIGN KEY (id_tipo_dispositivo) REFERENCES TipoDispositivo(id_tipo_dispositivo),
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
  FOREIGN KEY (id_evento) REFERENCES Evento(id_evento)
);

CREATE TABLE TipoEvento (
  id_tipo_evento INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Evento (
  id_evento INT AUTO_INCREMENT PRIMARY KEY,
  id_dispositivo INT,
  fecha_generacion DATETIME,
  id_tipo_evento INT,
  FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo),
  FOREIGN KEY (id_tipo_evento) REFERENCES TipoEvento(id_tipo_evento)
);

