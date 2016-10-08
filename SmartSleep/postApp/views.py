from django.shortcuts import render
from .models import postInformation
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


@csrf_exempt
def postNewInfo(request):
    if request.method == 'POST':
        deviceID = request.POST['deviceID']
        location = request.POST['location']
        data = request.POST['data']

        reply = {}

        try:
            newInfo = postInformation.objects.create(deviceID=deviceID, location=location, data=data)
            newInfo.save()
            reply['result'] = "ok"
        except Exception as e:
            reply['result'] = "Error while saving data to database"

        return JsonResponse(reply)
