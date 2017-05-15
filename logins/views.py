# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

# Create your views here.
from .models import User
from django.http import HttpResponse
import MySQLdb
# from .forms import Login,RegisterForm
def index(request):
    acount = User.objects.all()
    template = loader.get_template('web/index.html')
    context = {
        'user': acount,
    }

    return HttpResponse(template.render(context, request))
    # return render(request, 'web/index.html')

def login(request):
    if request.method == 'POST':
        phone=request.POST.get('phone')
        password=request.POST.get('pass')
        if phone =='' or password =='':
            return render(request, 'web/login.html', {'message': "Bạn phải nhập đầy đủ thông tin"})
        else:
            try:
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                user = None
            if user is None :
                return render(request, 'web/login.html', {'message': "Tài khoản không tồn tai"})
            else:
                if user.password==password:
                    return HttpResponseRedirect('/index')
                else:
                    return render(request, 'web/login.html', {'message': "Sai mật khẩu"})




    return render(request, 'web/login.html')

def register(request):
    if request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Register success</h1></br>")
        response.write("Your username: " + request.POST.get('phone') + "</br>")
        phone = request.POST.get('phone')
        password = request.POST.get('pass')
        email = request.POST.get('email')
        name = request.POST.get('name')
        birthday = request.POST.get('birthday')
        account= User(phone=phone,password=password,access_token="",name=name,email=email,birthday=birthday)
        account.save()
        return response

    return render(request, 'web/register.html')
def permission(request,phone):
    template = loader.get_template('web/permission.html')
    context = {
        'user': phone,
    }

    return HttpResponse(template.render(context, request))