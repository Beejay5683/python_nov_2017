from django.shortcuts import render, redirect
import random


# Create your views here.
def index(request):
	if request.session.get('total') == None:
		request.session['total'] = 0
	

	return render(request, 'goldapp/index.html')

def process(request):
	if request.session.get('activities')== None:
		request.session['activities'] = []
	activity = request.session['activities']

	if request.POST['building']=='farm':
		request.session['gold']=random.randrange(10,21)
		request.session['total'] += request.session['gold']
		activity.append('Earned '+str(request.session['gold'])+' gold from the farm!')
		print 'Farm'+str(request.session['gold'])
	elif request.POST['building']== 'cave':
		request.session['gold']=random.randrange(5,11)
		request.session['total'] += request.session['gold']
		activity.append('Earned '+str(request.session['gold'])+' gold from the cave!')
		print 'Cave'+str(request.session['gold'])
	elif request.POST['building']== 'home':
		request.session['gold']=random.randrange(2,6)
		request.session['total'] += request.session['gold']
		activity.append('Earned '+str(request.session['gold'])+' gold from the home!')
		print 'Home '+str(request.session['gold'])
	elif request.POST['building']== 'casino':
		request.session['gold']=random.randrange(-50,51)
		request.session['total'] += request.session['gold']
		if request.session['gold']>=0:
			activity.append('\nEarned '+str(request.session['gold'])+' gold from the casino!')
			print 'Casino Earned '+str(request.session['gold'])
		else:
			activity.append('\nLost '+str(abs(request.session['gold']))+' gold from the casino')
			print 'Casino lost'+str(abs(request.session['gold']))

	return redirect('/')