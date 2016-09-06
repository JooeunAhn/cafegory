from django.conf.urls import url, include
from django.contrib import admin
from cafe.views import index, cafe_detail, cafe_new, cafe_edit, cafe_list, cafe_comment_edit, cafe_comment_del

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^cafe/(?P<location>[a-z]+)$',cafe_list, name='cafe_list'),
    url(r'^cafe/(?P<pk>\d+)$', cafe_detail, name="cafe_detail"),
    url(r'^cafe/new/$', cafe_new, name="cafe_new"),
    url(r'^cafe/edit/(?P<pk>\d+)$', cafe_edit, name="cafe_edit"),
    url(r'^comment/(?P<pk>\d+)/edit/$', cafe_comment_edit, name="cafe_comment_edit"),
    url(r'^comment/(?P<pk>\d+)/del/$', cafe_comment_del, name="cafe_comment_del"),
]
