from django.conf.urls import url, include
from apps.ligas.views import index
urlpatterns = [
    url(r'^$', index ),
]
