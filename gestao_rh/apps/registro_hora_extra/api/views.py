from rest_framework import viewsets

from gestao_rh.apps.registro_hora_extra.api.serializers import HoraExtraSerializer
from gestao_rh.apps.registro_hora_extra.models import HoraExtra


class HoraExtraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HoraExtra.objects.all()
    serializer_class = HoraExtraSerializer