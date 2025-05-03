from django.urls import include,path
from . import views

urlpatterns = [
    path('brutb', views.home, name=''),
    path('propriedade', views.propriedade, name='propriedade'),
]
