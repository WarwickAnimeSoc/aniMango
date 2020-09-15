from django.conf.urls import url

from . import views

app_name = 'stream'

urlpatterns = [
    url(r'^$', views.stream, name='stream'),
    url(r'^viewtick/(?P<token>.+)$', views.view, name='viewtick'),
    url(r'^viewcount/$', views.view_count, name='viewcount')
]
