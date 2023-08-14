from django.shortcuts import render

from rest_framework import generics
from .serializers import EvenementSerializer, ArtisteSerializer, ProgrammeSerializer, StreamingEnDirectSerializer 
from .models import Evenement, Artiste, Programme, StreamingEnDirect

class EvenementCreateAPIView(generics.CreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    
    
class EvenementAPIView(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    
class ArtisteCreateAPIView(generics.CreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    
   
class ArtisteAPIView(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    

class ProgrammeAPIView(generics.ListCreateAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    
    
class StreamingEnDirectAPIView(generics.ListCreateAPIView):
    queryset = StreamingEnDirect.objects.all()
    serializer_class = StreamingEnDirectSerializer
