from ...database.conectDB import conectarDB
from werkzeug.security import generate_password_hash, check_password_hash


class UsuarioModel:
    def __init__(
        self,
        id=None,
        nombre="",
        apellido="",
        email="",
        password=None,
        telefono=None,
        direccion=None,
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
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return []
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM usuarios ORDER BY id ASC")
                usuarios = cursor.fetchall()
                return usuarios if usuarios else []
        except Exception as ex:
            print(f"Error al obtener usuarios: {ex}")
            return []
        finally:
            conn.close()

    def obtener_usuario(self):
        conn = conectarDB.conectar()
        if not conn:
            print("No se puede conectar a la base de datos")
            return None
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id=%s", (self.id,))
                return cursor.fetchone()
        except Exception as ex:
            print(f"Error al obtener usuario: {ex}")
            return None
        finally:
            conn.close()

    def crear_usuario(self):
        conn = conectarDB.conectar()
        if not conn:
            return False
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT COUNT(*) AS total FROM usuarios")
                resultado = cursor.fetchone()
                sin_usuarios = resultado['total'] == 0

                rol_final = 'administrador' if sin_usuarios else self.rol

                cursor.execute(
                    """
                    INSERT INTO usuarios 
                    (nombre, apellido, email, password, telefono, direccion, rol, especialidad, disponible, activo, fecha_registro)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
                    """,
                    (
                        self.nombre,
                        self.apellido,
                        self.email,
                        self.generar_password(self.password) if self.password else None,
                        self.telefono,
                        self.direccion,
                        rol_final,
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

    @staticmethod
    def modificar_usuario(id, data):
        conn = conectarDB.conectar()
        if not conn:
            return False

        try:
            # Hashear password solo si vino una nueva
            password_hash = None
            if "password" in data and data["password"]:
                password_hash = generate_password_hash(data["password"])

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """
                    UPDATE usuarios SET 
                        nombre=%s,
                        apellido=%s,
                        email=%s,
                        password=%s,
                        telefono=%s,
                        direccion=%s,
                        rol=%s,
                        especialidad=%s,
                        disponible=%s,
                        activo=%s
                    WHERE id=%s
                    """,
                    (
                        data.get("nombre"),
                        data.get("apellido"),
                        data.get("email"),
                        password_hash,
                        data.get("telefono"),
                        data.get("direccion"),
                        data.get("rol"),
                        data.get("especialidad"),
                        data.get("disponible"),
                        data.get("activo"),
                        id,
                    ),
                )
                conn.commit()

                return cursor.rowcount > 0
        except Exception as e:
            print("Error en modificar_usuario:", e)
            return False
        finally:
            conn.close()

    def eliminar_usuario(self):
        conn = conectarDB.conectar()
        if not conn:
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

    def generar_password(self, password: str) -> str:
        return generate_password_hash(password)

    def chequear_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
    
    
    @staticmethod
    def obtener_usuario_por_email(email: str):
        conn = conectarDB.conectar()
        if not conn:
            return None
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
                return cursor.fetchone()
        except Exception as ex:
            print(f"Error al obtener usuario por email: {ex}")
            return None
        finally:
            conn.close()

