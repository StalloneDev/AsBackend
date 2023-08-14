from django.urls import path
from .views import ReservationAPIView, PaiementAPIView

urlpatterns = [
    path('api/reservations/', ReservationAPIView.as_view(), name='reservations-api'),
    path('api/paiements/', PaiementAPIView.as_view(), name='paiements-api'),
]
