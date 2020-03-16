# --------------AGRAGANDO LIBERIAS FRAMEWORK --------------
from rest_framework import routers, serializers, viewsets

from Profile.models import Profile
from Profile.models import Ocupacion
from Profile.models import EstadoCivil
from Profile.models import Genero
from Profile.models import Ciudad
from Profile.models import Estado

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'edad']
        fields = ('__all__')

class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = ('__all__')

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('__all__')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('__all__')



