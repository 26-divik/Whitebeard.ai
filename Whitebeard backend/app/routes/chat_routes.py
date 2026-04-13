from flask import Flask, jsonify, request ,Blueprint, session
from app.controller.chat_controller.chat_controller import message
from app.controller.db_controller.mongo_controller import get_chat,save_chat,delete_chat,get_user_chats,create_chat
from app.auth_middleware import login_required
from app.controller.db_controller.sql_controller import get_user_by_id
routes_ch = Blueprint('c', __name__)
@routes_ch.route('/all_chats', methods=['POST'])
@login_required
def get_all_chats():
    user = get_user_by_id(session.get('user_id'))
    is_all_chats, chat_list = get_user_chats(user['email'])
    if not user:
        return jsonify({"error": "User not found"}), 404 
    if not is_all_chats:
        return jsonify({"error": chat_list}), 400  
    return jsonify({"chats": chat_list}), 200
@routes_ch.route('/create_chat', methods=['POST'])
@login_required
def create():
    user = get_user_by_id(session.get('user_id'))
    is_chat_created, chat_id = create_chat(user['email'])
    if not user:
        return jsonify({"error": "User not found"}), 404 
    if not is_chat_created:
        return jsonify({"error": chat_id}), 400  
    return jsonify({"chat_id": chat_id}), 200

@routes_ch.route('/chat/<chat_id>', methods=['GET'])
@login_required
def get_chat_by_id(chat_id):
    chat = get_chat(chat_id)
    if not chat:
        return jsonify({"error": "Chat not found"}), 404
    return jsonify({"chat": chat}), 200
@routes_ch.route('/message', methods=['POST'])
@login_required
def send_message():
    return message()
@routes_ch.route('/delete_chat/<chat_id>', methods=['DELETE'])
@login_required
def delete_chat_by_id(chat_id):
    is_deleted,confirmation_msg = delete_chat(chat_id)
    if not is_deleted:
        return jsonify({"error": confirmation_msg}), 404
    return jsonify({"message": confirmation_msg}), 200