from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
	    # r'^$' : regex (r) that matches an empty string (^$)
	    url(r'^$', views.index, name='index'),
	    url(r'^about/', views.about, name='about'),
	    url(r'category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	    )
