from django import template
from .settings import *

register = template.Library()

@register.inclusion_tag(LOGIN_INCLUSION_TEMPLATE)
def login(title):
	return{'login_url':LOGIN_URL, 'title':title}