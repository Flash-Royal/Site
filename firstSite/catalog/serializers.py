from rest_framework import serializers
from .models import GameGenre

class GameGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGenre
        fields = ('idName', 'name', 'description')
