from django.urls import path, include
from rest_framework import routers
from teams.views import TeamsView, PlayersView


router = routers.DefaultRouter()

app_name = 'teams'
urlpatterns = [
    path('', include(router.urls)),
    path('teams/', TeamsView.as_view(), name='all-teams'),
    path('players/', PlayersView.as_view(), name='all-players')
]