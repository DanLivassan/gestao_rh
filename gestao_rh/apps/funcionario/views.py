from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Funcionario
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

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
    fields = ['departamentos', 'nome']
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
    fields = ['departamentos', 'nome']
    template_name_suffix = '_update_form'


class DeleteFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionario-list')