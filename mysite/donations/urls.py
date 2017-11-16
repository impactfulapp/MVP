from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /donations/
    url(r'^$', views.index, name='index'),
    # ex: /donations/5/
    url(r'^(?P<donation_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /donations/login
    url(r'^login/$', views.login, name='login'),
]
