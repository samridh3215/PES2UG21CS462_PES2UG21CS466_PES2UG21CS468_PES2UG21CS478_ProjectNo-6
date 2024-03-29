from django.shortcuts import render
from  django.views.decorators.csrf import csrf_exempt
import json
from django.http.response import HttpResponse
from core.models import CustomerAccount
# Create your views here.
@csrf_exempt
def signUp(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            CustomerAccount.objects.create(email=data['email'], passwd=data['password']).save()
            return HttpResponse("Registered")
        except Exception as e:
            return HttpResponse(e)
    
@csrf_exempt
def signIn(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if (CustomerAccount.objects.filter(email=data['email'], passwd=data['password']).exists()):
            return HttpResponse("SignedIN")
        else:
            return HttpResponse("Wrong creds")