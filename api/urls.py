# -*- coding: utf-8 -*-
#AUTHOR: Samuel M.H. <samuel.mh@gmail.com>


from django.conf.urls import patterns,  url

from views import ListResources, Resource


urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = ListResources.as_view(),
        name = 'endpoint'
    ),              
    url(
        regex = r'^(?P<username>\w+)$',
        view  = ListResources.as_view()
    ),
    url(
        regex = r'^(?P<username>\w+)/(?P<alias>\w+)$',
        view  = Resource.as_view()
    ),
)
