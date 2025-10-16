from ...database.conectDB import conectarDB


class TurnoModel:
    def __init__(
        self,
        id=0,
        fecha_hora="",
        id_mascota=0,
        id_veterinario=0,
        id_servicio=0,
        estado="pendiente",
        notas="",
        fecha_creacion="",
    ):
        self.id = id
        self.fecha_hora = fecha_hora
        self.id_mascota = id_mascota
        self.id_veterinario = id_veterinario
        self.id_servicio = id_servicio
        self.estado = estado
        self.notas = notas
        self.fecha_creacion = fecha_creacion

    def serializar(self):
        return {
            "id": self.id,
            "fecha_hora": self.fecha_hora,
            "id_mascota": self.id_mascota,
            "id_veterinario": self.id_veterinario,
            "id_servicio": self.id_servicio,
            "estado": self.estado,
            "notas": self.notas,
            "fecha_creacion": self.fecha_creacion,
        }

    @staticmethod
    def deserializar(data: dict):
        return TurnoModel(
            id=data.get("id", 0),
            fecha_hora=data.get("fecha_hora", ""),
            id_mascota=data.get("id_mascota", 0),
            id_veterinario=data.get("id_veterinario", 0),
            id_servicio=data.get("id_servicio", 0),
            estado=data.get("estado", "pendiente"),
            notas=data.get("notas", ""),
            fecha_creacion=data.get("fecha_creacion", ""),
        )

    @staticmethod
    def obtener_turnos():
        conn = conectarDB.conectar()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return []
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM turnos")
                turnos = cursor.fetchall()
                return turnos
        except Exception as ex:
            print(f"Error al obtener turnos: {ex}")
            return []
        finally:
            conn.close()

    def obtener_turno(self):
        conn = conectarDB.conectar()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return False
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM turnos WHERE id = %s", (self.id,))
                turno = cursor.fetchone()
                return turno if turno else False
        except Exception as ex:
            print(f"Error al obtener el turno: {ex}")
            return False
        finally:
            conn.close()

    def crear_turno(self):
        conn = conectarDB.conectar()
        if conn is None:
            return False
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """
                    INSERT INTO turnos (fecha_hora, id_mascota, id_veterinario, id_servicio, estado, notas, fecha_creacion)
                    VALUES (%s, %s, %s, %s, %s, %s, NOW())
                    """,
                    (
                        self.fecha_hora,
                        self.id_mascota,
                        self.id_veterinario,
                        self.id_servicio,
                        self.estado,
                        self.notas,
                    ),
                )
            conn.commit()
            return True
        except Exception as ex:
            print(f"Error al crear el turno: {ex}")
            return False
        finally:
            conn.close()

    def modificar_turno(self):
        conn = conectarDB.conectar()
        if conn is None:
            return False
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """
                    UPDATE turnos SET fecha_hora=%s, id_mascota=%s, id_veterinario=%s, id_servicio=%s,
                    estado=%s, notas=%s WHERE id=%s
                    """,
                    (
                        self.fecha_hora,
                        self.id_mascota,
                        self.id_veterinario,
                        self.id_servicio,
                        self.estado,
                        self.notas,
                        self.id,
                    ),
                )
            conn.commit()
            return True
        except Exception as ex:
            print(f"Error al modificar el turno: {ex}")
            return False
        finally:
            conn.close()

    def eliminar_turno(self):
        conn = conectarDB.conectar()
        if conn is None:
            return False
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("DELETE FROM turnos WHERE id = %s", (self.id,))
            conn.commit()
            return True
        except Exception as ex:
            print(f"Error al eliminar el turno: {ex}")
            return False
        finally:
            conn.close()
