"""EduTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, admin_checker
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/login/', admin_checker, name="admin_checker"), 
    url(r'^admin/', admin.site.urls), #this url is linking to the django default database, to help ease development process.
    #/admin/login/

    #----this set of urls are included urls from the other apps in the website----
    #----what this does is to make sure that the urls in the other apps are properly linked to this website url
    url(r'^accounts/', include(('accounts.urls','accounts'), namespace='accounts')),

    #----this set of urls are the urls for this very part of the website----
    url(r'^$', Home.as_view(), name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# ----this is pure django rest framework----
urlpatterns = format_suffix_patterns(urlpatterns)
