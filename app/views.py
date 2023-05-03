from genericpath import exists
from math import prod
from urllib import response
#import requests #NOS PERMITE LEER EL API
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect
from django.contrib import messages
from.forms import *
from.models import *
# Create your views here.

def index (request):
    
    
    return render(request, 'index.html')

def registrar(request):
    datos = {
        'form' : formularioRegistro()
    }
    if request.method == 'POST':
        formulario = formularioRegistro(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            #messages.success(request,'Registrado correctamente!')
            #User.groups.add(Empleado)
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'app/registration/register.html', datos)