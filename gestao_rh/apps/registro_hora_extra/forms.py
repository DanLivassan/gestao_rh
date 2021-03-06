from django.forms import ModelForm
from .models import HoraExtra
from ..funcionario.models import Funcionario


class RegistroHoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa = user.funcionario.empresa
        )

    class Meta:
        model = HoraExtra
        fields = ['motivo', 'funcionario', 'horas', 'utilizadas', 'criada_em']
