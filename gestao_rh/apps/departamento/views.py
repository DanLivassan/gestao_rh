from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Departamento
from django.urls import reverse_lazy, reverse


class ListDepartamento(ListView):
    model = Departamento

    def get_queryset(self):
        self.empresa = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=self.empresa)


class CreateDepartamento(CreateView):
    model = Departamento
    fields = ['nome']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        departamento = form.save(commit=False)
        empresa = self.request.user.funcionario.empresa
        departamento.empresa = empresa
        departamento.save()
        return super(CreateDepartamento, self).form_valid(form)

    def get_success_url(self):
        return reverse('departamento-list')


class UpdateDepartamento(UpdateView):
    model = Departamento
    fields = ['nome']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('departamento-list')


class DeleteDepartamento(DeleteView):
    model = Departamento
    success_url = reverse_lazy('departamento-list')
