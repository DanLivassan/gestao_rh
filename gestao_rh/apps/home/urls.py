from .views import index, new_index
from django.urls import path

urlpatterns = [
    path('old', index, name='home'),
    path('', new_index, name='new-index')
]