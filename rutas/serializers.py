from rest_framework import serializers
from .models import TblMovilidad,TblMovilidadRuta


class MovilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMovilidad
        fields = '__all__'
class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMovilidadRuta
        fields = '__all__'
    