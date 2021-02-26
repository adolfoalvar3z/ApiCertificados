from django.shortcuts import render
from rest_framework import viewsets
from .models import Pregunta
from .models import Respuesta
from .models import Certificado
from .serializers import *

# Create your views here.
class PreguntaViewSet(viewsets.ModelViewSet):
    serializer_class = PreguntaSerializer
    queryset = Pregunta.objects.all()

class RespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = RespuestaSerializer
    queryset = Respuesta.objects.all()

class CertificadoViewSet(viewsets.ModelViewSet):
    serializer_class = CertificadoSerializer
    queryset = Certificado.objects.all()