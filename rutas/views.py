from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TblMovilidadRuta,TblMovilidad
from .serializers import RutaSerializer,MovilidadSerializer


class IndexView(APIView):
    
    def get(self, request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class RutasView(APIView):
    
    def get(self, request):
        dataRutas = TblMovilidadRuta.objects.all()
        serRutas = RutaSerializer(dataRutas, many=True)
        return Response(serRutas.data)
    
    def post(self, request):
        serRuta = RutaSerializer(data=request.data)
        serRuta.is_valid(raise_exception=True)
        serRuta.save()
        return Response(serRuta.data)
    
class RutaDetailView(APIView):
    
    def get(self, request, ruta_id):
        dataRuta = TblMovilidadRuta.objects.get(pk=ruta_id)
        serRuta = RutaSerializer(dataRuta)
        return Response(serRuta.data)
    
    def put(self, request, ruta_id):
        dataRuta = TblMovilidadRuta.objects.get(pk=ruta_id)
        serRuta = RutaSerializer(dataRuta, data=request.data)
        serRuta.is_valid(raise_exception=True)
        serRuta.save()
        return Response(serRuta.data)
    
    def delete(self, request, ruta_id):
        dataRuta = TblMovilidadRuta.objects.get(pk=ruta_id)
        serRuta = RutaSerializer(dataRuta)
        dataRuta.delete()
        return Response(serRuta.data)
    

    
class MovilidadView(APIView):
    
    def get(self, request):
        dataMovilidad = TblMovilidad.objects.all()
        serMovilidad = MovilidadSerializer(dataMovilidad, many=True)
        return Response(serMovilidad.data)
    
    def post(self, request):
        serMovilidad = MovilidadSerializer(data=request.data)
        serMovilidad.is_valid(raise_exception=True)
        serMovilidad.save()
        return Response(serMovilidad.data)
    
class MovilidadDetailView(APIView):
    
    def get(self, request, movilidad_id):
        dataMovilidad = TblMovilidad.objects.get(pk=movilidad_id)
        serMovilidad = MovilidadSerializer(dataMovilidad)
        return Response(serMovilidad.data)
    
    def put(self, request, movilidad_id):
        dataMovilidad = TblMovilidad.objects.get(pk=movilidad_id)
        serMovilidad = MovilidadSerializer(dataMovilidad, data=request.data)
        serMovilidad.is_valid(raise_exception=True)
        serMovilidad.save()
        return Response(serMovilidad.data)
    
    def delete(self, request, movilidad_id):
        dataMovilidad = TblMovilidad.objects.get(pk=movilidad_id)
        serMovilidad = MovilidadSerializer(dataMovilidad)
        dataMovilidad.delete()
        return Response(serMovilidad.data)

'''
class MovilidadView(APIView):
    
    def get(self, request):
        movilidad = dict(Ruta.MOVILIDAD_CHOICE)
        return JsonResponse(movilidad)
'''