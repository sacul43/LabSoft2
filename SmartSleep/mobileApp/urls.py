from django.conf.urls import url
from django.http import HttpResponseRedirect

from . import views

urlpatterns  = [
        url(r'login', views.login, name="login"),
        url(r'home', views.home, name="home"),
#####################Urls para cadastro###################### -->
        url(r'cadastroFis', views.cadastroFis, name="cadastroFis"),
        url(r'cadastroJur', views.cadastroJur, name="cadastroJur"),
         ########################################### -->

          ####################Url para a mainpage de um usuário pessoa juridica####################### -->
        url(r'mainpageJur', views.mainpageJur, name="mainpageJur"),
          ########################################### -->
]
