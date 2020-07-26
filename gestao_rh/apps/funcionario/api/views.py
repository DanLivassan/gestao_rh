from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from gestao_rh.apps.funcionario.api.serializers import FuncionarioSerializer
from gestao_rh.apps.funcionario.models import Funcionario
from rest_framework.permissions import IsAuthenticated


class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer