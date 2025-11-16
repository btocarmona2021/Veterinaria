from flask import Blueprint, request, jsonify
from .turno_controller import TurnoController

turno_bp = Blueprint("turno_bp", __name__)


@turno_bp.route("/turnos", methods=["GET"])
def obtener_turnos():
    turnos = TurnoController.obtener_turnos()
    return jsonify(turnos), 200


@turno_bp.route("/turno/<int:id>", methods=["GET"])
def obtener_turno(id):
    turno = TurnoController.obtener_turno(id)
    if turno:
        return jsonify(turno), 200
    return jsonify({"error": "Turno no encontrado"}), 404


@turno_bp.route("/turno", methods=["POST"])
def crear_turno():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    nuevo_id = TurnoController.crear_turno(data)
    return jsonify({"message": "Turno creado", "id": nuevo_id}), 201


@turno_bp.route("/turno/<int:id>", methods=["PUT"])
def modificar_turno(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    modificado = TurnoController.modificar_turno(id, data)
    return jsonify({"modificado": modificado}), 200


@turno_bp.route("/turno/<int:id>", methods=["DELETE"])
def eliminar_turno(id):
    eliminado = TurnoController.eliminar_turno(id)
    if eliminado:
        return jsonify({"message": "Turno eliminado"}), 200
    return jsonify({"error": "Turno no encontrado"}), 404
