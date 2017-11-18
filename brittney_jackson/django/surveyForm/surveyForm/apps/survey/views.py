from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
  return render(request, 'survey/index.html')

def process(request):
 	if request.session.get('counter') == None:
 		request.session['counter'] = 0
 	
 	print request.session['counter']
 	print request.POST['name']
 	print request.POST['location']
	print request.POST['language']
	print request.POST['comment']

 	request.session['name'] = request.POST['name']
 	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']

	return redirect('/result')

def result(request):
	request.session['counter'] += 1
	

	return render(request, 'survey/result.html')



