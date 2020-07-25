import csv
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from .models import Funcionario
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
import json

def home(request):
    return HttpResponse("Funcionando")


class ListFuncionario(ListView):
    model = Funcionario
    paginate_by = 50

    def get_queryset(self):
        self.empresa = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=self.empresa)


class CreateFuncionario(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = '-'.join(funcionario.nome.lower().split(' '))
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(CreateFuncionario, self).form_valid(form)


class UpdateFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    template_name_suffix = '_update_form'


class DeleteFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionario-list')


class CSVFuncionario(View):

    def get(self, request, pk):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        funcionario = get_object_or_404(Funcionario, pk=pk)
        response['Content-Disposition'] = 'attachment; filename="'+funcionario.nome+'.csv"'
        writer = csv.writer(response)
        writer.writerow([funcionario.nome, funcionario.empresa])
        for horas in funcionario.horaextra_set.all():
            writer.writerow([horas.motivo, horas.horas])
        return response
