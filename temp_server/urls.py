from django.conf.urls import patterns, include, url
from django.contrib import admin
from temp_display import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^temps/$', views.MainView.as_view(), name='index'),
)