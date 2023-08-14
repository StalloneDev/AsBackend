from django.urls import path
from .views import RestaurationAPIView

urlpatterns = [
    path('api/restaurations/', RestaurationAPIView.as_view(), name='restaurations-api'),
]
