from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns  = [
        url(r'login', views.login, name="login"),
        url(r'postNewInfo', views.postNewInfo, name="postNewInfo"),
        url(r'temperaturas', views.temperaturas, name="temperaturas"),
        url(r'umidades', views.umidades, name="umidades"),
        url(r'ruidos', views.ruidos, name="ruidos"),
        url(r'luminosidades', views.luminosidades, name="luminosidades"),
        url(r'', views.umidades, name="umidades"),
]
