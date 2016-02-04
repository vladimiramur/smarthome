from django.conf.urls import patterns, include, url
from .import views

urlpatterns = patterns('',
    
    url(r'^$', views.index, name='index'),
    url(r'^form_upload/$', views.post_form_upload, name='post_form_upload'),
    url(r'^relay/$', views.my_view, name='my_view'),
    url(r'^swich/$', views.my_swich, name='my_swich'),

                       

)
