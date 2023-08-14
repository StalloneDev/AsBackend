from django.urls import path
from .views import FormationAPIView

urlpatterns = [
    path('api/formations/', FormationAPIView.as_view(), name='formations-api'),
]