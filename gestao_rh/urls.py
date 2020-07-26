from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from gestao_rh.apps.funcionario.api.views import FuncionarioViewSet
from gestao_rh.apps.registro_hora_extra.api.views import HoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'funcionario', FuncionarioViewSet)
router.register(r'hora-extra', HoraExtraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionario/', include('gestao_rh.apps.funcionario.urls')),
    path('empresa/', include('gestao_rh.apps.empresa.urls')),
    path('departamento/', include('gestao_rh.apps.departamento.urls')),
    path('documento/', include('gestao_rh.apps.documento.urls')),
    path('hora-extra/', include('gestao_rh.apps.registro_hora_extra.urls')),
    path('', include('gestao_rh.apps.home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pdf/', include('gestao_rh.apps.pdf.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
