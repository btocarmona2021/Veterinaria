from flask import Flask
from .modulos.usuarios.usuario_routes import usuario_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(usuario_bp)
    @app.route("/")
    def home():
        return "<h1>Hola desde Flask</h1>"
    return app