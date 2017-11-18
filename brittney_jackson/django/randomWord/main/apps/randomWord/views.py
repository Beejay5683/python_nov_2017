from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def rwordGen():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def index(request):

	request.session['counter']=0

	return render(request, 'randomWord/index.html')

def generate(request):
	request.session['counter'] += 1

	random = rwordGen(14)# generate a random work on click of this button

 	return redirect('/')

def reset(request):

	request.session['counter']=0
	return redirect('/')