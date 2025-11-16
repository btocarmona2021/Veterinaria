from ...database.conectDB import conectarDB
from werkzeug.security import generate_password_hash, check_password_hash


class UsuarioModel:
    def __init__(
        self,
        id=None,
        nombre="",
        apellido="",
        email="",
        password="",
        telefono="",
        direccion="",
        rol="cliente",
        especialidad=None, 
        disponible=True,
        fecha_registro=None, 
        activo=True,
    ):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.telefono = telefono
        self.direccion = direccion
        self.rol = rol
        self.especialidad = especialidad
        self.disponible = disponible
        self.fecha_registro = fecha_registro
        self.activo = activo

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "rol": self.rol,
            "especialidad": self.especialidad,
            "disponible": self.disponible,
            "fecha_registro": self.fecha_registro,
            "activo": self.activo,
        }

    @staticmethod
    def obtener_usuarios():
        conn = conectarDB.conectar()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return []

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM usuarios")
                return cursor.fetchall()
        except Exception as ex:
            print(f"Error al obtener usuarios: {ex}")
            return []
        finally:
            conn.close()

    def obtener_usuario(self):
        conn = conectarDB.conectar()
        if conn is None:
            print("No se puede conectar a la base de datos")
            return False

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id=%s", (self.id,))
                return cursor.fetchone()
        except Exception as ex:
            print(f"Error al obtener usuario: {ex}")
            return False
        finally:
            conn.close()

    def crear_usuario(self):
        conn = conectarDB.conectar()
        if conn is None:
            return False

        password_encriptado = generate_password_hash(self.password, method="sha256")

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """
                    INSERT INTO usuarios 
                    (nombre, apellido, email, password, telefono, direccion, rol, especialidad, disponible, activo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        self.nombre,
                        self.apellido,
                        self.email,
                        password_encriptado,
                        self.telefono,
                        self.direccion,
                        self.rol,
                        self.especialidad,
                        self.disponible,
                        self.activo,
                    ),
                )
                conn.commit()
                return cursor.lastrowid 
        except Exception as ex:
            print(f"Error al crear usuario: {ex}")
            return False
        finally:
            conn.close()

    def modificar_usuario(self):
        conn = conectarDB.conectar()
        if conn is None:
            return False

        password_encriptado = generate_password_hash(self.password, method="sha256")

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """
                    UPDATE usuarios
                    SET nombre=%s, apellido=%s, email=%s, password=%s, telefono=%s,
                        direccion=%s, rol=%s, especialidad=%s, disponible=%s, activo=%s
                    WHERE id=%s
                    """,
                    (
                        self.nombre,
                        self.apellido,
                        self.email,
                        password_encriptado,
                        self.telefono,
                        self.direccion,
                        self.rol,
                        self.especialidad,
                        self.disponible,
                        self.activo,
                        self.id,
                    ),
                )
                conn.commit()
                return cursor.rowcount > 0
        except Exception as ex:
            print(f"Error al modificar usuario: {ex}")
            return False
        finally:
            conn.close()

    def eliminar_usuario(self):
        conn = conectarDB.conectar()
        if conn is None:
            return False

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id=%s", (self.id,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as ex:
            print(f"Error al eliminar usuario: {ex}")
            return False
        finally:
            conn.close()
