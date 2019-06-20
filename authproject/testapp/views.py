from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  testapp.forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from testapp import forms
from testapp.models import gadi
from django.http import HttpResponseRedirect
from testapp.forms import MyForm 
import requests
def home_page(request):
	return render(request,'testapp/index.html')
@login_required
def apti_exams(request):
	username=None
	if(request.user.is_authenticated()):
		username = request.user.username
		qs=gadi.objects.get(username=username)
	res2=requests.get('https://api.thingspeak.com/channels/581726/fields/1/last.json?results=2')
	val1=res2.json()
	requests.post('https://api.thingspeak.com/update?api_key=FSBHHFZK8LJ9GYZ6&field1='+str(qs.phoneno))
	if val1['field1']=='0':
		k=0
	else:
		k=1
	return render(request,'testapp/aptitudeexam.html',{'qs':qs,'k':k})
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
@login_required
def profile(request):
	username=None
	if(request.user.is_authenticated()):
		username = request.user.username
		qs=gadi.objects.get(username=username)
	return render(request,'testapp/profile.html',{'qs':qs})
@login_required
def form_handle(request):
    form = MyForm()
    if request.method=='POST':
        form = MyForm(request.POST)
        res1=requests.get('https://api.thingspeak.com/channels/581726/fields/1/last.json?results=2')
        val1=res1.json()
        print(val1)
        if(val1['field1']=='0'):
        	requests.post('https://api.thingspeak.com/update?api_key=PY42F6YVI1HHTEMQ&field1='+str(1))
        else:
        	requests.post('https://api.thingspeak.com/update?api_key=PY42F6YVI1HHTEMQ&field1='+str(0))
    return render(request,'testapp/base1.html',{'form':form})
def park(request):
	res1=requests.get('https://api.thingspeak.com/channels/646309/fields/1/last.json?api_key=ZKYWHSD3FUPCO8YI')
	val2=res1.json()
	if(val2['field1']=='1'):
		a=0
		requests.post('https://api.thingspeak.com/update?api_key=9OVZGYDI8UTKJYO2&field1=0')
	else:
		a=1
		requests.post('https://api.thingspeak.com/update?api_key=9OVZGYDI8UTKJYO2&field1=1')
	if(request.user.is_authenticated()):
		username = request.user.username
		qs=gadi.objects.get(username=username)
	return render(request,'testapp/aptitudeexam.html',{'a':a,'qs':qs})
def stop(request):
	username=None
	if(request.user.is_authenticated()):
		username = request.user.username
		qs=gadi.objects.get(username=username)
	requests.post('https://api.thingspeak.com/update?api_key=PY42F6YVI1HHTEMQ&field1=0')
	k=0
	return render(request,'testapp/aptitudeexam.html',{'qs':qs,'k':k})