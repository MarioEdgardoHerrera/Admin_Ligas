from django.conf.urls import url


from apps.equipos.views import index_equipos
urlpatterns = [
    url(r'^index$',index_equipos)
]
