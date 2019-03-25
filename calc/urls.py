from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suma', views.sumar_index, name='suma_index'),
    path('suma/<int:numero>', views.sumar_num, name='sumar'),
    path('suma/<int:numero1>/<int:numero2>', views.sumar, name='sumar'),
    path('resta', views.restar_index, name='resta_index'),
    path('resta/<int:numero>', views.restar_num, name='sumar'),
    path('resta/<int:numero1>/<int:numero2>', views.restar, name='restar'),
    path('multi', views.multiplicar_index, name='multi_index'),
    path('multi/<int:numero>', views.multi_num, name='sumar'),
    path('multi/<int:numero1>/<int:numero2>', views.multiplicar, name='multiplicar'),
    path('div', views.dividir_index, name='dividir_index'),
    path('div/<int:numero>', views.div_num, name='sumar'),
    path('div/<int:numero1>/<int:numero2>', views.dividir, name='dividir'),
    re_path(r'.', views.error, name='error'),
]