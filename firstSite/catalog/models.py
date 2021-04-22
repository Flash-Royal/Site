from django.db import models
from django.urls import reverse

# Create your models here.
class GameGenre(models.Model):
    idName = models.CharField(max_length = 100, help_text = "Enter Game Genre url id")
    name = models.CharField(max_length = 100, help_text = "Enter Game Genre name")
    description = models.TextField(max_length = 1000, help_text = "Description about game genre")

    def getLink(self):
        return reverse('GenreDetail', args = [str(self.idName)])
