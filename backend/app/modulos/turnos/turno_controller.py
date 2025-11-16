from .turno_model import TurnoModel


class TurnoController:

    @staticmethod
    def obtener_turnos():
        return TurnoModel.obtener_turnos()

    @staticmethod
    def obtener_turno(id):
        return TurnoModel.obtener_turno(id)

    @staticmethod
    def crear_turno(data):
        return TurnoModel.crear_turno(data)

    @staticmethod
    def modificar_turno(id, data):
        return TurnoModel.modificar_turno(id, data)

    @staticmethod
    def eliminar_turno(id):
        return TurnoModel.eliminar_turno(id)
