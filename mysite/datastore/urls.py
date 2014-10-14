from django.conf.urls import patterns, url

from datastore import views

# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index')
# )

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^acquisition/', views.acquisitions, name='acquisitions'),
    url(r'^(?P<acq_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<acq_id>\d+)/coordinates/$', views.coordinates, name='coordinates'),
    url(r'^(?P<acq_id>\d+)/values/$', views.values, name='values'),
)