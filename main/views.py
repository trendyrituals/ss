from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, EnquiryForm

# Create your views here.
def home(request):
	return render(request,'main/home.html',{})

def contact_us(request):
	form = EnquiryForm(request.POST or None)
	context = {
		'form':form
	}
	return render(request,'main/contact.html',context)

def about(request):
	return render(request,'main/about.html',{})



def login_view(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')

		user = authenticate(username=username,password=password)
		try:
			login(request,user)
			return redirect('/dash/')
		except:
			return redirect('/login/')

	context = {
		'form':form
	}
	return render(request,'main/login.html',context)
