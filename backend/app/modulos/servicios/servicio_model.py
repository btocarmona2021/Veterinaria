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
    def deserializar(data:dict):
        return ServicioModel(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
            descripcion=data.get("descripcion", ""),
            precio=data.get("precio", 0),
            duracion_estimada=data.get("duracion_estimada", 0),
        )

    @staticmethod
    def obtener_servicios():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM servicios")
                servicios = cursor.fetchall()
        except Exception as e:
            print(f'Error al obtener los servicios: {e}')
            servicios = []  
        finally:
            conn.close()
            
    @staticmethod
    def obtener_servicio(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM servicios WHERE id = %s", (self.id,))
                servicio = cursor.fetchone()
                if servicio:
                    return servicio
                else:
                    return None
        except Exception as e:
            print(f'Error al obtener el servicio: {e}')
            return None
        finally:
            conn.close()
        
    @staticmethod
    def crear_servicio(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO servicios (nombre, descripcion, precio, duracion_estimada) VALUES (%s, %s, %s, %s)",
                    (self.nombre, self.descripcion, self.precio, self.duracion_estimada)
                )
                conn.commit()
                lastRow = cursor.lastrowid
                if lastRow:
                    return True
                else:
                    return None
        except Exception as e:
            print(f'Error al crear el servicio: {e}')
            return False
        finally:
            conn.close()
    @staticmethod
    def mmodificar_servicio(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE servicios SET nombre = %s, descripcion = %s, precio = %s, duracion_estimada = %s WHERE id = %s",
                    (self.nombre, self.descripcion, self.precio, self.duracion_estimada, self.id)
                )
                conn.commit()
                return True
        except Exception as e:
            print(f'Error al actualizar el servicio: {e}')
            return False
        finally:
            conn.close()
    
    @staticmethod
    def eliminar_servicio(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM servicios WHERE id = %s", (self.id,))
                conn.commit()
                return True
        except Exception as e:
            print(f'Error al eliminar el servicio: {e}')
            return False
        finally:
            conn.close()
            
            