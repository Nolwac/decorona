from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from django_channels_chat.consumer import *
from django.conf.urls import url

application = ProtocolTypeRouter({
	"websocket": AuthMiddlewareStack(
		URLRouter([
		path('staff/', StaffConsumer),
		path('user/<username>/', UserConsumer),
		path('chat/<chat_name>/', ChatConsumer),
		])
		)
	})
#Note that we are using django_channels_chat consumer app to run this project.