from django.urls import path
from . import views

app_name = 'gestion_tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('consolaAdministrador', views.consolaAdministrador, name='consolaAdministrador'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),
    path('eliminarUsuario/<str:ind>', views.eliminarUsuario, name='eliminarUsuario'),
    path('verProductos/<str:ind>', views.verProductos, name='verProductos'),
    path('nuevoProducto/<str:ind>', views.nuevoProducto, name='nuevoProducto'),
    path('eliminarProducto/<str:ind>/<str:pind>', views.eliminarProducto, name='eliminarProducto'),
]