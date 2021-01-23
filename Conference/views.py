from django.views.generic import ListView
from .models import models
from .models import Game
from .models import Team



class GameListView(ListView):
    model = Game
    template_name = 'game_list.html'
    ordering = ['-week_number']

class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'
    ordering = ['-wins']
