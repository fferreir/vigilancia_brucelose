from django.urls import include,path
from . import views

app_name = 'brutb'
urlpatterns = [
    path('index', views.home, name='index'),
    path('lista_propriedades', views.lista_propriedades, name='lista_propriedades'),
    path('propriedade', views.propriedade, name='propriedade'),
]
