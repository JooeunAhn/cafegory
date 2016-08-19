from django.conf.urls import url, include
from django.contrib import admin
from cafe.views import index, cafe_detail, cafe_new, cafe_edit

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<pk>\d+)$', cafe_detail, name="cafe_detail"),
    url(r'^new/$', cafe_new, name="cafe_new"),
    url(r'^edit/(?P<pk>\d+)$', cafe_edit, name="cafe_edit")
]
