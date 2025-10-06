from .servicio_controller import ServicioController
from flask import Blueprint, request, jsonify

servicio_bp = Blueprint("servicio_bp", __name__)


@servicio_bp.route("/servicios", methods=["GET"])
def obtener_servicios():
    servicios = ServicioController.obtener_servicios()
    return jsonify(servicios), 200


@servicio_bp.route("/servicio/<int:id>", methods=["GET"])
def obtener_servicio(id):
    servicio = ServicioController.obtener_servicio(id)
    if servicio:
        return jsonify(servicio), 200
    else:
        return jsonify({"error": "Servicio no encontrado"}), 404


@servicio_bp.route("/servicio", methods=["POST"])
def crear_servicio():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400
    result = ServicioController.crear_servicio(data)
    if result:
        return jsonify({"message": "Servicio creado exitosamente"}), 201
    else:
        return jsonify({"error": "Error al crear el servicio"}), 500


@servicio_bp.route("/servicio", methods=["PUT"])
def modificar_servicio():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400
    result = ServicioController.modificar_servicio(data)
    if result:
        return jsonify({"message": "Servicio modificado exitosamente"}), 200
    else:
        return jsonify({"error": "Error al modificar el servicio"}), 500


@servicio_bp.route("/servicios/<int:id>", methods=["DELETE"])
def eliminar_servicio(id):
    result = ServicioController.eliminar_servicio(id)
    if result:
        return jsonify({"message": "Servicio eliminado exitosamente"}), 200
    else:
        return jsonify({"error": "Error al eliminar el servicio"}), 500
