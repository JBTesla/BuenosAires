from.models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formularioRegistro(UserCreationForm):

    class Meta:
        model= User
        fields = ['username','first_name','last_name','email','password1','password2']


