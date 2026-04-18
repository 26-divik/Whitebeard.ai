from flask import Blueprint
from app.controller.login_controller import auth_controller
from app.auth_middleware import login_required 
routes_lg = Blueprint('u', __name__)
@routes_lg.route('/signup', methods=['POST'])
def signup():
    return auth_controller.signup()
@routes_lg.route('/login', methods=['POST'])
def login():
    return auth_controller.login()
@routes_lg.route('/logout', methods=['POST'])
@login_required
def logout():
    return auth_controller.logout()
