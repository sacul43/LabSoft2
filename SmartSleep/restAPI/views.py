from django.shortcuts import render
from django.template.context_processors import csrf
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        reply = {}

        exists = False
        try:
            for user in User.objects(username=username, password=password):
                exists = True

            if exists == False:
                reply['result'] = "Login invalido"
                print("login invalido")
                return JsonResponse(reply)
                #User.objects.create(username=username, password=password).save()
            else:
                reply['result'] = "Login Okay"
                print('logado: ' + user.username)
        except Exception as e:
            print(e)
            reply['result'] = "Erro no banco de dados"

        return JsonResponse(reply)
