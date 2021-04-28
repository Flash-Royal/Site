from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .serializers import *

def main(request):
    return render(request,'main.html')

class Main(APIView):
    renderer_classes = [MultiPartParser,TemplateHTMLRenderer]
    template_name = 'main.html'

    def get(self, request):
        game = {}
        image = []
        gameGenre = GameGenre.objects.all()
        gameImages = GameImages.objects.order_by().distinct()
        for i in gameGenre:
            game[i] = Game.objects.values('id', 'name', 'gameGenre').filter(gameGenre = i)[0]
        for i in game.values():
            if not image:
                imageBuf = GameImages.objects.filter(nameGame = i['id']).values()[0]
                image = GameImages.objects.filter(id = imageBuf['id'])
            else:
                imageBuf = GameImages.objects.filter(nameGame = i['id']).values()[0]
                image = image | GameImages.objects.filter(id = imageBuf['id'])
        return Response({'gameGenres' : gameGenre, 'images' : image})

class GenreDetail(APIView):
    renderer_classes = [MultiPartParser,TemplateHTMLRenderer]
    template_name = 'gameGenreTemplate.html'

    def get(self, request, genre):
        gameGenre = GameGenre.objects.all()
        genreName = GameGenre.objects.values('id', 'name','description').get(idName = genre)
        games = Game.objects.filter(gameGenre = genreName['id'])
        images = GameImages.objects.all()
        return Response({'genreName' : genreName, 'games' : games, 'gameGenres' : gameGenre, 'images' : images})
# Create your views here.
