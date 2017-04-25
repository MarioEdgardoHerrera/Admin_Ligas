from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_jugadore'),
    url(r'^jugadores/nuevo/$', views.jugadores_view, name='jugadores_crear'),
    ] 