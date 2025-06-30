from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
   return render(request,"about.html")

def old_url(request):
    return redirect("clinic:new_url")

def new_url(request):
    return HttpResponse("This is new page")