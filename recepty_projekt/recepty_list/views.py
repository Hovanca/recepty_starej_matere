from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReceptSerializer
#from .serializers import  IngredientsSerializer
from .models import Recept
#from .models import Ingredients
# Create your views here.

class ReceptView(viewsets.ModelViewSet):
    serializer_class = ReceptSerializer
    queryset = Recept.objects.all()

