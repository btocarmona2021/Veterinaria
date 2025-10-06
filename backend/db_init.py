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

# Tabla principal de usuarios con roles
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
    "  `especialidad` varchar(50) NULL COMMENT 'Solo para veterinarios',"
    "  `disponible` tinyint(1) DEFAULT 1 COMMENT 'Solo para veterinarios',"
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
    "  `edad` int,"
    "  `fecha_nacimiento` date,"
    "  `sexo` enum('Macho','Hembra'),"
    "  `color` varchar(30),"
    "  `peso` decimal(5,2),"
    "  `id_usuario` int(11) COMMENT 'Dueño (cliente)',"
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
    "  `duracion_estimada` int COMMENT 'Duración en minutos',"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

TABLES["turnos"] = (
    "CREATE TABLE `turnos` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `fecha_hora` datetime NOT NULL,"
    "  `id_mascota` int(11) NOT NULL,"
    "  `id_veterinario` int(11) COMMENT 'Usuario con rol veterinario',"
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
    "  `id_veterinario` int(11) COMMENT 'Usuario con rol veterinario',"
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

# Semillas para el sistema
SEEDS["usuarios"] = (
    "INSERT INTO usuarios (nombre, apellido, email, password, telefono, direccion, rol, especialidad, disponible) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    [
        # Administrador
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
        # Veterinarios
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
        # Clientes
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
    ],
)

SEEDS["mascotas"] = (
    "INSERT INTO mascotas (nombre, especie, raza, edad, fecha_nacimiento, sexo, color, peso, id_usuario) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    [
        ("Firulais", "Perro", "Labrador", 3, "2020-05-15", "Macho", "Dorado", 25.5, 4),
        ("Michi", "Gato", "Siamés", 2, "2021-02-20", "Hembra", "Blanco", 4.2, 5),
    ],
)

SEEDS["servicios"] = (
    "INSERT INTO servicios (nombre, descripcion, precio, duracion_estimada) "
    "VALUES (%s, %s, %s, %s)",
    [
        ("Consulta general", "Consulta veterinaria básica", 1500.00, 30),
        ("Vacunación", "Aplicación de vacunas", 2000.00, 20),
        ("Desparasitación", "Tratamiento antiparasitario", 1200.00, 15),
        ("Castración", "Procedimiento quirúrgico", 5000.00, 60),
        ("Urgencia", "Atención de emergencia", 3000.00, 45),
    ],
)

SEEDS["turnos"] = (
    "INSERT INTO turnos (fecha_hora, id_mascota, id_veterinario, id_servicio, estado, notas) "
    "VALUES (%s, %s, %s, %s, %s, %s)",
    [
        ("2023-06-15 10:00:00", 1, 2, 1, "completado", "Control anual"),
        ("2023-06-16 11:30:00", 2, 3, 2, "completado", "Vacuna antirrábica"),
    ],
)

SEEDS["historial_medico"] = (
    "INSERT INTO historial_medico (id_mascota, fecha, id_veterinario, diagnostico, tratamiento, observaciones, peso_actual, proxima_visita) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    [
        (
            1,
            "2023-06-15 10:00:00",
            2,
            "Saludable",
            "Ninguno",
            "Mascota en buen estado",
            25.5,
            "2024-06-15",
        ),
        (
            2,
            "2023-06-16 11:30:00",
            3,
            "Vacunación rutinaria",
            "Vacuna antirrábica",
            "Sin reacciones adversas",
            4.2,
            "2024-06-16",
        ),
    ],
)


# Funciones para crear la base de datos y tablas
def create_database(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'",
        )
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database already exists")
        else:
            print(err)
    else:
        print(f"Database {DB_NAME} created successfully.")


def create_tables(tables, cursor):
    cursor.execute(f"USE {DB_NAME}")
    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Creating table {table_name}: ", end="")
            cursor.execute(table_description)
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


def seeds_tables(seed, cursor):
    cursor.execute(f"USE {DB_NAME}")
    for table_name in seed:
        seed_description = seed[table_name]
        try:
            print(f"Seeding table {table_name}: ", end="")
            cursor.executemany(seed_description[0], seed_description[1])
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


# Conexión y ejecución
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
    print("Database setup completed successfully!")

except Error as err:
    print(f"Error: {err}")
finally:
    if "cursor" in locals() and cursor is not None:
        cursor.close()
    if "cxn" in locals() and cxn is not None:
        cxn.close()
