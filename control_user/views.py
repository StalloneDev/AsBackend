from rest_framework import viewsets, permissions, generics, status
from .models import Utilisateur
from .serializers import UtilisateurSerializer, UtilisateurInscriptionSerializer, UtilisateurConnexionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DemandeRecuperationMotDePasseSerializer

from rest_framework.authtoken.models import Token


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = (permissions.AllowAny,)


class DemandeRecuperationMotDePasseAPIView(generics.GenericAPIView):
    serializer_class = DemandeRecuperationMotDePasseSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Un e-mail a été envoyé avec les instructions pour réinitialiser votre mot de passe.'})
    
    
class UtilisateurInscriptionAPIView(generics.CreateAPIView):
    serializer_class = UtilisateurInscriptionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        utilisateur = serializer.save()
        return Response({'detail': 'Inscription réussie.'}, status=status.HTTP_201_CREATED)

class UtilisateurConnexionAPIView(generics.GenericAPIView):
    serializer_class = UtilisateurConnexionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        utilisateur = serializer.validated_data['utilisateur']
        # Effectuez ici toute autre action requise lors de la connexion, par exemple, générer un jeton d'accès ou définir une session.
       
        # token, _ = Token.objects.get_or_create(user=utilisateur)
        
        return Response({'detail': 'Connexion réussie.'})
    
class UtilisateurAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UtilisateurInscriptionSerializer(data=request.data)
        if serializer.is_valid():
            utilisateur = serializer.save()
            return Response({'detail': 'Inscription réussie.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        utilisateurs = Utilisateur.objects.all()
        serializer = UtilisateurInscriptionSerializer(utilisateurs, many=True)
        return Response(serializer.data)
    

