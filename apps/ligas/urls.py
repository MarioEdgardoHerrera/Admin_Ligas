from django.conf.urls import url, include

from apps.ligas.views import index, liga_view

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',liga_view, name='liga_crear'),
]
