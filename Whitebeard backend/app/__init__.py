from flask import Flask, request, jsonify, session
from flask_session import Session
from app.routes.auth_routes import routes_lg
from app.routes.chat_routes import routes_ch
from app.controller.db_controller import initialize_database
import os 
from flask_cors import CORS
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
    CORS(app, supports_credentials=True, origins=["example.com"])
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "Welcome to the API"})

    @app.errorhandler(400)
        def bad_request(e):
            return jsonify({"error": "Bad request", "details": str(e)}), 400
    
        @app.errorhandler(401)
        def unauthorized(e):
            return jsonify({"error": "Unauthorized. Please log in."}), 401
    
        @app.errorhandler(403)
        def forbidden(e):
            return jsonify({"error": "Forbidden. You do not have access to this resource."}), 403
    
        @app.errorhandler(404)
        def not_found(e):
            return jsonify({"error": f"Route '{request.path}' not found."}), 404
    
        @app.errorhandler(405)
        def method_not_allowed(e):
            return jsonify({"error": f"Method '{request.method}' is not allowed on this route."}), 405
    
        @app.errorhandler(HTTPException)
        def handle_http_exception(e):
            # Catches any other HTTP error (413, 429, etc.) as a clean JSON response
            return jsonify({"error": e.name, "details": e.description}), e.code
    
        @app.errorhandler(Exception)
        def handle_unexpected_error(e):
            # Catches any unhandled Python exception so the server never returns raw HTML
            app.logger.error(f"Unhandled exception: {str(e)}", exc_info=True)
            return jsonify({"error": "An unexpected server error occurred. Please try again later."}), 500

    return app

