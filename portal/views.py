from django.shortcuts import render
from django.http import HttpResponse
from .forms import doctorForm
from portal.models import doctor 

def register(request):
	return render(request, 'easydoctor/signUp.html')

def signIn(request):
	return render(request, 'easydoctor/signIn.html')

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
		doctorData = "{0}</br> {1}</br> {2}</br> {3}".format(e.first().firstName, e.first().lastName, e.first().displayName, e.first().emailId)    
		#return(HttpResponse("%s" %doctorData))
		return render(request, 'easydoctor/dashboard.html')
	else :
		return(HttpResponse("Check Credintials"))
