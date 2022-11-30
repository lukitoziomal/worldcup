from rest_framework import serializers
from teams.models import Team, Player


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    nationality = serializers.SlugField(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'