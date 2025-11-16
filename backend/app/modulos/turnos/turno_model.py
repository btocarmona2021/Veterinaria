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

    # ============================================================
    # SERIALIZAR
    # ============================================================

    def serializar(self, mascota=None, veterinario=None, servicio=None):
        data = {
            "id": self.id,
            "fecha_hora": self.fecha_hora,
            "estado": self.estado,
            "notas": self.notas,
            "fecha_creacion": self.fecha_creacion,
        }

        if mascota:
            data["mascota"] = mascota

        if veterinario:
            data["veterinario"] = veterinario

        if servicio:
            data["servicio"] = servicio

        return data

    # ============================================================
    # MÉTODOS ESTÁTICOS
    # ============================================================

    @staticmethod
    def obtener_turnos():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """
                    SELECT 
                        t.id, t.fecha_hora, t.estado, t.notas, t.fecha_creacion,
                        m.id AS mascota_id, m.nombre AS mascota_nombre, m.raza AS mascota_raza,
                        u.id AS vet_id, u.nombre AS vet_nombre, u.apellido AS vet_apellido,
                        s.id AS serv_id, s.nombre AS serv_nombre, s.precio AS serv_precio
                    FROM turnos t
                    JOIN mascotas m ON t.id_mascota = m.id
                    JOIN usuarios u ON t.id_veterinario = u.id
                    JOIN servicios s ON t.id_servicio = s.id
                    ORDER BY t.fecha_hora ASC
                    """
                )
                rows = cursor.fetchall()

            turnos = []
            for r in rows:
                turno = TurnoModel(
                    id=r["id"],
                    fecha_hora=r["fecha_hora"],
                    estado=r["estado"],
                    notas=r["notas"],
                    fecha_creacion=r["fecha_creacion"],
                )
                turnos.append(
                    turno.serializar(
                        mascota={
                            "id": r["mascota_id"],
                            "nombre": r["mascota_nombre"],
                            "raza": r["mascota_raza"],
                        },
                        veterinario={
                            "id": r["vet_id"],
                            "nombre": r["vet_nombre"],
                            "apellido": r["vet_apellido"],
                        },
                        servicio={
                            "id": r["serv_id"],
                            "nombre": r["serv_nombre"],
                            "precio": r["serv_precio"],
                        },
                    )
                )
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
                return cursor.fetchone()
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
                    fecha_hora=%s, id_mascota=%s, id_veterinario=%s, id_servicio=%s,
                    estado=%s, notas=%s
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
