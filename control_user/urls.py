from django.urls import path, include
from rest_framework import routers
from .views import UtilisateurViewSet
from .views import UtilisateurInscriptionAPIView, UtilisateurConnexionAPIView, UtilisateurAPIView


from .views import DemandeRecuperationMotDePasseAPIView


router = routers.DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)



urlpatterns = [
    
    path('api/', include(router.urls)),
    path('api/recuperation-mot-de-passe/', DemandeRecuperationMotDePasseAPIView.as_view(), name='recuperation-mot-de-passe'),
    
    path('api/inscription/', UtilisateurInscriptionAPIView.as_view(), name='inscription'),
    path('api/connexion/', UtilisateurConnexionAPIView.as_view(), name='connexion'),
    path('api/utilisateur/', UtilisateurAPIView.as_view(), name='utilisateur'),

]