from rest_framework import serializers
from .models import GameGenre, Game, GameImages

class GameGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGenre
        fields = ('idName', 'name', 'description')

class GameSerializer(serializers.ModelSerializer):
    gameGenre = serializers.StringRelatedField()
    class Meta:
        model = Game
        fields = ('name', 'description', 'gameGenre')

class GameImagesSerializer(serializers.ModelSerializer):
    nameGame = serializers.StringRelatedField()
    class Meta:
        model = GameImages
        fields = ('nameGame', 'image')
