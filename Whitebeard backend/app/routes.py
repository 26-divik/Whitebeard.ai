from flask import Flask, jsonify, request ,Blueprint
from app.controller.login_controller import auth_controller
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/signup', methods=['POST'])
def signup():
    return auth_controller.signup()
