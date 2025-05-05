from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('propriedade', views.detalhe_propriedade, name='propriedade'),
    path('lista_propriedades', views.lista_propriedades, name='lista_propriedades'),
]
