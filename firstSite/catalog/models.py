from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class GameGenre(models.Model):
    idName = models.CharField(max_length = 100, help_text = "Enter Game Genre url id")
    name = models.CharField(max_length = 100, help_text = "Enter Game Genre name")
    description = models.TextField(max_length = 1000, help_text = "Description about game genre")

    def getLink(self):
        return reverse('GenreDetail', args = [str(self.idName)])

    def gameList(self):
        selfGames = Game.objects.filter(gameGenre__name = self.name)
        return ','.join([game.name for game in selfGames])

    def __str__(self):
            return self.idName

class Game(models.Model):
    name = models.CharField(max_length = 100, help_text = "Enter Game name")
    description = models.TextField(max_length = 1000, help_text = "Description about game")
    gameGenre = models.ForeignKey('GameGenre', on_delete=models.SET_NULL, null=True)

    def __str__(self):
            return str(self.name)

class GameImages(models.Model):
    nameGame = models.ForeignKey('Game', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'games')

    def __str__(self):
            return str(self.nameGame)

    def imageGenre(self):
        selfImages = Game.objects.filter(name = self.nameGame)
        return ','.join([game.gameGenre.name for game in selfImages])

    def imageGame(self):
        selfImages = Game.objects.filter(name = self.nameGame)
        return ','.join([game.name for game in selfImages])
