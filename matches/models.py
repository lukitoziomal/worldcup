from django.db import models
from teams.models import Team, Player


EVENT_TYPES = (
    ('G', 'Goal'),
    ('A', 'Assist'),
    ('Y', 'YellowCard'),
    ('R', 'RedCard'),
    ('S', 'Substitution'),
    ('OG', 'OwnGoal')
)


class Match(models.Model):
    date = models.DateField()
    stage = models.CharField(max_length=20)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Home')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Away')
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    events = models.ManyToManyField('Event')

    def __str__(self):
        return f'({self.stage}) {self.home_team} - {self.away_team}'


class Event(models.Model):
    type = models.CharField(choices=EVENT_TYPES, max_length=2)
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True, related_name='player2')
    clock = models.CharField(max_length=10)
