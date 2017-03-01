from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name = "my_index"),
    url(r'^add$', views.add, name = "add"),
    url(r'^create$', views.create, name = "create"),
    url(r'^destination/(?P<id>\d+)$', views.offset, name = "show"),
    url(r'^update/(?P<id>\d+)$', views.update, name = "update"),

]
