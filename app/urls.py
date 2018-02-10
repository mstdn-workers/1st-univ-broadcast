from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^redirected$', views.redirected, name='redirected'),
    url(r'^$', views.index, name='index'),
]