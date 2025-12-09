from flask import request, jsonify, Blueprint
from .usuario_controller import UsuarioController
from flask_jwt_extended import jwt_required

usuario_bp = Blueprint("usuario_bp", __name__)


@usuario_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos inválidos"}), 400

        nuevo_id = UsuarioController.crear_usuario(data)
        if nuevo_id:
            return jsonify({"message": "Usuario creado", "id": nuevo_id}), 201
        else:
            return jsonify({"error": "No se pudo crear usuario"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@usuario_bp.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    try:
        usuarios = UsuarioController.obtener_usuarios()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@usuario_bp.route("/usuarios/<int:id>", methods=["GET"])
@jwt_required()
def obtener_usuario(id):
    try:
        usuario = UsuarioController.obtener_usuario(id)
        if usuario:
            return jsonify(usuario), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@usuario_bp.route("/usuarios/<int:id>", methods=["PUT"])
@jwt_required()
def modificar_usuario(id):
    try:
        data = request.get_json()

      
        if not data:
            return jsonify({"error": "Datos inválidos"}), 400
        modificado = UsuarioController.modificar_usuario(id, data)
        if modificado:
            return jsonify({"message": "Usuario modificado exitosamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@usuario_bp.route("/usuarios/<int:id>", methods=["DELETE"])
@jwt_required()
def eliminar_usuario(id):
    try:
        eliminado = UsuarioController.eliminar_usuario(id)

        if eliminado:
            return jsonify({"message": "Usuario eliminado correctamente"}), 200
        else:
            return jsonify({"error": "No se en contro el usaurio"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
