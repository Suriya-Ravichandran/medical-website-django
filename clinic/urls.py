from django.urls import path
from . import views

app_name="clinic"

urlpatterns = [
    path("",views.index,name="index"),
    path("about/<int:id>",views.about,name="about"),
    path("old_url",views.old_url,name="old_url"),
    path("new_url",views.new_url,name="new_url"),
]
