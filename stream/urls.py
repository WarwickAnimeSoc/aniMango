from django.conf.urls import url

from . import views

app_name = 'stream'

urlpatterns = [
    url(r'^$', views.stream, name='stream'),
]
