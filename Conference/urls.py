from django.urls import path
from . import views

urlpatterns = [
    path('standings', views.TeamListView.as_view(), name='team_list'),
    path('scoreboard', views.GameListView.as_view(), name='game_list'),


]