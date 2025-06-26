from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    data="Welcome Back To App"

    product=[
        {"pid":1,"pname":"apple","price":300.0,"dist":"30%"},
        {"pid":2,"pname":"mango","price":300.0,"dist":"30%"},
        {"pid":3,"pname":"graphs","price":300.0,"dist":"30%"},
        {"pid":4,"pname":"jack fruit","price":300.0,"dist":"30%"},
    ]

    return render(request,"demo.html",{"data":data,"product":product})

def about(request,id):
    return HttpResponse(f"This is a about page: {id}")

def old_url(request):
    return redirect("clinic:new_url")

def new_url(request):
    return HttpResponse("This is new page")