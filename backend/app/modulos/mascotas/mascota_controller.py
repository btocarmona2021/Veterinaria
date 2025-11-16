from .mascota_model import MascotaModel


class MascotaController:

    @staticmethod
    def obtener_mascotas():
        return MascotaModel.obtener_mascotas()

    @staticmethod
    def obtener_mascota(id):
        return MascotaModel.obtener_mascota(id)

    @staticmethod
    def crear_mascota(data):
        return MascotaModel.crear_mascota(data)

    @staticmethod
    def modificar_mascota(id, data):
        return MascotaModel.modificar_mascota(id, data)

    @staticmethod
    def eliminar_mascota(id):
        return MascotaModel.eliminar_mascota(id)
