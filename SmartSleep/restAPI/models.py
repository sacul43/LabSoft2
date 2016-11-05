from django.db import models
from mongoengine import *
import datetime

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)

class information(Document):
    deviceID = StringField(required=True)
    location = StringField(required=True)
    data = StringField(required=True)
    dataType = StringField(required=True)
    dateTime = DateTimeField(default=datetime.datetime.now)
