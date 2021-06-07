from django.contrib import admin
from .models import Furniture, Images

@admin.register(Furniture)
class FurnitureDisplay(admin.ModelAdmin):
    list_display = ('name', 'idName', 'imagesFurniture')

@admin.register(Images)
class ImagesDisplay(admin.ModelAdmin):
    list_display = ('nameFurniture', 'image')
# Register your models here.
