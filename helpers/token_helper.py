import hashlib
from datetime import datetime, timedelta, timezone
import jwt # type: ignore

def hash_pw(password:str) ->str:
    salt = "5gz"
    password_salted = password+salt
    hashed = hashlib.md5(password_salted.encode())
    return hashed.hexdigest()

def generate_token(username, key) -> str:
    payload_data = {
            'sub': username, #Subject of the token
            'iat': (datetime.now(timezone.utc)),
            'exp':(datetime.now(timezone.utc) + timedelta(hours=1)),
        }
    
    token = jwt.encode(payload=payload_data, key = key)
    return token

