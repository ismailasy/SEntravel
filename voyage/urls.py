from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listing ,name="listing"),
    url(r'^(?P<voyage_id>[0-9]+)/$', views.detail_voyage,name="detail_voyage"),
    url(r'^search/$', views.search,name="search"),

]  
