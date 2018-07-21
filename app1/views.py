from django.http import HttpResponse
from django.shortcuts import render
from django.core.context_precessors import csrf
from django.contrib.auth import authenticate, login

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, '/templates/home.html', {'app1': p})
    else:
        return HttpResponse("invalid user")

def loggedin(request):
	return render_to_response(loggedin.html.
		                      {'full_name': request.user.usernmae})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
