from .usuario_model import UsuarioModel


class UsuarioController:
    @staticmethod
    def obtener_usuarios():
        return UsuarioModel.obtener_usuarios()

    @staticmethod
    def obtener_usuario(id):
        return UsuarioModel(id=id).obtener_usuario()

    @staticmethod
    def crear_usuario(data: dict):
        print(data)
        usuario = UsuarioModel(**data)
        return usuario.crear_usuario()

    @staticmethod
    def modificar_usuario(id, data: dict):
        data["id"] = id
        usuario = UsuarioModel(**data)
        return usuario.modificar_usuario()

    @staticmethod
    def eliminar_usuario(id):
        usuario = UsuarioModel(id=id)
        return usuario.eliminar_usuario()
