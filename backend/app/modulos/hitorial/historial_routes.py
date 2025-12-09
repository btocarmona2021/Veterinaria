from flask import Blueprint, request
from .historial_controller import HistorialController
from flask_jwt_extended import jwt_required

historial_bp = Blueprint("historial_bp", __name__)


@historial_bp.route("/historial", methods=["GET"])
def obtener_historial():
    return HistorialController.obtener_historial()


@historial_bp.route("/historial/<int:id_historial>", methods=["GET"])
@jwt_required()
def obtener_historial_por_id(id_historial):
    return HistorialController.obtener_historial_por_id(id_historial)


@historial_bp.route("/historial", methods=["POST"])
@jwt_required()
def crear_historial():
    data = request.json
    return HistorialController.crear_historial(data)


@historial_bp.route("/historial/<int:id_historial>", methods=["PUT"])
@jwt_required()
def actualizar_historial(id_historial):
    data = request.json
    return HistorialController.actualizar_historial(id_historial, data)


@historial_bp.route("/historial/<int:id_historial>", methods=["DELETE"])
@jwt_required()
def eliminar_historial(id_historial):
    return HistorialController.eliminar_historial(id_historial)
