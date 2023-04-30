from django.contrib import admin
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('employees/', views.employees, name="employees")
]
