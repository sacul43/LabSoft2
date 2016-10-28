from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns  = [
        url(r'login', views.login, name="login"),
]
