from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import doctorForm
from portal.models import doctor 


def index(request) :
	return render(request, 'easydoctor/index.html')

def signUp(request):
	if 'session_id' not in request.session:
		return render(request, 'easydoctor/signUp.html')
	else:
		return redirect('http://localhost:8000/portal/dashboard/')
	
def signIn(request):
	if 'session_id' not in request.session:
		return render(request, 'easydoctor/signIn.html')
	else:
		return redirect('http://localhost:8000/portal/dashboard/')

def dashboard(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/signIn/')
	else:
		return render(request, 'easydoctor/dashboard.html')

def registerDoctor (request):
	data = doctorForm(request.POST)
	if data.is_valid():
  		data.save()
		return(HttpResponse('<p>Thank you</p>'))
	else :
		return(HttpResponse('<p>Could not Register</p>'))

def showDoctor (request, doctorId):
	e = doctor.objects.filter(id=doctorId)
	doctorData = "{0}</br> {1}</br> {2}</br> {3}".format(e.first().firstName, e.first().lastName, e.first().displayName, e.first().emailId)    
	return(HttpResponse("%s" %doctorData))

def verify (request):
	email = request.POST['email']
	password = request.POST['password']
	e = doctor.objects.filter(emailId=email,password=password)
	if e.count() == 1:

		request.session['session_id'] = request.COOKIES.get('sessionid') 
		request.session['displayName'] = e.first().displayName

		doctorData = {'firstName': e.first().firstName, 'lastName' : e.first().lastName, 'displayName' : e.first().displayName, 'emailId' : e.first().emailId }    
		#return(HttpResponse("%s" %doctorData))
		# for key, value in request.session.items():
		# 	print str(key) + " : " + str(value)
		return redirect('http://localhost:8000/portal/dashboard/')
	else :
		return(HttpResponse("Check Credintials"))

def logout(request):
    try:
        del request.session['session_id'], request.session['displayName']
    except KeyError:
        pass
    return redirect('http://localhost:8000/portal/signIn/')
    # return HttpResponse("You're logged out.")
