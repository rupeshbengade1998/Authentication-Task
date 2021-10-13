from django.shortcuts import render ,HttpResponseRedirect
from .forms import SignupForm, Edituserform,EditAdminform
from django.contrib import messages
from django.contrib.auth .forms import AuthenticationForm ,PasswordChangeForm,SetPasswordForm,UserChangeForm 
from django.contrib.auth import login , logout ,authenticate, update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    if request.method=="POST":
      fm=SignupForm(request.POST)
      if fm.is_valid():
        messages.success(request,"account is created")
        fm.save()
    else:
     fm=SignupForm()
    return render(request,"enroll/signup.html",{'form':fm})


def userlogin(request):
  if not request.user.is_authenticated: 
    if request.method=="POST":
      fm=AuthenticationForm(request.POST, data=request.POST)
      if fm.is_valid():
        uname=fm.cleaned_data['username']
        upass=fm.cleaned_data['password']
        user=authenticate(username=uname, password=upass)
        if user is not None:
          login(request,user)
          messages.success(request,"login successfully")
          return HttpResponseRedirect('/dashborad/')
    else:            
      fm=AuthenticationForm()
    return render(request,'enroll/userlogin.html',{'form':fm})
  else:
    return HttpResponseRedirect('/dashborad/')


def user_dashborad(request):
  if request.user.is_authenticated:
    return render(request,'enroll/dashborad.html',{'name':request.user.username})
  else:
   return HttpResponseRedirect('/login/')

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
