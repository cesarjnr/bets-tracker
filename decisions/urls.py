from django.urls import path

from .views import get_decisions

urlpatterns = [
    path('', get_decisions, name='decisions')
]