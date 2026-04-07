from flask import Flask, request, jsonify
from app.routes import routes_bp
from app.controller.db_controller import initialize_database


def create_app():
    app = Flask(__name__)
    initialize_database()
    app.register_blueprint(routes_bp,url_prefix='/api')

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "Welcome to the API"})

    return app

