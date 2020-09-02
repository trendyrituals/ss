from django.shortcuts import render, redirect
from .forms import ShopkeeperForm
from main.models import Profile

from django.contrib.auth import logout

from django.contrib.auth.models import Group

import time

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		name = Profile.objects.get(user_name = request.user.username)
		usr = request.user.username
		context = {
			'usr': usr,
			'name' : name
		}
		return render(request,'dash/home.html',context)
	else:
		return redirect('/login/')


def create_shopkeeper(request):
	if request.user.is_authenticated:
		form = ShopkeeperForm(request.POST or None)
		if form.is_valid():
			user_name = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			re_password = form.cleaned_data.get('re_password')
			if password == re_password:
				user_register = form.save(commit=False)
				user_register.set_password(password)
				user_register.save()
				group = Group.objects.get(name='shopkeeper')
				user_register.groups.add(group)

				ref = Profile.objects.get(user_name= request.user.username)
				nme = ref.user_name
				code = ref.user_code

				a = time.time()
				b = str(a)
				c = b.split('.')
				gen_code = c[0]

				shoppy = Profile(user_name=user_name,user_code=gen_code,ref_user=nme,ref_user_code=code)
				shoppy.save()

				return redirect('/dash/detail/')

		context = {
			'form': form
		}
		return render(request,'dash/shopkeeper.html',context)
	else:
		return redirect('/login/')



def create_customer(request):
	if request.user.is_authenticated:
		return render(request,'dash/customer.html',{})
	else:
		return redirect('/login/')



def detail_view(request):
	if request.user.is_authenticated:
		listt = Profile.objects.filter(ref_user = request.user.username).order_by('-id')

		context = {
			'obj_list': listt
		}
		return render(request,'dash/detail.html',context)


def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('/')



