from django.contrib import admin
from django.urls import path
from register.views import*

urlpatterns = [
    path('register/', Register, name = 'Register'),
]