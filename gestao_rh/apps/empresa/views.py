from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class CreateEmpresa(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()


class UpdateEmpresa(UpdateView):
    model = Empresa
    fields = ['nome']


