from django.shortcuts import render

from rest_framework import generics
from .serializers import FormationSerializer
from .models import Formation

class FormationAPIView(generics.ListCreateAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer
