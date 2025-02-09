from django.urls import path
from . import views

urlpatterns = [
    path('brutb', views.home, name=''),
]
