from django.urls import path
from .views import EvenementCreateAPIView, EvenementAPIView, ArtisteCreateAPIView, ArtisteAPIView, ProgrammeAPIView, StreamingEnDirectAPIView

urlpatterns = [
    path('api/evenements/creer/', EvenementCreateAPIView.as_view(), name='creer-evenement'),
    path('api/evenements/', EvenementAPIView.as_view(), name='evenements-api'),
  
    path('api/artistes/creer/', ArtisteCreateAPIView.as_view(), name='creer-artiste'),
    path('api/artistes/', ArtisteAPIView.as_view(), name='artistes-api'),
    
    path('api/programmes/', ProgrammeAPIView.as_view(), name='programmes-api'),
  
    path('api/streaming/', StreamingEnDirectAPIView.as_view(), name='streaming-api'),
]