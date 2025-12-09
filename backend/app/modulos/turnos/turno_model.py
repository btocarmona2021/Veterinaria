from ...database.conectDB import conectarDB


class TurnoModel:
    def __init__(
        self,
        id=0,
        fecha_hora="",
        id_mascota=0,
        id_veterinario=0,
        id_servicio=0,
        estado="",
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
            "fecha_hora": str(self.fecha_hora),
            "estado": self.estado,
            "notas": self.notas,
            "fecha_creacion": self.fecha_creacion,
            "id_mascota": self.id_mascota,
            "id_veterinario": self.id_veterinario,
            "id_servicio": self.id_servicio,
        }

    @staticmethod
    def obtener_turnos():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM turnos ORDER BY fecha_hora ASC")
                rows = cursor.fetchall()

            turnos = []
            for r in rows:
                turno = TurnoModel(
                    id=r["id"],
                    fecha_hora=r["fecha_hora"],
                    id_mascota=r["id_mascota"],
                    id_veterinario=r["id_veterinario"],
                    id_servicio=r["id_servicio"],
                    estado=r["estado"],
                    notas=r["notas"],
                    fecha_creacion=r["fecha_creacion"],
                )
                turnos.append(turno.serializar())

            return turnos

        except Exception as e:
            print("ERROR EN obtener_turnos:", e)
            return []
        finally:
            conn.close()

    @staticmethod
    def obtener_turno(id):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM turnos WHERE id=%s", (id,))
                row = cursor.fetchone()

                if not row:
                    return None

                turno = TurnoModel(
                    id=row["id"],
                    fecha_hora=row["fecha_hora"],
                    id_mascota=row["id_mascota"],
                    id_veterinario=row["id_veterinario"],
                    id_servicio=row["id_servicio"],
                    estado=row["estado"],
                    notas=row["notas"],
                    fecha_creacion=row["fecha_creacion"],
                )

                return turno.serializar()

        except Exception as e:
            print("ERROR obtener_turno:", e)
            return None
        finally:
            conn.close()

    @staticmethod
    def crear_turno(data):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO turnos 
                    (fecha_hora, id_mascota, id_veterinario, id_servicio, estado, notas, fecha_creacion)
                    VALUES (%s,%s,%s,%s,%s,%s,NOW())
                    """,
                    (
                        data["fecha_hora"],
                        data["id_mascota"],
                        data["id_veterinario"],
                        data["id_servicio"],
                        data.get("estado", "pendiente"),
                        data.get("notas", ""),
                    ),
                )
                conn.commit()
                return cursor.lastrowid
        except Exception as e:
            print("ERROR crear_turno:", e)
            return None
        finally:
            conn.close()

    @staticmethod
    def modificar_turno(id, data):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE turnos SET 
                        fecha_hora=%s,
                        id_mascota=%s,
                        id_veterinario=%s,
                        id_servicio=%s,
                        estado=%s,
                        notas=%s
                    WHERE id=%s
                    """,
                    (
                        data["fecha_hora"],
                        data["id_mascota"],
                        data["id_veterinario"],
                        data["id_servicio"],
                        data["estado"],
                        data["notas"],
                        id,
                    ),
                )
                conn.commit()
                return True
        except Exception as e:
            print("ERROR modificar_turno:", e)
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar_turno(id):
        conn = conectarDB.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM turnos WHERE id=%s", (id,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print("ERROR eliminar_turno:", e)
            return False
        finally:
            conn.close()
