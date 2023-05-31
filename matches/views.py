from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from rest_framework import viewsets
from matches.models import Match
from matches.serializers import MatchSerializer


class MatchesAPIView(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchesView(ListView):
    def get(self, *args, **kwargs):
        matches = Match.objects.all()
        context = {'matches': matches}
        return render(self.request, 'matches.html', context)


class LadderView(View):
    def get(self, *args, **kwargs):
        context = {}
        return render(self.request, 'ladder.html', context)
