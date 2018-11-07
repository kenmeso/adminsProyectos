from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^lista/nueva/$', views.lista_nueva, name='lista_nueva'),
    path('', views.lista_lista, name='lista_lista'),
    path('lista/lista', views.lista_lista, name='lista_lista'),
    path('lista/<int:pk>/editar/', views.lista_editar, name='lista_editar'),
    url(r'^lista/(?P<pk>\d+)/remove/$', views.lista_remove, name='lista_remove'),
    path('lista/<int:pk>/', views.lista_detalle, name='lista_detalle'),
    path('proyecto/lista', views.proyecto_lista, name='proyecto_lista'),
    url(r'^proyecto/nuevo/$', views.proyecto_nuevo, name='proyecto_nuevo'),
    path('proyecto/<int:pk>/editar/', views.proyecto_editar, name='proyecto_editar'),
    url(r'^proyecto/(?P<pk>\d+)/remove/$', views.proyecto_remove, name='proyecto_remove'),
]
