from peewee import *
import re 

db = MySQLDatabase('TestSchema', user='arda', password='adana123',
                         host='34.65.69.42', port=3306)

class User_n(Model):
    username = CharField()
    password = CharField()
    email = CharField()
    authcode = IntegerField()
    class Meta:
        database = db


    def validate_mail(mail):
        regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
        return re.match(regex, mail)
