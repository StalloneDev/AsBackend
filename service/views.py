from django.shortcuts import render

from rest_framework import generics
from .serializers import ServiceSerializer
from .models import Service

class ServiceAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer