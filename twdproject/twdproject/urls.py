from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Matches a URL that begins with admin/, then
    # gives the remainder to the next urls.py file.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
)
