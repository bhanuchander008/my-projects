
from django.conf.urls import url,include
from .restapi import post

urlpatterns = [
                #url(r'^test/',Test),
                #url(r'^apinum/(?P<_Number>[\w\-]+)/$',getNumber),
                url(r'^apipost/(?P<_Number>[\w\-]+)/',post),
            #    url(r'^api2/',Put)
]
