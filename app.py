from flask import Flask, request
from helpers.models import User_n
from helpers.http_helper import HttpResponse
from helpers.token_helper import generateToken, hashPw
from helpers.validation_helper import validateMail
import jwt # type: ignore
import peewee as pw

app = Flask("__main__")


@app.route('/api/user', methods = ['POST', 'GET', 'DELETE'])
def getRequest():
    req = request.json
    if request.method == 'POST':
        addUser(req)
    elif request.method == "GET":
        getUser(req)
    elif request.method == "DELETE":
        deleteUser(req)


def addUser(req):
    query = User_n.select().where(User_n.username == req['username'] or User_n.email == req['email']  )
    user = query.execute()

    for user in User_n.select():
        if(user.username == req['username'] or user.email == req['email']):
            HttpResponse.saveErrorLogs("User already exists!")
            return HttpResponse().BadRequest("User already exists!").makeResponse()
        
    if User_n.validate_mail(req['email']):
        hashed = hashPw(req['password'])

        user = User_n.create(username = req['username'], 
                        password = hashed,
                        email = req['email'], 
                        authcode = req['authcode'])
        
        user.save()
        return HttpResponse().Created("User saved").makeResponse()
    else:
        return HttpResponse().BadRequest("Invalid email format!") .makeResponse()


def getUser(req):
    hashed = hashPw(req['password'])
    query = User_n.select().where(User_n.username == req['username'] , User_n.password == hashed) 
    if query:
        token = generateToken(req['username'])
        return{
            "token" : token,
            "expireDate" : ["exp"]
        }

    else:
        return HttpResponse().NotFound("Wrong username or password!").makeResponse()


def deleteUser(req):
    token = req['token']
    try:
        username = jwt.decode(token, "secret", algorithms=["HS256"])['sub']
        query = User_n.select().where(User_n.username == username)
        for user in query:
            if(user.authcode == 2):
                try: 
                    user_to_delete = User_n.get(User_n.username == req['username'])
                    user_to_delete.delete_instance()
                    return HttpResponse().Success("User is deleted!") .makeResponse()
                except pw.DoesNotExist:
                        
                    return HttpResponse().NotFound("User not found!") .makeResponse() 
            else:
                return HttpResponse().Unauthorized("Unauthorized operation attempt!") .makeResponse()
            
        
    except jwt.ExpiredSignatureError:
        return HttpResponse().RequestTimeOut("Signature has expired!") .makeResponse()
    


@app.route("/api/user/authupdate", methods = ['PUT'])
def updateUser(req):
    token = req['token']
    try:
        username = jwt.decode(token, algorithms=["HS256"])['sub']
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

