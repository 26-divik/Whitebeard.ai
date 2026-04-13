from flask import Flask, request, jsonify, session
from flask_session import Session
from app.routes.auth_routes import routes_lg
from app.routes.chat_routes import routes_ch
from app.controller.db_controller import initialize_database
import os 
import dotenv
dotenv.load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = os.getenv('session_secret')
    Session(app)
    initialize_database()
    app.register_blueprint(routes_lg,url_prefix='/u')
    app.register_blueprint(routes_ch,url_prefix='/c')

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "Welcome to the API"})

    return app

