from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse        

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
