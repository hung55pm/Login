from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^index$', views.index, name='index'),
]
