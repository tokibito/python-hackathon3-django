from django.conf.urls.defaults import *
from core.models import Person, Book
from core.views import AddListViews

urlpatterns = patterns('',
  url(r'^$', 'core.views.index', name='index'),
  url(r'^person/', include(AddListViews(Person).urls)),
  url(r'^book/', include(AddListViews(Book, '_book').urls)),
)
