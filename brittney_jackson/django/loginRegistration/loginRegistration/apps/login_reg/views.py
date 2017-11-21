from django.shortcuts import render, redirect, HttpResponse
from .models import Users



# Create your views here.

def index(request):
	if request.session.get('errors') == None:
		request.session['errors'] =[]
                               
	return render(request, 'login_reg/index.html') 

def register(request):
	if request.method == 'POST':
		errors = Users.objects.register_validation(request.POST)
		print errors
		if len(errors) != 0:
			request.session['errors'] = errors
			return redirect('/')
		else:
			user= Users.objects.register(request.POST)
			request.session['user_id'] = user.id
			print user.id
			return redirect('/success')

def login(request):
	errors = Users.objects.login_validation(request.POST)
	print errors
	if len(errors) != 0:
		request.session['errors'] = errors
		return redirect('/')
	else:
		user= Users.objects.login(request.POST)
		print user
		request.session['user_id'] = user.id
		request.session['name']=user.first_name
		return redirect('/success')

def success(request):

	return render(request, 'login_reg/success.html')