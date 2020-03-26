from django.conf.urls import url
from .views import *



#this are urls specific to accounts

urlpatterns = [
    url(r'^login/$', UserLogin.as_view(), name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^activate/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', account_activation, name='account_activation'),
]
