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

        r = requests.post("http://127.0.0.1:8000/restAPI/login", data={"username" : username, "password" : password})

        r = r.json()

        if r['result'] == "Login Okay":
            return redirect('/mobileApp/home')
        else:
            return redirect('/mobileApp/login')


@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'mainPage.html', {})

 #####################Views para cadastro###################### -->

@csrf_exempt
def cadastroFis(request):

    if request.method == "GET":

        return render(request, 'cadastroFis.html', {})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        nome = request.POST['nome']
        CPF = request.POST['CPF']
        endereco = request.POST['endereco']
        email = request.POST['email']
        telefone = request.POST['telefone']

        r = requests.post("http://127.0.0.1:8000/restAPI/cadastroFis", data={"username" : username, "password" : password, "nome" : nome, "CPF" : CPF, "enderco" : endereco, "email" : email, "telefone" : telefone})


        return HttpResponseRedirect('/mobileApp/login')



@csrf_exempt
def cadastroJur(request):

        return render(request, 'cadastroJur.html', {})

 ########################################### -->


######################Views da mainpage de um usuario pessoa juridica##################### -->
@csrf_exempt
def mainpageJur(request):
        return render(request, 'mainpageJur.html', {})
########################################### -->
