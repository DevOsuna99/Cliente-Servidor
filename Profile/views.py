from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

#Importar Modelo
from Profile.models import Profile
#Importar Serializer
from Profile.serializer import ProfileSerializers

class ProfileList(APIView):
    #METODO GET PARA SOLICITAR INFORMACION
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Create your views here.

# Create your views here.
