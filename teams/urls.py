from django.urls import path, include
from rest_framework import routers
from teams.views import TeamsView, PlayersView


router = routers.DefaultRouter()
router.register('teams', TeamsView, basename='all-teams')
router.register('players', PlayersView, basename='all-players')

app_name = 'teams'
urlpatterns = [
    path('', include(router.urls))
]