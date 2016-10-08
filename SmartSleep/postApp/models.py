from django.db import models
from mongoengine import *

class postInformation(Document):
	deviceID = StringField(required=True)
	location = StringField(required=True)
	data = StringField(required=True)
	dateTime = DateTimeField(auto_now=True)
