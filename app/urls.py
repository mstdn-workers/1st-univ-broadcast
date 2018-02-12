from django.conf.urls import url, include
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^auth$', views.auth, name='auth'),
    url(r'broadcast$', views.broadcast, name='broadcast'),
    url(r'^$', views.index, name='index'),
]