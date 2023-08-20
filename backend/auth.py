import jwt
from datetime import datetime, timedelta

SECRET_KEY = "de3d973e375affa76a4d1e4611a2d6642729750809a30012c38c6f8b9f6f8cd2" 
ALGORITHM = "HS256" 

users = {
    "user123": {"password": "password123", "name": "John Doe"}
}

def generate_jwt_token(user_id):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1)  # Token expiration time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        user_id = username 
        return user_id
    return None