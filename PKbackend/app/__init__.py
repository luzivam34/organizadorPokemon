from flask import Flask

# função que cria o app
def create_app():
    app = Flask(__name__)

    # importação do blueprint
    from .routes.pokemon_route import pokemon_bp

    # registro de routes
    app.register_blueprint(pokemon_bp)


    return app