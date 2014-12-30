# -*- coding: utf-8 -*-
#AUTHOR: Samuel M.H. <samuel.mh@gmail.com>

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Redirection(models.Model):
    id = models.CharField(max_length = 200, primary_key=True)
    user = models.ForeignKey(User)
    alias = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    public = models.BooleanField(default=False)
    last_refresh = models.DateTimeField(auto_now=True)
    prints = models.IntegerField()
    
    
    @staticmethod
    def _mkid(user, alias):
        return('{0}-{1}'.format(user,alias))
    
    
    @staticmethod
    def _get_user(username):
        return(User.objects.get(username=username))
      
    
    def save(self,*args, **kwargs):
        self.last_refresh = datetime.now()
        super(Redirection, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return(self.id)

    #
    ### View methods
    #
    
    @classmethod
    def visit(cls, username, alias):
        '''
        Visit a redirection. Prints +1.
        
        Returns:
            retval: URL to be redirected to.
            exception: user not valid, alias not valid, not public
        '''
        user = cls._get_user(username)
        id = cls._mkid(user, alias)
        redirection = cls.objects.get(id=id)
        if not redirection.public:
            raise ValueError('Not public redirection')
        redirection.prints +=1
        redirection.save()
        return(redirection.url)


    
    #
    ### API methods
    #
    
    
    @classmethod
    def get (cls, username, public=False):
        query = {'user': cls._get_user(username)}
        if public:
            query['public'] = True
        return(Redirection.objects.filter(**query))


    @classmethod
    def create(cls,username,alias,url,public,password):
        '''
        Create a redirection
        '''
        if url==None or url=='':
            raise ValueError('URL is empty.')
        
        redirection = cls(
            user = cls._get_user(username),
            alias = alias,
            url = url,
            public = public,
            password = password,
            id = cls._mkid(username,alias),
            prints = 0            
        )
        redirection.save()
        return(True)
    
    
    @classmethod
    def delete(cls, username, alias):
        redirection = cls.objects.get(
            user = cls._get_user(username),
            alias = alias
        )
        super(cls, redirection).delete()
        return(True)
