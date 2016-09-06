from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import mypage
urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': 'cafe:index'}, name='logout'),
    url(r'^mypage/$', mypage, name="mypage"),
]
