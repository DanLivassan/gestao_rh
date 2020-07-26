from ..models import HoraExtra
from rest_framework import serializers


class HoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraExtra
        fields = ['motivo', 'horas', 'utilizadas', 'criada_em']

