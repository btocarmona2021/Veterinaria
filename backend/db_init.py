import mysql.connector
from mysql.connector import Error, errorcode
import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
    "raise_on_warnings": True,
}

TABLES = {}
SEEDS = {}

TABLES["usuarios"] = (
    "CREATE TABLE `usuarios` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `apellido` varchar(100) NULL,"
    "  `email` varchar(100) NOT NULL UNIQUE,"
    "  `password` varchar(255) NOT NULL,"
    "  `telefono` varchar(20) NULL,"
    "  `direccion` varchar(100) NULL,"
    "  `rol` enum('administrador','veterinario','cliente') NOT NULL,"
    "  `especialidad` varchar(50) NULL,"
    "  `disponible` tinyint(1) DEFAULT 1,"
    "  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,"
    "  `activo` tinyint(1) DEFAULT 1,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

TABLES["mascotas"] = (
    "CREATE TABLE `mascotas` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `especie` varchar(30) NOT NULL,"
    "  `raza` varchar(50),"
    "  `fecha_nacimiento` date,"
    "  `sexo` enum('Macho','Hembra'),"
    "  `color` varchar(30),"
    "  `peso` decimal(5,2),"
    "  `id_usuario` int(11),"
    "  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`id_usuario`) REFERENCES `usuarios`(`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

TABLES["servicios"] = (
    "CREATE TABLE `servicios` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `descripcion` text,"
    "  `precio` decimal(10,2),"
    "  `duracion_estimada` int,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

TABLES["turnos"] = (
    "CREATE TABLE `turnos` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `fecha_hora` time NOT NULL,"
    "  `id_mascota` int(11) NOT NULL,"
    "  `id_veterinario` int(11),"
    "  `id_servicio` int(11),"
    "  `estado` enum('pendiente','confirmado','completado','cancelado') DEFAULT 'pendiente',"
    "  `notas` text,"
    "  `fecha_creacion` datetime DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`id_mascota`) REFERENCES `mascotas`(`id`),"
    "  FOREIGN KEY (`id_veterinario`) REFERENCES `usuarios`(`id`),"
    "  FOREIGN KEY (`id_servicio`) REFERENCES `servicios`(`id`)"
    ") ENGINE=InnoDB"
)

TABLES["historial_medico"] = (
    "CREATE TABLE `historial_medico` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `id_mascota` int(11) NOT NULL,"
    "  `fecha` datetime NOT NULL,"
    "  `id_veterinario` int(11),"
    "  `diagnostico` text,"
    "  `tratamiento` text,"
    "  `observaciones` text,"
    "  `peso_actual` decimal(5,2),"
    "  `proxima_visita` date,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`id_mascota`) REFERENCES `mascotas`(`id`),"
    "  FOREIGN KEY (`id_veterinario`) REFERENCES `usuarios`(`id`)"
    ") ENGINE=InnoDB"
)


SEEDS["usuarios"] = (
    "INSERT INTO usuarios (nombre, apellido, email, password, telefono, direccion, rol, especialidad, disponible) "
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    [
        (
            "Admin",
            "Sistema",
            "admin@vet.com",
            "$2y$10$Hn...",
            "111111111",
            "Calle Admin 1",
            "administrador",
            None,
            1,
        ),
        (
            "Laura",
            "García",
            "laura@vet.com",
            "$2y$10$Hn...",
            "222222222",
            "Calle Vet 1",
            "veterinario",
            "General",
            1,
        ),
        (
            "Carlos",
            "Méndez",
            "carlos@vet.com",
            "$2y$10$Hn...",
            "333333333",
            "Calle Vet 2",
            "veterinario",
            "Cirugía",
            1,
        ),
        (
            "Juan",
            "Pérez",
            "juan@cliente.com",
            "$2y$10$Hn...",
            "444444444",
            "Calle Cliente 1",
            "cliente",
            None,
            1,
        ),
        (
            "María",
            "Gómez",
            "maria@cliente.com",
            "$2y$10$Hn...",
            "555555555",
            "Calle Cliente 2",
            "cliente",
            None,
            1,
        ),
        (
            "Pedro",
            "Lopez",
            "pedro@cliente.com",
            "$2y$10$Hn...",
            "555111222",
            "Casa 3",
            "cliente",
            None,
            1,
        ),
        (
            "Ana",
            "Torres",
            "ana@cliente.com",
            "$2y$10$Hn...",
            "551223344",
            "Casa 4",
            "cliente",
            None,
            1,
        ),
        (
            "Lucas",
            "Rivas",
            "lucas@vet.com",
            "$2y$10$Hn...",
            "551119988",
            "Vet 3",
            "veterinario",
            "Dermatología",
            1,
        ),
        (
            "Sofía",
            "Martinez",
            "sofia@cliente.com",
            "$2y$10$Hn...",
            "551111222",
            "Casa 8",
            "cliente",
            None,
            1,
        ),
        (
            "Diego",
            "Suarez",
            "diego@cliente.com",
            "$2y$10$Hn...",
            "559998877",
            "Casa 9",
            "cliente",
            None,
            1,
        ),
    ],
)

SEEDS["mascotas"] = (
    "INSERT INTO mascotas (nombre, especie, raza,fecha_nacimiento, sexo, color, peso, id_usuario) "
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
    [
        ("Firulais", "Perro", "Labrador", "2020-05-15", "Macho", "Dorado", 25.5, 4),
        ("Michi", "Gato", "Siamés","2021-02-20", "Hembra", "Blanco", 4.2, 5),
        ("Rocky", "Perro", "Pitbull","2019-07-11", "Macho", "Gris", 30.1, 6),
        ("Luna", "Gato", "Mestizo","2022-08-14", "Hembra", "Negro", 3.5, 7),
        ("Toby", "Perro", "Beagle","2018-03-02", "Macho", "Tricolor", 10.2, 9),
        ("Nala", "Gato", "Persa","2020-11-20", "Hembra", "Crema", 5.4, 10),
        ("Max", "Perro", "Ovejero","2017-10-01", "Macho", "Negro", 34.0, 4),
        ("Kira", "Gato", "Bengalí","2021-09-17", "Hembra", "Dorado", 4.8, 5),
        ("Coco", "Perro", "Caniche","2016-04-09", "Macho", "Blanco", 8.0, 6),
        ("Milo", "Gato", "Mestizo","2019-06-25", "Macho", "Gris", 4.0, 7),
    ],
)

SEEDS["servicios"] = (
    "INSERT INTO servicios (nombre, descripcion, precio, duracion_estimada) "
    "VALUES (%s,%s,%s,%s)",
    [
        ("Consulta general", "Consulta veterinaria básica", 1500, 30),
        ("Vacunación", "Aplicación de vacunas", 2000, 20),
        ("Desparasitación", "Tratamiento antiparasitario", 1200, 15),
        ("Castración", "Procedimiento quirúrgico", 5000, 60),
        ("Urgencia", "Atención de emergencia", 3000, 45),
        ("Radiografía", "Estudios por imagen", 4500, 40),
        ("Baño", "Baño y cepillado", 2500, 50),
        ("Corte de uñas", "Servicio rápido", 800, 10),
        ("Limpieza dental", "Higiene bucal", 3500, 35),
        ("Guardería", "Cuidado diario", 7000, 480),
    ],
)

SEEDS["turnos"] = (
    "INSERT INTO turnos (fecha_hora, id_mascota, id_veterinario, id_servicio, estado, notas) "
    "VALUES (%s,%s,%s,%s,%s,%s)",
    [
        ("2023-01-10 09:00:00", 1, 2, 1, "completado", "Control general"),
        ("2023-01-12 10:30:00", 2, 3, 2, "completado", "Vacunación"),
        ("2023-02-03 11:00:00", 3, 2, 3, "pendiente", "Desparasitación anual"),
        ("2023-02-10 09:45:00", 4, 8, 5, "confirmado", "Atención urgente"),
        ("2023-03-01 14:00:00", 5, 2, 4, "pendiente", "Castración programada"),
        ("2023-03-15 15:30:00", 6, 3, 7, "pendiente", "Baño completo"),
        ("2023-04-20 12:20:00", 7, 8, 9, "completado", "Limpieza dental"),
        ("2023-05-17 13:00:00", 8, 3, 8, "confirmado", "Corte de uñas"),
        ("2023-06-08 16:00:00", 9, 2, 6, "pendiente", "Radiografía de control"),
        ("2023-07-21 17:40:00", 10, 8, 1, "pendiente", "Consulta por tos"),
    ],
)

SEEDS["historial_medico"] = (
    "INSERT INTO historial_medico (id_mascota, fecha, id_veterinario, diagnostico, tratamiento, observaciones, peso_actual, proxima_visita) "
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
    [
        (
            1,
            "2023-01-10 09:00:00",
            2,
            "Control sano",
            "Ninguno",
            "Buen estado",
            25.5,
            "2024-01-10",
        ),
        (
            2,
            "2023-01-12 10:30:00",
            3,
            "Vacunación completa",
            "Aplicación vacuna",
            "Sin efectos",
            4.2,
            "2024-01-12",
        ),
        (
            3,
            "2023-02-03 11:00:00",
            2,
            "Parásitos leves",
            "Desparasitante",
            "Mejorando",
            30.1,
            "2023-08-03",
        ),
        (
            4,
            "2023-02-10 09:45:00",
            8,
            "Golpe leve",
            "Antiinflamatorios",
            "Reposo",
            3.5,
            "2023-03-10",
        ),
        (
            5,
            "2023-03-01 14:00:00",
            2,
            "Revisión pre-cirugía",
            "Ninguno",
            "Apto",
            10.2,
            "2023-03-15",
        ),
        (
            6,
            "2023-03-15 15:30:00",
            3,
            "Dermatitis",
            "Corticoides",
            "Control en 1 mes",
            5.4,
            "2023-04-15",
        ),
        (
            7,
            "2023-04-20 12:20:00",
            8,
            "Tártaro dental",
            "Limpieza",
            "Sin complicaciones",
            34.0,
            "2024-04-20",
        ),
        (
            8,
            "2023-05-17 13:00:00",
            3,
            "Garras largas",
            "Corte de uñas",
            "Normal",
            4.8,
            "2023-11-17",
        ),
        (
            9,
            "2023-06-08 16:00:00",
            2,
            "Sospecha fractura",
            "Radiografía",
            "Estudio enviado",
            8.0,
            "2023-07-08",
        ),
        (
            10,
            "2023-07-21 17:40:00",
            8,
            "Tos leve",
            "Jarabe",
            "Observación",
            4.0,
            "2023-08-21",
        ),
    ],
)


def create_database(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'",
        )
    except Error as err:
        print(err)
    else:
        print(f"Database {DB_NAME} created successfully.")


def create_tables(tables, cursor):
    cursor.execute(f"USE {DB_NAME}")
    for name in tables:
        try:
            print(f"Creating table {name}: ", end="")
            cursor.execute(tables[name])
        except Error as err:
            print(err.msg)
        else:
            print("OK")


def seeds_tables(seed, cursor):
    cursor.execute(f"USE {DB_NAME}")
    for name in seed:
        try:
            print(f"Seeding table {name}: ", end="")
            cursor.executemany(seed[name][0], seed[name][1])
        except Error as err:
            print(err.msg)
        else:
            print("OK")


try:
    cxn = mysql.connector.connect(**DB_CONFIG)
    cursor = cxn.cursor()

    create_database(cursor)

    CONF_DB = DB_CONFIG.copy()
    CONF_DB["database"] = DB_NAME
    cxn = mysql.connector.connect(**CONF_DB)
    cursor = cxn.cursor()

    create_tables(TABLES, cursor)
    seeds_tables(SEEDS, cursor)

    cxn.commit()
    print("Database configuracion completada!")

except Error as err:
    print(f"Error: {err}")
finally:
    if "cursor" in locals():
        cursor.close()
    if "cxn" in locals():
        cxn.close()
