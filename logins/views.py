# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import RegisterForm,Login


def register(request):
    if request.method == 'POST':
        response = HttpResponse()
        return response

    registerForm = RegisterForm()
    return render(request, 'web/register.html', {'form': registerForm})
def index(request):
    return render(request, 'web/index.html')

def login(request):
    if request.method == 'POST':
        response = HttpResponse()
        return response

    login = Login()
    return render(request, 'web/login.html', {'form': login})

def verFactura(request, id_factura):
    if request.POST.get('click', False):
        registerForm = RegisterForm()
        return render(request, 'web/register.html', {'form': registerForm})