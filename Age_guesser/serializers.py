from rest_framework import serializers
from .models import AgePrediction
import datetime


class AgePredictionSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.SerializerMethodField()

    class Meta:
        model = AgePrediction
        fields = '__all__'
        
    def get_date_of_birth(self, obj):
        date_of_birth_str = obj.date_of_birth
        date_of_birth = datetime.datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
        return date_of_birth.strftime('%Y-%m-%d')