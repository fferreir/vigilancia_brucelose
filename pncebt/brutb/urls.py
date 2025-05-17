from django.urls import include,path
from . import views

app_name = 'brutb'
urlpatterns = [
    path('index', views.home, name='index'),
    path('', views.lista_propriedades, name='lista_propriedades'),
    path('propriedade/lista/', views.lista_propriedades, name='lista_propriedades'),
    path('propriedade/adiciona/', views.propriedade, name='propriedade_adiciona'),
    path('propriedade/<str:cod_rebanho_estudo>/', views.propriedade_detalhe, name='propriedade_detalhe'),
]
