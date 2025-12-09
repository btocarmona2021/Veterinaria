from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from .modulos.usuarios.usuario_routes import usuario_bp
from .modulos.mascotas.mascota_routes import mascota_bp
from .modulos.servicios.servicio_routes import servicio_bp
from .modulos.turnos.turno_routes import turno_bp
from .modulos.hitorial.historial_routes import historial_bp
from .modulos.auth.auth_routes import auth_bp
from flask_jwt_extended import JWTManager
from flask import request, jsonify, Blueprint
from datetime import timedelta

load_dotenv()
def create_app()->Flask:
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
    jwt_expires = int(os.getenv("JWT_EXPIRES", 15))
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=jwt_expires)
    JWTManager(app)
    CORS(app)
    api_bp = Blueprint('api',__name__,url_prefix='/api_v1')
    api_bp.register_blueprint(usuario_bp)
    api_bp.register_blueprint(mascota_bp)
    api_bp.register_blueprint(servicio_bp)
    api_bp.register_blueprint(turno_bp)
    api_bp.register_blueprint(historial_bp)
    api_bp.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    @app.route("/")
    def home():
        return "<h1>Hola desde Flask</h1>"
    return app
