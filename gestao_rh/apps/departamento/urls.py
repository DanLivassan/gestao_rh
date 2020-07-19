
from django.urls import path
from .views import *
urlpatterns = [
    path('', ListDepartamento.as_view(), name="departamento-list"),
    path('update/<pk>', UpdateDepartamento.as_view(), name="departamento-update"),
    path('delete/<pk>', DeleteDepartamento.as_view(), name="departamento-delete"),
    path('create/', CreateDepartamento.as_view(), name="departamento-create"),
]