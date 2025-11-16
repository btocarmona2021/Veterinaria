from flask import jsonify
from .historial_model import HistorialModel


class HistorialController:

    @staticmethod
    def obtener_historial():
        data = HistorialModel.obtener_historial()
        return jsonify(data), 200

    @staticmethod
    def obtener_historial_por_id(id_historial):
        data = HistorialModel.obtener_por_id(id_historial)
        if data:
            return jsonify(data), 200
        return jsonify({"error": "Historial no encontrado"}), 404

    @staticmethod
    def crear_historial(data):
        resultado = HistorialModel.crear_historial(data)
        return jsonify(resultado), 201

    @staticmethod
    def actualizar_historial(id_historial, data):
        resultado = HistorialModel.actualizar_historial(id_historial, data)
        return jsonify(resultado), 200

    @staticmethod
    def eliminar_historial(id_historial):
        resultado = HistorialModel.eliminar_historial(id_historial)
        return jsonify(resultado), 200
