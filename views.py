# -*- coding: utf-8 -*-
#AUTHOR: Samuel M.H. <samuel.mh@gmail.com>

from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import django.http

from models import Redirection


@login_required
def main(request):
    return(render(request, 'main.html',{
        'page':'smh_redirections',
        'username': request.user.username,
    }))


@login_required
def help(request):
    return(render(request, 'help.html'))


class RedirectionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(*args, **kwargs)
    
    
    def get(self,request,username,alias):
        try:
            retval = redirect(Redirection.visit(username, alias), permanent=False)
        except:
            raise django.http.Http404
        return(retval)
    
    
    def post(self,request,username,alias):
        retval = None       
        try:
            #Get Redirection object
            try:
                r = Redirection.objects.get(id=Redirection._mkid(username,alias))        
            except:
                msg = 'Not "{0}" redirection for username "{1}".'.format(alias,username)
                retval = django.http.HttpResponseNotFound(msg)
                raise ValueError(msg)
            #Password
            try:
                password = request.POST['password']
            except:
                msg = 'Missing param "password".'
                retval = django.http.HttpResponseBadRequest(msg)
                raise ValueError(msg)
            else:
                if r.password=='':
                    msg = 'Empty configured password (not editable).'
                    retval = django.http.HttpResponseNotAllowed(msg)
                    raise ValueError(msg)
                if r.password!=password:
                    msg = 'Wrong password.'
                    retval = django.http.HttpResponseNotAllowed(msg)
                    raise ValueError(msg)
            #URL and update
            try:
                url = request.POST['url']
            except:
                url = 'http://'+request.META['REMOTE_ADDR']
            finally:
                r.url = url
                r.save()
                retval = django.http.HttpResponse('Redirection refreshed.')
        except Exception as e:
            pass
        return(retval)
        