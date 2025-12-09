from ...database.conectDB import conectarDB
from ..usuarios.usuario_model import UsuarioModel


class MascotaModel:
    def __init__(
        self,
        id=0,
        nombre="",
        especie="",
        raza="",
        fecha_nacimiento="",
        sexo="",
        color="",
        peso=0,
        id_usuario=None,
        fecha_registro="",
    ):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.color = color
        self.peso = peso
        self.id_usuario = id_usuario
        self.fecha_registro = fecha_registro

    def serializar(self):
        data = {
            "id": self.id,
            "nombre": self.nombre,
            "especie": self.especie,
            "raza": self.raza,
            "fecha_nacimiento": self.fecha_nacimiento,
            "sexo": self.sexo,
            "color": self.color,
            "peso": self.peso,
            "id_usuario": self.id_usuario,
            "fecha_registro": self.fecha_registro,
        }

        if self.id_usuario:
            duenio = UsuarioModel(id=self.id_usuario).obtener_usuario()
            if duenio:
                duenio.pop("password", None)  # Seguridad
                data["duenio"] = duenio

        return data

    @staticmethod
    def obtener_mascotas():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM mascotas")
                rows = cursor.fetchall()

                mascotas = []
                for m in rows:
                    mascota = MascotaModel(**m)
                    mascotas.append(mascota.serializar())
                return mascotas
        finally:
            conn.close()

    @staticmethod
    def obtener_mascota(id):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM mascotas WHERE id = %s", (id,))
                m = cursor.fetchone()
                if not m:
                    return None
                mascota = MascotaModel(**m)
                return mascota.serializar()
        finally:
            conn.close()

    @staticmethod
    def crear_mascota(data):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO mascotas 
                    (nombre, especie, raza,fecha_nacimiento, fecha_registro, sexo, color, peso, id_usuario)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        data["nombre"],
                        data["especie"],
                        data["raza"],
                        data["fecha_nacimiento"],
                        data["fecha_registro"],
                        data["sexo"],
                        data["color"],
                        data["peso"],
                        data["id_usuario"],
                    ),
                )
                conn.commit()
                return cursor.lastrowid
        finally:
            conn.close()

    @staticmethod
    def modificar_mascota(id, data):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE mascotas SET 
                    nombre=%s, especie=%s, raza=%s,fecha_nacimiento=%s, fecha_registro=%s,
                    sexo=%s, color=%s, peso=%s, id_usuario=%s
                    WHERE id=%s
                    """,
                    (
                        data["nombre"],
                        data["especie"],
                        data["raza"],
                        data["fecha_nacimiento"],
                        data["fecha_registro"],
                        data["sexo"],
                        data["color"],
                        data["peso"],
                        data["id_usuario"],
                        id,
                    ),
                )
                conn.commit()
                return True
        finally:
            conn.close()

    @staticmethod
    def eliminar_mascota(id):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM mascotas WHERE id = %s", (id,))
                conn.commit()
                return cursor.rowcount > 0
        finally:
            conn.close()
