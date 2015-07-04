from django.conf.urls import patterns, url

from institutos import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]

