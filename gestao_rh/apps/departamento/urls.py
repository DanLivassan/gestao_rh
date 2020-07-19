
from django.urls import path
from .views import ListDepartamento
urlpatterns = [
    path('', ListDepartamento.as_view(), name="departamento-list"),
    path('update/<pk>', ListDepartamento.as_view(), name="departamento-update"),
    path('delete/<pk>', ListDepartamento.as_view(), name="departamento-delete"),
    path('create/', ListDepartamento.as_view(), name="departamento-create"),
]