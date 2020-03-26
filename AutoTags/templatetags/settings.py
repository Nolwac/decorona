"""
This is were all the settings for your AutoTags is. You can set the auto tag to target the particular template file you want when dealing
with inclusion tags.
"""

from django.conf import settings #importing the django settings module to give us access to the django settings available.

try:
	LOGIN_INCLUSION_TEMPLATE = settings.LOGIN_INCLUSION_TEMPLATE
except:
	LOGIN_INCLUSION_TEMPLATE = 'blog/login_inclusion_template.html'
	
try:
	LOGIN_URL = settings.LOGIN_URL
except:
	LOGIN_URL = '/accounts/login/'
	
try:
	SIGNUP_INCLUSION_TEMPLATE = settings.SIGNUP_INCLUSION_TEMPLATE
except:
	SIGNUP_INCLUSION_TEMPLATE = 'blog/signup_inclusion_template.html'
try:
	SIGNUP_URL = settings.SIGNUP_URL
except:
	SIGNUP_URL = '/accounts/signup/'