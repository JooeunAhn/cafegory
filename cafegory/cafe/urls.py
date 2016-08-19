from django.conf.urls import url, include
from django.contrib import admin
from cafe.views import index, cafe_detail, cafe_new, cafe_edit, cafe_list

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^cafe/(?P<location>[a-z]+)$',cafe_list, name='cafe_list'),
    url(r'^cafe/(?P<pk>\d+)$', cafe_detail, name="cafe_detail"),
    url(r'^cafe/new/$', cafe_new, name="cafe_new"),
    url(r'^cafe/edit/(?P<pk>\d+)$', cafe_edit, name="cafe_edit")
]
