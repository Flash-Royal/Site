from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import *

# def main(request):
#     return render(request,'main.html')

class Main(APIView):
    renderer_classes = [MultiPartParser,TemplateHTMLRenderer]
    template_name = 'main.html'

    def get(self, request):
        furnitures = Furniture.objects.all()
        return Response({'furn':furnitures})

class FurnitureDetail(APIView):
    renderer_classes = [MultiPartParser, TemplateHTMLRenderer]
    template_name = 'templeFurn.html'

    def changeNewID(self, mass, index):
        for item in mass:
            if item.newID >= index:
                item.newID += 1

    def parseData(self, mass):
        grid1 = []
        grid2 = []
        if len(mass) < 4:
            for i in range(len(mass)):
                if (i < (len(mass) // 2 + len(mass) % 2)):
                    grid1.append(list(mass)[i])
                else:
                    grid2.append(list(mass)[i])
        else:
            for i in range(len(mass)):
                if (i < (len(mass) - 2)):
                    grid1.append(list(mass)[i])
                else:
                    grid2.append(list(mass)[i])

        for id, item in enumerate(grid1):
            item.newID = id

        for id, item in enumerate(grid2):
            item.newID = id

        return grid1, grid2
    def get(self, request, furniture):
        arr = []
        furns = Furniture.objects.all()
        furn = Furniture.objects.values('id','name','idName').get(idName = furniture)
        images = Images.objects.filter(nameFurniture = furn['id'])
        texts = Texts.objects.filter(nameFurniture = furn['id'])
        grid1Images, grid2Images = self.parseData(images)
        grid1Texts, grid2Texts = self.parseData(texts)

        return Response({'furns' : furns, 'furn' : furn, 'gr1Text' : grid1Texts, 'gr2Text' : grid2Texts, 'gr1Im' : grid1Images, 'gr2Im' : grid2Images})


# Create your views here.
