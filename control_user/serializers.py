from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Utilisateur

from django.contrib.auth.forms import PasswordResetForm



class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id', 'username', 'email')
        


class UtilisateurInscriptionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Utilisateur
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        utilisateur = Utilisateur(**validated_data)
        utilisateur.set_password(password)
        utilisateur.save()
        return utilisateur

class UtilisateurConnexionSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        utilisateur = authenticate(username=username, password=password)

        if not utilisateur:
            raise serializers.ValidationError('Identifiants de connexion invalides.')

        attrs['utilisateur'] = utilisateur
        return attrs



class DemandeRecuperationMotDePasseSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        form = PasswordResetForm({'email': value})
        if not form.is_valid():
            raise serializers.ValidationError("Cette adresse e-mail n'est associée à aucun compte.")
        return value

    def save(self):
        request = self.context.get('request')
        email = self.validated_data['email']
        form = PasswordResetForm({'email': email})
        form.is_valid()
        form.save(request=request)
        


 