from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.catalog, name='catalog'),
    url(r'^filterSideBar/$', views.filterSideBar, name='filterSideBar'),
    url(r'^search/$', views.search, name='search'),
]
