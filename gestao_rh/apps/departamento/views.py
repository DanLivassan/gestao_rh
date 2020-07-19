from django.views.generic.list import ListView
from .models import Departamento


class ListDepartamento(ListView):
    model = Departamento

    def get_queryset(self):
        self.empresa = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=self.empresa)


