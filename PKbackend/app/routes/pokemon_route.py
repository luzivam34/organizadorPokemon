from flask import Blueprint, jsonify

pokemon_bp = Blueprint("pokemon_bp", __name__)

@pokemon_bp.route("/")
def index():
    return jsonify({
        "message": "backend rodando !",
        "status": "ok"
    }), 200