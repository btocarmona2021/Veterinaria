from .servicio_model import ServicioModel


class ServicioController:

    @staticmethod
    def obtener_servicios():
        servicios = ServicioModel.obtener_servicios()
        return servicios

    @staticmethod
    def obtener_servicio(id):
        servicio = ServicioModel.obtener_servicio(id)
        if servicio:
            return servicio

    @staticmethod
    def crear_servicio(data: dict):
        servicio = ServicioModel(
            data["id"],
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["duracion_estimada"],
        )
        result = ServicioModel.crear_servicio()
        return result

    @staticmethod
    def modificar_servicio(data: dict):
        servicio = ServicioModel(
            data["id"],
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["duracion_estimada"],
        )
        result = ServicioModel.modificar_servicio(servicio)
        return result
    
    @staticmethod
    def eliminar_servicio(id):
        servicio = ServicioModel(id=id)
        result = ServicioModel.eliminar_servicio(servicio)
        return result