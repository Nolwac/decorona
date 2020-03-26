from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)

class UserLoginForm(forms.Form):
	"""what this form class does is to create a form interface that can be used to login a user to the website"""
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
	email = forms.EmailField(required = True, help_text='Email is required', max_length=200)
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
