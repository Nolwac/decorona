from django import template
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

register = template.Library()

@register.inclusion_tag('channels_chat/chat_box.html')
def chat_box(request):
	if request.user.is_authenticated:
		dynamic_username = request.user
	else:
		dynamic_username = get_new_string()
	return {'request':request, 'dynamic_chat_username':dynamic_username}