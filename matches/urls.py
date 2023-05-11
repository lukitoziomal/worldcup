from django.urls import path, include
from rest_framework import routers
from matches.views import MatchesView


router = routers.DefaultRouter()
router.register('matches', MatchesView, basename='all-matches')

app_name = 'matches'
urlpatterns = [

]