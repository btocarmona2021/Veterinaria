from flask import request, jsonify,Blueprint
from .usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario_bp', __name__)
@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        usuarios = UsuarioController.obtener_usuarios()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@usuario_bp.route('/usuario/<int:id>', methods=['GET'])
def obtener_usuario(id):
    try:
        usuario = UsuarioController.obtener_usuario(id)
        print(usuario)
        if usuario:
            return jsonify(usuario), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@usuario_bp.route('/usuario', methods=['POST'])
def crear_usuario():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Dados inválidos'}), 400
        usuario = UsuarioController.crear_usuario(data)
        return jsonify(usuario), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def modificar_usuario(id):
    try:
        data = request.get_json()
        print(data)
        if not data:
            return jsonify({'error': 'Datos inválidos'}), 400
        data['id'] = id
        usuario = UsuarioController.modificar_usuario(data)
        return jsonify(usuario), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    
@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        usuario = UsuarioController.eliminar_usuario(id)
        print(f"detalle de usuario {usuario}")
        if usuario != False:
            return jsonify({'message': 'Usuario eliminado'}), 200
        else:
            return jsonify({'error': 'No se encontro el usuario'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500