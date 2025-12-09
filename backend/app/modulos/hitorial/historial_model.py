from ...database.conectDB import conectarDB


class HistorialModel:

    def __init__(
        self,
        id,
        id_mascota,
        fecha,
        id_veterinario,
        diagnostico,
        tratamiento,
        observaciones,
        peso_actual,
        proxima_visita,
    ):

        self.id = id
        self.id_mascota = id_mascota
        self.fecha = fecha
        self.id_veterinario = id_veterinario
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.observaciones = observaciones
        self.peso_actual = peso_actual
        self.proxima_visita = proxima_visita

    def to_dict(self):
        return {
            "id": self.id,
            "id_mascota": self.id_mascota,
            "fecha": self.fecha,
            "id_veterinario": self.id_veterinario,
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento,
            "observaciones": self.observaciones,
            "peso_actual": self.peso_actual,
            "proxima_visita": self.proxima_visita,
        }

    @staticmethod
    def obtener_historial():
        db = conectarDB.conectar()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT 
                id,
                id_mascota,
                fecha,
                id_veterinario,
                diagnostico,
                tratamiento,
                observaciones,
                peso_actual,
                proxima_visita
            FROM historial_medico
            ORDER BY fecha DESC
        """

        cursor.execute(query)
        resultados = cursor.fetchall()

        return [HistorialModel(**r).to_dict() for r in resultados]


    @staticmethod
    def obtener_por_id(id_historial):
        db = conectarDB.conectar()
        cursor = db.cursor(dictionary=True)

        query = """
            SELECT 
                id,
                id_mascota,
                fecha,
                id_veterinario,
                diagnostico,
                tratamiento,
                observaciones,
                peso_actual,
                proxima_visita
            FROM historial_medico
            WHERE id = %s
        """

        cursor.execute(query, (id_historial,))
        r = cursor.fetchone()

        return HistorialModel(**r).to_dict() if r else None

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

    @staticmethod
    def eliminar_historial(id_historial):
        db = conectarDB.conectar()
        cursor = db.cursor()

        query = "DELETE FROM historial_medico WHERE id = %s"

        cursor.execute(query, (id_historial,))
        db.commit()

        return {"mensaje": "Historial eliminado correctamente"}
