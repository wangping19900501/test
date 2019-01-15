from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

# Create your views here.
def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request, new_user)
			return redirect('index')
	else:
		form = UserForm()
		return render(request, 'adduser.html', {'form': form})

def signin(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			return HttpResponse('Login Failed')
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

def post(request):
	if request.method == "POST":
		form = PostForm