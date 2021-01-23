from django.db import models

class Team(models.Model):
    school = models.CharField(max_length=50, primary_key=True)
    mascot = models.CharField(max_length=50)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    def __str__(self):
        return str(self.school)


class Game(models.Model):
     game_number=models.AutoField(primary_key=True)
     week_number = models.IntegerField(default=1)
     home_team_score=models.IntegerField(default=0)
     away_team_score=models.IntegerField(default=0)
     home_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="home_team")
     away_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="away_team")
     winner = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="winner")
     loser = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="loser")

     def __str__(self):
         return str(self.game_number)
