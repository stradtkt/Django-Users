from django.conf.urls import url
from . import views 

app_name = "users"

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^login-page$', views.login_page, name='login_page'),
    url(r'^register-page$', views.register_page, name='register_page'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^dashboard/delete/(?P<id>\d+)$', views.delete_user, name='delete_user'),
    url(r'^dashboard/profile/(?P<id>\d+)$', views.profile, name='profile'),
]
