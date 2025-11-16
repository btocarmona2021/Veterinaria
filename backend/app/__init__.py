from flask import Flask
from flask_cors import CORS
from .modulos.usuarios.usuario_routes import usuario_bp
from .modulos.mascotas.mascota_routes import mascota_bp
from .modulos.servicios.servicio_routes import servicio_bp
from .modulos.turnos.turno_routes import turno_bp
from .modulos.hitorial.historial_routes import historial_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(mascota_bp)
    app.register_blueprint(servicio_bp)
    app.register_blueprint(turno_bp)
    app.register_blueprint(historial_bp)
    @app.route("/")
    def home():
        return "<h1>Hola desde Flask</h1>"
    return app