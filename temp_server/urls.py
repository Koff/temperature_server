from django.conf.urls import patterns, include, url
from django.contrib import admin
from temp_display import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^temps/$', views.Last5Reads.as_view(), name='index'),
    url(r'^temps/24hours', views.Last24Hours.as_view(), name='detail_last_24_hours'),
)
