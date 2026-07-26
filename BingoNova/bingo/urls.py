from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),

    path(
        'partida/<int:jugador_id>/',
        views.partida,
        name='partida'
    ),

    path(
        'sacar/<int:jugador_id>/',
        views.sacar,
        name='sacar'
    ),

    path(
        'bingo/<int:jugador_id>/',
        views.bingo,
        name='bingo'
    ),

]