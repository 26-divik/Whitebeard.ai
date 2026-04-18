from flask import request, jsonify
from google import genai
from dotenv import load_dotenv
from app.controller.db_controller.mongo_controller import get_chat, save_chat
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

def message():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON format"}), 400

    if not isinstance(data, dict):
        return jsonify({"error": "JSON must be an object"}), 400

    chat_id = data.get("chat_id")
    usr_msg = data.get('message') 


    if not usr_msg or not chat_id:
        return jsonify({"error": "Message or chat_id field is required"}), 400

    chat = get_chat(chat_id)
    
    if chat is not None:
        user_input = f"Act as an ai assistant whose name is Whitebeard, inspired from the character of the anime One Piece and answer the question based on the following conversation history: {chat} and the new question is: {usr_msg}"
    else:
        user_input = f"Act as an ai assistant whose name is Whitebeard, inspired from the character of the anime One Piece and answer the question which is: {usr_msg}"

    try:
        user_input_tokens = len(user_input)/4

        user_message_tokens = len(user_message)/4
    except Exception as e:
        return jsonify({"error": f"Failed to calculate tokens: {str(e)}"}), 500


    if user_input_tokens > 1048576:
        if user_message_tokens > 1048576:
            return jsonify({"error": "Message is too long."}), 400
        return jsonify({"error": "Conversation history is too long. Please start a new chat."}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=user_input,
        )
        bot_response = response.text
        
    except Exception as e:
        return jsonify({"error": f"Error occurred during generation: {str(e)}"}), 500

    save_chat(chat_id, usr_msg, bot_response)

    return jsonify({"response": bot_response}), 200