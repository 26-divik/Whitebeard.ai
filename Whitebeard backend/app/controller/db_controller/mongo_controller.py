from pymongo import MongoClient
import dotenv
import os
import uuid
dotenv.load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["chats"]
collections= db["chats"]

def get_chat(chat_id):
      chat = collections.find_one({"chat_id": chat_id})
      if chat is not None:
          return chat["chat"]
      return None
def save_chat(chat_id, question, answer):
    if chat_id is not None:
        collections.update_one({"chat_id": chat_id}, {"$push":  {"chat.questions": question, "chat.answers": answer}})
    
def create_chat(user_id):
    try:
        success, chats = get_user_chats(user_id)
        if success and len(chats) >= 15:
            return False, "Too many chats, limit is 15"
        chat_id =str(uuid.uuid4())
        collections.insert_one({"chat_id": chat_id, "chat": {"questions": [], "answers": []}, "user_id": user_id})
        return True,chat_id
    except Exception as e:
        return False, str(e)
    
def delete_chat(chat_id):
    try:
        result = collections.delete_one({"chat_id": chat_id})
        if result.deleted_count == 1:   
            return True, f"Chat with chat_id: {chat_id} deleted successfully"
        else:
            return False, f"No chat found with chat_id: {chat_id}"
    except Exception as e:
        return False, str(e)
    
def get_user_chats(user_id):
    try:
        chats = collections.find({"user_id": user_id})
        if not chats:
            return False, "No chats found for the specified user"
        chat_list = []
        for chat in chats:    
            chat_list.append({"chat_id": chat["chat_id"], "chat":chat["chat"] if chat["chat"] else None})
        return True, chat_list
    except Exception as e:
        return False, str(e)

def get_user_id_by_chat_id(chat_id):
    try:
        chat = collections.find_one({"chat_id": chat_id})
        if chat is not None:
            return True, chat["user_id"]
        return False, "Chat not found"
    except Exception as e:
        return False, str(e)