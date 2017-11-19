from django.shortcuts import render, redirect

# Create your views here.

def index(request):

	return render(request, 'sessionWords/index.html')

def addWord(request):


	if request.session.get('allinfo') == None:
		request.session['allinfo'] =[]

	if request.POST.get('size') == None:
		request.session['size']= 'h4'
	else:
		request.session['size'] = request.POST['size']

	x=[request.POST['word'], request.POST['color'], request.session['size']]

	allinfo=request.session['allinfo']
	allinfo.append(x)

	print allinfo

	for i in request.session['allinfo']:
		print i[0]

	
	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')