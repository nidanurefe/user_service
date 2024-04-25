import hashlib
from datetime import datetime, timedelta, timezone
import jwt # type: ignore
import logging
from .http_helper import HttpResponse

def hash_pw(password:str) ->str:
    salt = "5gz"
    password_salted = password+salt
    hashed = hashlib.md5(password_salted.encode())
    return hashed.hexdigest()

def generate_token(username) -> str:
    payload_data = {
            'sub': username, #Subject of the token
            'iat': (datetime.now(timezone.utc)),
            'exp':(datetime.now(timezone.utc) + timedelta(hours=1)),
        }
    
    token = jwt.encode(payload_data, "secret", algorithm="HS256")
    return token

def question_token(token):
    try:
        username = jwt.decode(token, "secret", algorithms=["HS256"])['sub']
        return HttpResponse().Success("Authcode is updated!") .makeResponse()
    except jwt.ExpiredSignatureError:
        return HttpResponse().RequestTimeOut("Signature has expired!") .makeResponse()



