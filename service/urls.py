from django.urls import path
from .views import ServiceAPIView

urlpatterns = [
    path('api/services/', ServiceAPIView.as_view(), name='services-api'),
]