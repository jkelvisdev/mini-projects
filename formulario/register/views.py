from django.shortcuts import render, HttpResponse

# Create your views here.

def Register(request):
	return render(request, 'register.html')

def registration_completed(request):

	return 