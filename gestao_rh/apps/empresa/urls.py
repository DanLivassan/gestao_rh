from .views import CreateEmpresa, UpdateEmpresa
from django.urls import path

urlpatterns = [
    path('novo', CreateEmpresa.as_view(), name="empresa-create"),
    path('atualizar/<int:pk>', UpdateEmpresa.as_view(), name="empresa-update")
]