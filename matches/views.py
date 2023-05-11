from rest_framework import viewsets
from matches.models import Match
from matches.serializers import MatchSerializer


class MatchesView(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
