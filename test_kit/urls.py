from django.urls import path
from .views import *


urlpatterns = [
    path('algorithm/<int:id>/', algorithm, name='algorithm'),

]
