from django.shortcuts import render, HttpResponse
from register.models import Register

# Create your views here.

def Login(request):

	return render(request, 'login.html')

def Logged(request):

	if request.method == 'POST':

		username = request.POST.get('username', 'empty')
		password = request.POST.get('password', 'empty')

		db_user = Register.objects.get(username = username)
		db_psw = db_user.password

		if db_user:

			#db_username, db_password = db_user[0], db_user[1]

			# return HttpResponse(f'username: {db_username} | Password: {db_password}')

			if db_psw == password:

				return HttpResponse(f'username: {db_user} | password: {db_psw}')
