from django.contrib import admin
from .models import Furniture, Images, Texts

@admin.register(Furniture)
class FurnitureDisplay(admin.ModelAdmin):
    list_display = ('name', 'idName', 'imageBack', 'imagesFurniture')

@admin.register(Images)
class ImagesDisplay(admin.ModelAdmin):
    list_display = ('nameFurniture', 'image')

@admin.register(Texts)
class TextsDisplay(admin.ModelAdmin):
    list_display = ('nameFurniture', 'text')
# Register your models here.
