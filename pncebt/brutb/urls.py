from django.urls import include,path
from . import views

app_name = 'brutb'
urlpatterns = [
    path('index', views.home, name='index'),
    path('propriedade/<str:cod_rebanho_estudo>', views.propriedade_detalhe, name='propriedade_detalhe'),
    path('propriedade/lista_propriedades', views.lista_propriedades, name='lista_propriedades'),
    path('propriedade', views.propriedade, name='propriedade'),
]
