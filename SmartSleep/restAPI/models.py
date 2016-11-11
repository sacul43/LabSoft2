from django.db import models
from mongoengine import *

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)

class information(Document):
    deviceID = StringField(required=True)
    location = StringField(required=True)
    data = StringField(required=True)
    dataType = StringField(required=True)
    dateTime = DateTimeField(auto_now=True)


class ClienteFis(Document):
    nome = StringField(required=True)
    CPF = StringField(required=True)
    endereco = StringField(required=True)
    email = StringField(required=True)
    telefone = StringField(required=True)
    user = ObjectIdField(required=True)
