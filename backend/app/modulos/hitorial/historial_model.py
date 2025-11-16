from ...database.conectDB import conectarDB


class HistorialModel:

    # =====================================================
    # OBTENER TODOS
    # =====================================================
    @staticmethod
    def obtener_historial():
        db = conectarDB.conectar()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT 
                h.id,
                h.fecha,
                h.diagnostico,
                h.tratamiento,
                h.observaciones,
                h.peso_actual,
                h.proxima_visita,

               
                m.nombre AS mascota_nombre,
                m.especie,
                m.raza,

                
                v.nombre AS veterinario_nombre,
                v.apellido AS veterinario_apellido,
                v.especialidad AS veterinario_especialidad

            FROM historial_medico h
            LEFT JOIN mascotas m ON h.id_mascota = m.id
            LEFT JOIN usuarios v ON h.id_veterinario = v.id
            ORDER BY h.fecha DESC
        """

        cursor.execute(query)
        return cursor.fetchall()

    # =====================================================
    # OBTENER UNO POR ID
    # =====================================================
    @staticmethod
    def obtener_por_id(id_historial):
        db = conectarDB.conectar()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT 
                h.id,
                h.fecha,
                h.diagnostico,
                h.tratamiento,
                h.observaciones,
                h.peso_actual,
                h.proxima_visita,

                
                m.nombre AS mascota_nombre,
                m.especie,
                m.raza,

                
                v.nombre AS veterinario_nombre,
                v.apellido AS veterinario_apellido,
                v.especialidad AS veterinario_especialidad

            FROM historial_medico h
            LEFT JOIN mascotas m ON h.id_mascota = m.id
            LEFT JOIN usuarios v ON h.id_veterinario = v.id
            WHERE h.id = %s
        """

        cursor.execute(query, (id_historial,))
        return cursor.fetchone()

    # =====================================================
    # CREAR
    # =====================================================
    @staticmethod
    def crear_historial(data):
        db = conectarDB.conectar()
        cursor = db.cursor()

        query = """
            INSERT INTO historial_medico 
            (id_mascota, fecha, id_veterinario, diagnostico, tratamiento, observaciones, peso_actual, proxima_visita)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            data["id_mascota"],
            data["fecha"],
            data.get("id_veterinario"),
            data.get("diagnostico"),
            data.get("tratamiento"),
            data.get("observaciones"),
            data.get("peso_actual"),
            data.get("proxima_visita"),
        )

        cursor.execute(query, valores)
        db.commit()

        return {"mensaje": "Historial creado correctamente", "id": cursor.lastrowid}

    # =====================================================
    # ACTUALIZAR
    # =====================================================
    @staticmethod
    def actualizar_historial(id_historial, data):
        db = conectarDB.conectar()
        cursor = db.cursor()

        query = """
            UPDATE historial_medico
            SET 
                id_mascota = %s,
                fecha = %s,
                id_veterinario = %s,
                diagnostico = %s,
                tratamiento = %s,
                observaciones = %s,
                peso_actual = %s,
                proxima_visita = %s
            WHERE id = %s
        """

        valores = (
            data["id_mascota"],
            data["fecha"],
            data.get("id_veterinario"),
            data.get("diagnostico"),
            data.get("tratamiento"),
            data.get("observaciones"),
            data.get("peso_actual"),
            data.get("proxima_visita"),
            id_historial,
        )

        cursor.execute(query, valores)
        db.commit()

        return {"mensaje": "Historial actualizado correctamente"}

    # =====================================================
    # ELIMINAR
    # =====================================================
    @staticmethod
    def eliminar_historial(id_historial):
        db = conectarDB.conectar()
        cursor = db.cursor()

        query = "DELETE FROM historial_medico WHERE id = %s"

        cursor.execute(query, (id_historial,))
        db.commit()

        return {"mensaje": "Historial eliminado correctamente"}
