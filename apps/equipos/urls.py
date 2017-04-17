from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index_equipos'),
    url(r'^equipos/nuevo/$',views.equipo_view, name='agregar_equipo'),
]
