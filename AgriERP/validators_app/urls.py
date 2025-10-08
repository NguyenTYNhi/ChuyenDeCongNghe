from django.urls import path
from .views import ValidatorDemoView

urlpatterns = [
    path('demo/', ValidatorDemoView.as_view(), name='validator-demo'),
]
