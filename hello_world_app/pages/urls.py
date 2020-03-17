from django.urls import path
from .views import homePaigeView

urlpatterns = [
    path('', homePaigeView, name='home')
]