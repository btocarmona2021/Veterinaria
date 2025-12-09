from ...database.conectDB import conectarDB


class ServicioModel:
    def __init__(self, id=0, nombre="", descripcion="", precio=0, duracion_estimada=0):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.duracion_estimada = duracion_estimada

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "duracion_estimada": self.duracion_estimada,
        }

    @staticmethod
    def obtener_servicios():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM servicios")
                rows = cursor.fetchall()
                return rows
        except Exception as e:
            print(f"Error al obtener los servicios: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def obtener_servicio(id):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM servicios WHERE id = %s", (id,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener el servicio: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def crear_servicio(data):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO servicios (nombre, descripcion, precio, duracion_estimada)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        data["nombre"],
                        data["descripcion"],
                        data["precio"],
                        data["duracion_estimada"],
                    ),
                )
                conn.commit()
                return cursor.lastrowid
        except Exception as e:
            print(f"Error al crear el servicio: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def modificar_servicio(id, data):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE servicios 
                    SET nombre=%s, descripcion=%s, precio=%s, duracion_estimada=%s
                    WHERE id=%s
                    """,
                    (
                        data["nombre"],
                        data["descripcion"],
                        data["precio"],
                        data["duracion_estimada"],
                        id,
                    ),
                )
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al modificar el servicio: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar_servicio(id):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM servicios WHERE id = %s", (id,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar el servicio: {e}")
            return False
        finally:
            conn.close()
