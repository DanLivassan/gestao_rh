from .views import home
from django.urls import path
from .views import ListFuncionario, UpdateFuncionario, DeleteFuncionario, CreateFuncionario

urlpatterns = [
    path('', home),
    path('list/', ListFuncionario.as_view(), name="funcionario-list"),
    path('update/<pk>', UpdateFuncionario.as_view(), name="funcionario-update"),
    path('delete/<pk>', DeleteFuncionario.as_view(), name="funcionario-delete"),
    path('create/', CreateFuncionario.as_view(), name="funcionario-create"),
]