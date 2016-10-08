from django.db import models
from mongoengine import *

class User(Document):
        username = StringField(required=True)
        password = StringField(required=True)
