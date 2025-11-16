from flask import Blueprint, request
from .historial_controller import HistorialController

historial_bp = Blueprint("historial_bp", __name__)


# ============================================
# OBTENER TODOS LOS HISTORIALES
# ============================================
@historial_bp.get("/historial")
def obtener_historial():
    return HistorialController.obtener_historial()


# ============================================
# OBTENER UNO POR ID
# ============================================
@historial_bp.get("/historial/<int:id_historial>")
def obtener_historial_por_id(id_historial):
    return HistorialController.obtener_historial_por_id(id_historial)


# ============================================
# CREAR
# ============================================
@historial_bp.post("/historial")
def crear_historial():
    data = request.json
    return HistorialController.crear_historial(data)


# ============================================
# ACTUALIZAR
# ============================================
@historial_bp.put("/historial/<int:id_historial>")
def actualizar_historial(id_historial):
    data = request.json
    return HistorialController.actualizar_historial(id_historial, data)


# ============================================
# ELIMINAR
# ============================================
@historial_bp.delete("/historial/<int:id_historial>")
def eliminar_historial(id_historial):
    return HistorialController.eliminar_historial(id_historial)
