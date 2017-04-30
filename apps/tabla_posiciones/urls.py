from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_tabla'),
    url(r'^tabla_posiciones/nuevo/$', views.tabla_view, name='mostrar_Tabla'),
]