from django.conf.urls import url, include
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^redirected$', views.redirected, name='redirected'),
    url(r'^redirect2auth$', views.redirect2auth, name='redirect2auth'),
    url(r'^$', views.index, name='index'),
]