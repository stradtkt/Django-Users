from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^login-page$', views.login_page),
    url(r'^register-page$', views.register_page),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/delete/(?P<id>\d+)$', views.delete_user),
    url(r'^dashboard/profile/(?P<id>\d+)$', views.profile),
    url(r'^dashboard/profile/(?P<id>\d+)/send_message$', views.send_message),
    url(r'^comments/(?P<id>\d+)$', views.comments),
    url(r'^comments/(?P<id>\d+)/send_comment$', views.send_comment),
]
