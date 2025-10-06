from .usuario_model import UsuarioModel


class UsuarioController:
    @staticmethod
    def obtener_usuarios():
        usuarios = UsuarioModel.obtener_usuarios()
        return usuarios

    @staticmethod
    def obtener_usuario(id):
        usuario = UsuarioModel(id=id).obtener_usuario()
        print(usuario)
        return usuario

    @staticmethod
    def crear_usuario(data: dict):
        usuario = UsuarioModel(
            id=data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            email=data["email"],
            password=data["password"],
            telefono=data["telefono"],
            direccion=data["direccion"],
            rol=data["rol"],
            especialidad=data["especialidad"],
            disponible=data["disponible"],
            fecha_registro=data["fecha_registro"],
            activo=data["activo"],
        )
        resultado = usuario.crear_usuario()
        return resultado

    @staticmethod
    def modificar_usuario(data: dict):
        usuario = UsuarioModel(
            id=data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            email=data["email"],
            password=data["password"],
            telefono=data["telefono"],
            direccion=data["direccion"],
            rol=data["rol"],
            especialidad=data["especialidad"],
            disponible=data["disponible"],
            fecha_registro=data["fecha_registro"],
            activo=data["activo"],
        )
        resultado = usuario.modificar_usuario()
        return resultado

    @staticmethod
    def eliminar_usuario(id):
        usuario = UsuarioModel(id=id)
        resultado = usuario.eliminar_usuario()
        return resultado
