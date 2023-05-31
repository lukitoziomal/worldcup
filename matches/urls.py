from django.urls import path, include
from rest_framework import routers
from matches.views import MatchesView, MatchesAPIView, LadderView


router = routers.DefaultRouter()
router.register('matches', MatchesAPIView, basename='all-matches')

app_name = 'matches'
urlpatterns = [
    path('list-of-matches', MatchesView.as_view(), name='matches'),
    path('', LadderView.as_view(), name='ladder')
]