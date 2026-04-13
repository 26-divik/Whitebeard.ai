from flask import session
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return {"error": "Unauthorized"}, 401
        return func(*args, **kwargs)
    return wrapper