from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        reply = {}

        try:
            client = MongoClient()
            db = client['smartsleep']
            user = db.login.find({"username":username,"password":password})
            print(user)
            if user is None:
             reply['result'] = "Login invalido"
             print("login invalido")
             return JsonResponse(reply)
            reply['result'] = "Login Okay"
            print('logado: ' + user)
        except Exception as e:
            reply['result'] = "Erro no banco de dados"

        return JsonResponse(reply)
