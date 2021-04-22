from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .serializers import *

def main(request):
    return render(request,'main.html')

# Create your views here.
