from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('propriedade', views.propriedade, name='propriedade'),
    path('propriedades_registradas', views.propriedades_registradas_por_estado, name='propriedades_registradas'),
]
