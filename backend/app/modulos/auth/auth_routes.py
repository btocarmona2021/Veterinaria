from flask import Blueprint, request, jsonify
from .auth_controller import AuthController as AuthC

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email y password son obligatorios"}), 400

    user_login = AuthC.login(email, password)

    return jsonify(user_login), user_login['status_code']
