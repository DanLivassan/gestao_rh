from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..funcionario.models import Funcionario


@login_required
def index(request):
    data = {'user': request.user}

    return render(request, "home/index.html", data)

