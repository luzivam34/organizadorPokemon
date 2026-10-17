from flask import Blueprint, jsonify

pokemon_bp = Blueprint("pokemon_bp", __name__)

@pokemon_bp.route("/api/teste", methods=["GET"])
def index():
    return jsonify({
        "mensagem": "Conexão com o flask realizada!",
        "status": "sucesso"
    }), 200