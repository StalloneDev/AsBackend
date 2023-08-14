from rest_framework import serializers
from .models import Evenement, Artiste, Programme, StreamingEnDirect

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'
        
class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = '__all__'
      
class StreamingEnDirectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingEnDirect
        fields = '__all__'
        

