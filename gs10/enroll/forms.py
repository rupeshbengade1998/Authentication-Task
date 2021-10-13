from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.forms import fields, widgets


class SignupForm(UserCreationForm):
    password2=forms.CharField(label='confrim password (again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username', 'first_name','last_name','email']
        labels={'email':'Email'}


class Edituserform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username', 'first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email'}



class EditAdminform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}


