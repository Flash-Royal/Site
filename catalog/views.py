from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import *

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
        return grid1, grid2

    def addID(self, mass, left = 0, multi = 1):
        for id, item in enumerate(mass):
            item.newID = (id + left) * multi
            print(multi, " --- ", item.newID)

    def get(self, request, furniture):
        furns = Furniture.objects.all()
        furn = Furniture.objects.values('id','name','idName').get(idName = furniture)
        images = Images.objects.filter(nameFurniture = furn['id'])
        texts = Texts.objects.filter(nameFurniture = furn['id'])

        grid1Images, grid2Images = self.parseData(images)
        self.addID(grid1Images, 1)
        self.addID(grid2Images, 1)

        grid1Texts, grid2Texts = self.parseData(texts)
        self.addID(grid1Texts, 1, len(grid1Images) // len(grid1Texts))
        self.addID(grid2Texts, 1, len(grid2Images) // len(grid2Texts))

        for i, item in enumerate(grid1Texts):
            self.changeNewID(grid1Images, item.newID + i)
            item.newID = item.newID + i

        for i, item in enumerate(grid2Texts):
            self.changeNewID(grid2Images, item.newID + i)
            item.newID = item.newID + i

        return Response({'furns' : furns, 'furn' : furn, 'gr1Text' : grid1Texts, 'gr2Text' : grid2Texts, 'gr1Im' : grid1Images, 'gr2Im' : grid2Images})
