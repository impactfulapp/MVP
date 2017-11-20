from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # ex: /donations/
    url(r'^$', views.index, name='index'),
    # ex: /donations/5/
    url(r'^(?P<donation_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /donations/login
    url(r'^login/$', views.login, name='login'),
    url(r'^connect_to_profile/$', views.connect_to_profile, name='connect_to_profile'),
    # ex: /donations/logout
    url(r'^logout/$', auth_views.logout, name='logout'),
    # social login urls
    url(r'^oath/', include('social_django.urls', namespace='social')),
    # settings pages
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
]

