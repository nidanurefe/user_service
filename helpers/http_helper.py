from __future__ import annotations
from flask import Response, make_response

class HttpResponse():
    def __init__(self, statusCode=200, isSuccess=True, responseMessage="", data:dict = {}) -> None:
        self.statusCode = statusCode
        self.isSuccess = isSuccess
        self.responseMessage = responseMessage
        self.data = data

    def BadRequest(self, responseMsg="400 Bad Request") -> HttpResponse:
        self.statusCode = 400
        self.isSuccess = False
        self.responseMessage = responseMsg
        return self

    def Unauthorized(self, responseMsg="401 Unauthorized!"):
        self.statusCode = 401
        self.responseMessage = responseMsg
        self.isSuccess = False
        return self

    def Forbidden(self, responseMsg="403 Forbidden!"):
        self.statusCode = 403
        self.isSuccess = False
        self.responseMessage = responseMsg
        return self

    def NotFound(self, responseMsg="404 Not Found"):
        self.statusCode = 404
        self.responseMessage =responseMsg
        self.isSuccess=False
        return self

    def MethodNotAllowed(self, responseMsg="Method Not Allowed"):
        self.statusCode = 405
        self.responseMessage = responseMsg
        self.isSuccess = False
        return self

    def RequestTimeOut(self, responseMsg="Response Time Out"):
        self.statusCode = 408
        self.responseMessage =responseMsg
        self.isSuccess = False
        return self

    def Created(self, responseMsg="201 Created"):
        self.statusCode = 201
        self.isSuccess = True
        self.responseMessage = responseMsg
        return self


    def makeResponse(self) -> Response: 
        return make_response(self.__dict__, self.statusCode)

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return self.__dict__

    def __getitem__(self, item):
        return self.__dict__[item]