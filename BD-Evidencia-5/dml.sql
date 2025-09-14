insert into Usuario (nombre , correo, contraseña, telefono) 
values ('ricardo', 'ricardo@gmail.com', 'ricardo123', '351-35484415'),
('manuel', 'manuel@gmail.com', 'manuel123', '351-35484414'),
('sofia', 'sofia@gmail.com', 'sofia123', '351-35484413'),
('roger', 'roger@gmail.com', 'roger123', '351-35484412'),
('lara', 'lara@gmail.com', 'lara123', '351-35484411'),
('cristian', 'cristian@gmail.com', 'cristian123', '351-35484410');

select * from Usuario;

insert into TipoDispositivo (nombre) 
values ('camara'),
('termotanque'),
('luz'),
('estufa electrica'),
('heladera'),
('televisor');

select * from TipoDispositivo;

insert into Dispositivo (esencial , configuracion, estado, id_tipo_dispositivo, id_usuario) 
values (false , 'smartfd3.v', 'prendido', 1 , 1),
(true , 'hotcustom2.0', 'prendido', 2 , 2),
(true , 'led', 'prendido', 3 , 3),
(false , 'calentador.v', 'prendido', 4 , 4),
(false , 'frigo.v', 'prendido', 5 ,5),
(false , 'smart.v', 'prendido', 6 , 6);

select * from Dispositivo;

insert into TipoEvento (nombre) 
values ('Ahorro'),
('Mantener'),
('Mantener'),
('Ahorro'),
('Ahorro'),
('Ahorro');

select * from TipoEvento;

insert into Evento (fecha_generacion, id_dispositivo, id_tipo_evento) 
values ('2025-01-15', 1 , 1),
('2025-11-05', 2 , 2),
('2025-06-09', 3 , 3),
('2025-01-19', 4, 4),
('2025-01-22', 5, 5),
('2025-04-18', 6, 6);

select * from Evento;