from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def rwordGen():





def index(request):

	request.session['counter']=0

  return render(request, 'randomWord/index.html')

def generate(request):

	random = rwordGen()# generate a random work on click of this button

 	return redirect('/')

def reset(request):

	request.session['counter']=0
	return redirect('/')