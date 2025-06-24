from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    a=10
    b=20
    result=a+b

    return HttpResponse(f"Hello world {result}")

def about(request):
    return HttpResponse("This is a about page")
