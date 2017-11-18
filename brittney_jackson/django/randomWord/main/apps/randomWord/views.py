from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random
import string

# Create your views here.
def rwordGen(n):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def index(request):
	if request.session.get('counter') == None:
		request.session['counter']=1
		request.session['word']= rwordGen(14)

	return render(request, 'randomWord/index.html')

def generate(request):
	request.session['counter'] += 1
	print request.session['counter']
	request.session['word'] = rwordGen(14)

 	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')