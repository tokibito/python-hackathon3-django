from django.conf.urls.defaults import *

urlpatterns = patterns('',
  url(r'^$', 'core.views.index', name='index'),
  url(r'^person/$', 'core.views.list_person', name='list_person'),
  url(r'^person/add$', 'core.views.add_person', name='add_person'),
)
