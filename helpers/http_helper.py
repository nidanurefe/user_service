from __future__ import annotations
from flask import Response, make_response
import logging

class HttpResponse():
    def __init__(self, statusCode=200, isSuccess=True, responseMessage="", data:dict = {}) -> None:
        self.statusCode = statusCode
        self.isSuccess = isSuccess
        self.responseMessage = responseMessage
        self.data = data

    def saveErrorLogs(message):
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename='./logs/stderr.log', encoding='utf-8', level=logging.DEBUG)
        return logger.error(message)
    
    def saveSuccessLogs(message):
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename='./logs/stdout.log', encoding='utf-8', level=logging.DEBUG)
        return logger.error(message)

    def BadRequest(self, responseMsg="400 Bad Request") -> HttpResponse:
        self.statusCode = 400
        self.isSuccess = False
        self.responseMessage = responseMsg
        self.saveErrorLogs()
        return self

    def Unauthorized(self, responseMsg="401 Unauthorized!"):
        self.statusCode = 401
        self.responseMessage = responseMsg
        self.isSuccess = False
        self.saveErrorLogs()
        return self

    def Forbidden(self, responseMsg="403 Forbidden!"):
        self.statusCode = 403
        self.isSuccess = False
        self.responseMessage = responseMsg
        self.saveErrorLogs()
        return self

    def NotFound(self, responseMsg="404 Not Found"):
        self.statusCode = 404
        self.responseMessage =responseMsg
        self.isSuccess=False
        self.saveErrorLogs()
        return self

    def MethodNotAllowed(self, responseMsg="Method Not Allowed"):
        self.statusCode = 405
        self.responseMessage = responseMsg
        self.isSuccess = False
        self.saveErrorLogs()
        return self

    def RequestTimeOut(self, responseMsg="Response Time Out"):
        self.statusCode = 408
        self.responseMessage =responseMsg
        self.isSuccess = False
        self.saveErrorLogs()
        return self

    def Created(self, responseMsg="201 Created"):
        self.statusCode = 201
        self.isSuccess = True
        self.responseMessage = responseMsg
        self.saveSuccessLogs()
        return self
    
    def Success(self, responseMsg="200 OK"):
        self.statusCode = 201
        self.isSuccess = True
        self.responseMessage = responseMsg
        self.saveSuccessLogs()
        return self


    def makeResponse(self) -> Response: 
        return make_response(self.__dict__, self.statusCode)

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return self.__dict__

    def __getitem__(self, item):
        return self.__dict__[item]
    
