# -*- coding: utf-8 -*-
#AUTHOR: Samuel M.H. <samuel.mh@gmail.com>

from django.contrib import admin
from models import Redirection

class RedirectionAdmin(admin.ModelAdmin):
    fields = ['user','alias','url','password','public']

admin.site.register(Redirection,RedirectionAdmin)