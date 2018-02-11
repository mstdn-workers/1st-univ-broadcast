from django.conf.urls import url, include
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^redirected$', views.redirected, name='redirected'),
     url(r'^$', views.index, name='index'),
]