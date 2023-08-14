from django.shortcuts import render

from rest_framework import generics
from .serializers import ReservationSerializer, PaiementSerializer
from .models import Reservation, Paiement

class ReservationAPIView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
class PaiementAPIView(generics.ListCreateAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer