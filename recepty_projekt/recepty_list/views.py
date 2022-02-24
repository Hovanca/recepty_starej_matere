from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReceptSerializer
from .models import Recept
# Create your views here.

class ReceptView(viewsets.ModelViewSet):
    serializer_class = ReceptSerializer
    queryset = Recept.objects.all()
