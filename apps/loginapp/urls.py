from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name = 'my_index'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^registration$', views.registration, name = 'my_registration'),
    url(r'^login$', views.login, name = 'my_login'),
]
