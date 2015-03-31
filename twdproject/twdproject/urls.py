from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Matches a URL that begins with admin/, then
    # gives the remainder to the next urls.py file.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
)

# For any file requested with a URL starting with /media,
# the request will be passed to the django.views.static view,
# which handles the upload of the file.
#
# WARNING! To be used only during development. On deployement,
# find a better solution!
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
        )
