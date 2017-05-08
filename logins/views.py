# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import Login,RegisterForm
def index(request):
    return render(request, 'web/index.html')

def login(request):
    if request.method == 'POST':
        response = HttpResponse()
        # response.write("<h1>Login success</h1></br>")
        # response.write("Your username: " + request.POST['phone'] + "</br>")
        return response

    # login = Login()
    return render(request, 'web/login.html')
    # return render(request, 'web/login.html', {'form': login})

def register(request):
    if request.method == 'POST':
        response = HttpResponse()
        # response.write("<h1>Register success</h1></br>")
        # response.write("Your username: " + request.POST['phone'] + "</br>")
        return response

    # register = RegisterForm()
    return render(request, 'web/register.html')
    # return render(request, 'web/register.html', {'form': register})
