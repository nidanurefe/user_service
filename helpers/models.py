from peewee import *

db = MySQLDatabase('SchemaName', user='user', password='password',
                         host='host', port='port')

class User_n(Model):
    username = CharField()
    password = CharField()
    email = CharField()
    authcode = IntegerField()
    class Meta:
        database = db



