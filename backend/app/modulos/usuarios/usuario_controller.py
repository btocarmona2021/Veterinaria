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
        usuario = UsuarioModel(**data)
        if not usuario.email or not usuario.password:
            return {
                "message": "Debe comp   letar todos los campos",
                "status_code": 500,
            }
        # existe_email = UsuarioModel.email_existe(usuario.email)
        # if existe_email:
        #     return {
        #         "message": "Este correo electronico ya se encuentra registrado",
        #         "status_code": 409,
        #     }

        resultado = usuario.crear_usuario()

        if resultado:
            return {
                "message": "El usuario ha sido creado correctamente",
                "status_code": 201,
            }

        return {"message": "Error al crear el usuario", "status_code": 500}

    @staticmethod
    def modificar_usuario(id, data: dict):
        return UsuarioModel.modificar_usuario(id,data)

    @staticmethod
    def eliminar_usuario(id):
        usuario = UsuarioModel(id=id)
        return usuario.eliminar_usuario()
