#Urls de app landing
from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'^$',index),
]