from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReceptSerializer
from .models import Recept
#for creating users
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
# Create your views here.

class ReceptView(viewsets.ModelViewSet):
    serializer_class = ReceptSerializer
    queryset = Recept.objects.all()


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfuly registered a new user"
            data['email'] = account.email
            data['username']  = account.username
            token = Token.objects.get(user = account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)