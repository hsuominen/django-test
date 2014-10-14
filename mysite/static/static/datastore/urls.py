from django.conf.urls import patterns, url

from datastore import views

# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index')
# )

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<acq_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<acq_id>\d+)/coordinates/$', views.coordinates, name='coordinates'),
    # ex: /polls/5/vote/
    url(r'^(?P<acq_id>\d+)/values/$', views.values, name='values'),
)