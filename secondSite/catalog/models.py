from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey


class Furniture(models.Model):
    idName = models.CharField(max_length = 100, help_text = "Enter furniture url id")
    name = models.CharField(max_length = 100, help_text = "Enter furniture name")
    imageBack = models.ImageField(upload_to = 'furniture')

    def __str__(self):
        return str(self.name)

    def imagesFurniture(self):
        selfFurnitures = Images.objects.filter(nameFurniture__name = self.name)
        return ','.join([furn.image for furn in selfFurnitures])

    def getLink(self):
        return reverse('FurnitureDetail', args = [str(self.idName)])

class Images(models.Model):
    nameFurniture = models.ForeignKey('Furniture', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'furniture')

    def __str__(self):
            return str(self.nameFurniture)

class Texts(models.Model):
    nameFurniture = models.ForeignKey('Furniture', on_delete=models.CASCADE)
    text = models.TextField()
# Create your models here.
