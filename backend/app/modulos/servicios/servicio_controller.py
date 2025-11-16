from .servicio_model import ServicioModel


class ServicioController:

    @staticmethod
    def obtener_servicios():
        return ServicioModel.obtener_servicios()

    @staticmethod
    def obtener_servicio(id):
        return ServicioModel.obtener_servicio(id)

    @staticmethod
    def crear_servicio(data):
        return ServicioModel.crear_servicio(data)

    @staticmethod
    def modificar_servicio(id, data):
        return ServicioModel.modificar_servicio(id, data)

    @staticmethod
    def eliminar_servicio(id):
        return ServicioModel.eliminar_servicio(id)
