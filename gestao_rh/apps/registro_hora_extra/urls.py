
from django.urls import path
from .views import *



urlpatterns = [
    path('', ListHoraExtra.as_view(), name="hora_extra-list"),
    path('update/<pk>', UpdateHoraExtra.as_view(), name="hora_extra-update"),
    path('delete/<pk>', DeleteHoraExtra.as_view(), name="hora_extra-delete"),
    path('create/', CreateHoraExtra.as_view(), name="hora_extra-create"),

    path('list-js/<int:funcionario_id>', ListJsHoraExtra.as_view(), name="hora_extra-list-js"),
    path('create-js/', CreateJsHoraExtra.as_view(), name="hora_extra-js-create"),
]