#Urls de app landing
from django.conf.urls import url
from .views import index,agregar

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^agregar/$',agregar, name="agregar"),
]