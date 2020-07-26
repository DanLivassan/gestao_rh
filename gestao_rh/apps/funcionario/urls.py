
from .views import home
from django.urls import path
from .views import ListFuncionario, UpdateFuncionario, DeleteFuncionario, CreateFuncionario, CSVFuncionario

from django.urls import include, path





urlpatterns = [
    path('', home),
    path('list/', ListFuncionario.as_view(), name="funcionario-lista"),
    path('update/<pk>', UpdateFuncionario.as_view(), name="funcionario-update"),
    path('delete/<pk>', DeleteFuncionario.as_view(), name="funcionario-delete"),
    path('create/', CreateFuncionario.as_view(), name="funcionario-create"),
    path('funcionario-csv/<pk>', CSVFuncionario.as_view(), name="funcionario-csv"),

]