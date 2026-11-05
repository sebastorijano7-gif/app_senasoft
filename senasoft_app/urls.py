from django.urls import path
from . import views

urlpatterns = [
    path('senasoft/', views.bienvenida, name='bienvenida'),
    path('senasoft/registro/', views.registro, name='registro'),
    path('senasoft/competidores/', views.competidores, name='competidores'),
]