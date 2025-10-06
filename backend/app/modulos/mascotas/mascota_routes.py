from flask import Blueprint, request, jsonify
from ..database.conectDB import conectarDB

from .mascota_model import MascotaModel

mascota_routes = Blueprint('mascota_routes', __name__)

@mascota_routes.route('/mascotas', methods=['GET'])
def obtener_mascotas():
    try:
        mascotas = MascotaModel.obtener_mascotas()
        return jsonify(mascotas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@mascota_routes.route('/mascota/<int:id>', methods=['GET'])
def obtener_mascota(id):
    try:
        mascota = MascotaModel.obtener_mascota({"id": id})
        if mascota:
            return jsonify(mascota), 200
        else:
            return jsonify({"error": "Mascota no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@mascota_routes.route('/mascota', methods=['POST'])
def crear_mascota():
    data = request.get_json()
    try:
        mascota = MascotaModel.crear_mascota(data)
        return jsonify(mascota), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@mascota_routes.route('/mascota', methods=['PUT'])
def modificar_mascota():
    data = request.get_json()
    try:
        mascota = MascotaModel.modificar_mascota(data)
        return jsonify(mascota), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@mascota_routes.route('/mascota/<int:id>', methods=['DELETE'])
def eliminar_mascota(id):
    try:
        resultado = MascotaModel.eliminar_mascota({"id": id})
        if resultado:
            return jsonify({"message": "Mascota eliminada exitosamente"}), 200
        else:
            return jsonify({"error": "Mascota no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

