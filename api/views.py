# -*- coding: utf-8 -*-
#AUTHOR: Samuel M.H. <samuel.mh@gmail.com>


from django.views.generic import View
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

from smh_jwt.decorators import jwt_required
from smh_jwt.models import IdToken

from smh_redirections.models import Redirection




#
### How to serialize model fields
#

serializer = {
    field: lambda x: x
    for field in 
    Redirection._meta.get_all_field_names()
}

serializer['last_refresh'] = lambda(x):int(x.strftime('%s'))*1000

def filter_fields(dicts,fields):
    return([
        {f:serializer[f](d[f]) for f in fields}
        for d in dicts
    ])



class ListResources(View):

    def get (self, request, username):
        try:
            jwt = IdToken.decode_from_request(request)
            assert(username==jwt['username'])
            public_only = False
            fields = ['alias','url','prints','password','public','last_refresh']
        except:
            public_only = True
            fields = ['alias','url']           
        try:
            retval = filter_fields(
                dicts = Redirection.get(username, public=public_only).values(),
                fields = fields
            )
        except:
            retval = []
        return(JsonResponse({'redirections':retval}))
      

    
    
class Resource(View):
        
    @method_decorator(csrf_exempt)
    @method_decorator(jwt_required)
    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(*args, **kwargs)
    
    
    def delete(self, request, username, alias):
        try:
            Redirection.delete(request.jwt['username'],alias)
            msg = 'OK'
            status = 200
        except Exception as e:
            msg = e
            status = 404
        return(JsonResponse({'msg':msg}, status=status))
            
            
            
    def put(self, request, username, alias):
        try:
            data = json.loads(request.body)
            Redirection.create(
                username=request.jwt['username'],
                alias=alias,
                url=data['url'],
                public=data['public'],
                password=data['password'],
            )
            msg = 'OK'
            status = 200 
        except Exception as e:
            msg = e.message
            status  = 404
        return(JsonResponse({'msg': msg}, status=status))
    
