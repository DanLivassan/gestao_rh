
from django.urls import path
from .views import *
urlpatterns = [
    path('list-funcionario', PdfListFuncionario.as_view(), name="pdf_funcionario_list"),
]