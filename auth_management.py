from flask import Flask, request
from helpers.models import User_n
from helpers.token_helper import hash_pw
from helpers.http_helper import HttpResponse
import jwt # type: ignore
import logging 

app = Flask('__main__')
logger = logging.getLogger(__name__)

@app.route("/api/user/authupdate", methods = ['PUT'])
def update_user():
    req = request.json
    token = req['token']
    try:
        username = jwt.decode(token, "secret", algorithms=["HS256"])['sub']
        query = User_n.select().where(User_n.username == username)
        for user in query:
            if(user.authcode == 2):
                User_n.update({User_n.authcode : req['authcode']}).where(User_n.username == req['username'])
                HttpResponse.saveSuccessLogs("Authcode is updated!")
                return HttpResponse().Success("Authcode is updated!") .makeResponse()
            else:
                HttpResponse.saveErrorLogs("Unauthorized operation attempt!")
                return HttpResponse().Unauthorized("Unauthorized operation attempt!") .makeResponse()
            
        HttpResponse.saveErrorLogs("User not found!")
        return HttpResponse().NotFound("User not found!") .makeResponse() 
        
    
    except jwt.ExpiredSignatureError:
        HttpResponse.saveErrorLogs("Signature has expired!")
        return HttpResponse().RequestTimeOut("Signature has expired!") .makeResponse()
  




if __name__ == "__main__":
    app.run(debug=True)