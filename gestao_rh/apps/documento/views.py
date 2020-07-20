from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Documento
from .models import Funcionario
from django.urls import reverse_lazy, reverse


class ListDocumento(ListView):
    model = Documento

    def get_queryset(self):
        funcionario = self.request.user.funcionario
        return Documento.objects.filter(propriedade_de=funcionario)


class CreateDocumento(CreateView):
    model = Documento
    fields = ['nome', 'arquivo']
    template_name_suffix = '_create_form'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.propriedade_de = Funcionario.objects.get(pk=self.kwargs['funcionario_id'])

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_absolute_url(self):
        return reverse('funcionario-update', args=[self.kwargs['funcionario_id']])

    def get_success_url(self):
        return reverse('funcionario-update', args=[self.kwargs['funcionario_id']])


class UpdateDocumento(UpdateView):
    model = Documento
    fields = ['nome']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('documento-list')


class DeleteDocumento(DeleteView):
    model = Documento
    success_url = reverse_lazy('documento-list')
