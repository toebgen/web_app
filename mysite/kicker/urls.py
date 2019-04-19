from django.urls import path

from . import views

# Namespacing the URL names
app_name = 'kicker'

urlpatterns = [
    # ex: /kicker/
    path('', views.index, name='index'),
    # ex: /kicker/players
    path('players/', views.players, name='players'),
    # ex: /kicker/games
    path('games/', views.games, name='games'),
    # ex: /kicker/player/3/
    path('player/<int:player_id>/', views.player, name='player'),
    # ex: /kicker/add_player/
    path('add_player/', views.add_player, name='add_player'),
   # ex: /kicker/game/2
    path('game/<int:game_id>/', views.game, name='game'),
   # ex: /kicker/add_game/
    path('add_game/', views.add_game, name='add_game'),
]