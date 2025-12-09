from flask_jwt_extended import create_access_token


class AuthModel:
    @staticmethod
    def login(email: str, password: str) -> dict:
        from ..usuarios.usuario_model import UsuarioModel as Usuario

        user = Usuario.obtener_usuario_por_email(email)

        if not user:
            return {"message": "Acceso denegado: email incorrecto", "status_code": 401}

        usuario = Usuario(**user)

        if not usuario.chequear_password(password):
            return {
                "message": "Acceso denegado: contraseña incorrecta",
                "status_code": 401,
            }
        else:
            jwt = create_access_token(identity=user["email"])

            return {
                "id":user["id"],
                "message": "Login exitoso",
                "nombre_apellido": user["nombre"] +" "+ user["apellido"],
                "email": user["email"],
                "rol": user["rol"],
                "jwt": jwt,
                "status_code": 200,
            }
