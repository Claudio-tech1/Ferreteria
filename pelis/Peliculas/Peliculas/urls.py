from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_view, name='catalogo'),
    path('ingresar/', views.ingresar_pelicula_view, name='ingresar_pelicula'),
    path('alertas/', views.alertas_stock_view, name='alertas_stock'),
    path('distribuidoras/', views.distribuidoras_view, name='distribuidoras'),
    path('eliminar/<int:pelicula_id>/', views.eliminar_pelicula_view, name='eliminar_pelicula'),
]