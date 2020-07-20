from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionario/', include('gestao_rh.apps.funcionario.urls')),
    path('empresa/', include('gestao_rh.apps.empresa.urls')),
    path('departamento/', include('gestao_rh.apps.departamento.urls')),
    path('documento/', include('gestao_rh.apps.documento.urls')),
    path('hora-extra/', include('gestao_rh.apps.registro_hora_extra.urls')),
    path('', include('gestao_rh.apps.home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
