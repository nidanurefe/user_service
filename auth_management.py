from flask import Flask, request
from helpers.models import User_n
from helpers.http_helper import HttpResponse
import jwt # type: ignore


app = Flask('__main__')


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
                return HttpResponse().Success("Authcode is updated!") .makeResponse()
            else:
                return HttpResponse().Unauthorized("Unauthorized operation attempt!") .makeResponse()
        return HttpResponse().NotFound("User not found!") .makeResponse() 
        
    
    except jwt.ExpiredSignatureError:
        return HttpResponse().RequestTimeOut("Signature has expired!") .makeResponse()
  




if __name__ == "__main__":
    app.run(debug=True)