from .servicio_controller import ServicioController
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

servicio_bp = Blueprint("servicio_bp", __name__)


@servicio_bp.route("/servicios", methods=["GET"])
@jwt_required()
def obtener_servicios():
    servicios = ServicioController.obtener_servicios()
    return jsonify(servicios), 200


@servicio_bp.route("/servicios/<int:id>", methods=["GET"])
@jwt_required()
def obtener_servicio(id):
    servicio = ServicioController.obtener_servicio(id)
    if servicio:
        return jsonify(servicio), 200
    return jsonify({"error": "Servicio no encontrado"}), 404


@servicio_bp.route("/servicios", methods=["POST"])
@jwt_required()
def crear_servicio():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    new_id = ServicioController.crear_servicio(data)
    if new_id:
        return jsonify({"message": "Servicio creado", "id": new_id}), 201

    return jsonify({"error": "Error al crear servicio"}), 500


@servicio_bp.route("/servicios/<int:id>", methods=["PUT"])
@jwt_required()
def modificar_servicio(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    ok = ServicioController.modificar_servicio(id, data)
    if ok:
        return jsonify({"message": "Servicio modificado"}), 200

    return jsonify({"error": "Error al modificar servicio"}), 500


@servicio_bp.route("/servicios/<int:id>", methods=["DELETE"])
@jwt_required()
def eliminar_servicio(id):
    ok = ServicioController.eliminar_servicio(id)
    if ok:
        return jsonify({"message": "Servicio eliminado"}), 200

    return jsonify({"error": "Error al eliminar servicio"}), 500
