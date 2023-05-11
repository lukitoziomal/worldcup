from rest_framework import serializers
from matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    home_team = serializers.SlugRelatedField(read_only=True, slug_field='country')
    away_team = serializers.SlugRelatedField(read_only=True, slug_field='country')

    class Meta:
        model = Match
        exclude = ['events']