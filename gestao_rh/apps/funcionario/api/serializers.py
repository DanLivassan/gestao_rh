from gestao_rh.apps.registro_hora_extra.api.serializers import HoraExtraSerializer
from ..models import Funcionario
from rest_framework import serializers


class FuncionarioSerializer(serializers.ModelSerializer):
    horas_extras = HoraExtraSerializer(many=True, source='horaextra_set')

    class Meta:
        model = Funcionario
        fields = ('nome', 'departamentos', 'empresa', 'imagem', 'get_total_horas_extra', 'horas_extras')

