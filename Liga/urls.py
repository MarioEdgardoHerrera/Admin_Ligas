"""Liga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('apps.ligas.urls'), name="inicio"),
    url(r'', include('apps.equipos.urls'), name="inicio"),
    url(r'', include('apps.jugadores.urls'), name="inicio"),
    url(r'', include('apps.tabla_posiciones.urls'), name="inicio"),
    url(r'^admin/', admin.site.urls),
    url(r'^ligas/', include ('apps.ligas.urls', namespace="ligas")),
    url(r'^equipos/', include ('apps.equipos.urls', namespace="equipos")),
    url(r'^jugadores/', include ('apps.jugadores.urls', namespace="jugadores")),
    url(r'^tabla_posiciones/', include ('apps.tabla_posiciones.urls', namespace="tabla_jugadores")),

]
