from django.urls import path
from .views import *


urlpatterns = [
    path('algorithm/<int:id>/', AlgorithmView.as_view(), name='algorithm'),
    path('algorithm/decison_box/<int:id>/', DecisionBoxView.as_view(), name='decision_box'),
    path('algorithm/connector/<int:id>/', ConnectorView.as_view(), name='connector'),

]
