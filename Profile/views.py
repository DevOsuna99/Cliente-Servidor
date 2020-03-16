from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

import coreapi
from rest_framework.schemas import AutoSchema

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

#Importar Modelo
from Profile.models import Profile
from Profile.models import Ocupacion
from Profile.models import EstadoCivil
from Profile.models import Genero
from Profile.models import Ciudad
from Profile.models import Estado
#Importar Serializer
from Profile.serializer import ProfileSerializers
from Profile.serializer import OcupacionSerializers
from Profile.serializer import EstadoCivilSerializers
from Profile.serializer import GeneroSerializers
from Profile.serializer import CiudadSerializers
from Profile.serializer import EstadoSerializers

class ListProfileAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
                extra_fields = [
                    coreapi.Field('nombre'),
                    coreapi.Field('apellidoPaterno'),
                    coreapi.Field('apellidoMaterno'),
                    coreapi.Field('edad'),
                    coreapi.Field('ciudad_id'),
                    coreapi.Field('genero_id'),
                    coreapi.Field('ocupacion_id'),
                    coreapi.Field('estado_id'),
                    coreapi.Field('estadoCivil_id')
                ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class ProfileList(APIView):
    permission_classes = []
    schema = ListProfileAutoShema()
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

class ListEstadoCivilAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
                extra_fields = [
                    coreapi.Field('estadoCivil'),
                ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields


class EstadoCivilList(APIView):
    permission_classes = []
    schema = ListEstadoCivilAutoShema()
    #METODO GET PARA SOLICITAR INFORMACION
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = EstadoCivil.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ListOcupacionAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
                extra_fields = [
                    coreapi.Field('ocupacion'),
                ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class OcupacionList(APIView):
    permission_classes = []
    schema = ListOcupacionAutoShema()
    #METODO GET PARA SOLICITAR INFORMACION
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Ocupacion.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ListGeneroAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
                extra_fields = [
                    coreapi.Field('genero'),
                ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class GeneroList(APIView):
    permission_classes = []
    schema = ListGeneroAutoShema()
    #METODO GET PARA SOLICITAR INFORMACION
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Genero.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ListCiudadAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
                extra_fields = [
                    coreapi.Field('ciudad'),
                    coreapi.Field('estado_id'),
                ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class CiudadList(APIView):
    permission_classes = []
    schema = ListCiudadAutoShema()
    #METODO GET PARA SOLICITAR INFORMACION
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Ciudad.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ListEstadoAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
                extra_fields = [
                    coreapi.Field('estado')
                ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class EstadoList(APIView):
    permission_classes = []
    schema = ListEstadoAutoShema()
    #METODO GET PARA SOLICITAR INFORMACION
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Estado.objects.filter(delete=False)
        #many = True si aplica si retorno multiples objetos
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Create your views here.

# Create your views here.
