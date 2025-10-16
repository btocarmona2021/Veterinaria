from ...database.conectDB import conectarDB
from ..usuarios.usuario_model import UsuarioModel as Usuario


class MascotaModel:
    def __init__(
        self,
        id=0,
        nombre="",
        especie="",
        raza="",
        edad=0,
        fecha_nacimiento="",
        sexo="",
        color="",
        peso="",
        usuario=Usuario,
        fecha_registro="",
    ):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.color = color
        self.peso = peso
        self.usuario = usuario
        self.fecha_registro = fecha_registro

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especie": self.especie,
            "raza": self.raza,
            "edad": self.edad,
            "fecha_nacimiento": self.fecha_nacimiento,
            "sexo": self.sexo,
            "color": self.color,
            "peso": self.peso,
            "usuario": self.usuario,
            "fecha_registro": self.fecha_registro,
        }

    @staticmethod
    def deserializar(data: dict):
        return dataModel(
            id=data("id", 0),
            nombre=data("nombre", ""),
            especie=data("especie", ""),
            raza=data("raza", ""),
            edad=data("edad", 0),
            fecha_nacimiento=data("fecha_nacimiento", ""),
            sexo=data("sexo", ""),
            color=data("color", ""),
            peso=data("peso", 0),
            usuario=data("usuario", None),
            fecha_registro=data("fecha_registro", ""),
        )

    @staticmethod
    def obtener_mascotas():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM mascotas")
                maskotas = cursor.fetchall()
                return maskotas
        except Exception as e:
            print(f"Error al obtener las datas: {e}")
            return []
        finally:
            conn.close()

    def obtener_mascota(self):
        conn = conectarDB.conectar()
        if not self.id:
            return None
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM mascotas WHERE id = %s", (self.id,))
                data = cursor.fetchone()
                if data:
                    print(data)
                    return data
                else:
                    return None
        except Exception as e:
            print(f"Error al obtener la data: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def crear_mascota(data: dict):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO datas (nombre, especie, raza, edad, fecha_nacimiento, sexo, color, peso, id_usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        data["nombre"],
                        data["especie"],
                        data["raza"],
                        data["edad"],
                        data["fecha_nacimiento"],
                        data["sexo"],
                        data["color"],
                        data["peso"],
                        data["usuario"],
                    ),
                )
                conn.commit()
                lastRow = cursor.lastrowid
                if lastRow:
                    return True
                else:
                    return None
        except Exception as e:
            print(f"Error al crear la data: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def modificar_mascota(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE mascotas SET nombre = %s, especie = %s, raza = %s, edad = %s, fecha_nacimiento = %s, sexo = %s, color = %s, peso = %s WHERE id = %s",
                    (
                        self.nombre,
                        self.especie,
                        self.raza,
                        self.edad,
                        self.fecha_nacimiento,
                        self.sexo,
                        self.color,
                        self.peso,
                        self.id,
                    ),
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Error al modificar la data: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar_mascota(self):
        if not self.id:
            return False
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM mascotas WHERE id = %s", (self.id,))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error al eliminar la data: {e}")
            return False
        finally:
            conn.close()
