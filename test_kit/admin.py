from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Operation)
admin.site.register(Question)
admin.site.register(DecisionBox)
admin.site.register(ConnectorToDecisionBox)
admin.site.register(Algorithm)
admin.site.register(Connector)