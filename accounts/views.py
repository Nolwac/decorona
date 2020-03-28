from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from .forms import *
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_caption = 'DeCorona Account Activation'
			message = render_to_string('accounts/account_activation_email.html', {
				'user':user,
				'domain':current_site,
				'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
				'token':account_activation_token.make_token(user),
				})
			to_email = form.cleaned_data.get('email')
			other_email = 'snappynolwac@gmail.com'
			email = EmailMessage(
				mail_caption, message, to=[to_email, other_email]
				)
			email.send()
			return render(request, 'accounts/registration_form_done.html', {'user':user, 'site':current_site})
	form = SignUpForm()
	return render(request, 'accounts/signup.html', {'form':form})
def account_activation(request, uid64, token):
	"""This is just to activate the a user account. Account activation and email confirmation is just to make sure that the user
	did not provide an invalid email during registration and that the email belongs to the user"""
	try:
		uid = force_text(urlsafe_base64_decode(uid64))
		user = User.objects.get(pk = uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return render(request, 'accounts/account_activation_done.html', {'user':user})
	else:
		return render(request, 'accounts/bad_activation.html', {})

def user_logout(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/')
	logout(request)
	return HttpResponseRedirect('/')

#---below is for class views ----

class UserLogin(View):
	"""this class takes care of login and logout"""
	def get(self, request):
		if request.user.is_authenticated:
			return HttpResponseRedirect('/')
		context = {
		}
		return render(request, 'accounts/login.html', context)
	def post(self, request):
		if request.user.is_authenticated:
			return HttpResponseRedirect('/')
		form = UserLoginForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			#userprofile = Profile.objects.create(user=instance.user, reference_id=get_reference_id(),)
			username=form.cleaned_data.get("username")
			password=form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None and user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
		return HttpResponseRedirect('/')
