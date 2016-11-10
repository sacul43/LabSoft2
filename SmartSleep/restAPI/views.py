from django.shortcuts import render
from django.template.context_processors import csrf
from .models import User, information
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime, timedelta
from mongoengine.queryset.visitor import Q

@csrf_exempt
def postNewInfo(request):
    if request.method == 'POST':
        deviceID = request.POST['deviceID']
        location = request.POST['location']
        data = request.POST['data']
        dataType = request.POST['dataType']

        print("%s %s %s %s" % (deviceID, location, data, dataType))

        reply = {}

        try:
            newInfo = information.objects.create(deviceID=deviceID, location=location, data=data, dataType=dataType)
            newInfo.save()
            reply['result'] = "ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)

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

@csrf_exempt
def temperaturas(request):
    if request.method == 'GET' and 'ultimosDias' in request.GET:
        result = [ ]
        if request.GET['ultimosDias']:
            ndias = int(request.GET['ultimosDias'])
            result = information.objects(Q(dataType = 'temperatura') & Q(dateTime__gte = datetime.now() - timedelta(days = ndias)))
        return HttpResponse(result.to_json(), content_type="application/json")
    if request.method == 'GET' and 'mediaUltimosDias' in request.GET:
        result = 0
        if request.GET['mediaUltimosDias']:
            ndias = int(request.GET['mediaUltimosDias'])
            result = information.objects(Q(dataType = 'temperatura') & Q(dateTime__gte = datetime.now() - timedelta(days = ndias))).average('data')
        return HttpResponse(result, content_type="application/json")
    if request.method == 'GET':
        result = information.objects(dataType = 'temperatura')
        return HttpResponse(result.to_json(), content_type="application/json")

@csrf_exempt
def umidades(request):
    if request.method == 'GET':
        result = information.objects(dataType = 'Umidade')
        return HttpResponse(result.to_json(), content_type="application/json")
