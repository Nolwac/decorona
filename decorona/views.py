# from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync #this is to help us convert the asyncrounous request to a syncronous one
import uuid

server_chat_sessions = []

def get_new_string():
	"""This gets new session string different from the previous existing ones"""
	string = str(uuid.uuid4())
	if string in server_chat_sessions:
		return get_new_string()
	else:
		server_chat_sessions.append(string)
		return string

class Home(View):
	def get(self, request):
		context={"dynamic_chat_username": get_new_string()}
		return render(request,'accounts/base.html',context)

def admin_checker(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/accounts/login/')
	elif not request.user.is_staff:
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/admin/')