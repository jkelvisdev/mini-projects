from django.contrib import admin
from django.urls import path
from register.views import*

urlpatterns = [
    path('register/', Sign_up, name = 'Register'),
    path('registration/', Registration, name = 'Registration')
]
