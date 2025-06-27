from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request,id):
    product=[
        {"pid":1,"pname":"Apple","price":300.0,"dist":"30%","image":"{% static 'asset/images/client.jpg' %}"},
        {"pid":2,"pname":"Mango","price":300.0,"dist":"30%","image":"/images/client.jpg"},
        {"pid":3,"pname":"Graphs","price":300.0,"dist":"30%","image":"/images/client.jpg"},
        {"pid":4,"pname":"Jack fruit","price":300.0,"dist":"30%","image":"/images/client.jpg"},
    ]
    productdetail=next((item for item in product if item["pid"] == int(id)),None)
    return render(request,"demo2.html",{"productdetail":productdetail})

def old_url(request):
    return redirect("clinic:new_url")

def new_url(request):
    return HttpResponse("This is new page")