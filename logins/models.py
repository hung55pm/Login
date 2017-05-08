# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
        phone= models.CharField(max_length=15, primary_key= True)
        password= models.CharField('Password',max_length=20)
        access_token= models.TextField(max_length=50)
        name =models.TextField('Name',max_length=50)
        birthday=models.DateTimeField("Ngày sinh")
        email=models.TextField('Email',max_length=20)