from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        r = requests.post("http://104.236.90.130:8000/restAPI/login", data={"username" : username, "password" : password})

        r = r.json()

        if r['result'] == "Login Okay":
            return redirect('/mobileApp/home')
        else:
            return redirect('/mobileApp/login')


@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'mainPage.html', {})
