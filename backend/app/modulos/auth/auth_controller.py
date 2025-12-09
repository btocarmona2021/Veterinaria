from .auth_model import AuthModel as Auth


class AuthController:
    @staticmethod
    def login(email: str, password: str):
        if not email or not password:
            return {"message": "Los datos no deben estar vacíos", "status_code": 400}

        return Auth.login(email, password)
