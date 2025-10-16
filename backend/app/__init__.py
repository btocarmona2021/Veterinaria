from flask import Flask
from .modulos.usuarios.usuario_routes import usuario_bp
from .modulos.mascotas.mascota_routes import mascota_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(mascota_bp)
    @app.route("/")
    def home():
        return "<h1>Hola desde Flask</h1>"
    return app