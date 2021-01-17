from django.shortcuts import render , redirect
from django.contrib.auth.models import User ,auth
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import photo

def instructions(request):
	return render(request,'instruction.html')


def index(request):
	pos = photo.objects.all()
	return render(request,'index.html',{'pos':pos})


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('index')
        else:
            error = " Sorry! username and Password didn't match, Please try again ! "
            return render(request, 'login.html',{'error':error})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
    	username = request.POST.get('username')
    	email = request.POST.get('email')
    	pass_1 = request.POST.get('password1')
    	pass_2 = request.POST.get('password2')
    	if pass_1 == pass_2:
            user = User.objects.create_user(
                                              username=username,
                                              email=email,
                                              password=pass_1,
                                             )
            user.save()
            print('user created')
            return HttpResponseRedirect("login")
    	else:
        	error = " Password Mismatch "
        	return render(request, 'signup.html',{"error":error})
    else:
    	return render(request, 'signup.html')


def profile(request, username):
	user = User.objects.get(username=username)
    
	pos = photo.objects.all()
	context = {
    	"user": user,
    	"pos": pos 
    }
	return render(request, 'profile.html', context)


# Create your views here. 
def addpost(request): 

	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid(): 
			form.save() 
			return redirect('success') 
	else: 
		form = PhotoForm() 
	return render(request, 'addpost.html', {'form' : form}) 


def success(request): 
	return render(request,'success.html') 

def logout(request):
    auth.logout(request)
    return redirect("login")
