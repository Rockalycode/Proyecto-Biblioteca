from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_prestamos, name='lista_prestamos'),
    path('eliminar/<int:pk>/', views.eliminar_prestamo, name='eliminar_prestamo'),
]