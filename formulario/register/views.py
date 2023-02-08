from django.shortcuts import render, HttpResponse
from register.models import Register

# Create your views here.

def Sign_up(request):

	return render(request, 'register.html')

def Registration(request):

	name = request.POST.get('firstname', 'warevar')
	lastname = request.POST.get('lastname', 'warevar')
	email = request.POST.get('email', 'warevar')
	username = request.POST.get('username', 'warevar')
	password = request.POST.get('password', 'warevar')
	cpassword = request.POST.get('cpass', 'warevar')

	if request.method == 'POST':

		if password == cpassword:

			db_username = Register.objects.filter(username=username)

			if db_username:

				return HttpResponse(f"Username: {db_username[0]} already exist")

			else:
				user = Register.objects.create(name = name, lastname = lastname, username = username, email = email, password = password)
				return render(request, 'login.html')

		else:

			return HttpResponse("Password doesn't match")