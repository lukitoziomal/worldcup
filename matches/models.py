from django.db import models
from teams.models import Team, Player


EVENT_TYPES = (
    ('G', 'Goal'),
    ('Y', 'YellowCard'),
    ('R', 'RedCard'),
    ('S', 'Substitution'),
    ('OG', 'OwnGoal')
)


class Match(models.Model):
    date = models.DateTimeField()
    stage = models.CharField(max_length=20)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    home_goals = models.IntegerField(min_value=0, max_value=20)
    away_goals = models.IntegerField(min_value=0, max_value=20)
    events = models.ManyToManyField('Event')

    def __str__(self):
        return f'({self.stage}) {self.home_team} - {self.away_team}'


class Event(models.Model):
    type = models.CharField(choices=EVENT_TYPES, max_length=2)
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
    clock = models.CharField(max_length=10)
