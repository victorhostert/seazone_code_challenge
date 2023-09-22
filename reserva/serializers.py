from rest_framework import serializers
from .models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
    
    def validate(self, data):
        """Checa se a data de check-out é posterior a data de check-in"""
        if data['check_out'] < data['check_in']:
            raise serializers.ValidationError({'check_out': 'A data de check-out não pode ser anterior a data de check-in'})

        return data