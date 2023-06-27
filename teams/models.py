from django.db import models


class Team(models.Model):
    country = models.CharField(max_length=30)
    short = models.CharField(max_length=3)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)

    def __str__(self):
        return self.country


class Player(models.Model):
    name = models.CharField(max_length=50)
    shirt_name = models.CharField(max_length=50)
    nationality = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.IntegerField()
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name