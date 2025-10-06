from ...database.conectDB import conectarDB
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioModel:
    def __init__(
        self,
        id=0,
        nombre="",
        apellido="",
        email="",
        password="",
        telefono="",
        direccion="",
        rol="cliente",
        especialidad="",
        disponible=True,
        fecha_registro="",
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
    def deserializar(data: dict):
        return UsuarioModel(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
            apellido=data.get("apellido", ""),
            email=data.get("email", ""),
            password=data.get("password", ""),
            telefono=data.get("telefono", ""),
            direccion=data.get("direccion", ""),
            rol=data.get("rol", "cliente"),
            especialidad=data.get("especialidad", ""),
            disponible=data.get("disponible", True),
            fecha_registro=data.get("fecha_registro", ""),
            activo=data.get("activo", True),
        )

    @staticmethod
    def obtener_usuarios():
        conn = conectarDB.conectar()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return []
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM usuarios")
                usuarios = cursor.fetchall()
                return usuarios
        except Exception as ex:
            print(f"Something went wrong {ex}")
            return []
        finally:
            conn.close()


    def obtener_usuario(self):
        conn = conectarDB.conectar()
        if conn is None:
            print("No se puede conectar a la base de datos")
            return []
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id=%s", (self.id,))
                usuario = cursor.fetchone()
                if usuario:
                    return usuario
                else:
                    return False
        except Exception as ex:
            print(f"Ha ocurrido un error {ex}")
        finally:
            conn.close()


    def crear_usuario(self):
        conn = conectarDB.conectar()
        password_encriptado = generate_password_hash(self.password, method='sha256')
        
        if conn is None:
            return []
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "INSERT INTO usuarios (id, nombre, apellido, email, password, telefono, direccion, rol, especialidad, disponible, fecha_registro, activo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.id,
                        self.nombre,
                        self.apellido,
                        self.email,
                        password_encriptado,
                        self.telefono,
                        self.direccion,
                        self.rol,
                        self.especialidad,
                        self.disponible,
                        self.fecha_registro,
                        self.activo,
                    ),
                )
            conn.commit()
            registro = cursor.lastrowid
            if registro:
                return True
            else:
                return False
        except Exception as ex:
            print(f"Ha ocurrido un error {ex}")
            return False
        finally:
            conn.close()
    
    
    def modificar_usuario(self):
        conn = conectarDB.conectar()
        password_encriptado = generate_password_hash(self.password,)
        
        if conn is None:
            return []
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "UPDATE usuarios SET nombre=%s, apellido=%s, email=%s, password=%s, telefono=%s, direccion=%s, rol=%s, especialidad=%s, disponible=%s, fecha_registro=%s, activo=%s WHERE id=%s",
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
                        self.fecha_registro,
                        self.activo,
                        self.id,
                    ),
                )
            conn.commit()
            return True
        except Exception as ex:
            return (f"Ha ocurrido un error {ex}")
        finally:
            conn.close()
            
    def eliminar_usuario(self):
        conn = conectarDB.conectar()
        if conn is None:
            return []
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id=%s", (self.id,))
            conn.commit()
            return True
        except Exception as ex:
            print({ex})
            return False
        finally:
            conn.close()