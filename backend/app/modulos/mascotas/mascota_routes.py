from flask import Blueprint, request, jsonify
from ...database.conectDB import conectarDB
from .mascota_controller import MascotaController

mascota_bp = Blueprint('mascota_bp', __name__)

@mascota_bp.route('/mascotas', methods=['GET'])
def obtener_mascotas():
    try:
        mascotas = MascotaController.obtener_mascotas()
        return jsonify(mascotas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@mascota_bp.route('/mascota/<int:id>', methods=['GET'])
def obtener_mascota(id):
    try:
        mascota = MascotaController.obtener_mascota(id)
        print(mascota)
        if mascota:
            return jsonify(mascota), 200
        else:
            return jsonify({"error": "Mascota no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@mascota_bp.route('/mascota', methods=['POST'])
def crear_mascota():
    data = request.get_json()
    try:
        mascota = MascotaController.crear_mascota(data)
        return jsonify(mascota), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@mascota_bp.route('/mascota', methods=['PUT'])
def modificar_mascota():
    data = request.get_json()
    try:
        mascota = MascotaController.modificar_mascota(data)
        return jsonify(mascota), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@mascota_bp.route('/mascota/<int:id>', methods=['DELETE'])
def eliminar_mascota(id):
    try:
        resultado = MascotaController.eliminar_mascota({"id": id})
        if resultado:
            return jsonify({"message": "Mascota eliminada exitosamente"}), 200
        else:
            return jsonify({"error": "Mascota no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

