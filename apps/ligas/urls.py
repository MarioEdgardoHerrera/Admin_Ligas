from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$',views.index, name='ver_index'),
    url(r'^ligas/nuevo/$',views.liga_view, name='liga_crear'),
]
