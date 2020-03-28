from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views import View


def algorithm(request, id):
	return HttpResponse("well done")