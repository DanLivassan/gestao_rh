
from django.urls import path
from .views import *
urlpatterns = [
    path('', ListDocumento.as_view(), name="documento-list"),
    path('update/<pk>', UpdateDocumento.as_view(), name="documento-update"),
    path('delete/<pk>', DeleteDocumento.as_view(), name="documento-delete"),
    path('create/<int:funcionario_id>', CreateDocumento.as_view(), name="documento-create"),
]