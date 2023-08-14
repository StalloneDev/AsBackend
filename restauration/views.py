from django.shortcuts import render

from rest_framework import generics
from .serializers import RestaurationSerializer
from .models import Restauration

class RestaurationAPIView(generics.ListCreateAPIView):
    queryset = Restauration.objects.all()
    serializer_class = RestaurationSerializer