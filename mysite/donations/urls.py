from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /donations/
    url(r'^$', views.index, name='index'),
    # ex: /donations/5/
    url(r'^(?P<donation_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /donations/login
    url(r'^login/$', views.login, name='login'),
    #url(r'^connect_to_profile/$', views.connect_to_profile, name='connect_to_profile'),
    # ex: /donations/logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/donations/'}),
    # social login urls
    url(r'^oath/', include('social_django.urls', namespace='social')),
    url(r'^oath/', include('django.contrib.auth.urls', namespace='auth')),
    # settings pages
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
    # populate charity list for autocomplete
    url(r'^ajax/get_charities/$', views.get_charities, name='get_charities'),
    # delete donation
    url(r'^delete_update/(?P<donation_id>\d+)/$',views.delete_update, name='delete_update'),
    # add or update donation
    url(r'^add_form/(?P<donation_id>\d+)/$', views.add_form, name='add_form'),


]
