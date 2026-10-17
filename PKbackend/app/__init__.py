from flask import Flask
from flask_cors import CORS

# função que cria o app
def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"])

    # importação do blueprint
    from .routes.pokemon_route import pokemon_bp

    # registro de routes
    app.register_blueprint(pokemon_bp)


    return app