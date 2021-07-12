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

    def get(self, request, furniture):
        furns = Furniture.objects.all()
        furn = Furniture.objects.values('id','name','idName').get(idName = furniture)
        images = Images.objects.filter(nameFurniture = furn['id'])
        return Response({'furns' : furns, 'furn' : furn, "images" : images})


# Create your views here.
