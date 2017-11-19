from django.shortcuts import render, redirect

# Create your views here.
def index(request):

	return render(request, 'amadonapp/index.html')

def buy(request):
	if request.session.get('total') == None:
		request.session['total'] = 0.00
	if request.session.get('items') == None:
		request.session['items'] = 0

	if request.POST['productid']=='shirt':
		request.session['price'] = 19.99
		request.session['total'] += request.session['price']
		request.session['items'] += int(request.POST['quantity'])
	elif request.POST['productid']=='sweater':
		request.session['price'] = 29.99
		request.session['total'] += request.session['price']
		request.session['items'] += int(request.POST['quantity'])
	elif request.POST['productid']=='cup':
		request.session['price'] = 4.99
		request.session['total'] += request.session['price']
		request.session['items'] += int(request.POST['quantity'])
	elif request.POST['productid']=='book':
		request.session['price'] = 49.99
		request.session['total'] += request.session['price']
		request.session['items'] += int(request.POST['quantity'])











	print request.session['total']
	print request.session['price']
	print request.session['items']

	return redirect('/checkout')

def checkout(request):

	return render(request, 'amadonapp/checkout.html')