from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import HoraExtra
from .models import Funcionario
from django.urls import reverse_lazy, reverse
from .forms import RegistroHoraExtraForm


class ListHoraExtra(ListView):
    model = HoraExtra

    def get_queryset(self):
        funcionario = self.request.user.funcionario
        return HoraExtra.objects.filter(funcionario__empresa=funcionario.empresa)


class CreateHoraExtra(CreateView):
    model = HoraExtra
    form_class = RegistroHoraExtraForm
    template_name_suffix = '_create_form'

    def get_form_kwargs(self):
        kwargs = super(CreateHoraExtra, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UpdateHoraExtra(UpdateView):
    model = HoraExtra
    form_class = RegistroHoraExtraForm
    template_name_suffix = '_update_form'

    def get_form_kwargs(self):
        kwargs = super(UpdateHoraExtra, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class DeleteHoraExtra(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('hora_extra-list')
