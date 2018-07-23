from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/templates/',views.login, name='login'),
    path('/templates/',views.loggedin, name='loggedin'),
    path('/templates/',views.invalid_login, name='invalid_login'),
    path('/templates/',views.logout, name='logout'),
]
