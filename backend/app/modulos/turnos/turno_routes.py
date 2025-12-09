from flask import Blueprint, request, jsonify
from .turno_controller import TurnoController
from flask_jwt_extended import jwt_required

turno_bp = Blueprint("turno_bp", __name__)


@turno_bp.route("/turnos", methods=["GET"])
@jwt_required()
def obtener_turnos():
    turnos = TurnoController.obtener_turnos()
    return jsonify(turnos), 200


@turno_bp.route("/turnos/<int:id>", methods=["GET"])
@jwt_required()
def obtener_turno(id):
    turno = TurnoController.obtener_turno(id)
    if turno:
        return jsonify(turno), 200
    return jsonify({"error": "Turno no encontrado"}), 404


@turno_bp.route("/turnos", methods=["POST"])
@jwt_required()
def crear_turno():
    from ..usuarios.usuario_model import UsuarioModel as Usuario
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    nuevo_id = TurnoController.crear_turno(data)
    return jsonify({"message": "Turno creado", "id": nuevo_id}), 201


@turno_bp.route("/turnos/<int:id>", methods=["PUT"])
@jwt_required()
def modificar_turno(id):
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    modificado = TurnoController.modificar_turno(id, data)
    return jsonify({"modificado": modificado}), 200


@turno_bp.route("/turnos/<int:id>", methods=["DELETE"])
@jwt_required()
def eliminar_turno(id):
    eliminado = TurnoController.eliminar_turno(id)
    if eliminado:
        return jsonify({"message": "Turno eliminado"}), 200
    return jsonify({"error": "Turno no encontrado"}), 404
