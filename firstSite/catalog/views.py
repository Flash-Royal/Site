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
        image = {}
        gameGenre = GameGenre.objects.all()
        gameImages = GameImages.objects.all()
        for i in gameGenre:
            game[i] = Game.objects.values('id', 'name').filter(gameGenre = i)[0]
        for i in game.values():
            image[i['name']] = GameImages.objects.values('image').filter(nameGame = i['id'])
        print(image)
        return Response({'images' : image})

# Create your views here.
