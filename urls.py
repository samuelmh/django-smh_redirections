# -*- coding: utf-8 -*-
#AUTHOR: Samuel M.H. <samuel.mh@gmail.com>

from django.conf.urls import patterns, include, url
from views import RedirectionView

urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = 'smh_redirections.views.main',
        name  = 'main'
    ),
    url(
        regex = r'^help$',
        view  = 'smh_redirections.views.help',
        name  = 'help'
    ),
    
    ### API
    url(
        regex = r'^api/v1/',
        view  = include('smh_redirections.api.urls', namespace = 'api'),
    ),
    
    ### Generic redirection
    url(
        regex = r'^(?P<username>\w+)/(?P<alias>\w+)$',
        view  = RedirectionView.as_view()
    ),
)
