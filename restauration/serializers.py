from rest_framework import serializers
from .models import Restauration

class RestaurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restauration
        fields = '__all__'