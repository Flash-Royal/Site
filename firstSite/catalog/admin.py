from django.contrib import admin
from .models import GameGenre, GameImages, Game
# Register your models here.
@admin.register(GameGenre)
class GameGenreAdmin(admin.ModelAdmin):
    list_display = ('idName', 'name', 'description', 'gameList')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'gameGenre')

@admin.register(GameImages)
class GameImagesAdmin(admin.ModelAdmin):
    list_display = ('imageGenre', 'nameGame', 'image')
