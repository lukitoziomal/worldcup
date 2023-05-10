from django.shortcuts import render
from rest_framework import viewsets
from teams.models import Team, Player
from teams.serializers import TeamSerializer, PlayerSerializer
from teams.pagination import PlayersPagination


class TeamsView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayersView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = PlayersPagination

