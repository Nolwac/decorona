import os
import django
from channels.routing import get_default_application

django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'decorona.settings')
application = get_default_application()