from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..funcionario.models import Funcionario


@login_required
def index(request):
    data = {'user': request.user}

    return render(request, "home/index.html", data)


def new_index(request):
    empresa_id = request.user.funcionario.empresa.id
    menu = [
        {'name': 'Editar empresa', 'url_name': 'empresa-update', 'param': empresa_id},
        {'name': 'Gerenciar Funcionários', 'url_name': 'funcionario-list'},
        {'name': 'Gerenciar Departamentos', 'url_name': 'departamento-list'},
        {'name': 'Horas extras', 'url_name': 'hora_extra-list'},
    ]

    return render(request, "home/newindex.html", {'menu_items': menu})

