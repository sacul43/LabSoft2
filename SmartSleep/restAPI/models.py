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
