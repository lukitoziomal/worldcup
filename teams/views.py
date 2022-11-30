from django.shortcuts import render
from rest_framework import generics
from teams.models import Team, Player
from teams.serializers import TeamSerializer, PlayerSerializer
from teams.pagination import PlayersPagination


class TeamsView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayersView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = PlayersPagination

